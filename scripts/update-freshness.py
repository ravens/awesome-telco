#!/usr/bin/env python3
"""
Update freshness dates for GitHub/GitLab projects in README.md

This script parses the README.md file, finds GitHub and GitLab links,
fetches the last update date from their APIs, and updates the [YYYY-MM] tags.

Usage:
    python scripts/update-freshness.py [--dry-run]

Options:
    --dry-run    Show what would be changed without modifying the file

Note: Set GITHUB_TOKEN environment variable for higher API rate limits.
"""

import json
import os
import re
import ssl
import sys
import time
import urllib.parse
import urllib.request
from pathlib import Path

# Rate limiting pause between API calls (seconds)
API_DELAY = 0.5

# Patterns to match repository URLs
GITHUB_PATTERN = re.compile(
    r'\[([^\]]+)\]\(https?://github\.com/([^/]+)/([^/\)]+?)(?:\.git)?(?:/[^\)]*)?\)'
)
GITLAB_PATTERN = re.compile(
    r'\[([^\]]+)\]\(https?://gitlab\.([^/]+)/([^/]+)/([^/\)]+?)(?:\.git)?(?:/[^\)]*)?\)'
)

# Pattern to match existing freshness dates
FRESHNESS_PATTERN = re.compile(r'`\[\d{4}-\d{2}\]`')


def fetch_json(url: str, headers: dict = None) -> tuple[dict | None, str | None]:
    """Fetch JSON from a URL.

    Returns:
        Tuple of (data, error_message). If successful, error_message is None.
    """
    try:
        req = urllib.request.Request(url)
        req.add_header("User-Agent", "awesome-telco-freshness-checker")
        if headers:
            for key, value in headers.items():
                req.add_header(key, value)

        # Create SSL context
        ctx = ssl.create_default_context()

        with urllib.request.urlopen(req, timeout=10, context=ctx) as response:
            if response.status == 200:
                return json.loads(response.read().decode("utf-8")), None
    except urllib.error.HTTPError as e:
        if e.code == 403:
            # Check if it's rate limiting
            try:
                body = json.loads(e.read().decode("utf-8"))
                if "rate limit" in body.get("message", "").lower():
                    return None, "RATE LIMITED"
            except (json.JSONDecodeError, AttributeError):
                pass
            return None, "FORBIDDEN"
        elif e.code == 404:
            return None, "NOT FOUND"
        return None, f"HTTP {e.code}"
    except urllib.error.URLError as e:
        return None, "CONNECTION ERROR"
    except json.JSONDecodeError:
        return None, "INVALID JSON"
    return None, "UNKNOWN ERROR"


def get_github_info(owner: str, repo: str) -> tuple[str | None, bool, str | None]:
    """Fetch last pushed date and archived status from GitHub API.

    Returns:
        Tuple of (date_string, is_archived, error_message)
    """
    url = f"https://api.github.com/repos/{owner}/{repo}"

    headers = {"Accept": "application/vnd.github.v3+json"}
    token = os.environ.get("GITHUB_TOKEN")
    if token:
        headers["Authorization"] = f"token {token}"

    data, error = fetch_json(url, headers)
    if data and "pushed_at" in data:
        date = data["pushed_at"][:7]  # YYYY-MM
        archived = data.get("archived", False)
        return date, archived, None
    return None, False, error


def get_gitlab_info(host: str, owner: str, repo: str) -> tuple[str | None, str | None]:
    """Fetch last activity date from GitLab API.

    Returns:
        Tuple of (date_string, error_message)
    """
    # URL encode the project path
    project_path = urllib.parse.quote(f"{owner}/{repo}", safe="")
    url = f"https://gitlab.{host}/api/v4/projects/{project_path}"

    data, error = fetch_json(url)
    if data and "last_activity_at" in data:
        return data["last_activity_at"][:7], None  # YYYY-MM
    return None, error


def update_line_with_date(line: str, name: str, date: str, archived: bool = False) -> str:
    """Update or insert freshness date and archived marker in a line."""
    result = line

    # Check if line already has a freshness date
    if FRESHNESS_PATTERN.search(result):
        # Replace existing date
        result = FRESHNESS_PATTERN.sub(f"`[{date}]`", result, count=1)
    else:
        # Insert after the link, before the description
        # Pattern: [Name](url) - Description
        # Should become: [Name](url) `[YYYY-MM]` - Description
        # Escape special regex chars in name
        escaped_name = re.escape(name)
        pattern = re.compile(rf'(\[{escaped_name}\]\([^\)]+\))(\s*-\s*)')
        if pattern.search(result):
            result = pattern.sub(rf'\1 `[{date}]`\2', result, count=1)

    # Handle archived marker
    if archived:
        # Add ⚠️ at the beginning if not already present
        if "⚠️" not in result:
            # Add ⚠️ after "- "
            result = re.sub(r'^(\s*-\s*)', r'\1⚠️ ', result)

    return result


def process_readme(readme_path: Path, dry_run: bool = False) -> dict:
    """Process README and update freshness dates."""
    content = readme_path.read_text(encoding="utf-8")
    lines = content.split("\n")

    stats = {"updated": 0, "failed": 0, "skipped": 0, "archived": 0}
    changes = []
    archived_repos = []

    for i, line in enumerate(lines):
        # Skip lines that are clearly not project entries
        if not line.strip().startswith("-"):
            continue

        # Check for GitHub links
        github_match = GITHUB_PATTERN.search(line)
        if github_match:
            name, owner, repo = github_match.groups()
            # Clean repo name (remove trailing stuff)
            repo = repo.split("#")[0].split("?")[0]

            print(f"Fetching: github.com/{owner}/{repo}...", end=" ", flush=True)
            date, is_archived, error = get_github_info(owner, repo)

            if date:
                new_line = update_line_with_date(line, name, date, archived=is_archived)
                if new_line != line:
                    changes.append((i, line, new_line))
                    stats["updated"] += 1
                    print(f"[{date}]", end="")
                else:
                    stats["skipped"] += 1
                    print("(no change)", end="")

                if is_archived:
                    stats["archived"] += 1
                    archived_repos.append(f"github.com/{owner}/{repo}")
                    print(" ⚠️ ARCHIVED (marked)")
                else:
                    print()
            else:
                stats["failed"] += 1
                print(f"FAILED ({error})")

            time.sleep(API_DELAY)
            continue

        # Check for GitLab links
        gitlab_match = GITLAB_PATTERN.search(line)
        if gitlab_match:
            name, host, owner, repo = gitlab_match.groups()
            repo = repo.split("#")[0].split("?")[0]

            print(f"Fetching: gitlab.{host}/{owner}/{repo}...", end=" ", flush=True)
            date, error = get_gitlab_info(host, owner, repo)

            if date:
                new_line = update_line_with_date(line, name, date)
                if new_line != line:
                    changes.append((i, line, new_line))
                    stats["updated"] += 1
                    print(f"[{date}]")
                else:
                    stats["skipped"] += 1
                    print("(no change)")
            else:
                stats["failed"] += 1
                print(f"FAILED ({error})")

            time.sleep(API_DELAY)

    # Apply changes
    if changes and not dry_run:
        for i, old_line, new_line in changes:
            lines[i] = new_line
        readme_path.write_text("\n".join(lines), encoding="utf-8")
        print(f"\nUpdated {readme_path}")
    elif changes and dry_run:
        print("\n--- DRY RUN - Changes that would be made: ---")
        for i, old_line, new_line in changes:
            print(f"Line {i+1}:")
            print(f"  - {old_line.strip()}")
            print(f"  + {new_line.strip()}")

    # Report archived repos
    if archived_repos:
        print("\n⚠️  Archived repositories (marked with ⚠️ in README):")
        for repo in archived_repos:
            print(f"   - {repo}")

    return stats


def main():
    dry_run = "--dry-run" in sys.argv

    # Find README.md
    script_dir = Path(__file__).parent
    repo_root = script_dir.parent
    readme_path = repo_root / "README.md"

    if not readme_path.exists():
        print(f"Error: {readme_path} not found")
        sys.exit(1)

    print(f"Processing {readme_path}")
    if dry_run:
        print("(DRY RUN - no changes will be made)\n")
    print()

    stats = process_readme(readme_path, dry_run)

    print(f"\nSummary:")
    print(f"  Updated:  {stats['updated']}")
    print(f"  Skipped:  {stats['skipped']}")
    print(f"  Failed:   {stats['failed']}")
    print(f"  Archived: {stats['archived']}")

    if not os.environ.get("GITHUB_TOKEN"):
        print("\nTip: Set GITHUB_TOKEN env var for higher API rate limits")


if __name__ == "__main__":
    main()
