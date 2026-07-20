# Awesome Telco [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

> A curated list of telecommunication resources, tools, and projects for building and understanding mobile networks.

Whether you're a student, developer, security researcher, or telecom professional, this list provides resources spanning the entire mobile network stack—from SIM cards to core network functions.

## New to Telecom?

If you're just getting started, here's a suggested learning path:

1. **Understand the basics** → Start with the [Documentation & Standards](#documentation--standards) section for 3GPP specs and tutorials
2. **Learn the architecture** → Read [ShareTechNote](http://www.sharetechnote.com/) and [Nick vs Networking](https://nickvsnetworking.com/category/plmn/)
3. **Set up a lab** → Try [Open5GS Docker](https://github.com/herlesupreeth/docker_open5gs) or [UERANSIM](https://github.com/aligungr/UERANSIM)
4. **Join the community** → Check the [Community](#community) section for Discord, Slack, and mailing lists

### Quick Glossary

| Term | Meaning |
|------|---------|
| **UE** | User Equipment (your phone/modem) |
| **RAN** | Radio Access Network (base stations) |
| **eNB/gNB** | 4G/5G base station |
| **EPC** | Evolved Packet Core (4G core network) |
| **5GC** | 5G Core Network |
| **MME** | Mobility Management Entity (4G control plane) |
| **AMF** | Access and Mobility Function (5G equivalent of MME) |
| **SGW/PGW** | Serving/Packet Gateway (4G user plane) |
| **UPF** | User Plane Function (5G user plane) |
| **SIM/USIM** | Subscriber Identity Module |
| **IMS** | IP Multimedia Subsystem (VoLTE/VoWiFi) |

See also: [3gpp.guru](https://3gpp.guru) for comprehensive 3GPP abbreviations.

### Status Indicators

| Icon | Meaning |
|------|---------|
| ⚠️ | Deprecated/Archived project |

**Freshness dates**: Key projects show a `[YYYY-MM]` tag indicating their last update. Run `scripts/update-freshness.py` to refresh these dates.

### Mobile Network Architecture

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                              MOBILE NETWORK OVERVIEW                        │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  ┌──────────┐     ┌──────────────────────┐     ┌──────────────────────────┐ │
│  │          │     │    Radio Access      │     │      Core Network        │ │
│  │    UE    │────▶│      Network         │────▶│                          │ │
│  │  (Phone) │     │                      │     │  ┌─────┐  ┌─────┐        │ │
│  │          │     │  ┌────┐    ┌────┐    │     │  │ MME │  │ AMF │ (CP)   │ │
│  └──────────┘     │  │eNB │    │gNB │    │     │  └─────┘  └─────┘        │ │
│       │           │  │(4G)│    │(5G)│    │     │  ┌─────┐  ┌─────┐        │ │
│  ┌──────────┐     │  └────┘    └────┘    │     │  │S/PGW│  │ UPF │ (UP)   │ │
│  │   SIM    │     │                      │     │  └─────┘  └─────┘        │ │
│  │  (USIM)  │     └──────────────────────┘     │           │              │ │
│  └──────────┘                                  └───────────┼──────────────┘ │
│                                                            │                │
│                                                            ▼                │
│                                               ┌────────────────────────┐    │
│                                               │   Internet / IMS / DN  │    │
│                                               └────────────────────────┘    │
│                                                                             │
│  Legend: CP = Control Plane, UP = User Plane, DN = Data Network             │
└─────────────────────────────────────────────────────────────────────────────┘
```

**Data flow**: UE ↔ SIM (authentication) → RAN (radio) → Core (routing/policy) → Internet/Services

---

## Getting Started Tutorials

Step-by-step guides for common tasks:

### Deploy a 5G Core + RAN Simulator (No Hardware)

The fastest way to understand 5G architecture:

1. **Install Docker** on your machine
2. **Clone Open5GS Docker**: `git clone https://github.com/herlesupreeth/docker_open5gs`
3. **Follow the README** to bring up the 5G core
4. **Install UERANSIM**: `git clone https://github.com/aligungr/UERANSIM`
5. **Connect UERANSIM to Open5GS** - simulate a gNB and UE
6. **Monitor with Wireshark** - capture NGAP/GTP traffic

📚 Full guide: [Open5GS Docker README](https://github.com/herlesupreeth/docker_open5gs)

### Program a SIM Card

To test with real UEs, you need programmable SIM cards:

1. **Buy programmable SIMs** from [sysmocom](https://shop.sysmocom.de/SIM-cards/)
2. **Get a SIM card reader** (PC/SC compatible)
3. **Install pySIM**: `pip install pysim`
4. **Read your SIM**: `pySIM-read.py -p 0`
5. **Program IMSI/Ki/OPc** to match your core network

📚 Full guide: [pySIM Wiki](https://osmocom.org/projects/pysim/wiki)

### Capture Live LTE Traffic

For research and debugging:

1. **Get a Qualcomm-based phone** (rooted) or modem
2. **Install QCSuper**: `git clone https://github.com/P1sec/QCSuper`
3. **Enable DIAG mode** on your device
4. **Capture**: `./qcsuper.py --usb-modem /dev/ttyUSB0 --wireshark-live`
5. **Analyze in Wireshark** with GSMTAP dissector

📚 Full guide: [QCSuper README](https://github.com/P1sec/QCSuper)

---

## Contents

- [SIM Cards](#sim-cards) - USIM, eSIM, SIM programming and management
- [User Equipment](#user-equipment) - Phones, modems, UE simulators
- [Radio Access Network](#radio-access-network) - 2G/3G/4G/5G base stations
- [Core Network](#core-network) - EPC, 5GC, MME, AMF, UPF, etc.
- [Interconnect](#interconnect) - IMS, SBC, SS7, Diameter
- [Protocols](#protocols) - Libraries and frameworks for telco protocols
- [Satellite Communication](#satellite-communication) - LEO/GEO satellite tooling
- [Infrastructure](#infrastructure) - NFV, SDN, Kubernetes for telco
- [Orchestration](#orchestration) - Automation and deployment
- [Lab & Testbeds](#lab--testbeds) - Ready-to-use environments
- [Testing](#testing) - TTCN-3, load testing, validation
- [AI & Machine Learning](#ai--machine-learning) - LLMs, PHY/RF ML, network optimization, RL environments
- [Security](#security) - Research, tools, IMSI catcher detection, and talks
- [Learning Resources](#learning-resources) - Blogs, docs, tutorials
- [Community](#community) - Forums, mailing lists, Discord, Slack

---

## SIM Cards

### SIM/USIM Tools & Hardware

- [PySIM](https://osmocom.org/projects/pysim/wiki) `[2025-12]` - Set of tools to read/explore/decode and program (write) SIM/USIM/ISIM cards. Essential for managing programmable SIM cards.
- [sysmoISIM-SJA5](https://www.sysmocom.de/products/sim/sysmoisim-sja5/) - Latest generation programmable SIM/UICC/USIM/ISIM card with 3GPP Release 17 support. Ideal for lab/research networks.
- [sysmo-usim-tool](https://gitea.sysmocom.de/sysmocom/sysmo-usim-tool) - Utility for managing proprietary bits of sysmoUSIM/sysmoISIM programmable cards.
- [SIMTrace2](https://osmocom.org/projects/simtrace2) - Hardware device + firmware to trace communication between phone and SIM card. Supports card-side emulation. Works with [ngff-cardem](https://osmocom.org/projects/ngff-cardem/wiki).
- [SIMTester](https://opensource.srlabs.de/projects/simtester) - Assess SIM card security: cryptanalytic attack surface and application attack surface.
- [GlobalPlatformPro](https://github.com/martinpaljak/GlobalPlatformPro) `[2026-06]` - CLI tool to load and manage applets on JavaCards, by Martin Paljak.
- [ARA-M Applet](https://github.com/bertrandmartel/aram-applet) `[2018-02]` - ARA-M implementation for JavaCards by Bertrand Martel.
- ⚠️ [HelloSTK2](https://github.com/mrlnc/HelloSTK2) `[2025-01]` - Guide to build and install SIM-Toolkit applets.
- [SUPI with pysim](https://gist.github.com/mrlnc/01d6300f1904f154d969ff205136b753) - Notes on enabling SUPI with pysim.
- [asterix](https://github.com/suma12/asterix) `[2019-06]` - Framework for smartcard communication based on pyscard.
- [SimServerAndroid](https://github.com/zhuowei/SimServerAndroid) `[2022-07]` - Get SIM card ICCID and run 3G Authentication over ADB shell.
- [ScapySMS](https://github.com/mnemonic-no/ScapySMS) `[2021-10]` - Scapy implementation of SMS-SUBMIT and (U)SIM Application Toolkit command packets.
- [USIM-https-server](https://github.com/fasferraz/USIM-https-server) `[2022-02]` - USIM HTTPS server API exposing AKA authentication over HTTP. Useful for lab/testing setups.
- [swicc-pcsc](https://github.com/tomasz-lisowski/swicc-pcsc) `[2024-07]` - PC/SC IFD handler bridging swICC-based software SIM cards to PC/SC applications. Companion to swSIM/swICC.
- [android-apdu-proxy](https://gitea.osmocom.org/sim-card/android-apdu-proxy) - Android app acting as APDU proxy for UICC/eUICC/SE communication. Hosted on **Osmocom Gitea**.
- [kiopcgenerator](https://gitea.osmocom.org/fixeria/kiopcgenerator) - Ki/OPc USIM card key generation from Op and Transport keys. Hosted on **Osmocom Gitea**.
- [SIM Explorer](https://sourceforge.net/projects/sim-explorer/) - SIM card explorer/decoder using smart card readers. Browse filesystem, decode EF/DF, export Cellebrite-compatible XML. Hosted on **SourceForge**.
- [apdu4j](https://github.com/martinpaljak/apdu4j) `[2026-06]` - APDU-level smart card communication library for Java. PC/SC and remote JSON interfaces. From the GlobalPlatformPro author.
- [UiccBrowser](https://github.com/cheeriotb/UiccBrowser) `[2026-06]` - Android app to browse the file system of a UICC/eUICC via the OMAPI. From the ISD-R-AccessProvider author.
- [sim-toolkit-refresh](https://github.com/cheeriotb/sim-toolkit-refresh) `[2020-08]` - Java Card applet implementing the SIM Toolkit REFRESH proactive command for SIM/STK testing on Android.
- [osmocom-sim-tools (mirror)](https://github.com/cheeriotb/osmocom-sim-tools) `[2018-12]` - Active fork of Osmocom sim-tools with additional features for sysmoUSIM/sysmoISIM cards.
- [onomondo-softsim-cli](https://github.com/onomondo/onomondo-softsim-cli) `[2026-06]` - CLI tool to provision Onomondo SoftSIM profiles.
- [mcc-mnc-itu](https://github.com/onomondo/mcc-mnc-itu) `[2025-07]` - Library to look up MCC/MNC operator information from the official ITU dataset.
- [simshell](https://github.com/kurbatoff/simshell) `[2025-10]` - Interactive shell for SIM, GlobalPlatform and JavaCard VM operations over APDU.

### eSIM / eUICC

- [eUICC and eSIM Developer Manual](https://euicc-manual.osmocom.org) - Comprehensive eSIM developer documentation from Osmocom.
- [Known eSIM Test Profiles](https://euicc-manual.osmocom.org/docs/rsp/known-test-profile/) - List of known test profiles for eSIM/eUICC testing and development.
- [lpac](https://github.com/estkme-group/lpac) `[2026-07]` - C-language implementation of a Consumer eSIM LPAd. Download/activate/deactivate profiles on eUICC.
- [EasyLPAC](https://github.com/creamlike1024/EasyLPAC) `[2026-04]` - lpac GUI Frontend for Linux and macOS.
- [OpenEUICC](https://github.com/estkme-group/openeuicc) `[2026-07]` - Fully open-source eSIM LPA (Local Profile Assistant) implementation for Android. System privilege required. Also available as [Magisk module](https://github.com/hzy132/OpenEUICC_for_Magisk).
- [LPAd SM-DP+ Connector](https://github.com/Truphone/LPAd_SM-DPPlus_Connector) `[2023-05]` - Local Profile Assistant for Device (LPAd) SM-DP+ Connector.
- [Generic-eUICC-Test-Profile](https://github.com/GSMATerminals/Generic-eUICC-Test-Profile-for-Device-Testing-Public) `[2026-05]` - Standardized test profiles for embedded UICCs.
- [ISD-R Access Provider](https://github.com/cheeriotb/ISD-R-AccessProvider) `[2021-01]` - Content provider for communicating with ISD-R in soldered eSIM on Android (Pixel4).
- [rlpa-server](https://github.com/estkme-group/rlpa-server) `[2024-07]` - Remote LPA Server for eSIM profile management, from the lpac team.
- [MiniLPA](https://github.com/EsimMoe/MiniLPA) `[2024-12]` - Professional cross-platform LPA UI for eSIM/eUICC management (GSMA SGP.22), built with Java Swing.
- [NekokoLPA](https://github.com/iebb/NekokoLPA) `[2026-06]` - Open-source LPA software for managing eSIM profiles on Android and iOS.
- [eUICC Probe](https://github.com/CursedHardware/euicc-probe) `[2025-10]` - eUICC diagnostic and probing tool in Kotlin. Inspect eUICC capabilities and profile information.
- [OpenRSP](https://github.com/Blockchain-Powered-eSIM/OpenRSP) `[2025-04]` - Open source Remote SIM Provisioning implementation for eSIM profile management.
- [Onomondo SoftSIM](https://github.com/onomondo/nrf-softsim) `[2026-07]` - SoftSIM integration for Nordic Semiconductor nRF91 Series. Software-based SIM for IoT. From Onomondo.
- [smdpp](https://github.com/ianchen0119/smdpp) `[2026-01]` - Early-stage open SM-DP+ (Subscription Manager Data Preparation+) implementation for eSIM remote provisioning research.
- [onomondo-eim](https://github.com/onomondo/onomondo-eim) `[2026-03]` - Open implementation of an eIM (eUICC IoT Manager) per GSMA SGP.31 for IoT eSIM remote provisioning. From Onomondo.
- [onomondo-ipa](https://github.com/onomondo/onomondo-ipa) `[2026-07]` - IoT Profile Assistant (IPA) implementation per SGP.32 providing on-device functions for SGP.32 eUICC provisioning by an SM-DP+. From Onomondo.
- [euicc-go](https://github.com/damonto/euicc-go) `[2026-07]` - Pure-Go implementation of the eUICC profile management protocol (SGP.22). Building block for LPA tooling.
- [notccid](https://github.com/estkme-group/notccid) `[2024-10]` - ESTKme-RED reader protocol, the non-CCID protocol used by the ESTKme programmable eSIM reader/writer hardware.
- [NekokoLPA2](https://github.com/iebb/NekokoLPA2) `[2026-07]` - Second-generation cross-platform open-source LPA UI for eSIM management on Android/iOS, by the original NekokoLPA author.
- [remocard](https://github.com/iebb/remocard) `[2026-01]` - Remote OMAPI companion app for NekokoLPA2, exposing a phone's secure element/eUICC over the network for remote LPA operations.
- [SecureElementAccessBypass](https://github.com/EsimMoe/SecureElementAccessBypass) `[2023-12]` - Android module to bypass SE ARA & ARF access restrictions for full SE access. Used in eUICC/SIM research on locked-down devices.
- [gsma-sgp22-asn1](https://github.com/CursedHardware/gsma-sgp22-asn1) `[2023-12]` - Standalone GSMA SGP.22 ASN.1 schema definitions extracted for use in eSIM tooling and codegen.
- [eSIM Wallet](https://github.com/Blockchain-Powered-eSIM/eSIM-Wallet) `[2024-06]` - Mobile eSIM wallet app, the user-facing companion to OpenRSP. From the Blockchain-Powered-eSIM project.
- [TSMS](https://github.com/BSI-Bund/TSMS) `[2026-02]` - German BSI reference Java API and OpenAPI spec for a Trusted Service Management System (BSI-TR-03165), used to install and personalize JavaCard applets on smartphone secure elements.


- [XiaomiEsimLPA](https://github.com/tehcneko/XiaomiEsimLPA) `[2026-01]` - A Magisk/KernelSU module trying to add native eSIM management support for Xiaomi devices with MIUI and Xiaomi HyperOS.
- [SIMTester](https://github.com/srlabs/SIMTester) `[2023-02]` - A tool to test SIM card security.
- [luci-app-epm](https://github.com/stich86/luci-app-epm) `[2025-10]` - LuCI app to manage eSIM Profile on OpenWrt Web Interface.
- [oneplus13t-esim](https://github.com/kinginu/oneplus13t-esim) `[2025-06]` - A Magisk module to enable native eSIM profile management for physical SIMs (e.g., 5ber, eSTK.me) directly with in the ColorOS settings app.
- [ecp-lpa-sdk-decompiled](https://github.com/CursedHardware/ecp-lpa-sdk-decompiled) `[2024-08]` - ECP LPA SDK (Decompiled).
- [YggdraSIM](https://github.com/1oT/YggdraSIM) `[2026-07]` - Python toolkit for SIM/eSIM and eUICC work: SCP03, SCP80, SCP11 (relay, local, eIM), SAIP profile packages, and a simulated UICC/eUICC engine. Uses upstream pySim dependencies.
- [esim](https://codeberg.org/d8/esim) - Hosted on **Codeberg**.
- [bnesim_quota_cli](https://codeberg.org/gigahertz/bnesim_quota_cli) - View BNESIM eSIM quotas from terminal. Hosted on **Codeberg**.
- [esim-qrcode-portal](https://github.com/CursedHardware/esim-qrcode-portal) `[2026-07]` - eSIM QRCode Portal.
- [uicc-chip-packages](https://github.com/CursedHardware/uicc-chip-packages) `[2024-01]` - UICC Chip Packaging.
- [UICC_SIM_Wiki](https://github.com/herlesupreeth/UICC_SIM_Wiki) `[2019-12]` - SIM part of steps involved in enabling UICC carrier privileges.
- [luci-app-hermes-euicc](https://github.com/KilimcininKorOglu/luci-app-hermes-euicc) `[2026-03]` - LuCI Web Interface App for Managing eSIM Profiles via Hermes eUICC.
- [openeuicc-bridge](https://github.com/Laiteux/openeuicc-bridge) `[2026-02]` - An Android ContentProvider that exposes OpenEUICC/EasyEUICC LPA functionality via ADB, enabling programmatic eSIM profile management.
- [pysim](https://gitea.osmocom.org/sim-card/pysim) - Python libraries and command line tools for SIM/UICC/USIM/ISIM card analysis and programming. Hosted on **Osmocom Gitea**.
- [euicc-manual](https://gitea.osmocom.org/sim-card/euicc-manual) - Osmocom eUICC and eSIM Developer Manual. Hosted on **Osmocom Gitea**.
- [gsma-esim-iot](https://gitea.osmocom.org/sim-card/gsma-esim-iot) - playground for exploring GSMA IoT eSIM. Hosted on **Osmocom Gitea**.
- [imsi-pseudo](https://gitea.osmocom.org/cellular-infrastructure/imsi-pseudo) - IMSI Pseudonymization for 2G/3G/4G. Hosted on **Osmocom Gitea**.
- [eSIM-SMS-Forwarder](https://github.com/cyDione/eSIM-SMS-Forwarder) `[2026-03]` - eUICC/eSIM管理 短信接收与转发
- [sysmo-usim-tool](https://github.com/herlesupreeth/sysmo-usim-tool) `[2020-10]` - Modified version of sysmo-usim-tool
- [onomondo-traffic](https://github.com/onomondo/onomondo-traffic) `[2025-04]` - Fetch your organization's traffic based on ip, iccid, or simid
- Additional sim-card sub-projects: [aram-applet](https://gitea.osmocom.org/sim-card/aram-applet), [hello-stk](https://gitea.osmocom.org/sim-card/hello-stk), [sim-tools](https://gitea.osmocom.org/sim-card/sim-tools), [simtrace2](https://gitea.osmocom.org/sim-card/simtrace2)
- [sigmo](https://github.com/damonto/sigmo) `[2026-07]` - Self-hosted web UI and API for managing ModemManager-based cellular modems and eSIM profiles.
- [react-native-sim-cards-manager](https://github.com/odemolliens/react-native-sim-cards-manager) `[2025-11]` - React Native plugin to manage SIM cards and eSIM.
- [SimAdmin](https://github.com/3899/SimAdmin) `[2026-07]` - SIM/eSIM, cellular network, SMS and DDNS management system for cellular CPE, travel routers and soft routers.
- [nothing-euicc](https://github.com/reindex-ot/nothing-euicc) `[2026-02]` - Magisk module that force-enables the eUICC (eSIM) on Nothing phones.
- [7600lpa](https://github.com/assofour/7600lpa) `[2026-04]` - SGP.22 eSIM LPA for the SIM7600G-H module: profile download, install and enable.
### SIM Emulation & Virtualization

- [swSIM](https://github.com/tomasz-lisowski/swsim) `[2026-05]` - A software-only SIM card.
- [swICC](https://github.com/tomasz-lisowski/swicc) `[2026-05]` - Framework for creating smart cards (ICC-based cards with contacts).
- [vsmartcard](https://github.com/frankmorgner/vsmartcard) `[2026-07]` - Umbrella project for emulation of smart card readers or smart cards.
- [Onomondo UICC](https://github.com/onomondo/onomondo-uicc) `[2026-07]` - Pure software implementation/emulation of SIM/UICC/USIM functionalities.
- [osmo-remsim](https://osmocom.org/projects/osmo-remsim/wiki) - Forward SIM card traffic to a remote SIM card via TCP/IP.
- [mobile-atlas](https://github.com/sbaresearch/mobile-atlas) `[2025-11]` - Geographically decouple SIM card and modem for scalable measurement platforms.
- [softsim-quecopen-unisoc-lte](https://github.com/onomondo/softsim-quecopen-unisoc-lte) `[2026-07]` - Onomondo SoftSIM integration for Quectel LTE modules using the UNISOC SDK, extending SoftSIM beyond the Nordic nRF91.
- [simLAB](https://github.com/kamwar/simLAB) `[2026-04]` - Smartcard editor and SIM/SAT simulator for exploring and emulating SIM/USIM card behavior.

### VoLTE/VoWiFi & Carrier Privileges

- [CoIMS_Wiki](https://github.com/herlesupreeth/CoIMS_Wiki) `[2025-10]` - Guide for overriding IMS settings to enable VoLTE/VoWiFi using Carrier Privileges. Companion app: [CoIMS](https://play.google.com/store/apps/details?id=com.sherle.coims).
- [pixel_ims_module](https://github.com/cxOrz/pixel_ims_module) `[2024-04]` - Magisk module that enables VoLTE, VoNR, and Wi-Fi Calling on rooted Pixel devices by modifying carrier config boolean flags.
- [aram-cardlet](https://github.com/cheeriotb/aram-cardlet) `[2018-12]` - Sample Java Card ARA-M applet for the Android Secure Element CTS, useful for carrier-privilege experimentation on SIMs.
- [App ARA-M Calculator](https://github.com/EsimMoe/AppARA-MCalculator) `[2023-12]` - Helper to compute the App ARA-M hash needed for Android carrier-privilege rules and SE access entries.
- [IMS-DC SDK (5G New Calling)](https://github.com/GSMATerminals/IMS-DC-SDK-Open-Source) `[2026-07]` - GSMA-published 5G New Calling Terminal SDK. Adds an IMS Data Channel on top of IMS audio/video and exposes AIDL interfaces for building data-channel apps (file sharing, doodle, customer service line). From China Telecom Research Institute via GSMA Terminals.
- [Pixel IMS (pixel-volte-patch)](https://github.com/kyujin-cho/pixel-volte-patch) `[2026-02]` - Rootless replacement for the Tensor Pixel VoLTE/IMS patch. Related Pixel IMS tooling: [Carrier IMS / TurboIMS](https://github.com/ryfineZ/carrier-ims-for-pixel) `[2026-02]`, [TurboIMS config tool](https://github.com/Turbo1123/TurboIMS) `[2025-10]`, [ImsForPixel](https://github.com/svenuks/ImsForPixel) `[2026-06]` (rootless VoLTE/VoNR/VoWiFi, no Shizuku), [Pixel 5G/VoLTE enabler](https://github.com/WZL203/Pixel-turn-on-5G-Volte-and-automatically-register-with-IMS) `[2025-10]`, [PixelIMS](https://github.com/VinujaHerath/PixelIMS) `[2026-05]` (for carriers without official Pixel support).
- [Samsung-IMS-Patcher](https://github.com/rezaf28/Samsung-IMS-Patcher) `[2025-09]` - LSPosed module to unlock Samsung-restricted carrier features on rooted Galaxy devices (VoWiFi, VoLTE, ViLTE, RCS, SMS over IP).


## User Equipment

### 4G

- [srsUE](https://github.com/srslte/srslte) `[2026-01]` - UE 4G modem part of the srsLTE project.
- [srsUE PR external NAS](https://github.com/srsLTE/srsLTE/pull/474) `[2026-01]` - a PR for srsLTE for external NAS message injection.
- [OAI UE](https://gitlab.eurecom.fr/oai/openairinterface5g/wikis/home) `[2026-07]` - Open Air Interface RAN 4G eNB/ 5G gNB to use on SDR-based radios.
- [Amarisoft](https://www.amarisoft.com) - Commercial UE Emulator by Amarisoft, company co-founded by [Bellard](https://bellard.org) on his original LTE software modem [work](https://bellard.org/lte/).
- [LTE-CellScanner](https://github.com/Evrytania/LTE-Cell-Scanner) `[2019-02]` - This is a collection of tools to locate and track LTE basestation cells using very low performance RF front ends.
- [LTE-CellScanner-SDR-X](https://github.com/JiaoXianjun/LTE-Cell-Scanner) `[2024-01]` - An OpenCL accelerated TDD/FDD LTE Scanner (from rtlsdr/hackRF/bladeRF A/D samples to PDSCH output and RRC SIB messages decoded).
- [S1APTester](https://github.com/magma/S1APTester) `[2022-12]` - A test tool that simulates the s1aptest functionality of a LTE network.

### 2G

- [OsmocomBB](https://osmocom.org/projects/baseband/wiki) - Open Source implementation of a 2G Mobile Station, including baseband firmware/PHY, L2, L3, etc.  Works with phones using TI Calypso chipset; SDR PHY is work-in-progress
- [FreeCalypso](https://www.freecalypso.org/) - Volunteer project building software derived from leaked source code for the TI calypso project

### Diagnostics, Monitor mode

- [SCAT](https://github.com/fgsect/scat) `[2026-06]` - this application parses diagnostic messages of Qualcomm and Samsung baseband through USB, and generates a stream of GSMTAP packet containing cellular control plane messages.
- [QCSuper](https://github.com/P1sec/QCSuper) `[2026-07]` - QCSuper is a tool communicating with Qualcomm-based phones and modems, allowing to capture raw 2G/3G/4G radio frames, among other things.
- [Network Signal Guru](http://m.qtrun.com/en/) - Android app able to parse Diag output from QC modem and display a lot of data for engineering field work.
- [SnoopSnitch](https://github.com/srlabs/snoopsnitch) `[2022-05]` - Android app that collects and analyzes mobile radio data to detect fake base stations, user tracking, and OTA updates via the DIAG protocol on a rooted phone. From SRLabs.
- [Diag-parser](https://github.com/moiji-mobile/diag-parser) `[2017-11]` - Parse the Qualcomm DIAG format and convert 2G, 3G and 4G radio messages to Osmocom GSMTAP for analysis in wireshark and other utilities.
- [LTE_monitor_c2xx](https://github.com/P1sec/LTE_monitor_c2xx) `[2014-11]` - The purpose of LTE_monitor_c2xx is to provide a LTE message debugging solution for Samsung C2xx-based chipsets.
- [XGoldmon](https://github.com/2b-as/xgoldmon) `[2013-12]` - xgoldmon is a small tool to convert the messages output by the USB logging mode of phones with Intel/Infineon XGold baseband processor.
- [Modmobmap](https://github.com/PentHertz/Modmobmap) `[2025-12]` - Map 2G/3G/4G and more cellular networks in real live with a simple smart phone, pretty much like osmocomBB monitoring feature.
- [Modmobjam](https://github.com/PentHertz/Modmobjam) `[2023-04]` - A smart jamming proof of concept for mobile equipments that could be powered with Modmobmap tool.
- [LTESniffer](https://github.com/SysSec-KAIST/LTESniffer) `[2024-10]` - An Open-source LTE Downlink/Uplink Eavesdropper
- [FALCON](https://github.com/falkenber9/falcon) `[2023-10]` - FALCON - Fast Analysis of LTE Control channels.
- [osmo-qcdiag](https://osmocom.org/projects/osmo-qcdiag/wiki) - Osmocom project for decoding Qualcomm DIAG messages. Use @hoernchen/gsmtap@ branch to feed 2G/3G/4G/SIM messages from DIAG into wireshark ia GSMTAP.
- [mbn-mcfg-tools](https://github.com/sbaresearch/mbn-mcfg-tools) `[2024-07]` - Tools for parsing, extracting, and packing Qualcomm MBN MCFG (Modem Configuration) files. From the mobile-atlas team at SBA Research.
- [TowerCollector](https://github.com/zamojski/TowerCollector) `[2026-06]` - Android contributor app for OpenCellID and BeaconDB. Records GPS-tagged GSM/UMTS/LTE/5G cell observations and uploads them to open cell databases.
- [gsm-parser](https://github.com/srlabs/gsm-parser) `[2021-11]` - SRLabs GSM/UMTS parser used by the SnoopSnitch backend for analyzing baseband logs and signaling.
- [CellularInfo](https://github.com/DevelopCubeLab/CellularInfo) `[2026-04]` - iOS TrollStore app exposing detailed cellular radio information.
- [libqmi](https://github.com/linux-mobile-broadband/libqmi) `[2026-07]` - The freedesktop.org WWAN modem stack (GitHub mirrors): QMI library, [libmbim](https://github.com/linux-mobile-broadband/libmbim) (MBIM library) and the [ModemManager](https://github.com/linux-mobile-broadband/ModemManager) daemon.
- [WiresharkQMIDissector](https://github.com/dnlplm/WiresharkQMIDissector) `[2025-10]` - Wireshark dissector for the QMI protocol used by Qualcomm-based modems.

## Radio Access Network

### RRH

- [O-RAN Software and seed code](https://o-ran-sc.org) - The O-RAN Software Community (SC) is a collaboration between the O-RAN Alliance and Linux Foundation with the mission to support the creation of software for the Radio Access Network (RAN). Introduction to O-RAN in a [LF video](https://www.youtube.com/watch?v=iJyb0pCWDKo). RIC platform (Gerrit mirrors): [ric-plt-e2](https://github.com/o-ran-sc/ric-plt-e2), [ric-plt-e2mgr](https://github.com/o-ran-sc/ric-plt-e2mgr), [ric-plt-ric-dep](https://github.com/o-ran-sc/ric-plt-ric-dep), [ric-plt-appmgr](https://github.com/o-ran-sc/ric-plt-appmgr), [ric-plt-xapp-frame](https://github.com/o-ran-sc/ric-plt-xapp-frame) ([py](https://github.com/o-ran-sc/ric-plt-xapp-frame-py), [cpp](https://github.com/o-ran-sc/ric-plt-xapp-frame-cpp)). xApps: [hw-python](https://github.com/o-ran-sc/ric-app-hw-python), [ts](https://github.com/o-ran-sc/ric-app-ts), [kpimon-go](https://github.com/o-ran-sc/ric-app-kpimon-go), [ad](https://github.com/o-ran-sc/ric-app-ad), [qp](https://github.com/o-ran-sc/ric-app-qp).
- [srsRAN O-RAN SC RIC](https://github.com/srsran/oran-sc-ric) `[2025-10]` - Simplified O-RAN SC RIC deployment with improved usability and xApp examples, from the srsRAN team.
- [FlexRIC](https://gitlab.eurecom.fr/mosaic5g/flexric) `[2026-07]` - O-RAN Alliance compliant Near-RT RIC and E2 Agent with xApp SDK in C/C++ and Python. Sub-200µs latency. Part of MOSAIC5G/OAI. Hosted on **GitLab (Eurecom)**.
- [ProtO-RU](https://github.com/NUS-CIR/ProtO-RU) `[2026-06]` - Software implementation of an O-RAN split-7.2 compatible Radio Unit using SDRs. From NUS.
- [xDevSM](https://github.com/wineslab/xDevSM) `[2026-07]` - Open-source framework for O-RAN E2 service models that simplifies xApp development for OSC Near-RT RIC. Supports KPM V3. From WiNES Lab / Northeastern University.
- [Colosseum Near-RT RIC](https://github.com/wineslab/colosseum-near-rt-ric) `[2025-12]` - Minimal O-RAN SC Near-RT RIC adapted for the Colosseum wireless network emulator. Supports concurrent multi-base-station and multi-xApp connections. From WiNES Lab.
- [xFAPI](https://github.com/coranlabs/xFAPI) `[2026-07]` - Facilitating interoperability in Open RAN via xFAPI interface. From CoRAN Labs.
- [O-RAN SC O-DU L2](https://github.com/o-ran-sc/o-du-l2) `[2026-05]` - O-RAN Software Community Distributed Unit Layer 2 implementation. Reference O-DU high with F1/E2 interfaces.
- [SCOPE](https://github.com/wineslab/colosseum-scope) `[2025-12]` - Open and Softwarized Prototyping Platform for NextG Systems on the Colosseum wireless network emulator. From WiNES Lab (ACM MobiSys).
- [ORANSlice](https://github.com/wineslab/ORANSlice) `[2025-12]` - Open-source 5G network slicing platform for O-RAN with xApp-based slice management. From WiNES Lab (ACM MobiCom'24).
- [dApp Framework](https://github.com/wineslab/dApp-framework) `[2026-07]` - Framework for distributed Apps (dApps) for O-RAN beyond the xApp/rApp model. From WiNES Lab.
- [dApp Library](https://github.com/wineslab/dApp-library) `[2026-06]` - Library counterpart to dApp-framework providing building blocks for writing dApps that run inside the O-RAN DU/CU. From WiNES Lab.
- [OSC RIC xApp Template](https://github.com/5GSEC/OSC-RIC-xApp-Template) `[2024-09]` - Python xApp development template for the O-RAN SC Near-RT RIC with SDL/RMR/E2 scaffolding. Useful starting point for new xApp authors.
- [OAI O1 Adapter](https://gitlab.eurecom.fr/oai/o1-adapter) `[2026-06]` - O-RAN O1/NETCONF adapter for OpenAirInterface gNB enabling integration with O-RAN SMOs. Hosted on **GitLab (Eurecom)**.
- [ai-ran-dgx-spark](https://github.com/rcbarke/ai-ran-dgx-spark) `[2025-12]` - Deployment automation for NVIDIA Aerial AI-RAN on the DGX Spark platform. Useful for getting Aerial running on GPU AI-RAN testbeds.
- [python-sample-app](https://github.com/ericsson-iap/python-sample-app) `[2026-02]` - Python Sample App for SMO Systems like Ericsson Intelligent Automation Platform. We aim to be ORAN aligned. Use this ...
- [AdapShare-An-RL-Based-Dynamic-Spectrum-Sharing-Solution-for-O-RAN](https://github.com/usnistgov/AdapShare-An-RL-Based-Dynamic-Spectrum-Sharing-Solution-for-O-RAN)
- [ns-o-ran-grafana](https://github.com/wineslab/ns-o-ran-grafana)
- Additional o-ran-sc sub-projects: [o-du-phy](https://github.com/o-ran-sc/o-du-phy), [nonrtric](https://github.com/o-ran-sc/nonrtric), [it-dep](https://github.com/o-ran-sc/it-dep), [ric-app-hw-go](https://github.com/o-ran-sc/ric-app-hw-go), [aiml-fw-aimlfw-dep](https://github.com/o-ran-sc/aiml-fw-aimlfw-dep), [oam](https://github.com/o-ran-sc/oam), [ric-app-hw](https://github.com/o-ran-sc/ric-app-hw), [aiml-fw-awmf-tm](https://github.com/o-ran-sc/aiml-fw-awmf-tm), +11 more

### 5G

- ⚠️ [srsRAN_Project](https://github.com/srsran/srsRAN_Project) `[2026-06]` - A complete ORAN-native 5G RAN solution. _Archived Feb 2026; successor is [OCUDU](https://ocudu.org/), a Linux Foundation project for open-source AI-RAN._
- [OAI NR](https://gitlab.eurecom.fr/oai/openairinterface5g/wikis/5g-nr-development-and-releases) `[2026-07]` - 5GNR related branch of the OAI code. You can follow the [weekly updates](https://trello.com/c/XBVaaHIO/26-5g-nr) to stay up to date.
- [UERANSIM](https://github.com/aligungr/UERANSIM) `[2026-07]` - UERANSIM is the state-of-the-art 5G UE and RAN (gNodeB) simulator. The project can be used for testing 5G Core Network and studying 5G System.
- ⚠️ [Software gNB for free5GC](https://github.com/Srajdax/gnb) `[2020-11]` - The gNB function was built on the model of the other free5GC CN functions using all the pattern and helper class defined by the free5GC team.
- [5G-tools.com](https://5g-tools.com/) - 5G-tools.com is devoted to modern standards of wireless communications, such as 5G, 4G, etc. Main mission of site to give engineers the useful software tools to create a wireless network
- ⚠️ [corescope](https://github.com/srsran/corescope) `[2021-12]` - CoreScope combines gNodeB and UE components without any radio transmission.
- [my5G-RANTester](https://github.com/my5G/my5G-RANTester) `[2024-04]` - my5G-RANTester is a gNB/UE simulator for testing 3GPP standards and stressing a 5G core.
- [free5GRAN](https://github.com/IMTSDRLab/free5GRAN) `[2021-10]` - free5GRAN is an open-source 5G RAN stack. The current version includes a receiver which decodes MIB & SIB1 data. It also acts as a cell scanner. free5GRAN works in SA mode. From Telecom Paris 5G laboratory - Institut Polytechnique de Paris.
- [pfm](https://github.com/arv-sajeev/pfm) `[2021-11]` - Implemented a prototype of gNB-CU-UP a network element of 5G Radio Network. Using DPDK, a set of data-plane processing libraries and NIC drivers for high speed packet processing applications.
- [PacketRusher](https://github.com/HewlettPackard/PacketRusher) `[2026-03]` - High performance 5G UE/gNB Simulator and CP/UP load tester. PacketRusher is an open-source tool dedicated to the performance testing and automatic validation of 5G Core Networks using simulated UE (user equipment) and gNodeB (5G base station). From Valentin D'Emmanuele - France.
- [py3gpp](https://github.com/catkira/py3gpp) `[2026-07]` - A Python package for 5G-NR simulations.
- [RFSwift](https://github.com/PentHertz/RF-Swift) `[2026-07]` -  powerful multi-platform RF toolbox that deploys specialized radio tools in seconds on Linux, Windows, and macOS. Provdes telecom_4G_5GNSA_* family of telecoms tools.
- [NVIDIA Aerial](https://github.com/NVIDIA/aerial-cuda-accelerated-ran) `[2026-05]` - SDK for building commercial-grade, AI-native, 3GPP and O-RAN compliant 5G/6G gNB software on NVIDIA GPU-accelerated platforms.
- [NVIDIA Aerial Framework](https://github.com/NVIDIA/aerial-framework) `[2025-12]` - Python toolchain for generating GPU-accelerated 5G/6G pipelines. MLIR-TensorRT compilation and real-time runtime. Companion to Aerial SDK.
- [alsoran](https://github.com/nplrkn/alsoran) `[2025-06]` - 5G gNodeB Centralized Unit (gNB-CU) written in Rust. From the author of qcore.
- [gnbsim (SD-Core)](https://github.com/omec-project/gnbsim) `[2026-07]` - gNB and UE simulator for testing 5G core networks, from the SD-Core/OMEC project.
- [free-ran-ue](https://github.com/free-ran-ue/free-ran-ue) `[2026-07]` - Next-generation open-source 5G RAN/UE simulator for free5GC with web frontend, multi-UE and ULCL support. Written in Go.
- [NIST O-RAN Testbed Automation](https://github.com/usnistgov/O-RAN-Testbed-Automation) `[2026-07]` - Turn-key automation for deploying 5G O-RAN testbeds. Supports Open5GS, OAI, free5GC, srsRAN, multiple UPFs and xApps. From NIST.
- [ns-O-RAN-flexric](https://github.com/Orange-OpenSource/ns-O-RAN-flexric) `[2026-07]` - RAN simulator with E2 termination compliant with FlexRIC. Supports E2AP v1.01, KPM v3, RC v1.01. From Orange.
- [ns3-oran](https://github.com/usnistgov/ns3-oran) `[2026-05]` - ns-3 module for modeling O-RAN-like behavior with Near-RT RIC, E2 reporting, and ML model support. From NIST.
- [sim-ns3-o-ran-e2](https://github.com/o-ran-sc/sim-ns3-o-ran-e2) `[2025-11]` - ns-3 module with O-RAN-compliant E2 interface support. From O-RAN SC.
- [NextMN-SRv6](https://github.com/nextmn/SRv6) `[2026-07]` - Experimental SRv6 MUP Endpoint Behaviors implementation (RFC 9433) for mobile user plane. From NextMN.
- [NextMN-UE-Lite](https://github.com/nextmn/UE-Lite) `[2026-07]` - Experimental 5G UE simulator from the NextMN project. Companion to [gNB-Lite](https://github.com/nextmn/gNB-Lite) and [CP-Lite](https://github.com/nextmn/CP-Lite).
- [Sionna Research Kit](https://github.com/NVlabs/sionna-rk) `[2026-07]` - GPU-accelerated research platform for AI-RAN from NVIDIA. Extends Sionna for AI-native radio access network research.
- [xDevSM xApps Examples](https://github.com/wineslab/xDevSM-xapps-examples) `[2026-07]` - Reference xApps built on the xDevSM framework for OSC Near-RT RIC. Companion to xDevSM. From WiNES Lab.
- [dApp-openairinterface5g](https://github.com/wineslab/dApp-openairinterface5g) `[2026-06]` - Custom OpenAirInterface 5G fork with the E3 Agent integrated for distributed Apps (dApps). From WiNES Lab.
- [srsRAN-docker (ONF)](https://github.com/opennetworkinglab/srsRAN-docker) `[2026-07]` - Docker build for srsRAN, packaged by Open Networking Foundation for Aether/SD-Core deployments.
- [o-du-phy-rel-f](https://github.com/NUS-CIR/o-du-phy-rel-f) `[2026-02]` - Mirror of O-DU PHY F-release with OAI patches, easing review of OAI changes to xRAN. From NUS-CIR.


- [srsGUI](https://github.com/srsran/srsGUI) `[2024-08]` - A graphics library for software radio.
- [BTS_Research](https://github.com/cn0xroot/BTS_Research) `[2025-05]` - 基于 SDR 开源方案& 商业授权方案 实现 2-5G 安全研究的一些资源整合.
- [TetraEar](https://github.com/syrex1013/TetraEar) `[2026-02]` - TETRA decoder for RTL-SDR with voice decoding, encryption support, and real-time spectrum analyzer.
- [srsRAN_4G_docs](https://github.com/srsran/srsRAN_4G_docs) `[2025-02]` - Documentation for srsRAN_4G from Software Radio Systems (SRS).
- [rt-mbms-modem](https://github.com/5G-MAG/rt-mbms-modem) `[2025-10]` - This repository holds an MBMS Modem, which main task is to convert a 5G BC input signal (received either as live I/Q raw data from the SDR or as prerecorded SDR sample file) to multicast IP packets on the output.
- [colosseum-scope-e2](https://github.com/wineslab/colosseum-scope-e2) `[2025-12]` - O-RAN E2 termination for SCOPE framework.
- [ran-tester-ue](https://github.com/oran-testing/ran-tester-ue) `[2026-07]` - Open source RAN UE centric security testing software.
- [op25-radio-stream](https://github.com/MostlyBuilds/op25-radio-stream) `[2026-05]` - OP25-based P25 radio decoder for RTL-SDR that runs in Docker and streams audio as an always-on RTSP/HLS feed through MediaMTX.
- [srsRAN_Project_Low_Latency](https://github.com/aygong/srsRAN_Project_Low_Latency) `[2025-09]` - Code for the paper "Towards URLLC with Open-Source 5G Software".
- [o-ran-e2sim](https://github.com/wineslab/o-ran-e2sim) `[2025-12]` - O-RAN E2 termination simulator from WiNES Lab.
- [open-ran-commercial-traffic-twinning-dataset](https://github.com/wineslab/open-ran-commercial-traffic-twinning-dataset) `[2025-12]` - Partially supported by the O-RAN ALLIANCE, by the U.S. NSF under grants CNS-1925601, CNS-2112471 and CNS-2120447, by the U.S. NTIA’s PWSCIF under Award No. 25-60-IF011, by the bRAIN project PID2021-128250NB-I00 funded by MCIN/AEI/10.13039/50 1100011033, and by the European Union ERDF "A way of making Europe.".
- [srsRAN_docs](https://github.com/srsran/srsRAN_docs) `[2023-08]` - Landing page for srsRAN Project and srsRAN 4G documentation.
- [OAI-colosseum-ric-integration](https://github.com/wineslab/OAI-colosseum-ric-integration) `[2023-03]` - OpenAirInterface integration with the Colosseum O-RAN testbed RIC. From WiNES Lab.
- [ns3-ntn-toolkit](https://github.com/Muhammaduazir69/ns3-ntn-toolkit) `[2026-07]` - End-to-end ns-3.43 simulator for 6G non-terrestrial networks. Five integrated modules: 3GPP Rel-17 TTE-aware Conditional Handover, O-RAN Near-RT + Space RIC with 13 xApps, sub-THz/THz physics (HITRAN, UM-MIMO, RIS, ISAC), ns3-ai fork with federated learning, NTN traffic — over SNS3, mmWave-NR, 3GPP TR 38.811. LEO/MEO/GEO.
- [srsRAN_Project_jbpf](https://github.com/xfoukas/srsRAN_Project_jbpf) `[2026-01]` - srsRAN Project fork with eBPF-based observability hooks (jbpf) for low-overhead RAN telemetry.
- [explora](https://github.com/wineslab/explora) `[2023-11]` - Code for the paper EXPLORA: AI/ML EXPLainability for the Open RAN Claudio Fiandrino, Leonardo Bonati, Salvatore d'Oro, Michele Polese, Tommaso Melodia, Joerg Widmer CoNEXT ’23, December 5–8, 2023, Paris, France DOI: 10.1145/3629141.
- [hybrid-gnss-5g-testbed](https://github.com/karim4353/hybrid-gnss-5g-testbed) `[2025-10]` - Starter testbed for hybrid GNSS–5G positioning in degraded environments (urban/indoor/tunnel). Python fallback (notebooks, simulator, algorithms, UI), optional MATLAB pseudocode, SDR integration guides, CI and example datasets. MIT.
- [xapp-oai](https://github.com/wineslab/xapp-oai) `[2025-05]` - xApp targeting OpenAirInterface 5G integration for the O-RAN Near-RT RIC. From WiNES Lab.
- [ue-nib-library](https://github.com/nokia/ue-nib-library) `[2021-07]` - A library that works together with Nokia’s UEEC xApp.
- [DRL-for-ORAN-Resource-Allocation](https://github.com/Rashadows/DRL-for-ORAN-Resource-Allocation) `[2026-02]` - Performance evaluation of several DRL algorithms in a discrete action-space for resource allocation in Open RAN.
- [OFDM_SDR_System](https://github.com/ctegdf/OFDM_SDR_System) `[2025-12]` - A Python implementation of an OFDM communication system from scratch. Visualize the physics of 5G/WiFi.
- [Q-RAN](https://github.com/coranlabs/Q-RAN) `[2025-10]` - Q-RAN: Quantum Secure O-RAN.
- [5g-RF-Hack-RedTeam](https://github.com/KevinDevSecOps/5g-RF-Hack-RedTeam) `[2025-09]` - Red Team toolkit for 5G security research using SDR (HackRF, Flipper Zero, etc.) Hecho con ♦️por CK.
- [OAI-Slicing-Intel](https://github.com/wineslab/OAI-Slicing-Intel) `[2024-03]` - RAN Slicing Code Based on OpenAirInterface 5G.
- [srs-5g-dashboard](https://github.com/shariquetelco/srs-5g-dashboard) `[2026-01]` - Real-time monitoring dashboard for srsRAN 5G gNB - IABG mbH.
- [rtl-sdr](https://gitea.osmocom.org/sdr/rtl-sdr) - Software to turn the RTL2832U into a SDR receiver. Hosted on **Osmocom Gitea**.
- [libosmo-dsp](https://gitea.osmocom.org/sdr/libosmo-dsp) - A library with SDR DSP primitives. Hosted on **Osmocom Gitea**.
- [srsRAN](https://gitea.osmocom.org/fixeria/srsRAN) - Open source SDR 4G/5G software suite with extNAS/RRCTL support (forked from https://github.com/srsran/srsRAN). Hosted on **Osmocom Gitea**.
- [sdrangelove](https://gitea.osmocom.org/sdr/sdrangelove) - SDR GUI supporting various input hardware. Hosted on **Osmocom Gitea**.
- [libmirisdr](https://gitea.osmocom.org/sdr/libmirisdr) - Software for the Mirics MSi2500 + MSi001 SDR platform. Hosted on **Osmocom Gitea**.
- [rt-mbs-examples](https://github.com/5G-MAG/rt-mbs-examples) `[2026-07]` - 5G-MAG reference tools and examples for 5G Multicast Broadcast Services (MBS).
- [5G-MAG Media Streaming & Broadcast](https://github.com/5G-MAG) `[2026-06]` - 5G-MAG Reference Tools for 5G Media Streaming and 5G Broadcast/MBMS: [5GMS Application Function](https://github.com/5G-MAG/rt-5gms-application-function) `[2026-06]`, [5GMS Application Server](https://github.com/5G-MAG/rt-5gms-application-server) `[2026-02]`, [libflute (FLUTE)](https://github.com/5G-MAG/rt-libflute) `[2026-04]`, [MBMS transmitter](https://github.com/5G-MAG/rt-mbms-tx) `[2025-10]`, [MBMS middleware](https://github.com/5G-MAG/rt-mbms-mw) `[2025-10]`.
- [NR-Scope](https://github.com/PrincetonUniversity/NR-Scope) `[2026-07]` - 5G Standalone cellular network telemetry tool for network measurement. From Princeton.
### 4G

- [OAI eNB/ gNB](https://gitlab.eurecom.fr/oai/openairinterface5g/wikis/home) `[2026-07]` - Open Air Interface RAN 4G eNB / 5G NR gNB to use on SDR-based radios.
- [srsLTE](https://github.com/srsran/srsRAN_4G) `[2026-01]` - srsLTE eNB 4G to use on SDR-based radios.
- ⚠️ [LTE-ciphercheck](https://github.com/mrlnc/LTE-ciphercheck) `[2022-09]` - srsLTE derivative to check for cipher configuration of an LTE network - test across the 256 possibilities using an SDR radio.
- ⚠️ [OpenLTE](https://sourceforge.net/projects/openlte/) - OpenLTE is an open source implementation of the 3GPP LTE specifications from Ben Wojtowicz. GNU Radio applications for LTE downlink/uplink with RTL-SDR, HackRF, USRP. Hosted on **SourceForge**. _Last updated 2021._
- ⚠️ [Cisco 4G nFAPI](https://github.com/cisco/open-nFAPI) `[2018-08]` - Open-nFAPI is implementation of the Small Cell Forum's network functional API or nFAPI for short. nFAPI defines a network protocol that is used to connect a Physical Network Function (PNF) running LTE Layer 1 to a Virtual Network Function (VNF) running LTE layer 2 and above.
- ⚠️ [CrocodileHunter](https://github.com/EFForg/crocodilehunter) `[2023-02]` - Crocodile Hunter is a tool to hunt fake eNodeBs, also known commonly as hailstorm, stingray, cell site simulators, or IMSI catchers. It works by listening for broadcast messages from all of the 4G stations in the area, inferring their location, and looking for unusual activity. From the EFF.
- [eNB s1 emulator](https://github.com/fasferraz/eNB) `[2026-01]` - This is an eNB emulator application done in python3 to interact with MME (S1AP) and SGW (S1-U). This application can be used to perform and simulate several EMM and ESM procedures, including user plane traffic. This application was tested with real MMEs (lab environment).
- [radisys_lte_enb_for_qualcomm_fsm9955](https://github.com/laf0rge/radisys_lte_enb_for_qualcomm_fsm9955) `[2021-06]` - Radisys Open Source code for a LTE eNB on Qualcomm FSM9955
- [sigover_injector](https://github.com/SysSec-KAIST/sigover_injector) `[2022-05]` - A tool for SigOver, signal overshadowing attack on the LTE broadcast signals in physical domain.

### 3G

- [OpenUMTS](https://github.com/RangeNetworks/OpenBTS-UMTS) `[2024-07]` - 3G NodeB
- [openbts-UMTS](https://github.com/PentHertz/OpenBTS-UMTS) `[2024-07]` - updated dependency and code to run OpenBTS-UMTS in 2023. Docker image available [here](https://hub.docker.com/r/penthertz/openbts-umts)
- [OsmoHNodeB](https://osmocom.org/projects/osmo-hnodeb) - Open Source implementation of the upper layers (RANAP/RUA/HNBAP/GTP/RTP) of a hNodeB.  Not usable standalone, requires lower-layer (RRC/RLC/MAC/PHY).

### 2G

- ⚠️ [OpenBTS](http://openbts.org) - 2G BTS with SDR-based radios. _Project discontinued; consider OsmoBTS for 2G needs._ See also [PentHertz/OpenBTS](https://github.com/PentHertz/OpenBTS) `[2025-07]` updated fork for Ubuntu 22/24 with latest UHD drivers.
- [YateBTS](https://wiki.yatebts.com/index.php/Main_Page) - 2G BTS with SDR-based radios.
- [OsmoTRX](https://osmocom.org/projects/osmotrx) - fork of OpenBTS tranceiver to use on SDR-based radios.
- [OsmoBTS](https://osmocom.org/projects/osmobts) - Open Source GSM BTS (Base Transceiver Station) with A-bis/IP interface.
- [OsmoPCU](https://osmocom.org/projects/osmopcu/wiki/OsmoPCU) - Open source GPRS PCU (Packet Control Unit) with Gb/IP interface. Supports OsmoBTS as well as Ericsson RBS2000/RBS6000.
- [OsmoBSC](https://osmocom.org/projects/osmobsc/wiki) - Open Source BSC (Base Station Controller) with Abis/E1 and Abis/IP support. Works with OsmoBTS, nanoBTS and various Nokia, Ericsson and Siemens BTS models.
- [osmo-trx](https://gitea.osmocom.org/cellular-infrastructure/osmo-trx) - Osmocom GSM/GPRS/EGPRS transceiver, originally forked from OpenBTS transceiver. For building SDR based GSM BTS with osmo-bts-trx. Hosted on **Osmocom Gitea**.
- [sim-tools](https://github.com/herlesupreeth/sim-tools) `[2021-01]` - Clone from the Osmocom sim-tools.git with added features
- [pysim](https://github.com/herlesupreeth/pysim) `[2025-05]` - Pysim repository from Osmocom with added features
- Additional cellular-infrastructure sub-projects: [meta-telephony](https://gitea.osmocom.org/cellular-infrastructure/meta-telephony), [libasn1c](https://gitea.osmocom.org/cellular-infrastructure/libasn1c), [mncc-python](https://gitea.osmocom.org/cellular-infrastructure/mncc-python), [training-materials](https://gitea.osmocom.org/cellular-infrastructure/training-materials), [asn1_docextract](https://gitea.osmocom.org/cellular-infrastructure/asn1_docextract)
- Additional osmocom sub-projects: [3grr](https://gitea.osmocom.org/osmocom/3grr), [docker-playground](https://gitea.osmocom.org/osmocom/docker-playground), [gapk](https://gitea.osmocom.org/osmocom/gapk), [libosmo-gprs](https://gitea.osmocom.org/osmocom/libosmo-gprs), [libosmo-netif](https://gitea.osmocom.org/osmocom/libosmo-netif), [libosmo-sigtran](https://gitea.osmocom.org/osmocom/libosmo-sigtran), [libosmocore](https://gitea.osmocom.org/osmocom/libosmocore), [pyhss](https://gitea.osmocom.org/osmocom/pyhss), +1 more

### TETRA

- [osmo-tetra](https://gitea.osmocom.org/tetra/osmo-tetra) - TETRA PHY/MAC layer implementation in C/Python. Supports receiving and decoding TETRA signals with SDR hardware (USRP, HackRF). Hosted on **Osmocom Gitea**.


- [Pocket25](https://github.com/SarahRoseLives/Pocket25) `[2026-07]` - Pocket25 - The Mobile P25 Radio Decoder.
- [dsd-neo](https://github.com/arancormonk/dsd-neo) `[2026-07]` - A modern, modular, and performance enhanced C/C++ decoder for digital voice. DMR, P25, NXDN, YSF, and more.
- [NyxScope](https://github.com/ICBizLabs/NyxScope) `[2026-07]` - Multi-protocol SDR receiver for Windows bundling open-source decoders (P25 Phase 1+2, DMR, NXDN and more) behind one UI.
- [Mobile-Trunked-Radio-Decoder](https://github.com/chrismuntean/Mobile-Trunked-Radio-Decoder) `[2026-03]` - Hardware stuff for mobile P25 phase 1 & 2 trunked radio decoder.
- [rtl_p25](https://github.com/rhodey/rtl_p25) `[2025-07]` - Command-line P25 decoder with liquid-dsp.
- [OpenScanner](https://github.com/briannippert/OpenScanner) `[2026-07]` - RTL-SDR web interface with P25 decoding.
- [OpenWebRX-Tetra-Plugin](https://github.com/mbbrzoza/OpenWebRX-Tetra-Plugin) `[2026-06]` - TETRA decoder module for OpenWebRX+ enabling reception and decoding of TETRA (Terrestrial Trunked Radio) digital radio signals in a web browser.
- [TetraDMO-Receiver](https://github.com/ctn008/TetraDMO-Receiver) `[2025-08]` - Fork from tetra-kit decoder to include option to decode DMO tetra signal from file.
- [florianpose/tetra-location-display](https://gitlab.com/florianpose/tetra-location-display) `[2026-02]` - PyQt5 Application for displaying vehicle positions received via Tetra PEI. Hosted on **GitLab**.
- [osmo-tetra-bb](https://gitea.osmocom.org/tetra/osmo-tetra-bb) - Custom DMO firmware for Motorola MTH300/Dolphin d700 TETRA handsets. Hosted on **Osmocom Gitea**.
- [trunk-recorder](https://github.com/TrunkRecorder/trunk-recorder) `[2026-07]` - Records calls from trunked radio systems (P25 & SmartNet) using SDR.
- [MMDVM_HS](https://github.com/juribeparada/MMDVM_HS) `[2026-07]` - MMDVM hotspot firmware for ZUMspot/MMDVM_HS boards (DMR, D-Star, etc.).
- [tetra-bluestation](https://github.com/MidnightBlueLabs/tetra-bluestation) `[2026-07]` - Implementation of large parts of the TETRA stack, from the TETRA:BURST team.
- [sdrpp-tetra-demodulator](https://github.com/cropinghigh/sdrpp-tetra-demodulator) `[2026-06]` - TETRA demodulator plugin for SDR++.
- [tetra-rtlsdr](https://github.com/alphafox02/tetra-rtlsdr) `[2026-02]` - RTL-SDR front-end for TETRA/telive, replacing GnuRadio with a single command.
- [flowstation](https://github.com/razvanzeces/flowstation) `[2026-07]` - TETRA base station in software, runs on Raspberry Pi.
- [turbine](https://github.com/norasector/turbine) `[2026-02]` - SDR software for capturing trunked radio systems.
- [GopherTrunk](https://github.com/MattCheramie/GopherTrunk) `[2026-07]` - Pure-Go, cross-platform RTL-SDR trunked-radio scanner and audio toolkit.
- [node-dmr-lib](https://github.com/rick51231/node-dmr-lib) `[2026-01]` - Motorola MotoTRBO DMR protocol research library.
- [p25-survey](https://github.com/blantonl/p25-survey) `[2026-05]` - Scan a frequency range for P25 control channels and log system metadata.
- [sigint](https://github.com/arall/sigint) `[2026-06]` - Multi-protocol SDR signal detection and triangulation system for ATAK.
- [op25 (boatbod)](https://github.com/boatbod/op25) `[2026-06]` - Actively-maintained fork of Osmocom OP25; the canonical P25 (phase 1 & 2) decoder for SDR.
- [OpenDMR](https://github.com/MW0MWZ/OpenDMR) `[2025-12]` - Open-source DMR AMBE codec for encoding/decoding DMR voice to/from PCM.
- [tr-stack](https://github.com/trunk-reporter/tr-stack) `[2026-07]` - Full P25 transcription stack: trunk-recorder + tr-engine + tr-dashboard integrated.
### Analog / 1G

- [osmocom-analog](https://gitea.osmocom.org/cellular-infrastructure/osmocom-analog) - Analog cellular network implementations: A-Netz, B-Netz, C-Netz, NMT, AMPS, TACS, and more. Hosted on **Osmocom Gitea**.
- [osmocom-analog-libraries](https://gitea.osmocom.org/cellular-infrastructure/osmocom-analog-libraries) - Various libraries developed in the context of osmocom-analog; mostly related to SDR and analog modulation/DSP/DTMF/telephony, audio processing etc. Hosted on **Osmocom Gitea**.

### PHY
- [gr-osmoSDR](https://osmocom.org/projects/gr-osmosdr) - Unified gnuradio input/output block for a variety of SDR devices, including FUNcube Dongle, OsmoSDR, RTL-SDR, MSi2500, SDRplay, SDR-IQ, AirSpy, rad10, HackRF, bladeRF, USSRP/UHD, UMtrx, RedPitaya, FreeSRP.
- [gr-gsm](https://github.com/ptrkrysik/gr-gsm) `[2025-03]` - GNU Radio blocks and tools for receiving GSM transmissions.
- [USRP B210](https://www.ettus.com/all-products/UB210-KIT/) - SDR Radio kit compatible with most of the SDR-based software modem implementations.
- [LimeSDR](https://limemicro.com/products/boards/limesdr/) - Affordable full-duplex SDR board, popular for srsRAN and OAI experimentation.
- [BladeRF](https://www.nuand.com/) - USB 3.0 SDR platform compatible with open source cellular stacks.
- [libresdr-fw-timestamps](https://github.com/pumatrax/libresdr-fw-timestamps) `[2025-11]` - LibreSDR firmware builds with timestamp support, enabling LTE/srsRAN use on this low-cost PlutoSDR derivative.
- [Kalibrate](https://github.com/steve-m/kalibrate-rtl) `[2023-08]` - Kalibrate, or kal, can scan for GSM base stations in a given frequency band and can use those GSM base stations to calculate the local oscillator frequency offset.
- [rtl-sdr](https://github.com/osmocom/rtl-sdr) `[2026-02]` - Library for turning a RTL2832-based DVB dongle into a Software Defined Receiver. Foundational for low-cost SDR-based cellular signal reception.
- ⚠️ [open5G_phy](https://github.com/catkira/open5G_phy) `[2025-04]` - A resource-efficient, customizable, synthesizable 5G NR lower PHY written in Verilog for FPGA targets.
- [neural_rx](https://github.com/NVlabs/neural_rx) `[2025-12]` - Real-time inference of 5G NR multi-user MIMO neural receivers from NVIDIA Research.
- [SoftNB](https://github.com/beginnerzjz/SoftNB) `[2025-09]` - SDR-based NB-IoT PHY signal processing.
- [zynq_timestamping](https://github.com/srsran/zynq_timestamping) `[2023-01]` - Open source Zynq FPGA timestamping for precise SDR timing in 5G RAN deployments. From SRS.
- [CyberEther](https://github.com/PentHertz/CyberEther) `[2026-03]` - High-performance GPU-accelerated signal processing and visualization framework. Runs anywhere. From PentHertz.
- [osmo-fl2k](https://gitea.osmocom.org/sdr/osmo-fl2k) - Turns USB 3.0 VGA adapters (FL2000-based) into low-cost SDR transmitters. Hosted on **Osmocom Gitea**.
- [gr-fosphor](https://gitea.osmocom.org/sdr/gr-fosphor) - GNU Radio spectrum visualization block with GPU-accelerated real-time waterfall display. Hosted on **Osmocom Gitea**.
- [GeoLibCov](https://github.com/Orange-OpenSource/GeoLibCov) `[2026-02]` - Geographic library for cell coverage modelling and topography generation. From Orange.
- [DragonOS](https://sourceforge.net/projects/dragonos-focal/) - Debian/Ubuntu-based Linux distro with 30+ pre-installed SDR tools (GNU Radio, gr-gsm, GQRX, etc.) for RF analysis, spectrum monitoring and telecom security. Hosted on **SourceForge**.
- [Gqrx SDR](https://www.gqrx.dk/) - Open source SDR receiver powered by GNU Radio, supporting RTL-SDR, HackRF, LimeSDR, USRP and more. [SourceForge](https://sourceforge.net/projects/gqrx/).
- [ML5G-PS-005](https://github.com/usnistgov/ML5G-PS-005) `[2023-05]` - Digital-twin-enabled 6G: Depth Map Estimation in mmWave systems
- [gr-soapy](https://gitlab.com/librespacefoundation/gr-soapy) `[2025-07]` - A GNURadio wrapper for the SoapySDR library Hosted on **GitLab**.
- [aml-jens](https://github.com/telekom/aml-jens) `[2025-10]` - JENS - a tool to simulate L4S marking of a Baseband Unit
- ⚠️ [gr-msod-sensor](https://github.com/usnistgov/gr-msod-sensor) `[2017-04]` - Gnuradio based Sensor for RF measurements that works with the Measured Spectrum Occupancy Database
- [sigint](https://github.com/petermartis/sigint) `[2026-03]` - Autonomous radio scanner & decoder for Raspberry Pi with RTL-SDR. Supports TETRA, DMR, P25, NXDN, dPMR, FM, AM.
- ⚠️ [rtlsdr-tv-whitespace-monitor](https://github.com/usnistgov/rtlsdr-tv-whitespace-monitor) `[2016-04]` - A TV whitespace monitor that uses RTL SDR.
- [ns3-mmwave-hbf](https://codeberg.org/gomezcuba/ns3-mmwave-hbf) - Hybrid Beamforming in 5G mmWave Networks: a Full-stack Perspective forked from https://github.com/mychele/ns3-mmwave-hbf Hosted on **Codeberg**.
- Additional sdr sub-projects: [gr-osmosdr](https://gitea.osmocom.org/sdr/gr-osmosdr), [gr-iqbal](https://gitea.osmocom.org/sdr/gr-iqbal), [gr-gsm](https://gitea.osmocom.org/sdr/gr-gsm), [airprobe](https://gitea.osmocom.org/sdr/airprobe), [ais-tx](https://gitea.osmocom.org/sdr/ais-tx), [libusrp](https://gitea.osmocom.org/sdr/libusrp)


## Core Network

### 5G

- [Open5GS](https://open5gs.org) `[2025-12]` - 5G, R14 4G EPC core with independent MME, HSS, SGW, PGW, PCRF, UPF, SMF, NRF functions. Follow-up of NextEPC. [github](https://github.com/open5gs)
- [OAI 5GCN](https://gitlab.eurecom.fr/oai/cn5g) - OAI(Open Air Interface) was initially developed by EURECOM, provides a 3GPP-Compliant 5G SA Core Network.
- ⚠️ [travelping-vpp](https://github.com/travelping/vpp) `[2021-01]` - UPF plugins implements a GTP-U user plane based on 3GPP TS 23.214 and 3GPP TS 29.244 Release 15, adding UPF as a plugin to VPP.
- ⚠️ [IITB 5G SBA PoC](https://github.com/iithnewslab/SBA-gRPC-5G) `[2019-08]` - Prototyping and Load Balancing the Service Based Architecture of 5G Core using NFV - [research paper from IITB](https://github.com/iithnewslab/SBA-gRPC-5G/blob/master/Presentation_Netsoft19_gRPC_5G.pdf)
- [Free5GC](https://www.free5gc.org/) `[2026-07]` - The free5GC is an open-source project for 5th generation (5G) mobile core network hosted by [CS Lab](https://cslab.cs.nycu.edu.tw/). Written in Golang. Per-NF repos: [AMF](https://github.com/free5gc/amf), [SMF](https://github.com/free5gc/smf), [AUSF](https://github.com/free5gc/ausf), [UDM](https://github.com/free5gc/udm), [UDR](https://github.com/free5gc/udr), [PCF](https://github.com/free5gc/pcf), [NRF](https://github.com/free5gc/nrf), [NSSF](https://github.com/free5gc/nssf), [NEF](https://github.com/free5gc/nef), [CHF](https://github.com/free5gc/chf), [N3IWF](https://github.com/free5gc/n3iwf), [TNGF](https://github.com/free5gc/tngf), [TNGFUE](https://github.com/free5gc/tngfue). Protocols: [NGAP](https://github.com/free5gc/ngap), [NAS](https://github.com/free5gc/nas), [PFCP](https://github.com/free5gc/pfcp), [SCTP](https://github.com/free5gc/sctp), [aper (PER)](https://github.com/free5gc/aper), [TLV](https://github.com/free5gc/tlv). Tooling: [openapi](https://github.com/free5gc/openapi), [util](https://github.com/free5gc/util), [webconsole](https://github.com/free5gc/webconsole), [go-gtp5gnl](https://github.com/free5gc/go-gtp5gnl).
- [5GC Swagger APIS](https://github.com/jdegre/5GC_APIs) `[2024-06]` - RESTful APIs of main Network Functions in the 3GPP 5G Core Network. R16.
- [5G GTP kernel driver](https://github.com/free5gc/gtp5g) `[2026-03]` - gtp5g is a customized Linux kernel module 5G GTP-U to handle packet by PFCP IEs such as PDR and FAR. Per 3GPP TS 29.281 and 3GPP TS 29.244.
- [UPF (OMEC)](https://github.com/omec-project/upf) `[2026-07]` - 4G/5G Mobile Core User Plane from the OMEC/SD-Core project. Successor to upf-epc.
- [OpenUPF](https://github.com/5GOpenUPF/openupf) `[2021-05]` - A 3GPP R16 compliant open source 5G core UPF (User Plane Function).
- [Katana Slice Manager](https://github.com/medianetlab/katana-slice_manager) `[2026-04]` - Katana Slice Manager is a central software component responsible for controlling all the devices comprising the network, providing an interface for creating, modifying, monitoring and deleting slices.
- [my5G-core](https://github.com/my5G/my5G-core) `[2021-01]` - Currently, my5G-core is a fork of the free5GC project, with some extensions to facilitate the deployment.
- [III-5GC-Free-Trial](https://github.com/III-5GC/III-5GC-Free-Trial) `[2021-05]` - The basic III-5GC is a free trial for lab research, prototype product testing and simple 5G end-to-end demonstration.
- [upf-bpf](https://github.com/navarrothiago/upf-bpf) `[2024-09]` - An open source C++ library powered by eBPF/XDP for user plane in mobile core network (5G/LTE).
- [5G_CN](https://github.com/wnlUc3m/5G_CN) `[2019-08]` - This is a basic implementation of a 5G Core Network supporting 4G LTE control signalling.
- [openupf](https://github.com/5GOpenUPF/openupf) `[2021-05]` - A 3GPP R16 compliant open source 5G core UPF (User Plane Function).
- [upf-xdp](https://github.com/801room/upf-xdp) `[2021-01]` -  it shows the possibility of using xdp to implement 5g upf.
- [SD-Core](https://opennetworking.org/sd-core/) - A 4G/5G core based on [OMEC](https://www.opennetworking.org/omec/) for 4G and a fork of [Free5GC](https://www.free5gc.org/) for 5G, with a P4-based UPF. Per-NF repos: [AMF](https://github.com/omec-project/amf), [SMF](https://github.com/omec-project/smf), [AUSF](https://github.com/omec-project/ausf), [NRF](https://github.com/omec-project/nrf), [PCF](https://github.com/omec-project/pcf), [UDM](https://github.com/omec-project/udm), [UDR](https://github.com/omec-project/udr), [N3IWF](https://github.com/omec-project/n3iwf), [NGAP](https://github.com/omec-project/ngap), [NAS](https://github.com/omec-project/nas), [SIMAPP](https://github.com/omec-project/simapp).
- [Magma](https://github.com/magma/magma) `[2026-07]` - Rearchitected core network with access gateway (MME+P/SGW), federation gateway for auth (S6a) and billing (Gx, Gy). Initiated by FB on a the OAI EPC code base.
- ⚠️ [5GCoreNetSDK](https://github.com/5GCoreNet/5GCoreNetSDK) `[2023-06]` - 5GCoreNetSDK is a fully-featured Golang SDK for developing inside 5GC (Release-18).
- [eupf](https://github.com/edgecomllc/eupf) `[2026-02]` - Open Source UPF built on eBPF.
- [UPG-VPP](https://github.com/travelping/upg-vpp) `[2026-04]` - High-performance User Plane Gateway (UPG) based on FD.io VPP from Travelping.
- [qcore](https://github.com/nplrkn/qcore) `[2026-03]` - The world's most lightweight 5G Core (probably)
- [NEF_emulator](https://github.com/medianetlab/NEF_emulator) `[2025-02]` - Configurable emulated environment for providing 3GPP Network Exposure Function (NEF) APIs. Enables testing of network applications against 5GC exposure capabilities.
- [Ella Core](https://github.com/ellanetworks/core) `[2026-07]` - Lightweight 5G core for private networks. Single binary with embedded DB, web UI, REST API, and OpenTelemetry. Written in Go.
- [UnifyAir Core](https://github.com/unifyair/unifyair-core) `[2025-11]` - 5G Core Network Functions (AMF, UPF, SMF) implementation in Rust, based on 3GPP Release 17.
- [HEXAeBPF](https://github.com/coranlabs/HEXAeBPF) `[2025-10]` - eBPF-defined interoperable 5G Core (eDC).
- [NextMN-UPF](https://github.com/nextmn/UPF) `[2026-07]` - Experimental user-space 5G UPF in Go. Interoperable with free5GC and UERANSIM.
- [claudia-5gc](https://github.com/francurieses/claudia-5gc) `[2026-07]` - From-scratch 5G Core Standalone (3GPP Rel-17): NRF, AMF, SMF, UPF, PCF, UDM.
- [opensource-5g-core](https://github.com/UmakantKulkarni/opensource-5g-core) `[2026-05]` - Helm charts and Dockerfiles to deploy open-source 5G core network components.
- [go-upf](https://github.com/free5gc/go-upf) `[2026-07]` - Go-based UPF implementation for free5GC.
- [SigScale CHF](https://github.com/sigscale/chf) `[2026-05]` - 3GPP 5GC Charging Function (CHF) in Erlang. Part of the SigScale telecom stack.
- [QORE](https://github.com/coranlabs/QORE) `[2025-11]` - Quantum Secure Core: Beyond 5G Core integrated with Post-Quantum Cryptography and QRNG. From CoRAN Labs.
- ⚠️ [SEPP](https://github.com/ellanetworks/sepp) `[2025-08]` - Open source 5G Security Edge Protection Proxy. From Ella Networks.
- [free5gc n3iwue](https://github.com/free5gc/n3iwue) `[2026-05]` - N3IWF UE simulator for non-3GPP access testing. From the free5GC project.
- [upf_p4_poc](https://github.com/801room/upf_p4_poc) `[2020-10]` - Proof of concept for 5G UPF based on P4 programmable data plane. From the upf-xdp author.
- [NWDAF](https://github.com/net-ty/mnc_NWDAF) `[2024-01]` - Network Data Analytics Function (NWDAF) implementation in Go.
- [OAI CN5G NWDAF](https://gitlab.eurecom.fr/oai/cn5g/oai-cn5g-nwdaf) `[2026-04]` - OpenAirInterface NWDAF with AnLF and MTLF separation per 3GPP Release 17. Hosted on **GitLab (Eurecom)**.
- [closed-loop-nwdaf](https://github.com/fatemeshafiee/closed-loop-nwdaf) `[2025-12]` - NWDAF integrated with OAI and Open5GS for closed-loop security automation. ML model provisioning via MLflow.
- [open5gs-nwdaf](https://github.com/cem8kaya/open5gs-nwdaf) `[2026-07]` - Open-source NWDAF implementation for Open5GS, compliant with 3GPP TS 23.288.
- [OAI CN5G LMF](https://gitlab.eurecom.fr/oai/cn5g/oai-cn5g-lmf) `[2026-07]` - OpenAirInterface Location Management Function for 5G positioning (UL-TDoA). Hosted on **GitLab (Eurecom)**.
- [nokia 5G Network Emulator](https://github.com/nokia/5g-network-emulator) `[2026-06]` - 5G network emulator from Nokia.
- [SD-Core Helm Charts](https://github.com/omec-project/sdcore-helm-charts) `[2026-07]` - Official Helm charts for packaging and deploying the SD-Core 5G core (Aether/OMEC).
- [UE-non3GPP](https://github.com/LABORA-INF-UFG/UE-non3GPP) `[2025-02]` - Open-source User Equipment for non-3GPP access via N3IWF. Useful for testing 5G core untrusted/trusted Wi-Fi access flows.
- [opncell](https://github.com/opncell/opncell) `[2026-07]` - OPNsense plugin that adds private 5G/LTE network capability out-of-the-box by integrating Open5GS with the OPNsense firewall.
- [OAI CN5G AMF](https://gitlab.eurecom.fr/oai/cn5g/oai-cn5g-amf) `[2026-07]` - OpenAirInterface 5G Access and Mobility Management Function (AMF). Active C++ implementation, Apache 2.0. Hosted on **GitLab (Eurecom)**. Companion NFs: [SMF](https://gitlab.eurecom.fr/oai/cn5g/oai-cn5g-smf), [UPF](https://gitlab.eurecom.fr/oai/cn5g/oai-cn5g-upf), [NRF](https://gitlab.eurecom.fr/oai/cn5g/oai-cn5g-nrf), [AUSF](https://gitlab.eurecom.fr/oai/cn5g/oai-cn5g-ausf), [UDM](https://gitlab.eurecom.fr/oai/cn5g/oai-cn5g-udm), [UDR](https://gitlab.eurecom.fr/oai/cn5g/oai-cn5g-udr), [PCF](https://gitlab.eurecom.fr/oai/cn5g/oai-cn5g-pcf), [NSSF](https://gitlab.eurecom.fr/oai/cn5g/oai-cn5g-nssf), [NEF](https://gitlab.eurecom.fr/oai/cn5g/oai-cn5g-nef).
- [5gdeploy](https://github.com/usnistgov/5gdeploy) `[2026-05]` - 5G core deployment helper for spinning up multi-NF 5GC topologies with various open-source cores (Open5GS, free5GC, OAI). From NIST.
- [Rapid5GS](https://rapid5gs.com) `[2026-07]` - One-command installer that takes a bare Debian box to a working Open5GS EPC/5GC, with systemd services and a live throughput monitor. From Alabama Lightwave, a working WISP. [github](https://github.com/joshualambert/rapid5gs)
- [openpacketcore-sdk](https://github.com/openpacketcore/openpacketcore-sdk) `[2026-07]` - Rust SDK for building cloud-native 5G packet core network functions: runtime chassis and 3GPP protocol codecs (GTP and others).
- [BESS (UPF)](https://github.com/omec-project/bess) `[2026-07]` - Berkeley Extensible Software Switch fork used to develop the OMEC/SD-Core 5G UPF (User Plane Function).
- [Nephio free5GC operators](https://github.com/nephio-project/free5gc) `[2026-02]` - Nephio operators and packages for deploying free5GC on Kubernetes via the Nephio framework.


- [docker_open5gs_volte_sms_config](https://github.com/s5uishida/docker_open5gs_volte_sms_config) `[2023-12]` - VoLTE and SMS Configuration for docker_open5gs.
- [open5gs-b210](https://github.com/StevenVanAcker/open5gs-b210) `[2025-11]` - Installation scripts for a dockerized VoLTE setup using Open5GS with an Ettus USRP B210.
- [simple_measurement_of_upf_performance](https://github.com/s5uishida/simple_measurement_of_upf_performance) `[2025-01]` - Simple Measurement of UPF Performance.
- [Private-5g-setup-with-Open5gs-and-srsRAN-and-B210](https://github.com/ManojPandekamat/Private-5g-setup-with-Open5gs-and-srsRAN-and-B210) `[2025-07]` - Setting up a real time 5g network using **Open5gs** as core and srsRAN as RAN which is connected to real 5G COTS Devices (5G Mobiles) using USRP B210 as BASE Satation.
- [simple_measurement_of_upf_performance_6](https://github.com/s5uishida/simple_measurement_of_upf_performance_6) `[2026-01]` - Simple Measurement of UPF Performance 6.
- [Task-offloading-in-private-5g-network-using-usrpB210](https://github.com/RAHUL2052003/Task-offloading-in-private-5g-network-using-usrpB210) `[2025-08]` - Real-time private 5G network setup using Open5GS and srsRAN with USRP B210 for task offloading.
- [k8s_srsran_open5gs](https://github.com/sulaimanalmani/k8s_srsran_open5gs) `[2026-03]` - Containerized/kubernetes deployment of E2E 5G testbed using srsRAN and Open5gs.
- [simple_measurement_of_upf_performance_9](https://github.com/s5uishida/simple_measurement_of_upf_performance_9) `[2026-01]` - Simple Measurement of UPF Performance 9.
- [Open5gs_Config](https://github.com/herlesupreeth/Open5gs_Config) `[2021-05]` - Open5gs Configuration files for IMS/VoLTE.
- [docker-open5gs-basic-config](https://codeberg.org/boxedtoast/docker-open5gs-basic-config) - Stripped down LTE only open5gs docker configs. Hosted on **Codeberg**.
- [s5uishida sample-config catalog](https://github.com/s5uishida) - Reference deployment configurations for Open5GS/free5GC + UERANSIM/srsRAN/OAI permutations. Topology variants: [Open5GS+UERANSIM](https://github.com/s5uishida/open5gs_5gc_ueransim_sample_config), [free5GC+UERANSIM](https://github.com/s5uishida/free5gc_ueransim_sample_config), [Open5GS EPC+OAI](https://github.com/s5uishida/open5gs_epc_oai_sample_config), [Open5GS+srsRAN](https://github.com/s5uishida/open5gs_5gc_srsran_sample_config), [free5GC+srsRAN](https://github.com/s5uishida/free5gc_srsran_sample_config), [Open5GS EPC+srsRAN](https://github.com/s5uishida/open5gs_epc_srsran_sample_config). Feature variants: [Prometheus metrics](https://github.com/s5uishida/open5gs_5gc_ueransim_metrics_sample_config), [S-NSSAI UPF select (Open5GS)](https://github.com/s5uishida/open5gs_5gc_ueransim_snssai_upf_sample_config) / [(free5GC)](https://github.com/s5uishida/free5gc_ueransim_snssai_upf_sample_config), [nearby UPF (Open5GS)](https://github.com/s5uishida/open5gs_5gc_ueransim_nearby_upf_sample_config) / [(free5GC)](https://github.com/s5uishida/free5gc_ueransim_nearby_upf_sample_config), VPP/DPDK UPF [(Open5GS)](https://github.com/s5uishida/open5gs_5gc_ueransim_vpp_upf_dpdk_sample_config) / [(free5GC)](https://github.com/s5uishida/free5gc_ueransim_vpp_upf_dpdk_sample_config), eUPF [(Open5GS 5GC)](https://github.com/s5uishida/open5gs_5gc_ueransim_eupf_sample_config) / [(Open5GS EPC)](https://github.com/s5uishida/open5gs_epc_srsran_eupf_sample_config), ULCL [(simple)](https://github.com/s5uishida/free5gc_ueransim_ulcl_sample_config) / [(I-UPF + 2 PSA-UPFs)](https://github.com/s5uishida/free5gc_ueransim_ulcl_2_sample_config), [SCP Model C](https://github.com/s5uishida/open5gs_5gc_ueransim_scp_model_c_sample_config).
- [5g-ngap](https://github.com/sigscale/5g-ngap) `[2023-06]` - NG Application Protocol (NGAP) (3GPP TS 38.413).
- [upf-benchmark](https://gitea.osmocom.org/cellular-infrastructure/upf-benchmark) - Tools and configs to set up UPF benchmarking. Hosted on **Osmocom Gitea**.
- [sylva-core](https://gitlab.com/sylva-projects/sylva-core) `[2026-07]` - This repository contains the core development of the Sylva Telco Cloud Stack Hosted on **GitLab**.
- [note_5g_suci_profile_ab](https://github.com/s5uishida/note_5g_suci_profile_ab) `[2026-06]` - A Note for 5G SUCI Profile A/B Scheme
- [oai5g-rru](https://github.com/sopnode/oai5g-rru) `[2026-07]` - OpenAirInterface 5G Core Network Deployment on SophiaNode/R2lab using Helm Charts and nepi-ng
- [nas-models](https://github.com/UnifyAir/nas-models) `[2025-10]` - 5G NR Nas Models
- [nextgcore](https://github.com/NextgCoreLab/nextgcore) `[2026-07]` - Open-source NextG 5G core (EPC) implementation.
- [rt-5gc-service-consumers](https://github.com/5G-MAG/rt-5gc-service-consumers) `[2026-06]` - 5G-MAG reusable service-consumer libraries for interacting with 5GC network functions over the service-based interface.
- [telecom-platform](https://github.com/nutcas3/telecom-platform) `[2026-05]` - Full-stack sovereign private 5G/LTE platform covering core network integration, subscriber management, charging and developer APIs (Go/Rust/eBPF).
- Additional omec-project sub-projects: [nssf](https://github.com/omec-project/nssf)
### 4G

- ⚠️ [NextEPC](https://nextepc.org) - R13 4G EPC core with independent MME, HSS, SGW, PGW, PCRF functions. [github](https://github.com/nextepc/) _Superseded by Open5GS._
- ⚠️ [C3PO](https://github.com/omec-project/c3po) `[2022-03]` - HSS, CDF, CTF, PCRF around Cassandra DB, and backed by hardware security through SGX from the [OMEC](https://www.opennetworking.org/omec/).
- ⚠️ [NGIC-RTC](https://github.com/omec-project/ngic-rtc) `[2021-05]` - Control User Plane Separated (CUPS) architecture 3GPP TS23501 based implementation of EPC Service and Packet Gateway functions (SGW, PGW) from the [OMEC](https://www.opennetworking.org/omec/).
- ⚠️ [OpenMME](https://github.com/omec-project/openmme) `[2020-10]` - OpenMME is a grounds up implementation of the Mobility Management Entity EPC S1 front end to the Cell Tower (eNB) from the [OMEC](https://www.opennetworking.org/omec/).
- [srsEPC](https://github.com/srslte/srslte) `[2026-01]` - light-weight LTE core network implementation with MME, HSS and S/P-GW.
- [corenet](https://github.com/mitshell/corenet) `[2024-03]` - Minimal 3G and LTE / EPC core network using Pycrate library.
- [erGW](https://github.com/travelping/ergw) `[2022-03]` - This is a 3GPP GGSN and PDN-GW implemented in Erlang.
- [vEPC IITB](https://github.com/networkedsystemsIITB/NFV_LTE_EPC) `[2018-06]` - vEPC is a simple virtualized form of Long Term Evolution Evolved Packet Core (LTE EPC) from IITB india.
- [pyHSS](https://gitlab.com/nickvsnetworking/pyhss) `[2021-01]` - PyHSS is a simple Home Subscriber Server (HSS) used by LTE (4G) Evolved Packet Core (EPC) networks, written in Python. 3GPP network elements like the MME and PCRF communicate with the HSS via the DIAMETER protocol, with some extensions defined by 3GPP.
- [coreswitch](https://github.com/coreswitch/coreswitch) `[2019-09]` - coreswitch is an open soruce project for EPC (Evolved Packet Core) of LTE and 5G infrastructure. Right now we are implementing MME (Mobility Management Entity).
- [SGs](https://github.com/fasferraz/SGs) `[2023-10]` - This is a MSS SGs SCTP Server written in python3 that can be used with a MME to test some SGs features, like IMSI Attach, Location Update, SMS (Sending/Receiving/Alerting) or Paging (for SMS or CS-Fallback).
- [dra-guard](https://github.com/acassen/dra-guard) `[2025-08]` - DRA-Guard is a SCTP proxy offering access to Diameter payload.
- [gtp-guard](https://github.com/acassen/gtp-guard) `[2026-06]` - The main goal of this project is to provide robust and secure extensions to GTP protocol (GPRS Tunneling Protocol).
- [osmo-s1gw](https://gitea.osmocom.org/erlang/osmo-s1gw) - S1AP gateway/proxy in Erlang for 4G LTE. Bridges eNB-facing and CN-facing IP networks. Hosted on **Osmocom Gitea**.
- [osmo-upf](https://gitea.osmocom.org/cellular-infrastructure/osmo-upf) - Osmocom UPF (User Plane Function) in C with PFCP session management. Hosted on **Osmocom Gitea**.
- [DIKEUE](https://github.com/SyNSec-den/DIKEUE) `[2023-06]` - This is the public release of the code of our paper titled "Noncompliance as Deviant Behavior: An Automated Black-box...
- [LibNbiot](https://github.com/telekom/LibNbiot) `[2023-04]` - Non-blocking MQTT-SN Library for NB-IoT
- [LTECoverageTool](https://github.com/usnistgov/LTECoverageTool) `[2020-05]` - The LTE Coverage Tool application and SDK enable first responders and public safety personnel to survey and evaluate ...
- [OAI-5G](https://github.com/herlesupreeth/OAI-5G) `[2016-11]` - EmPOWER Agent integration with OpenAirInterface stack
- [5G-NR-LTE-Sidelink-Capacity-Estimator](https://github.com/usnistgov/5G-NR-LTE-Sidelink-Capacity-Estimator) `[2022-10]` - This tool computes the expected link capacity in data rate (Mbit/s) for sidelink considering 5G New Radio (NR) and Lo...
- [edrx](https://github.com/fasferraz/edrx) `[2021-06]` - NB-IoT paging in extendedDRX
- [Sidelink-5G-OAI-dashboard](https://github.com/shariquetelco/Sidelink-5G-OAI-dashboard) `[2026-01]` - Real-time tactical monitoring dashboard for OpenAirInterface 5G Sidelink Mode 2 D2D communications
- [qppsim](https://github.com/usnistgov/qppsim) `[2019-03]` - A Tool for Rapid Prototyping of LTE QoS, Priority and Pre-emption
- [OAI-Colosseum](https://github.com/wineslab/OAI-Colosseum) `[2025-11]` - OpenAirInterface configs and tools
- [C-V2XInteroperabilityAnalyzer](https://github.com/usnistgov/C-V2XInteroperabilityAnalyzer) `[2025-04]` - Cellular Vehicle-to-Everything (C-V2X) Interoperability Analyzer based on SAE and IEEE 1609.x standards
- [nr-prose-ns3-module](https://github.com/usnistgov/nr-prose-ns3-module) `[2024-10]` - ns-3 module for 5G NR ProSe

### 3G

- [OsmoHNBGW](https://osmocom.org/projects/osmohnbgw) - An Open Source implenentation of a HNB-GW (HomeNodeB-Gateway), implementing the Iuh, IuCS and IuPS interfaces. It aggregates the Iuh links from femtocells (hNodeBs) and presents them as regular IuCS and IuPS towards MSC and SGSN.

### 2G + 3G

- [OsmoMSC](https://osmocom.org/projects/osmomsc/wiki) - Open Source implementation of a MSC (Mobile Switching Centre). It provides a 3GPP AoIP interface towards BSCs like OsmoBSC as well as 3GPP IuCS towards RNCs or HNB-GWs like OsmoHNBGW as well as GSUP towards OsmoHLR.
- [OsmoHLR](https://osmocom.org/projects/osmo-hlr/wiki/OsmoHLR) - Open Source implementation of a HLR (Home
  Location Register).  It provides a GSUP protocol interface to OsmoMSC and OsmoSGSN.
- [OsmoSGSN](https://osmocom.org/projects/osmosgsn/wiki/OsmoSGSN) - Open Source implementation of a SGSN (Serving GPRS Support Node).  It provides a Gb/IP interface towards PCUs, an IuCS interface towards RNC/HNBGW, a GSUP interface to OsmoHLR and the GTP based Gp interface to the GGSN.
- [OsmoGGSN](https://osmocom.org/projects/openggsn/wiki) - Open Source implementation of a GGSN (Gateway GPRS Support Node).  It provides a Gp interface towards the SGSN and a Gi interface toward the external IP network.
- [OsmoMGW](https://osmocom.org/projects/osmo-mgw/wiki) - Open Source implementation of a MGW (Media GateWay).  It is used by OsmoBSC, OsmoMSC as well as OsmoHNBGW to provide RTP user plane routing/multiplexing. Supports LCLS and IuFP.
- [OsmoSTP](https://osmocom.org/projects/osmo-stp/wiki) - Open Source implementation of a STP (Signal Transfer Point).  It is used to route SS7 traffic between other software (like MSC, BSC, ...) via M3UA, SUA and SCCPlite.
- [OsmoCBC](https://gitea.osmocom.org/cellular-infrastructure/osmo-cbc) - Cell Broadcast Centre in C. Distributes cell broadcast and emergency alert messages via CBSP protocol, with REST API. Hosted on **Osmocom Gitea**.
- [OsmoSMLC](https://gitea.osmocom.org/cellular-infrastructure/osmo-smlc) - Serving Mobile Location Centre for cellular network location services. Hosted on **Osmocom Gitea**.
- [osmo-sip-connector](https://gitea.osmocom.org/cellular-infrastructure/osmo-sip-connector) - MNCC-to-SIP bridge for OsmoMSC VoIP interfacing. Hosted on **Osmocom Gitea**.


- [osmo-ci](https://gitea.osmocom.org/osmocom/osmo-ci) - Osmocom Continuous Integration. Hosted on **Osmocom Gitea**.
- [libosmocore](https://gitea.osmocom.org/osmocom/libosmocore) - Common foundation library for all Osmocom projects (libosmocore, libosmogsm, libosmovty, libosmogb, libosmosim, libosmocodec). Hosted on **Osmocom Gitea**.
- [libosmo-abis](https://gitea.osmocom.org/osmocom/libosmo-abis) - Osmocom library for A-bis (E1/IP) interface. Hosted on **Osmocom Gitea**.
- [libosmo-netif](https://gitea.osmocom.org/osmocom/libosmo-netif) - Osmocom library for network/socket abstraction and osmux audio multiplex. Hosted on **Osmocom Gitea**.
- [libosmo-gprs](https://gitea.osmocom.org/osmocom/libosmo-gprs) - Osmocom GPRS protocol stack libraries. Hosted on **Osmocom Gitea**.
- [gapk](https://gitea.osmocom.org/osmocom/gapk) - GSM Audio Pocket Knife: transcoding between GSM voice codec formats. Hosted on **Osmocom Gitea**.
- [pyosmocom](https://gitea.osmocom.org/osmocom/pyosmocom) - Python osmocom core libraries for scripting and automation. Hosted on **Osmocom Gitea**.
- [osmo-dev](https://gitea.osmocom.org/osmocom/osmo-dev) - Osmocom Top-level Makefile and dev tools. Hosted on **Osmocom Gitea**.
- [osmo-rfds](https://gitea.osmocom.org/sdr/osmo-rfds) - RF delay simulator using ADALM-PLUTO. Hosted on **Osmocom Gitea**.
- [osmo-tacdb](https://gitea.osmocom.org/osmocom/osmo-tacdb) - TAC DB + Android app to collect them. Hosted on **Osmocom Gitea**.
- [osmo-codegen](https://gitea.osmocom.org/osmocom/osmo-codegen) - WIP Code Generator for GSM 04.08 encoder/decoder. Hosted on **Osmocom Gitea**.
- [osmo-adsb-gen](https://gitea.osmocom.org/sdr/osmo-adsb-gen) - Osmcoom ADS-B test signal generator. Hosted on **Osmocom Gitea**.
- [ergw-pgw](https://github.com/travelping/ergw-pgw) `[2018-02]` - PGW GGSN Docker Container.
- [osmo-bsc-nat](https://gitea.osmocom.org/cellular-infrastructure/osmo-bsc-nat) - Osmocom BSC NAT: Aggregate multiple BSCs (A interfaces) in one BSC/A-interface. Hosted on **Osmocom Gitea**.
- [osmo-bsc](https://gitea.osmocom.org/cellular-infrastructure/osmo-bsc) - Osmocom's Base Station Controller for 2G mobile networks. Hosted on **Osmocom Gitea**.
- [osmo-bts](https://gitea.osmocom.org/cellular-infrastructure/osmo-bts) - Osmocom Base Transceiver Station (BTS). Hosted on **Osmocom Gitea**.
- [osmo-msc](https://gitea.osmocom.org/cellular-infrastructure/osmo-msc) - Osmocom Mobile Switching Centre. Hosted on **Osmocom Gitea**.
- [osmo-sgsn](https://gitea.osmocom.org/cellular-infrastructure/osmo-sgsn) - Osmocom Serving GPRS Support Node for 2G(GPRS) and 3G(UMTS). Hosted on **Osmocom Gitea**.
- [osmo-ggsn](https://gitea.osmocom.org/cellular-infrastructure/osmo-ggsn) - Osmocom Gateway GPRS Support Node (GGSN), successor of OpenGGSN. Hosted on **Osmocom Gitea**.
- [osmo-gsm-tester](https://gitea.osmocom.org/cellular-infrastructure/osmo-gsm-tester) - Osmocom GSM Tester, jenkins integrated GSM hardware testing. Hosted on **Osmocom Gitea**.
- [osmo-gsm-manuals](https://gitea.osmocom.org/cellular-infrastructure/osmo-gsm-manuals) - Official Osmocom User Manuals (shared / common parts and build scripts). Hosted on **Osmocom Gitea**.
- [osmo-hnbgw](https://gitea.osmocom.org/cellular-infrastructure/osmo-hnbgw) - Osmocom Home NodeB Gateway, for attaching femtocells to the 3G CN (OsmoMSC, OsmoSGSN). Hosted on **Osmocom Gitea**.
- [osmo-hlr](https://gitea.osmocom.org/cellular-infrastructure/osmo-hlr) - Osmocom HLR for GSUP protocol towards OsmoSGSN and OsmoMSC. Hosted on **Osmocom Gitea**.
- [osmo-pcu](https://gitea.osmocom.org/cellular-infrastructure/osmo-pcu) - Osmocom Packet control Unit (PCU): Network-side GPRS (RLC/MAC); BTS- or BSC-colocated. Hosted on **Osmocom Gitea**.
- [osmo-gbproxy](https://gitea.osmocom.org/cellular-infrastructure/osmo-gbproxy) - Omocom GPRS Gb interface aggregation/conversion proxy (between PCU/BSS and SGSN). Hosted on **Osmocom Gitea**.
- [osmo-iuh](https://gitea.osmocom.org/cellular-infrastructure/osmo-iuh) - Osmocom code for the Iuh interface (HNBAP, RUA, RANAP). Hosted on **Osmocom Gitea**.
- [osmo-el2tpd](https://gitea.osmocom.org/cellular-infrastructure/osmo-el2tpd) - Osmocom L2TP daemon compatible with Ericsson L2TP dialect (SIU). Hosted on **Osmocom Gitea**.
- [osmo-python-tests](https://gitea.osmocom.org/cellular-infrastructure/osmo-python-tests) - Hosted on **Osmocom Gitea**.
- [osmo-hnodeb](https://gitea.osmocom.org/cellular-infrastructure/osmo-hnodeb) - (upper layers of) HomeNodeB. Hosted on **Osmocom Gitea**.
- [osmo-e1-recorder](https://gitea.osmocom.org/cellular-infrastructure/osmo-e1-recorder) - Osmocom E1/T1 span recorder. Hosted on **Osmocom Gitea**.
- [osmo-bts-amp](https://gitea.osmocom.org/cellular-infrastructure/osmo-bts-amp) - BTS side amplifier (PA+LNA+Duplexer). Hosted on **Osmocom Gitea**.
- [osmo-rbs](https://gitea.osmocom.org/cellular-infrastructure/osmo-rbs) - Tools for experimentation with Ericsson RBS. Hosted on **Osmocom Gitea**.
- [osmo-abi-check](https://gitea.osmocom.org/cellular-infrastructure/osmo-abi-check) - Osmocom ABI Check. Hosted on **Osmocom Gitea**.
- [osmo-subscr-impex](https://gitea.osmocom.org/sim-card/osmo-subscr-impex) - Osmocom subscriber authentication data importer/exporter. Hosted on **Osmocom Gitea**.
- [osmo-ccid-firmware](https://gitea.osmocom.org/sim-card/osmo-ccid-firmware) - USB CCID firmware project for (currently only) sysmoOCTSIM. Hosted on **Osmocom Gitea**.
- [osmo-remsim](https://gitea.osmocom.org/sim-card/osmo-remsim) - Osmocom Remote SIM Software Suite. Hosted on **Osmocom Gitea**.
- [osmo-sim-auth](https://gitea.osmocom.org/sim-card/osmo-sim-auth) - A command line tool for (U)SIM authentication. Hosted on **Osmocom Gitea**.
- [osmo_gsup](https://gitea.osmocom.org/erlang/osmo_gsup) - Erlang implementation of GSUP codec. Hosted on **Osmocom Gitea**.
- [mgw_nat](https://gitea.osmocom.org/erlang/mgw_nat) - Erlang MGW NAT/MASQ implementation. Hosted on **Osmocom Gitea**.
### OSS/BSS

- [Sigscale OCS](https://github.com/sigscale/ocs) `[2026-07]` - SigScale OCS includes a 3GPP AAA server function for authentication, authorization and accounting (AAA) of subscribers using DIAMETER or RADIUS protocols.
- [Bodastage CE](https://gitlab.com/bts-ce/bts-ce) `[2019-05]` - Boda Telecom Suite - Community Edition (BTS-CE) is an open source vendor-agnostic telecommunication network management platform. Hosted on **GitLab**.
- [CGRateS](https://github.com/cgrates/cgrates) `[2026-07]` - Real-time Charging System for Telecom & ISP environments. Cloud-ready micro-services with CDR mediation, LCR, fraud detection and multi-tenant support.
- [BillRun](https://github.com/BillRun/system) `[2026-07]` - Open source Telecom BSS: CDR mediation, real-time OCS, rating/charging (prepaid, postpaid, roaming, wholesale), and fraud detection.
- [SigScale CGF](https://github.com/sigscale/cgf) `[2025-08]` - 3GPP Charging Gateway Function (CGF) in Erlang. Part of the SigScale telecom stack.
- [SigScale HSS](https://github.com/sigscale/hss) `[2023-12]` - 3GPP Home Subscriber Server (HSS) in Erlang. Part of the SigScale telecom stack.
- [Kuwaiba](https://sourceforge.net/projects/kuwaiba/) - Enterprise-grade open source network inventory and CMDB for telecom. Supports 5G, GPON, SDH, MPLS topologies. Hosted on **SourceForge**.
- [Nokia OSSMediator](https://github.com/nokia/OSSMediator) `[2026-05]` - OSS Mediator for telecom network management. From Nokia.
- [free5gc cdrFileParser](https://github.com/free5gc/cdrFileParser) `[2025-05]` - TS 32.297 CDR file decoder CLI. From the free5GC project.
- [CDRTool](https://github.com/AGProjects/cdrtool) `[2026-05]` - CDR mediation and rating engine for Call Detail Records. From AG Projects.
- [OpenCDRRate](https://sourceforge.net/p/opencdrrate/home/Home/) - Scalable CDR rating, taxation and invoicing system for telecom/VoIP. Hosted on **SourceForge**.
- [jBilling](https://sourceforge.net/projects/jbilling/) - Open source enterprise billing system in Java with CDR mediation module for telecom. Hosted on **SourceForge**.


- [hepsub-voipmonitor](https://github.com/sipcapture/hepsub-voipmonitor) `[2019-05]` - HEP Pub-Sub Client for OSS Voipmonitor Sniffer.
- [rate-o-mat](https://github.com/sipwise/rate-o-mat) `[2026-06]` - Rating daemon for the NGCP.
- [open5gs-nms](https://github.com/paulmataruso/open5gs-nms) `[2026-07]` - Web-based network management UI for Open5GS.
## Interconnect

### SBC, IMS

- [Freeswitch](https://freeswitch.org/confluence/display/FREESWITCH/Python_SBC) - Popular SIP stack that could be used as Session Border Controller (SBC)
- [IMS Clearwater](http://www.projectclearwater.org) - Clearwater is an open source implementation of IMS (the IP Multimedia Subsystem).
- [Kamailio](https://www.kamailio.org) - SIP stack used for VoLTE and SBC. CLI control tool: [kamcli](https://github.com/kamailio/kamcli) `[2026-07]`.
- [go-eventsocket](https://github.com/fiorix/go-eventsocket) `[2024-09]` - FreeSWITCH Event Socket library for the Go programming language.
- [Asterisk](https://github.com/asterisk/asterisk) `[2026-07]` - The most widely deployed open-source PBX and telephony engine. SIP, PJSIP, WebRTC, conferencing, and IVR.
- [PJSIP](https://github.com/pjsip/pjproject) `[2026-07]` - Free and open-source multimedia communication library implementing SIP, SDP, RTP, STUN, TURN, and ICE. Foundation for many VoIP/IMS clients.
- [HOMER](https://github.com/sipcapture/homer) `[2026-07]` - 100% Open-Source SIP/VoIP/RTC packet capture and monitoring platform. Essential for VoLTE/VoWiFi troubleshooting. Ecosystem: [homer-ui](https://github.com/sipcapture/homer-ui), Docker variants ([10](https://github.com/sipcapture/homer-docker), [7](https://github.com/sipcapture/homer7-docker), [5](https://github.com/sipcapture/homer5-docker)), [installer](https://github.com/sipcapture/homer-installer), [config](https://github.com/sipcapture/homer-config), [puppet](https://github.com/sipcapture/homer-puppet), [snmp bridge](https://github.com/sipcapture/homer-snmp), legacy viewers ([homer-view](https://github.com/sipcapture/homer-view), [react](https://github.com/sipcapture/homer-view-react)).
- [Routr](https://github.com/fonoster/routr) `[2026-07]` - A programmable, cloud-native SIP server for building modern telephony systems.
- [rsipstack](https://github.com/restsend/rsipstack) `[2026-07]` - SIP stack in Rust for building SIP applications (UA, proxy, B2BUA).
- [livekit/sip](https://github.com/livekit/sip) `[2026-07]` - SIP-to-WebRTC bridge for LiveKit, connecting PSTN/SIP trunks to WebRTC rooms.
- [webrtc-sip-gw](https://github.com/florian-h05/webrtc-sip-gw) `[2025-12]` - WebRTC-SIP gateway for AVM Fritz!Box, built on Kamailio and rtpengine.
- [flowcat](https://github.com/AreevAI/flowcat) `[2026-07]` - Self-hosted, native-Rust runtime for real-time voice agents over SIP/WebRTC.
- [VoiceBlender](https://github.com/VoiceBlender/voiceblender) `[2026-07]` - Programmable voice platform with SIP/WebRTC call control, multi-party mixing, recording, TTS/STT, and pluggable AI agents (ElevenLabs, VAPI, Pipecat, Deepgram), driven via REST API, webhooks, and a WebSocket event stream.
- [active-call](https://github.com/miuda-ai/active-call) `[2026-07]` - A SIP/WebRTC voice agent.
- [OpenSIPS](https://opensips.org/) - GPL multi-functional SIP server: proxy, registrar, load balancer, SBC, NAT traversal. Former OpenSER. [SourceForge (legacy)](https://sourceforge.net/projects/opensips/) / [GitHub](https://github.com/OpenSIPS/opensips). Community Edition platforms: [SBC CE](https://github.com/OpenSIPS/opensips-sbc-ce), [SoftSwitch CE](https://github.com/OpenSIPS/opensips-softswitch-ce) ([config](https://github.com/OpenSIPS/opensips-softswitch-ce-config)), [AI Voice Connector CE](https://github.com/OpenSIPS/opensips-ai-voice-connector-ce). Other: [opensips-js](https://github.com/OpenSIPS/opensips-js) (browser SIP), [opensips-ng](https://github.com/OpenSIPS/opensips-ng) (next-gen prototype).
- [P-KISS-SBC](https://github.com/mwolff44/pk-sbc) `[2026-06]` - Simple SIP/RTP session border controller built on Kamailio and RTPEngine.
- [Flexisip](https://github.com/BelledonneCommunications/flexisip) `[2026-07]` - SIP proxy server with push notification gateway, presence and conference servers; powers the linphone.org infrastructure. From Belledonne Communications.
- [MikoPBX](https://github.com/mikopbx/Core) `[2026-07]` - Free open-source PBX built on Asterisk 22 with a web UI, deployable as ISO, Docker, LXC or cloud image.
- [FS PBX](https://github.com/nemerald-voip/fspbx) `[2026-07]` - Multi-tenant PBX platform on FreeSWITCH with a modern web UI, fax, device provisioning and REST APIs.
- [gsm-sip-bridge](https://github.com/selvakn/gsm-sip-bridge) `[2026-07]` - GSM-to-SIP voice bridge in Rust routing calls from Quectel cellular modules to a SIP server.
- [OpenIMSs](https://github.com/VoicenterTeam/openimss) `[2023-10]` - Open source environment for real-life development of IMS-based 4G/5G/NR voice/video/data/RCS services. Extends docker_open5gs.
- [FusionPBX](https://www.fusionpbx.com/) - Multi-tenant PBX and voice switch for FreeSWITCH with IVR, call center, provisioning and more. [SourceForge](https://sourceforge.net/directory/pbx/).
- [DjangoPBX](https://codeberg.org/DjangoPBX/DjangoPBX) `[2026-02]` - Full-featured domain-based multi-tenant PBX driven by Django and FreeSWITCH with REST API, call center, and provisioning. Hosted on **Codeberg**.
- [Sofia-SIP](https://github.com/freeswitch/sofia-sip) `[2026-06]` - Open-source SIP User-Agent library (RFC3261 compliant) maintained by FreeSWITCH. Originally from Nokia Research Center.
- [OpalVOIP](https://sourceforge.net/projects/opalvoip/) - C++ multi-platform VoIP library supporting H.323, SIP, and IAX2. Used by Ekiga softphone. Hosted on **SourceForge**.
- [OpenSIPS IMS CE](https://github.com/OpenSIPS/opensips-ims-ce) `[2026-07]` - IMS CSCF (P-CSCF, I-CSCF, S-CSCF) compliant with 3GPP TS 124 228 for VoLTE. Docker-based, designed to work on top of Open5GS.
- [rtpengine](https://github.com/sipwise/rtpengine) `[2026-07]` - Kernel-assisted high-performance RTP/RTCP media proxy for Kamailio, OpenSIPS and other SIP proxies. Handles transcoding, recording, DTLS-SRTP. From Sipwise.
- [sipgo](https://github.com/emiago/sipgo) `[2026-07]` - SIP library for building fast SIP services in Go. Full RFC3261 stack with transport, transaction and dialog layers.
- [LibreSBC](https://github.com/hnimminh/libresbc) `[2026-07]` - Open source Session Border Controller built on FreeSWITCH. Multi-tenant, clustering, REST API, WebUI.
- [drachtio-server](https://github.com/drachtio/drachtio-server) `[2026-07]` - SIP call processing server controllable via Node.js. Companion [signaling resource framework](https://github.com/drachtio/drachtio-srf) and [FreeSWITCH media resource function](https://github.com/drachtio/drachtio-fsmrf) `[2026-06]`. Used for building telephony apps.
- [Sippy B2BUA](https://github.com/sippy/b2bua) `[2026-07]` - RFC3261-compliant SIP Back-to-Back User Agent in Python. Works with RTPproxy, OpenSIPS, Kamailio. Go port: [go-b2bua](https://github.com/sippy/go-b2bua).
- [Restcomm Media Server](https://github.com/RestComm/media-core) `[2024-01]` - Java media server for real-time communications. SIP-based conferencing, IVR, transcoding and announcements.
- [Kamailio IMS Config](https://github.com/herlesupreeth/Kamailio_IMS_Config) `[2024-06]` - Fixed Kamailio IMS configuration files for basic VoLTE calling. Companion to docker_open5gs.
- [DVRTC](https://github.com/EnableSecurity/DVRTC) `[2026-06]` - Damn Vulnerable Real-Time Communications: intentionally vulnerable VoIP/WebRTC platform for security training (SIP, RTP, TURN). From the SIPVicious team.
- [libsrtp](https://github.com/cisco/libsrtp) `[2026-07]` - Reference open-source SRTP/SRTCP library originally from Cisco, widely used in WebRTC, SIP and IMS media stacks.
- [FHoSS (maintained fork)](https://github.com/herlesupreeth/FHoSS) `[2023-08]` - Maintained fork of OpenIMSCore's FHoSS HSS with bug-fixes and added VoLTE/VoWiFi features.
- [aringo](https://github.com/cgrates/aringo) `[2026-03]` - Asterisk ARI connector in Go, maintained by the CGRateS team. Useful glue for integrating Asterisk with rating/CDR pipelines.
- [beswitched](https://codeberg.org/tychosoft/beswitched) `[2026-04]` - eXosip-based SIP key-system/softswitch by David Sugar (GNU Bayonne author) targeting residential and small-office deployments. C++20, AGPLv3. Hosted on **Codeberg**.
- [Fonoster](https://github.com/fonoster/fonoster) `[2026-07]` - Open-source alternative to Twilio: programmable voice/SMS APIs for building telephony applications. Monorepo for the Fonoster platform.
- [heplify](https://github.com/sipcapture/heplify) `[2026-07]` - Lightweight HEP capture agent for HOMER. Captures SIP/RTCP/RTP and forwards to a HEP collector for VoIP troubleshooting and monitoring.
- [heplify-server](https://github.com/sipcapture/heplify-server) `[2026-07]` - HEP capture server for HOMER. Receives, decodes and stores HEP-encapsulated SIP/RTC traffic. Companion to heplify.
- [captagent](https://github.com/sipcapture/captagent) `[2026-07]` - 100% open-source packet capture agent for HEP/HOMER. C-based, supports SIP, RTCP, RTP, DNS and ISUP capture.
- [homer-app](https://github.com/sipcapture/homer-app) `[2026-07]` - HOMER 7 frontend and API server (Go). Web UI and REST API for the SIP/VoIP/RTC packet capture and monitoring stack.
- [opensips-cli](https://github.com/OpenSIPS/opensips-cli) `[2026-07]` - Official interactive CLI tool for controlling and monitoring OpenSIPS servers.
- [opensips-cp](https://github.com/OpenSIPS/opensips-cp) `[2026-07]` - Official OpenSIPS Web Control Panel for system and user provisioning, MI/statistics inspection and module configuration.
- [SIPssert](https://github.com/OpenSIPS/SIPssert) `[2026-05]` - Testing framework for complex VoIP setups, used to drive conformity tests of OpenSIPS scenarios. Companion repo: [sipssert-opensips-tests](https://github.com/OpenSIPS/sipssert-opensips-tests).
- [docker-opensips](https://github.com/OpenSIPS/docker-opensips) `[2026-05]` - Official Docker image repository for OpenSIPS.
- [opensips-mcp-server](https://github.com/OpenSIPS/opensips-mcp-server) `[2026-04]` - Model Context Protocol (MCP) server exposing OpenSIPS operations to LLM agents. Pair with [opensips-skills](https://github.com/VoicenterTeam/opensips-skills) for Claude Code.
- [opensips-skills](https://github.com/VoicenterTeam/opensips-skills) `[2026-07]` - Claude Code plugin providing two coordinated Agent Skills for working with OpenSIPS. Companion to opensips-mcp-server.
- [SEMS](https://github.com/sipwise/sems) `[2026-07]` - SIP Express Media Server: fast, flexible SIP application/media server for IVR, conferencing, B2BUA scenarios. Maintained by Sipwise.
- [diago](https://github.com/emiago/diago) `[2026-07]` - VoIP framework in Go (built on sipgo) for building dialog-oriented telephony applications. Companion CLI: [gophone](https://github.com/emiago/gophone).
- [diagox](https://github.com/emiago/diagox) `[2026-07]` - Simple Ingress/Egress service for SIP/RTP/WebRTC built on diago. Useful as a lightweight SBC-style component.
- [voiptests](https://github.com/sippy/voiptests) `[2026-07]` - Meta-repository wiring up interop tests between latest OpenSIPS, Kamailio, Sippy B2BUA and rtpproxy.
- [libg722](https://github.com/sippy/libg722) `[2026-06]` - Maintained C implementation of the ITU-T G.722 wideband audio codec. Used by sippy/rtpproxy and other VoIP media stacks.
- [SentryPeerHQ](https://github.com/SentryPeer/SentryPeerHQ) `[2026-06]` - Web/SaaS frontend for [SentryPeer](https://github.com/SentryPeer/SentryPeer): VoIP fraud detection and threat intelligence dashboard for SIP networks.


- [paStash](https://github.com/sipcapture/paStash) `[2025-08]` - pastaʃ'ʃ = Spaghetti I/O Event Data Processing, Interpolation, Correlation and beyond :spaghetti:.
- [rtcagent](https://github.com/sipcapture/rtcagent) `[2026-07]` - RTCAgent is an eBPF powered HEP Agent for HOMER/HEPIC.
- [hep-wireshark](https://github.com/sipcapture/hep-wireshark) `[2025-11]` - HOMER HEP Wireshark Dissector.
- [wireshark/wireshark-containers](https://gitlab.com/wireshark/wireshark-containers) `[2026-07]` - Containers that focus on Wireshark. Hosted on **GitLab**.
- [hepagent.rs](https://github.com/sipcapture/hepagent.rs) `[2023-04]` - Next-Gen HEP Capture Agent in Rust.
- [onomondo-live](https://github.com/onomondo/onomondo-live) `[2025-04]` - Capture all traffic sent in and out of a device, from the Onomondo network.
- [hepfix.js](https://github.com/sipcapture/hepfix.js) `[2023-10]` - IPFIX Gateway for HEP & HOMER.
- [anon_pcap](https://github.com/wmnsk/anon_pcap) `[2024-10]` - Mini python script to replace specified value in PCAP(or any binary) file.
- [hepsub-apiban](https://github.com/sipcapture/hepsub-apiban) `[2026-05]` - HOMER/HEPSUB Integration for APIban.org.
- [UPSIPP](https://github.com/sipcapture/upsipp) `[2026-07]` - SIP endpoint monitor and status page powered entirely by GitHub Actions, Issues and Pages, with SIP probes executed by gossipper.
- [hepsub-cgrates](https://github.com/sipcapture/hepsub-cgrates) `[2019-07]` - HOMER HEPSub client example for CGRages.
- [statstrmr](https://github.com/sipcapture/statstrmr) `[2016-03]` - JSON-HEP Statistics Streamer for HOMER 5.x.
- [helm-charts](https://github.com/sipcapture/helm-charts) `[2025-12]` - HOMER helm charts.
- [homer10](https://github.com/fonoster/homer10) `[2025-06]` - Minimal Homer 10 Lab.
- [pcaputils](https://github.com/wmnsk/pcaputils) `[2017-11]` - Utilities to handle PCAP files, written in Go.
- [wireshark](https://gitea.osmocom.org/osmocom/wireshark) - wireshark.org protocol dissector with Osmocom additions. Hosted on **Osmocom Gitea**.
- [osmo-pcap](https://gitea.osmocom.org/osmocom/osmo-pcap) - Tools for distributed pcap recording (osmo-pcap-server, osmo-pcap-client). Hosted on **Osmocom Gitea**.
- [osmo-sysmon](https://gitea.osmocom.org/osmocom/osmo-sysmon) - Osmocom System Monitor. Hosted on **Osmocom Gitea**.
- [wireshark-mate](https://gitea.osmocom.org/osmocom/wireshark-mate) - wireshark MATE configuration for use with GSM/UMTS/LTE protocols. Hosted on **Osmocom Gitea**.
- [osmo-pcap-reiniger](https://gitea.osmocom.org/osmocom/osmo-pcap-reiniger) - tool for anonymization of (telecom) PCAP files. Hosted on **Osmocom Gitea**.

- [ZLMediaKit](https://github.com/ZLMediaKit/ZLMediaKit) `[2026-07]` - WebRTC/RTSP/RTMP/HTTP/HLS/HTTP-FLV/WebSocket-FLV/HTTP-TS/HTTP-fMP4/WebSocket-TS/WebSocket-fMP4/GB28181/SRT/STUN/TURN server and client framework based on C++11.
- [stunner](https://github.com/firefart/stunner) `[2026-07]` - Stunner is a tool to test and exploit STUN, TURN and TURN over TCP servers.
- [coturn](https://github.com/coturn/coturn) `[2026-07]` - Free open-source TURN and STUN server. The de-facto standard for NAT traversal in WebRTC and VoIP deployments.
- [pion/turn](https://github.com/pion/turn) `[2026-07]` - Go library for building TURN clients and servers, from the Pion WebRTC project.
- [pion/stun](https://github.com/pion/stun) `[2026-07]` - Go implementation of STUN (RFC 5389/8489). Companion library to pion/turn.
- [pion/webrtc](https://github.com/pion/webrtc) `[2026-07]` - Pure Go implementation of the WebRTC API. Core protocol libraries: [ice](https://github.com/pion/ice), [rtp](https://github.com/pion/rtp), [rtcp](https://github.com/pion/rtcp), [srtp](https://github.com/pion/srtp), [sctp](https://github.com/pion/sctp), [datachannel](https://github.com/pion/datachannel), [interceptor](https://github.com/pion/interceptor).
- [STUNTMAN](https://github.com/jselbie/stunserver) `[2026-05]` - Open-source STUN server and client implementing RFC 5389 with RFC 5769 test vectors.
- [always-online-stun](https://github.com/pradt2/always-online-stun) `[2026-07]` - Curated list of publicly available STUN servers, validated and refreshed every hour.
- [turn-rs](https://github.com/mycrl/turn-rs) `[2026-07]` - Pure Rust TURN server with high performance and low resource consumption.
- [processone/stun](https://github.com/processone/stun) `[2026-03]` - STUN and TURN library for Erlang/Elixir. Core library powering eturnal.
- [eturnal](https://github.com/processone/eturnal) `[2026-06]` - STUN / TURN standalone server.
- [violet](https://github.com/paullouisageneau/violet) `[2025-06]` - Lightweight STUN/TURN server.
- [restund](https://github.com/baresip/restund) `[2026-07]` - Modular STUN/TURN server from the baresip project.
- [stuncheck](https://github.com/Pepelux/stuncheck) `[2025-12]` - Set of tools to audit and exploit STUN/TURN servers.
- ⚠️ [coturn-chart](https://github.com/small-hack/coturn-chart) `[2026-06]` - Coturn Helm Chart to provide a STUN/TURN Server on Kubernetes.
- [videowhisper-webrtc](https://github.com/videowhisper/videowhisper-webrtc) `[2025-04]` - Free open source WebRTC signaling server: peer to peer WebRTC live streaming, handles multiple channels (streams) and viewers per channel, support for STUN/TURN (tested with Coturn), accounts and resource limitation plans. Includes support for commercial modules with extra features (RTMP/HLS).
- [sharef](https://github.com/emiago/sharef) `[2021-07]` - Sharef command line tool for sending streaming files over webrtc.
- [certman](https://github.com/FreePBX/certman) `[2026-07]` - Module of FreePBX (Certificate Manager) :: Certificate Manager for Asterisk. Used for TLS, DTLS connection (think WebRTC and secure traffic).
- [openfire-pionturn-plugin](https://github.com/igniterealtime/openfire-pionturn-plugin) `[2025-12]` - This plugin provides a TURN/STUN Server for Openfire.
- [pion](https://github.com/pion/pion) `[2026-04]` - A monorepo housing Pion's open-source *in-progress* applications: Ion, a Pion-based SFU, and Tion, a TURN/STUN server, both built as open-source, aiming to be batteries included and production-ready.
- [ansible-role-coturn](https://github.com/wazo-platform/ansible-role-coturn) `[2026-07]` - Setup coturn TURN/STUN server.
- [coturn-secure-config](https://github.com/EnableSecurity/coturn-secure-config) `[2026-06]` - Secure configuration templates for coturn TURN server with Docker test environment.
- ⚠️ [~~docker-eturnal~~](https://github.com/tiredofit/docker-eturnal) `[2025-05]` - Dockerized STUN/TURN server.
- [LetItSno](https://codeberg.org/leecowdrey/LetItSno) - Bare metal server configuration steps for hosting OpenShift inside virtual machines, in turn provided nested virtualization. Hosted on **Codeberg**.
- [webrtc-test](https://github.com/RestComm/webrtc-test) `[2018-05]` - Framework for functional and Load Testing of WebRTC.
- [webrtcomm](https://github.com/RestComm/webrtcomm) `[2018-06]` - WebRTCComm is a simple high level JavaScript WebRTC framework for Web Developers to add Real Time Communications and IM Capabilities to any website.
- [olympus](https://github.com/RestComm/olympus) `[2022-11]` - RestComm WebRTC Application.
- [restcomm-web-sdk](https://github.com/RestComm/restcomm-web-sdk) `[2018-12]` - RestComm WebRTC JavaScript SDK.

- [mediamtx](https://github.com/bluenviron/mediamtx) `[2026-07]` - Ready-to-use SRT / WebRTC / RTSP / RTMP / LL-HLS / MPEG-TS / RTP media server and media proxy that allows to read, publish, proxy, record and playback video and audio streams.
- [media-server](https://github.com/ireader/media-server) `[2026-05]` - C library implementing RTSP/RTP/RTMP/HLS/MPEG-TS/DASH/MP4 for building streaming media servers.
- [Jitsi Videobridge](https://github.com/jitsi/jitsi-videobridge) `[2026-07]` - WebRTC-compatible SFU video router powering Jitsi Meet, scaling to hundreds of conferences per server.
- [kraken](https://github.com/MixinNetwork/kraken) `[2026-07]` - High-performance WebRTC audio SFU in pure Go.
- [Live777](https://github.com/binbat/live777) `[2026-07]` - Simple, high-performance edge WebRTC SFU in Rust supporting WHIP/WHEP.
- [ejabberd](https://github.com/processone/ejabberd) `[2026-07]` - Robust, Ubiquitous and Massively Scalable Messaging Platform (XMPP, MQTT, SIP Server).
- [kamailio](https://github.com/kamailio/kamailio) `[2026-07]` - Kamailio - The Open Source SIP Server for large VoIP and real-time communication platforms, focusing on flexibility, security and scalability.
- [jigasi](https://github.com/jitsi/jigasi) `[2026-06]` - Jigasi: a server-side application acting as a gateway to Jitsi Meet conferences. Currently allows regular SIP clients to join meetings and provides transcription capabilities.
- [atm0s-media-server](https://github.com/8xFF/atm0s-media-server) `[2026-07]` - Decentralized, Global-Scale Media Server written in Rust (WebRTC/Whip/Whep/Rtmp/Sip).
- [jsip](https://github.com/usnistgov/jsip) `[2024-07]` - JSIP: Java SIP specification Reference Implementation (moved from java.net).
- [sylkserver](https://github.com/AGProjects/sylkserver) `[2026-07]` - SIP/XMPP/WebRTC Application Server.
- [mediaproxy](https://github.com/AGProjects/mediaproxy) `[2026-06]` - SIP media relay for RTP/RTCP and UDP streams, designed to work with OpenSIPS and Kamailio.
- [python3-sipsimple](https://github.com/AGProjects/python3-sipsimple) `[2026-07]` - SIP SIMPLE SDK in Python: full SIP stack with audio, video, messaging, presence and file transfer. From AG Projects.
- [blink-qt](https://github.com/AGProjects/blink-qt) `[2026-07]` - Blink SIP client for desktop (Qt), built on the SIP SIMPLE SDK. From AG Projects.
- [sylk-webrtc](https://github.com/AGProjects/sylk-webrtc) `[2026-07]` - WebRTC client for SylkServer, supporting audio/video calls and conferencing. From AG Projects.
- [OpenXCAP](https://github.com/AGProjects/openxcap) `[2026-07]` - Fully featured XCAP server (RFC 4825) for presence and resource-list management. From AG Projects.
- [MSRPRelay](https://github.com/AGProjects/msrprelay) `[2025-11]` - MSRP relay (RFC 4976) for NAT traversal of MSRP sessions. From AG Projects.
- [custompbx](https://github.com/custompbx/custompbx) `[2026-04]` - API server and Web GUI for FreeSWITCH written in Go and Angular.
- [mod_audio_stream](https://github.com/amigniter/mod_audio_stream) `[2026-01]` - FreeSWITCH module to stream audio to websocket and receive response.
- [sems](https://github.com/sems-server/sems) `[2026-07]` - Sip Express Media Server.
- [mod_bcg729](https://github.com/xadhoom/mod_bcg729) `[2025-07]` - FreeSWITCH G.729 module using the opensource bcg729 implementation by Belledonne Communications.
- [sipgrep](https://github.com/sipcapture/sipgrep) `[2025-09]` - SIPGREP: Display and Troubleshoot SIP signaling over IP networks in console.
- [kamailioexamples](https://github.com/altanai/kamailioexamples) `[2026-01]` - VoIP architectures and use cases involving Kamailio SIP Server and its modules includes RTPEngine.
- [sipgox](https://github.com/emiago/sipgox) `[2025-01]` - Extra libs for sipgo.
- [kamailio](https://github.com/sipwise/kamailio) `[2026-07]` - Kamailio SIP Proxy with Sipwise patches.
- [call-api](https://github.com/OpenSIPS/call-api) `[2025-12]` - Call API is a front-end layer for managing advanced SIP call flows. It listens for WebSocket connections and talks JSON-RPC 2.0 over them.
- [rtp_cluster](https://github.com/sippy/rtp_cluster) `[2024-05]` - RTP Cluster is a front-end for multiple RTPproxies.
- [mod_whisper](https://github.com/cyrenity/mod_whisper) `[2025-06]` - A FreeSWITCH module to interface to your speech recognition server over websocket.
- [asterisk-consul-module](https://github.com/sboily/asterisk-consul-module) `[2025-12]` - Register Asterisk on consul.
- [esip](https://github.com/processone/esip) `[2026-03]` - ProcessOne SIP server component in Erlang.
- [rtpbreakr](https://github.com/sipcapture/rtpbreakr) `[2022-03]` - RTP Audio Juicer.
- [kamailio-tests](https://github.com/kamailio/kamailio-tests) `[2026-06]` - Test Units For Kamailio SIP Server.
- [mod_openai_asr](https://github.com/aks-tel/mod_openai_asr) `[2026-07]` - Freeswitch Speech-To-Text module. More aks-tel modules: [mod_openai_tts](https://github.com/aks-tel/mod_openai_tts), [mod_google_asr](https://github.com/aks-tel/mod_google_asr), [mod_google_tts](https://github.com/aks-tel/mod_google_tts), [mod_piper_tts](https://github.com/aks-tel/mod_piper_tts), [mod_quickjs](https://github.com/aks-tel/mod_quickjs), [mod_xconf](https://github.com/aks-tel/mod_xconf).
- [mod_whisper_asr](https://github.com/aks-tel/mod_whisper_asr) `[2025-01]` - FreeSWITCH ASR module using OpenAI Whisper for speech recognition.
- [mod_udptun](https://github.com/aks-tel/mod_udptun) `[2026-07]` - FreeSWITCH helper module for cloning and tunnelling RTP/UDP traffic.
- [mod_xconf](https://github.com/aks-tel/mod_xconf) `[2026-07]` - Simple high-performance conference module for FreeSWITCH.
- [mod_funasr](https://github.com/zhoutuan/mod_funasr) `[2025-06]` - FreeSWITCH ASR module fork from mod_audio_stream， use FunASR online cpu version.
- [siremis](https://github.com/asipto/siremis) `[2026-07]` - SIREMIS - Kamailio SIP Server Records Management Interface System.
- [puppet-asterisk](https://github.com/lelutin/puppet-asterisk) `[2026-06]` - Asterisk puppet module.
- [hepgen.js](https://github.com/sipcapture/hepgen.js) `[2025-06]` - Barebone HEP Generator for SIP-less Devs.
- [MyIP](https://github.com/folkertvanheusden/MyIP) `[2026-04]` - IPv4 / IPv6 stack (with http-, vnc-, sip-, snmp-, mqtt- and ntp server) which runs in userspace on linux, written in c++.
- [go-rtp_cluster](https://github.com/sippy/go-rtp_cluster) `[2025-01]` - GoLang version of the rtp_cluster.
- [sipsettings](https://github.com/FreePBX/sipsettings) `[2026-07]` - Module of FreePBX (Asterisk SIP Settings) :: Use to configure Various Asterisk SIP Settings in the General section of sip.conf. Also includes an auto-configuration tool to determine NAT settings. The module assumes Asterisk version 1.4 or higher. Some settings may not exist in Asterisk 1.2 and will be ignored by Asterisk.
- [mod_openai_tts](https://github.com/aks-tel/mod_openai_tts) `[2026-07]` - Freeswitch Speech-To-Text module.
- [HEPjack.js](https://github.com/sipcapture/HEPjack.js) `[2022-12]` - Elegantly Sniff Forward-Secrecy TLS/SIP to HEP at the source using Frida.
- [freeswitch_module_golang_sample](https://github.com/iuridiniz/freeswitch_module_golang_sample) `[2025-06]` - Sample module for FreeSWITCH using golang.
- [libHappy](https://github.com/folkertvanheusden/libHappy) `[2026-04]` - libHappy is a library with which you can interface an audio source/sink to a SIP server. It should be as easy to use as possible.
- [streamcore-server](https://github.com/streamcoreai/streamcore-server) `[2026-06]` - Open-source realtime voice agent server in Go with WebRTC (WHIP), barge-in, streaming STT/LLM/TTS pipelines, plugin system, multi-language SDKs, SIP telephony, ESP32 support & fully local mode.
- [asterisk-cli](https://github.com/FreePBX/asterisk-cli) `[2026-07]` - Module of FreePBX (Asterisk CLI) :: Provides an interface allowing you to run a command as if it was typed into Asterisk CLI.
- [Asterisk-eSpeak](https://github.com/zaf/Asterisk-eSpeak) `[2026-02]` - Asterisk dialplan application for eSpeak text-to-speech. Companion [Asterisk-Flite](https://github.com/zaf/Asterisk-Flite) provides the same for Flite TTS.
- [ansible-opensips](https://github.com/OpenSIPS/ansible-opensips) `[2026-01]` - Ansible role for installing OpenSIPS.
- [go-rtpengine](https://github.com/SilvaMendes/go-rtpengine) `[2025-10]` - The go-rtpengine project by Samuel da Silva Mendes is a Go-based client library designed to interact with the NGCP RTPengine, a high-performance proxy for RTP streams commonly used in VoIP and SIP environments.
- [docker-opensips-cp-all-tools](https://github.com/OpenSIPS/docker-opensips-cp-all-tools) `[2024-07]` - Docker Compose recipe with all OpenSIPS CP tools.
- [asterisk-ajam](https://github.com/staskobzar/asterisk-ajam) `[2026-04]` - Ruby module for interacting with Asterisk management interface (AMI) through HTTP.
- [mod_quickjs](https://github.com/aks-tel/mod_quickjs) `[2026-07]` - Alternative javascript module for Freeswitch.
- [mod_audio_fork](https://github.com/W1ck3dZA/mod_audio_fork) `[2026-02]` - Freeswitch Module For Streaming Audio Over Websockets.
- [gse](https://github.com/cisco/gse) `[2024-03]` - Game State Encoder and Decoder for RTP.
- [SetAPN](https://github.com/herlesupreeth/SetAPN) `[2021-05]` - App to set Internet and IMS APN and force usage of IPv4 over IPv4v6.
- [mod_google_asr](https://github.com/aks-tel/mod_google_asr) `[2026-07]` - Freeswitch Speech-to-Text module.
- [mod_piper_tts](https://github.com/aks-tel/mod_piper_tts) `[2026-03]` - Freeswitch Text-to-Speech module.
- [mod_google_tts](https://github.com/aks-tel/mod_google_tts) `[2026-07]` - Freeswitch Text-To-Speech module.
- [ejabberd](https://codeberg.org/holger/ejabberd) - XMPP/MQTT/SIP server. Hosted on **Codeberg**.
- [freeswitch-modules-libs](https://github.com/lonelyxmas/freeswitch-modules-libs) `[2025-06]` - dependency modules and libs for easycallcenter365.
- [webrtc_phone](https://github.com/sippy/webrtc_phone) `[2025-05]` - WebRTC -> SIP phone built using Sippy B2BUA and Sippy RTPProxy.
- [elecirc](https://github.com/sippy/elecirc) `[2023-07]` - SIP-Pecker: Bot to Monitor and Report Status and Availability of SIP Endpoints.
- [SentryPeer-FreePBX-Module](https://github.com/SentryPeer/SentryPeer-FreePBX-Module) `[2023-05]` - This module queries the SentryPeer Phone Number API when making outbound calls from your FreePBX system to help prevent VoIP cyberattacks, fraudulent VoIP phone calls (toll fraud) and improve cybersecurity by detecting early stage reconnaissance attempts.
- [kamailio-exec-module-examples](https://github.com/EnableSecurity/kamailio-exec-module-examples) `[2023-01]` - Examples referenced from https://www.rtcsec.com/article/kamailio-exec-module-considered-harmful.
- [sbc-rtpengine-sidecar](https://github.com/jambonz/sbc-rtpengine-sidecar) `[2026-07]` - publishes rtp engine status to sbc sip servers.
- [xphone-rust](https://github.com/x-phone/xphone-rust) `[2026-05]` - Rust library for SIP calling and RTP media — register with a trunk or accept calls as a SIP server. Decoded PCM audio via crossbeam channels.
- [mod_openai_realtime](https://github.com/VoiSmart/mod_openai_realtime) `[2026-07]` - FreeSWITCH module to stream audio to OpenAI real-time API with playback via websocket.
- [python-opensips](https://github.com/OpenSIPS/python-opensips) `[2026-05]` - Python module used to communicate with OpenSIPS.
- [app_tdd](https://github.com/dgorski/app_tdd) `[2025-07]` - TDD Module for Asterisk.
- [Sippy_Recorder](https://github.com/sippy/Sippy_Recorder) `[2025-05]` - Example SIP Recorder Server (RFC 7866) build on top of Sippy Python SIP Stack/UA and RTPProxy.
- [ansible-opensips-cp](https://github.com/OpenSIPS/ansible-opensips-cp) `[2025-05]` - Ansible role for installing OpenSIPS CP.
- [arimanager](https://github.com/FreePBX/arimanager) `[2026-07]` - Module of FreePBX (Asterisk REST Interface Users) :: Asterisk 12 introduces the Asterisk REST Interface (ARI), a set of RESTful API's for building Asterisk based applications. This module provides the ability to add and remove ARI users.
- [wsip](https://github.com/emiago/wsip) `[2024-03]` - Wiresip is GO SIP library for easy building SIP stateful proxies.
- [sip_test_data](https://github.com/sippy/sip_test_data) `[2014-10]` - Some real-world looking test data and python code to use it.
- [xphone-go](https://github.com/x-phone/xphone-go) `[2026-07]` - Go library for SIP calling and RTP media — register with a trunk or accept calls as a SIP server. Decoded PCM audio via Go channels.
- [AREDN-Phonebook](https://github.com/swissdigitalnet/AREDN-Phonebook) `[2026-07]` - Lightweight SIP server and phonebook distribution for AREDN networks.
- [avr-asterisk](https://github.com/agentvoiceresponse/avr-asterisk) `[2026-01]` - This is a lightweight Asterisk Docker image optimized for VoIP applications. The image is based on Ubuntu 22.04 and includes only essential modules and features.
- [opensips2019_tutorial](https://github.com/sippy/opensips2019_tutorial) `[2019-05]` - Scrips and configuration files related to the "Advanced RTP media handling using OpenSIPS and RTPProxy: distributed media processing, stream injection, call recording & lawful intercept" tutorial.
- [asterisk-phonebook](https://codeberg.org/post-factum/asterisk-phonebook) - Simple and stupid MySQL-based Asterisk phonebook with PHP-based Web-interface. Hosted on **Codeberg**.
- [asterisk-cpp](https://codeberg.org/augcampos/asterisk-cpp) - The free C++ library for Asterisk PBX integration. (asterisk-java port). Hosted on **Codeberg**.
- [doubango](https://gitea.osmocom.org/ims-volte-vowifi/doubango) - Fork of the doubango IMS client library, upstream at https://github.com/DoubangoTelecom/doubango. Hosted on **Osmocom Gitea**.
- [asterisk-soa-demo](https://codeberg.org/OlafRadicke/asterisk-soa-demo) - Hosted on **Codeberg**.
- [docker-asterisk](https://codeberg.org/m00walker32/docker-asterisk) - Implementacion minima de asterisk en docker. Hosted on **Codeberg**.
- [denwasei](https://codeberg.org/tychosoft/denwasei) - Generic SIP utilities, agents, and command line tools in the spirit of telephony. Hosted on **Codeberg**.
- [minirtp](https://codeberg.org/tychosoft/minirtp) - Small pure C rtp packet builder. Hosted on **Codeberg**.
- [freeswitch-rpm-packaging](https://codeberg.org/timando/freeswitch-rpm-packaging) - Hosted on **Codeberg**.
- [familiar](https://codeberg.org/tychosoft/familiar) - A DECT-like tiny phone system using the sip protocol for purely local devices/. Hosted on **Codeberg**.
- [FreePBX17-Podman-Quadlets](https://codeberg.org/Spoljarevic/FreePBX17-Podman-Quadlets) - FreePBX17 deployed rootless via systemd using Podman Quadlets. Hosted on **Codeberg**.
- [djangopbx-install](https://codeberg.org/DjangoPBX/djangopbx-install) - DjangoPBX - Installer for an example PBX system driven by Django and FreeSwitch. Hosted on **Codeberg**.
- [bash-asterisk-room-close](https://codeberg.org/pkgstore/bash-asterisk-room-close) - Hosted on **Codeberg**.
- [ESP32-SIP](https://codeberg.org/RevK/ESP32-SIP) - Simple SIP client. Hosted on **Codeberg**.
- [pbx](https://codeberg.org/eja/pbx) - A powerful and versatile AI-powered PBX for Asterisk, WhatsApp, Telegram, with text and audio support, built on Tibula. Hosted on **Codeberg**.
- [spycraft](https://codeberg.org/tychosoft/spycraft) - SIP call analysis thru packet inspection. Hosted on **Codeberg**.
- [BCh_SIP_wro](https://codeberg.org/Bartek-Tester/BCh_SIP_wro) - Hosted on **Codeberg**.
- [asterisk-config](https://codeberg.org/mpmc/asterisk-config) - Asterisk configuration with a focus on UK usage. Hosted on **Codeberg**.
- [asterisk-rooms](https://codeberg.org/pkgstore/asterisk-rooms) - Hosted on **Codeberg**.
- [asterisk-chan-quectel](https://codeberg.org/mpmc/asterisk-chan-quectel) - Asterisk channel driver for Quectel and SimCOM modules. Hosted on **Codeberg**.
- [pk-sbc](https://codeberg.org/mwolff44/pk-sbc) - P-KISS-SBC - simple and stupid SIP/RTP SBC - AGPL v3 - Based on kamailio / RTP Engine. Hosted on **Codeberg**.
- [freeswitch-container](https://codeberg.org/thefinn93/freeswitch-container) - Hosted on **Codeberg**.
- [feditel-astconf](https://codeberg.org/winter/feditel-astconf) - default asterisk config for a feditel server. Hosted on **Codeberg**.
- [ansible-prototype](https://gitea.osmocom.org/ims-volte-vowifi/ansible-prototype) - Hosted on **Osmocom Gitea**.
- [SWu-IKEv2](https://gitea.osmocom.org/ims-volte-vowifi/SWu-IKEv2) - A IPsec/ikev2 client written in python for VoWifi testing. Upstream: https://github.com/fasferraz/SWu-IKEv2. Hosted on **Osmocom Gitea**.
- [asterisk-conf](https://codeberg.org/ol-telecom/asterisk-conf) - Hosted on **Codeberg**.
- [Restcomm-Connect](https://github.com/RestComm/Restcomm-Connect) `[2023-04]` - The Open Source Cloud Communications Platform.
- [sip-servlets](https://github.com/RestComm/sip-servlets) `[2024-01]` - Leading SIP - IMS - WebRTC Application Server.
- [jain-sip](https://github.com/RestComm/jain-sip) `[2024-01]` - Disclaimer: This repository is a git-svn mirror of the project found at http://java.net/projects/jsip whose original repository is developed collaboratively by the Advanced Networking Technologies Division at the National Institute of Standards and Technology (NIST) - an agency of the United States Department of Commerce and by a community of in...
- [restcomm-android-sdk](https://github.com/RestComm/restcomm-android-sdk) `[2020-02]` - Android Mobile SDK to easily integrate communication features (WebRTC, messaging, presence, voice, video, screensharing) based on RestComm into native Mobile Applications.
- [sipunit](https://github.com/RestComm/sipunit) `[2023-04]` - Contains SipUnit SIP Testing framework.
- [jain-sip.ext](https://github.com/RestComm/jain-sip.ext) `[2024-01]` - JAIN-SIP-Ext provides extensions done by TeleStax, Inc. for some features that are not supported by the main jain sip stack, like DNS Support (RFC3263).
- [jain-sip.ha](https://github.com/RestComm/jain-sip.ha) `[2024-01]` - JAIN-SIP-HA : Provides extensions done by TeleStax for high availability and fault tolerance through replication of various states of the stack. It supports Call Established Failover or Early Dialog Failover.
- [tas](https://github.com/RestComm/tas) `[2018-05]` - VoLTE & VoWifi Telephony Application Server.
- [sip-presence-service](https://github.com/RestComm/sip-presence-service) `[2018-05]` - Mirror of http://code.google.com/p/sip-presence-service/.
- [jain-sip.docs](https://github.com/RestComm/jain-sip.docs) `[2018-05]` - Documentation for https://github.com/RestComm/jain-sip.
- [jain-slee.sip](https://github.com/RestComm/jain-slee.sip) `[2024-01]` - JAIN SLEE SIP Resource Adaptor Repository.
- [ngrep-sip](https://github.com/sipwise/ngrep-sip) `[2026-06]` - capture SIP flow based on ngrep command.
- [kamailio-config-tests](https://github.com/sipwise/kamailio-config-tests) `[2026-06]` - Kamailio configuration tests.
- [osmo-mgw](https://gitea.osmocom.org/cellular-infrastructure/osmo-mgw) - Osmocom Media Gateway (RTP proxy and RTP/E1 gateway). Hosted on **Osmocom Gitea**.
- [custompbx](https://github.com/custompbx/custompbx) `[2026-04]` - API server and Web GUI for FreeSwitch written in Golang and Angular
- [eventsocket](https://github.com/fiorix/eventsocket) `[2015-06]` - Twisted protocol for the FreeSWITCH's Event Socket
- [voip_perf](https://github.com/jchavanton/voip_perf) `[2026-03]` - SIP performance test tool
- [mod_whisper_asr](https://github.com/aks-tel/mod_whisper_asr) `[2025-01]` - Freeswitch ASR module
- [mod_udptun](https://github.com/aks-tel/mod_udptun) `[2026-07]` - A helper module for the Freeswitch to cloning and tunnelling RTP/UDP traffic
- [sipbench](https://github.com/novartc/sipbench) `[2026-07]` - High-performance SIP stress testing tool based on eBPF/XDP
- [mod_xconf](https://github.com/aks-tel/mod_xconf) `[2026-07]` - Simple and high performance conference module for the Freeswitch
- [cipbx](https://github.com/arthur-s/cipbx) `[2025-09]` - cipbx — a minimalistic VoIP call testing tool implementing a simple echo server in Go using diago
- [astmanproxy](https://codeberg.org/augcampos/astmanproxy) - Asterisk Manager Proxy. Hosted on **Codeberg**.
- [always-online-stun](https://github.com/pradt2/always-online-stun) `[2026-07]` - A list of publicly available STUN servers, refreshed every hour.
- [turn-rs](https://github.com/mycrl/turn-rs) `[2026-07]` - A pure rust implemented turn server.
- [stun](https://github.com/processone/stun) `[2026-03]` - STUN and TURN library for Erlang / Elixir
- Additional FreePBX sub-projects: [cdr](https://github.com/FreePBX/cdr), [cxpanel](https://github.com/FreePBX/cxpanel), [paging](https://github.com/FreePBX/paging), [userman](https://github.com/FreePBX/userman), [logfiles](https://github.com/FreePBX/logfiles), [xmpp](https://github.com/FreePBX/xmpp), [manager](https://github.com/FreePBX/manager), [restart](https://github.com/FreePBX/restart), +2 more
- Additional sipcapture sub-projects: [HEP](https://github.com/sipcapture/HEP), [HEPop](https://github.com/sipcapture/HEPop), [awesome-hep](https://github.com/sipcapture/awesome-hep), [hepipe.js](https://github.com/sipcapture/hepipe.js), [gossipper](https://github.com/sipcapture/gossipper), [hepipe](https://github.com/sipcapture/hepipe), [hep-js](https://github.com/sipcapture/hep-js), [captagent-js](https://github.com/sipcapture/captagent-js), +15 more
### SS7

- [Restcomm SS7](https://github.com/restcomm/jss7) `[2024-06]` - Open Source Java SS7 stack that allows Java apps to communicate with legacy SS7 communications equipment.
- [Restcomm USSD Gateway](https://github.com/RestComm/ussdgateway) `[2024-01]` - Open source USSD Gateway based on Restcomm jSS7 stack. MAP-based USSD services over SS7/SIGTRAN.
- [SigFW](https://github.com/P1sec/SigFW) `[2024-10]` - Open Source Signaling Firewall for SS7, Diameter filtering, antispoof and antisniff.
- [yate](https://github.com/yatevoip/yate) `[2026-06]` - Open Source Telephony engine with support of MTP2/MTP3 over TDM, M2PA, M2UA, M3UA, SCCP, TCAP
- [libtcap](https://github.com/sipwise/libtcap) `[2026-06]` - C library for extracting fields from Sigtran TCAP/INAP messages. From Sipwise.
- [baresip](https://github.com/baresip/baresip) `[2026-07]` - Modular SIP User-Agent library with audio/video, RTP, and ICE support.
- [baresip-studio](https://github.com/juha-h/baresip-studio) `[2026-07]` - Android SIP client built on the baresip library.
- [SIP.js](https://github.com/onsip/SIP.js) `[2026-06]` - Simple and powerful JavaScript SIP signaling library for the browser (WebRTC).
- [sipsorcery](https://github.com/sipsorcery-org/sipsorcery) `[2026-07]` - WebRTC, SIP and VoIP library for C# and .NET, designed for real-time communications.
- [sipexer](https://github.com/miconda/sipexer) `[2026-07]` - Modern and flexible SIP/VoIP CLI tool. From the Kamailio author.
- [siproxd](https://github.com/hb9xar/siproxd) `[2026-05]` - SIP proxy/masquerading daemon for NAT traversal, long-running project.
- [secsipidx](https://github.com/asipto/secsipidx) `[2026-04]` - Secure SIP Identity Extensions (IETF STIR/SHAKEN) CLI and REST API tool.
- [siphon](https://github.com/siphon-project/siphon-sip) `[2026-07]` - High-performance SIP proxy, B2BUA, and IMS platform with Python scripting.
- [FSClient](https://github.com/mitchcapper/FSClient) `[2026-03]` - Full Windows softphone built on FreeSWITCH.
- [Linphone](https://github.com/BelledonneCommunications/linphone-desktop) `[2026-07]` - Free SIP/VoIP video softphone from Belledonne Communications. GitHub mirrors of the linphone.org GitLab: [Android](https://github.com/BelledonneCommunications/linphone-android), [iOS](https://github.com/BelledonneCommunications/linphone-iphone).
- [esphome-intercom](https://github.com/n-IA-hane/esphome-intercom) `[2026-07]` - VoIP/SIP stack for ESPHome and Home Assistant: local SIP phones, softphone, and intercom support on ESP32 hardware.
- [freeswitch_exporter](https://github.com/mroject/freeswitch_exporter) `[2026-03]` - Prometheus exporter for FreeSWITCH.
- [kamailio_exporter](https://github.com/florentchauveau/kamailio_exporter) `[2026-07]` - Prometheus exporter for the Kamailio SIP server.
- [mod_telegram](https://github.com/kvishnivetsky/mod_telegram) `[2026-05]` - FreeSWITCH module for integration with the Telegram network.
- [callcontrol](https://github.com/AGProjects/callcontrol) `[2025-06]` - Call Control Application for OpenSIPS. From AG Projects.

### SMPP / SMS Gateways

- [go-smpp](https://github.com/fiorix/go-smpp) `[2026-04]` - This is an implementation of SMPP 3.4 for Go, based on the original smpp34 from Kevin Patel.
- [Selenium SMPPSim](http://www.seleniumsoftware.com/downloads.html) - (software disappeared) - possible mirror [here](https://github.com/haifzhan/SMPPSim).
- [smppgui](https://github.com/ukarim/smppgui) `[2026-04]` - SMPP gui client
- [Kannel](https://www.kannel.org/) - Compact and powerful open source WAP and SMS gateway, used globally for SMS delivery at scale. [SourceForge](https://sourceforge.net/projects/kannelrelease/).
- [Jasmin SMS Gateway](https://github.com/jookies/jasmin) `[2026-04]` - Open source SMS gateway in Python/Twisted with SMPP and HTTP APIs, message routing/filtering, and real-time billing. Web management UI: [jasmin-web-panel](https://github.com/101t/jasmin-web-panel).
- [Kamex](https://github.com/vaska94/Kamex) `[2026-01]` - Modernized fork of Kannel with WAP removed. 16,000+ msg/sec, SMPP 3.3/3.4/5.0, EMI/UCP, HTTP, Prometheus metrics, Kubernetes health checks.


- [sms-api-server](https://github.com/fiorix/sms-api-server) `[2026-04]` - HTTP API to send SMS via SMPP.
- [go-smpp](https://github.com/CursedHardware/go-smpp) `[2022-12]` - A complete implementation of SMPP v5 protocol, written in golang.
- [sms_smsc](https://github.com/P1sec/sms_smsc) `[2014-07]` - Android application which allows sending SMS, with a specific SMSC without changing system defaults.
- [smscgateway](https://github.com/RestComm/smscgateway) `[2024-01]` - RestComm SMS Gateway (SMSC) to send/receive SMS from/to Operators Network (GSM).
- [smpp-extensions](https://github.com/RestComm/smpp-extensions) `[2024-01]` - Extensions for configuration, management and monitoring of the Restcomm Cloudhopper SMPP Stack.
- [osmo_smsc](https://gitea.osmocom.org/erlang/osmo_smsc) - [WIP] Osmocom SMSC implementation in Erlang. Hosted on **Osmocom Gitea**.
- [libsmpp34](https://gitea.osmocom.org/cellular-infrastructure/libsmpp34) - Osmocom fork of Open SMPP 3.4 Library. Hosted on **Osmocom Gitea**.
- [rsms](https://github.com/symphos/rsms) `[2026-06]` - Rust four-protocol SMS gateway (CMPP/SMGP/SMPP/SGIP) with long-message splitting and sliding-window flow control.
- [smppsink](https://github.com/PowerMeMobile/smppsink) `[2026-05]` - SMPP gateway simulator from the Power Alley Gateway suite.
- [smpp-relay-service](https://github.com/rixtrayker/smpp-relay-service) `[2026-02]` - Lightweight SMPP gateway for SMS routing and delivery tracking.
- [android-sms-gateway](https://github.com/capcom6/android-sms-gateway) `[2026-07]` - Turn an Android phone into an SMS gateway with a REST API for sending and receiving messages. Companion [standalone server](https://github.com/android-sms-gateway/server) and client libraries ([Go](https://github.com/android-sms-gateway/client-go), [Python](https://github.com/android-sms-gateway/client-py), [TS](https://github.com/android-sms-gateway/client-ts), [PHP](https://github.com/android-sms-gateway/client-php)).
- [textbee](https://github.com/vernu/textbee) `[2026-07]` - Open-source SMS gateway turning Android phones into senders, with web dashboard and REST API.
- [playSMS](https://github.com/playsms/playsms) `[2026-07]` - Web interface for SMS gateways and bulk SMS services, in PHP. Long-running project.
- [traccar-sms-gateway](https://github.com/traccar/traccar-sms-gateway) `[2026-07]` - Android SMS gateway app from the Traccar GPS tracking project.
- [android_income_sms_gateway_webhook](https://github.com/bogkonstantin/android_income_sms_gateway_webhook) `[2026-06]` - Simple Android app forwarding incoming SMS to a URL webhook.
- [sms-gammu-gateway](https://github.com/pajikos/sms-gammu-gateway) `[2026-06]` - REST API gateway for sending and receiving SMS through gammu-supported GSM modems.
- [gomsggw](https://github.com/sagostin/gomsggw) `[2026-07]` - Multi-protocol messaging gateway bridging SMPP/MM4 with REST APIs and webhooks.
- [luci-app-sms-tool](https://github.com/4IceG/luci-app-sms-tool) `[2025-10]` - OpenWrt LuCI interface for SMS / USSD / AT commands on cellular modems. Successors: [JS version](https://github.com/4IceG/luci-app-sms-tool-js) `[2026-07]`, [ModemManager variant](https://github.com/4IceG/luci-app-sms-manager) `[2026-07]`.
- [luci-app-5gmodem](https://github.com/fildunsky/luci-app-5gmodem) `[2026-07]` - OpenWrt LuCI app for 5G modems: signal/band management, TTL fixing, SMS inbox and USSD/AT console.
- [sms-gateway (mattboston)](https://github.com/mattboston/sms-gateway) `[2026-07]` - Self-hosted SMS gateway in Go with WebUI and REST API for USB GSM modems.
- [sms2mqtt](https://github.com/Domochip/sms2mqtt) `[2025-11]` - Send and receive SMS through MQTT using a USB GSM dongle via gammu.
- [sms-server](https://github.com/morgverd/sms-server) `[2026-02]` - Self-hosted SMS gateway for Raspberry Pi and GSM modems with HTTP/WebSocket APIs, encrypted message storage and delivery tracking.
- [Sendium](https://github.com/cytechmobile/sendium) `[2026-07]` - Open-source SMS gateway in Java.
- [goip](https://github.com/styryl/goip) `[2026-01]` - Server and client for GoIP GSM VoIP gateways for sending and receiving SMS.
- [Vendel](https://github.com/JimScope/vendel) `[2026-07]` - Open-source SMS gateway for your own devices. Companion [Android app](https://github.com/JimScope/vendel-android).
## Satellite Communication
- [Hughes_OneWeb_Monitor](https://github.com/nickvsnetworking/Hughes_OneWeb_Monitor) `[2025-04]` - Hughes OneWeb Terminal Prometheus Exporter
- [SatNOGS](https://gitlab.com/librespacefoundation/satnogs) - Open Source Global Satellite Ground Station Network focused on LEO satellites, from the Libre Space Foundation. Hosted on **GitLab**.
- [gr-leo](https://gitlab.com/librespacefoundation/gr-leo) `[2025-10]` - GNU Radio Out-of-Tree module simulating the telecommunication channel between orbiting satellites and ground stations, from Libre Space Foundation / ESA SDR Makerspace. Hosted on **GitLab**.
- [OpenSN](https://github.com/OpenSN-Library/OpenSN-Library) `[2026-05]` - Open source library for emulating LEO satellite networks. Container-based, 5-10x faster than StarryNet.
- [Satellite-Open-Source](https://github.com/jwwthu/Satellite-Open-Source) `[2026-07]` - Curated collection of open source code and data for satellite communication research.
- [Hypatia](https://github.com/snkas/hypatia) `[2024-05]` - LEO satellite network simulation framework with ns-3 packet-level simulation and CesiumJS visualization. Supports Starlink and Kuiper constellations. Published at ACM IMC 2020.
- [LEOViz](https://github.com/clarkzjw/LEOViz) `[2026-01]` - LEO satellite constellation measurement and visualization tool for Starlink/OneWeb. Grafana/CesiumJS integration. From University of Victoria.
- [GNSS-SDR](https://sourceforge.net/projects/gnss-sdr/) - Open source software-defined GNSS (Global Navigation Satellite Systems) receiver written in C++ and based on GNU Radio. Hosted on **SourceForge**.
- [OAI-5G-NR-NTN](https://github.com/ngkore/OAI-5G-NR-NTN) `[2026-04]` - Deployment guide and configurations for OpenAirInterface 5G NR over Non-Terrestrial Networks using RFsimulator with both GEO and LEO satellite scenarios.
- [starlink-grpc-tools](https://github.com/sparky8512/starlink-grpc-tools) `[2026-05]` - De-facto reference Python toolkit for talking to the SpaceX Starlink user terminal's local gRPC API: stats, history, alerts, Prometheus/InfluxDB exporters.
- [starlink_exporter](https://github.com/clarkzjw/starlink_exporter) `[2026-01]` - Self-contained Prometheus exporter and Grafana stack for Starlink dish telemetry. Companion to LEOViz from the same author.
- [ground-station](https://github.com/sgoudelis/ground-station) `[2026-07]` - Browser-based ground station suite for satellite tracking, SDR reception, hardware control, and telemetry decoding.
- [SGP.NET](https://github.com/parzivail/SGP.NET) `[2026-05]` - C# SGP4 satellite prediction library with TLE loading and coordinate system conversions.
- [svarog](https://github.com/gut-space/svarog-server) `[2026-05]` - Ground station network server for receiving satellite transmissions on VHF, UHF, and more.
- [open5gs-satellite](https://github.com/root-hbx/open5gs-satellite) `[2026-01]` - Open5GS adapted for satellite (NTN) network research.
- [ntn-operators](https://github.com/thc1006/ntn-operators) `[2026-07]` - Kubernetes operators for non-terrestrial networks: satellite ephemeris, ground station lifecycle, and cell management.
- [LeoHoSim_MATLAB](https://github.com/jtlee-97/LeoHoSim_MATLAB_2024) `[2026-05]` - Time-stepped MATLAB simulator for 5G NTN with a 600 km LEO constellation (per 3GPP TR 38.821) and a hybrid handover mechanism for handheld UEs.
- [sdr-o-ran-platform](https://github.com/thc1006/sdr-o-ran-platform) `[2026-04]` - SDR + cloud-native O-RAN research platform for satellite NTN with AI/ML (DRL) optimization and quantum-safe (NIST PQC) cryptography.


- [The Things Stack](https://github.com/TheThingsNetwork/lorawan-stack) `[2026-07]` - Open-source LoRaWAN Network Server. Powers The Things Network and The Things Industries.
- [ChirpStack](https://github.com/chirpstack/chirpstack) `[2026-07]` - Open-source LoRaWAN Network Server with Class A/B/C, multicast, FUOTA, and MQTT/HTTP integrations.
- [chirpstack-packet-multiplexer](https://github.com/chirpstack/chirpstack-packet-multiplexer) `[2026-02]` - Forward Semtech UDP packet-forwarder data to multiple LoRaWAN network servers simultaneously.
- [Helium router](https://github.com/helium/router) `[2026-05]` - LoRaWAN Network Server used by the Helium network, in Erlang.
- [LoRa_Craft](https://github.com/PentHertz/LoRa_Craft) `[2025-11]` - Some Scapy layers and tools to study LoRa PHY and LoRaWAN.
- [lorawan-analyzer](https://github.com/1rabbit/lorawan-analyzer) `[2026-02]` - Real-time LoRaWAN traffic analyzer. Works with any LoRaWAN gateway on any LNS : ChirpStack, TTN, Helium... ChirpStack unlocks additional application-level enrichment.
- [LoRaWAN-SIM](https://github.com/deltazita/LoRaWAN-SIM) `[2026-06]` - A LoRaWAN simulator for confirmed/unconfirmed transmissions and multiple gateways.
- [maverick](https://github.com/antonygiomarxdev/maverick) `[2026-04]` - Offline-first LoRaWAN gateway + network server in a single binary. Runs on Raspberry Pi. No cloud required.
- [ttn-gateway-collector](https://github.com/bertrik/ttn-gateway-collector) `[2026-07]` - Collects data from multiple TTN (v3) gateways for LoRaWAN traffic analysis.
- [librespacefoundation/python-satellitetle](https://gitlab.com/librespacefoundation/python-satellitetle) `[2026-06]` - Fetch satellite TLEs from various online sources. Hosted on **GitLab**.
- [nixos-lorawan-gateway](https://github.com/DistRap/nixos-lorawan-gateway) `[2025-09]` - NixOS LoRaWAN Gateway.
- [elora](https://github.com/Orange-OpenSource/elora) `[2026-05]` - An ns-3 module for end-to-end LoRaWAN emulation with real network server stacks.
- [librespacefoundation/picobus](https://gitlab.com/librespacefoundation/picobus) `[2026-04]` - 8p pico-satellite deployer. Hosted on **GitLab**.
- [wisevision_lorawan_bridge](https://github.com/wise-vision/wisevision_lorawan_bridge) `[2026-04]` - Streams data from ChirpStack / LoRaWAN gateways straight into ROS 2 topics.
- [chirpstack-basicstation-eu868](https://github.com/furkankayam/chirpstack-basicstation-eu868) `[2026-03]` - ✅ Production-ready ChirpStack v4 LoRaWAN stack with BasicStation gateway support on Docker.
- [lorawan-simulator](https://github.com/emanuele-dedonatis/lorawan-simulator) `[2026-02]` - An open-source LoRaWAN® network simulator to simulate multiple gateways and devices for testing LoRaWAN® applications without physical hardware.
- [LoRaWAN-Basic-Station-RAK831-](https://github.com/WGLabz/LoRaWAN-Basic-Station-RAK831-) `[2025-12]` - LoRa Basics™ Station - The LoRaWAN Gateway Software.
- [heltec-wireless-tracker](https://github.com/lacyberfabrique/heltec-wireless-tracker) `[2025-10]` - Tracker GPS LoRaWAN basé sur Heltec Wireless Tracker (ESP32-S3 + SX1262 + GPS). Transmet en temps réel les coordonnées GPS via LoRaWAN (TTN/ChirpStack) avec affichage sur écran TFT intégré, gestion OTAA persistante et réception downlink pour la distance depuis la gateway.
- [PiWAN](https://github.com/Cosmic-Pulse/PiWAN) `[2025-06]` - An all-in-one gateway solution for Raspberry Pi + LoRaWAN using BasicStation and Grafana.
- [librespacefoundation/pystrf](https://gitlab.com/librespacefoundation/pystrf) `[2023-01]` - Python based radio frequency satellite tracking. Hosted on **GitLab**.
- [xiao-lora-water-meter](https://codeberg.org/JF002/xiao-lora-water-meter) - Low-power battery operated LoRaWAN pulse counter, intended to be used as a water meter, to monitor the water usage of my house. Hosted on **Codeberg**.
- [lorawan](https://codeberg.org/hiltsu/lorawan) - This repository contains files and resources for my personal LoRaWAN project. The goal is to build a complete LoRaWAN hardware and software stack covering the field device (node), the gateway, and network management. Hosted on **Codeberg**.
- [uwan](https://codeberg.org/b00bl1k/uwan) - 📶 Uwan Micro LoRaWAN Stack. Hosted on **Codeberg**.
- [lorawan_decode](https://codeberg.org/StephanWaldtmann/lorawan_decode) - Hosted on **Codeberg**.
- [lorawan-weatherbuoy-infographic](https://codeberg.org/pinecone460/lorawan-weatherbuoy-infographic) - infographic about LoRaWAN-connected buoys communicating and measuring oceanic weather data. final project for oceanography 161 (intro to evnironmental monitoring) at the university of washington. Hosted on **Codeberg**.
- [node-red-applications](https://codeberg.org/loralarm/node-red-applications) - Applications for Lora devices done in node-red. LoraLarm.org. Hosted on **Codeberg**.
- [pyLoRa](https://codeberg.org/fab/pyLoRa) - LoRa Transmissions of Gemini or Gopher posts over USB-Stick (serial) in Python3. Hosted on **Codeberg**.
- [seeed-lorawan-kit](https://codeberg.org/Supernova/seeed-lorawan-kit) - Customization of the Seeed LoRaWAN Kit firmware for other sensors. Hosted on **Codeberg**.
- [satellite-solar-power-budget](https://gitlab.com/librespacefoundation/satellite-solar-power-budget) Hosted on **GitLab**.
- [satnogs-ops](https://gitlab.com/librespacefoundation/satnogs-ops) `[2026-07]` - Repository for tracking SatNOGS Operations Hosted on **GitLab**.
## Protocols

### ASN1-based, S1AP/NGAP

- [Pycrate](https://github.com/pycrate-org/pycrate) `[2026-06]` - A Python library to ease the development of encoders and decoders for various protocols and file formats, especially telecom ones. Provides an ASN.1 compiler and a CSN.1 runtime.
- [pycrate-rs](https://github.com/EFForg/pycrate-rs) `[2025-07]` - Rust telecom protocol parser generated from pycrate. From the EFF (Rayhunter project).
- [bazel-pycrate](https://github.com/ravens/bazel-pycrate) `[2023-07]` - A bazel-based pycrate ready jupyter notebook env
- [hampi](https://github.com/gabhijit/hampi) `[2025-08]` - The Goal of this project is to implement an ASN.1 Compiler in Rust which can generate Rust bindings for different ASN.1 specifications.
- [Eclipse Titan TTCN-3 (core)](https://gitlab.eclipse.org/eclipse/titan/titan.core/) `[2026-07]` - Open source TTCN-3 compiler and runtime from Ericsson/Eclipse, with built-in ASN.1 BER/PER/XML codecs. Used for telecom protocol conformance testing. Hosted on **GitLab (Eclipse)**.
- [oxirush-ngap](https://github.com/linouxis9/oxirush-ngap) `[2026-04]` - Auto-generated Rust APER codec for 5G NGAP from official 3GPP ASN.1 definitions. Companion to oxirush-nas.
- [ASN1-Definitions](https://github.com/handymenny/ASN1-Definitions) `[2026-06]` - S1AP, NGAP, LTE and NR RRC ASN.1 definitions extracted from Wireshark.

### NAS 4G/5G and Milenage

- [mts-nas](https://github.com/ericsson-mts/mts-nas) `[2023-04]` - Project to decode/encode Non-Access Stratum (NAS) protocol.
- [LTE-security](https://fabricioapps.blogspot.com/2012/05/lte-security.html) - a Windows application that implements all the security procedures for LTE referred in Annex A and Annex B of 3GPP 33.401. Last update in 2020, direct [link](https://www.dropbox.com/s/adpa2yuac99riqt/LTE%20Security%203.3.zip?dl=0)
- [milenage](https://github.com/emakeev/milenage) `[2020-10]` - Go implementation of milenage ciphers.
- [nas-5gs](https://github.com/hzane/nas-5gs) `[2020-02]` - Routines for Non-Access-Stratum (NAS) protocol for NAS-NR(5GS).
- [oxirush-nas](https://github.com/linouxis9/oxirush-nas) `[2026-04]` - A Rust Library that allows the decoding/encoding of NAS-5G messages. From Valentin D'Emmanuele - France.
- [CryptoMobile](https://github.com/P1sec/CryptoMobile) `[2023-01]` - C implementations with Python bindings for mobile network cryptographic algorithms (Milenage, TUAK, Kasumi, SNOW, ZUC). From P1 Security.
- [milenage (Go)](https://github.com/wmnsk/milenage) `[2025-05]` - MILENAGE algorithm implementation in Go for 3G/4G/5G AKA authentication.
- [oxirush-security](https://github.com/linouxis9/oxirush-security) `[2026-03]` - 5G NAS security algorithms in Rust — key derivation, NIA/NEA integrity and ciphering, and SUCI concealment per 3GPP TS 33.501. Companion to oxirush-nas/ngap.

### GTP/PFCP

- [Kernel GTP-U](https://osmocom.org/projects/linux-kernel-gtp-u) - This is an implementation of the GTP-U (user plane) inside the Linux kernel.
- [go-gtp](https://github.com/wmnsk/go-gtp) `[2026-07]` - Package gtp provides simple and painless handling of GTP(GPRS Tunneling Protocol), implemented in the Go Programming Language.
- [go-pfcp](https://github.com/wmnsk/go-pfcp) `[2026-04]` - PFCP(Packet Forwarding Control Protocol) is a signaling protocol used in mobile networking infrastructure(LTE EPC, 5GC) to realize CUPS architecture(Control and User Plane Separation, not a printing system) defined in 3GPP TS29.244.
- [gtplib](https://github.com/travelping/gtplib) `[2025-09]` - Erlang GTPv1/GTPv2 library.
- [gtpv2](https://github.com/blorticus/gtpv2) `[2021-09]` - GPRS Tunneling Protocol Library for golang.
- [scapy-gtp](https://github.com/secdev/scapy/blob/master/scapy/contrib/gtp.py) `[2026-07]` - Scapy (A interactive packet manipulation program) GTP layer. Spec: 3GPP TS 29.060 and 3GPP TS 29.274. Some IEs: 3GPP TS 24.008.
- [gtp_dialer](https://github.com/fasferraz/gtp_dialer) `[2025-11]` - GTPv1/GTPv2 Dialer
- [nwGTPv2](https://sourceforge.net/projects/nwgtpv2/) - Free and open source implementation of eGTP (GTPv2) control plane, supporting S11, S5, S8 EPC interfaces. Also provides nwEPC SAE-Gateway framework. Hosted on **SourceForge**.
- [pfcpsim](https://github.com/omec-project/pfcpsim) `[2026-07]` - PFCP client simulator for UPF testing. From the SD-Core/OMEC project.
- [pfcplib](https://github.com/travelping/pfcplib) `[2024-06]` - Erlang library for encoding/decoding PFCP frames per 3GPP TS 29.244. From Travelping.
- [OpenGGSN](https://sourceforge.net/projects/ggsn/) - Open source Gateway GPRS Support Node (GGSN) with SGSN emulator for core network testing. Maintained within Osmocom. Hosted on **SourceForge**.
- [NextMN go-pfcp-networking](https://github.com/nextmn/go-pfcp-networking) `[2026-07]` - PFCP networking functionalities on top of go-pfcp. From the NextMN project.
- [libosmo-pfcp](https://gitea.osmocom.org/osmocom/libosmo-pfcp) - C library for PFCP protocol encoding/decoding and session endpoint management. Hosted on **Osmocom Gitea**.
- [gtp-load-gen](https://gitea.osmocom.org/cellular-infrastructure/gtp-load-gen) - High-performance GTP-U load generator using Linux io_uring. Hosted on **Osmocom Gitea**.
- [gtp-rs](https://github.com/ErvinsK/gtp-rs) `[2025-12]` - Pure Rust implementation of 3GPP GTP (GTPv1 and GTPv2) protocols.
- [free5gc gtp5g-tracer](https://github.com/free5gc/gtp5g-tracer) `[2025-10]` - Debug gtp5g kernel module using eBPF. From the free5GC project.
- [rs-pfcp](https://github.com/xandlom/rs-pfcp) `[2026-07]` - Rust implementation of the PFCP protocol (3GPP TS 29.244), modeled on go-pfcp. Includes an interop test harness against the Go reference.
- [gopacket-gtp](https://github.com/nextmn/gopacket-gtp) `[2026-07]` - Patch for gopacket fixing serialization of GTP Extension Headers. From the NextMN project.
- [simple_pfcp_client](https://github.com/s5uishida/simple_pfcp_client) `[2026-03]` - Minimal PFCP client useful for poking at UPFs and validating PFCP exchanges during 5GC labs.


- [diameter](https://github.com/mensonen/diameter) `[2026-03]` - A diameter stack implementation written in python.
- [gtp_u_edp](https://github.com/travelping/gtp_u_edp) `[2018-06]` - GTPv1-U Proxy.
- [iptables_ext_gtp](https://github.com/herlesupreeth/iptables_ext_gtp) `[2017-10]` - iptables extension for gtp encap and decap.
- [gtp_u_kmod](https://github.com/travelping/gtp_u_kmod) `[2023-10]` - GTPv1-U Erlang interface process for Kernel Datapath.
- [asn1c](https://gitea.osmocom.org/osmocom/asn1c) - asn1c (Lev Walkin) extended with features required by MAP/TCAP. Hosted on **Osmocom Gitea**.
- [libosmo-sccp-legacy](https://gitea.osmocom.org/osmocom/libosmo-sccp-legacy) - Currently maintained software should use libosmo-sigtran instead. Hosted on **Osmocom Gitea**.
- [libosmo-sccp](https://gitea.osmocom.org/osmocom/libosmo-sccp) - SCCP + SIGTRAN (SUA/M3UA) libraries as well as OsmoSTP. Hosted on **Osmocom Gitea**.
- [osmo-uecups](https://gitea.osmocom.org/cellular-infrastructure/osmo-uecups) - Osmocom UE/MME/SGW/SGSN side GTP-U Implementation with control/user plane separation. Hosted on **Osmocom Gitea**.
- [libgtpnl](https://gitea.osmocom.org/cellular-infrastructure/libgtpnl) - netlink library for Linux kernel GTP code. Hosted on **Osmocom Gitea**.
- [asn1-ss7](https://gitea.osmocom.org/cellular-infrastructure/asn1-ss7) - ITU/ETSI/3GPP ASN1 files for TCAP, ROS, MAP and CAP. Hosted on **Osmocom Gitea**.
- [osmo_ss7](https://gitea.osmocom.org/erlang/osmo_ss7) - Erlang implementation of M2UA/M3UA/MTP3/SCCP/ISUP codec + utils. Hosted on **Osmocom Gitea**.
- [osmo_map](https://gitea.osmocom.org/erlang/osmo_map) - Erlang implementation of TCAP/MAP. Hosted on **Osmocom Gitea**.
- [osmo_sccp](https://gitea.osmocom.org/erlang/osmo_sccp) - Erlang implementation of SCCP (ITU-T Q.71x). Hosted on **Osmocom Gitea**.
- [cisco_pfcp](https://github.com/dufourgilles/cisco_pfcp) `[2026-03]` - Wireshark PFCP decoder updated with Cisco CUPS-specific IEs.
### SCTP

- [sctp](https://github.com/ishidawataru/sctp) `[2025-11]` - Stream Control Transmission Protocol (SCTP) in Go.
- [usrsctp](https://github.com/sctplab/usrsctp) `[2025-10]` - This is a userland SCTP stack supporting FreeBSD, Linux, Mac OS X and Windows.
- [PySCTP](https://github.com/P1sec/pysctp) `[2026-02]` - PySCTP - SCTP bindings for Python.
- [MTS: Multiprotocol Test Tool](https://github.com/ericsson-mts/mts) `[2023-11]` - MTS (Multi-protocol Test Suite) is a multi-protocol testing tool specially designed for telecom IP-based architectures (see above "Features" section for more details).
- [scapy-sctp](https://github.com/secdev/scapy/blob/master/scapy/layers/sctp.py) `[2026-07]` - Scapy (A interactive packet manipulation program) SCTP layer.
- [ellora](https://github.com/gabhijit/ellora/) `[2023-11]` - Rust SCTP Toolkit. The Goal of this project is to make safe bindings for Linux SCTP stack that can be used within Rust's `async` ecosystem.
- [sctplb](https://github.com/omec-project/sctplb) `[2026-07]` - SCTP Load Balancer for 5G core networks. From the SD-Core/OMEC project.
- [sctp-go](https://github.com/thebagchi/sctp-go) `[2026-01]` - SCTP library for Go using native kernel sockets.
- [go-sctp](https://github.com/georgeyanev/go-sctp) `[2025-12]` - Go SCTP implementation with net-package-style Dial/Listen API.

### VoWiFi/VoLTE

- [SWu-IKEv2](https://github.com/fasferraz/SWu-IKEv2) `[2026-04]` - SWu client emulator in Python that establishes an IKEv2/IPSec tunnel with an ePDG, implementing both control plane (IKEv2) and user plane (IPSec).
- [osmo-epdg](https://gitea.osmocom.org/erlang/osmo-epdg) - Implement an ePDG with an embedded AAA server. osmo-ePDG also requires a modified [strongswan-epdg](https://gitea.osmocom.org/ims-volte-vowifi/strongswan-epdg). Hosted on **Osmocom Gitea**.
- [ims-client](https://gitea.osmocom.org/septs/ims-client) - IMS client with SWu (VoWiFi) protocol in PHP. Hosted on **Osmocom Gitea**.
- [NWu-Non3GPP-5GC](https://github.com/fasferraz/NWu-Non3GPP-5GC) `[2024-09]` - NWu IKEv2/IPSec dialer for 5GC N3IWF (Non-3GPP Interworking Function). From the author of eNB s1 emulator and gtp_dialer.
- [GBA_ME](https://github.com/fasferraz/GBA_ME) `[2023-10]` - Generic Bootstrapping Architecture (GBA) ME emulator in Python. From fasferraz.
- [vowifi-epdg-scanning](https://github.com/sbaresearch/vowifi-epdg-scanning) `[2026-07]` - VoWiFi ePDG scanning toolkit and dataset from SBA Research, used to enumerate and probe operator ePDG endpoints worldwide.
- [vowifi-sms](https://github.com/dmitzsaz/vowifi-sms) `[2025-10]` - Go-based VoWiFi (IMS/ePDG) client capable of registering to a carrier IMS over Wi-Fi and receiving SMS without an active mobile connection.
- [carrier_wifi_http_server](https://github.com/herlesupreeth/carrier_wifi_http_server) `[2023-03]` - Server hosting the carrier certificate used by handsets to encrypt the IMSI when authenticating to WLAN (Hotspot 2.0) and ePDG (VoWiFi).
- [free5gc/ike](https://github.com/free5gc/ike) `[2026-05]` - free5GC's standalone IKEv2 implementation used by N3IWF/TNGF. Reusable as a Go IKE library outside free5GC.
- [vowifi_gateway](https://github.com/pagecat/vowifi_gateway) `[2026-07]` - VoWiFi-to-SIP gateway with voice and SMS support, needing only a Linux server and a PC/SC card reader.


### Diameter

- [go-diameter](https://github.com/fiorix/go-diameter) `[2026-05]` - Package go-diameter is an implementation of the Diameter Base Protocol RFC 6733 and a stack for the Go programming language.
- [jdiameter](https://github.com/RestComm/jdiameter/) `[2024-01]` - RestComm jDiameter provides an Open Source Java implementation of the Diameter standard for Authentication, Authorization, and Accounting (AAA).
- ⚠️ [diafuzzer](https://github.com/Orange-OpenSource/diafuzzer) `[2019-10]` - Diameter fuzzer, based on specifications of Diameter applications following rfc 3588 / 6733 from Orange.
- [bromelia](https://github.com/heimiricmr/bromelia) `[2024-05]` - A Python micro framework for building Diameter protocol applications.
- [freeDiameter](http://www.freediameter.net/) - Open source implementation of the Diameter protocol (RFC 6733). Extensible platform for AAA with modular architecture. Also available on [GitLab (Eurecom)](https://gitlab.eurecom.fr/oai/freediameter).
- [Open Diameter](https://sourceforge.net/projects/diameter/) - Open source C++ implementation of the Diameter protocol, licensed under GPLv2/LGPLv2. Hosted on **SourceForge**.
- [eradius](https://github.com/travelping/eradius) `[2026-06]` - Erlang RADIUS server framework. From Travelping.
- [prometheus_diameter_collector](https://github.com/travelping/prometheus_diameter_collector) `[2026-05]` - Diameter Prometheus.io collector for monitoring Diameter signaling. From Travelping.
- [xk6-diameter](https://github.com/lwlee2608/xk6-diameter) `[2025-10]` - k6 extension for Diameter protocol load testing. Written in Go.
- [diameter-rs](https://github.com/lwlee2608/diameter-rs) `[2025-10]` - Rust implementation of the Diameter Protocol (RFC 6733).
- [SigScale RADIUS](https://github.com/sigscale/radierl) `[2025-02]` - RADIUS protocol stack for Erlang with EAP and DIAMETER transport support. Part of the SigScale telecom stack.
- [quarkus-jdiameter](https://github.com/quarkiverse/quarkus-jdiameter) `[2026-06]` - Quarkus extension adding Diameter protocol support, based on jDiameter.
- [VolkDS/diameter](https://github.com/VolkDS/diameter) `[2026-07]` - Implementation of the Diameter Base Protocol (RFC 6733) for C++.
- [blorticus-go/diameter](https://github.com/blorticus-go/diameter) `[2026-03]` - Diameter protocol implementation for Golang.

### SS7/SIGTRAN

- [go-m3ua](https://github.com/wmnsk/go-m3ua) `[2026-01]` - Package m3ua provides easy and painless handling of M3UA protocol in pure Golang.
- [go-sccp](https://github.com/wmnsk/go-sccp) `[2025-06]` - Package sccp provides simple and painless handling of SCCP(Signaling Connection Control Part) in SS7/SIGTRAN stack, implemented in the Go Programming Language.
- [libosmo-sccp](https://git.osmocom.org/libosmo-sccp/) - SCCP Library
- [go-tcap](https://github.com/wmnsk/go-tcap) `[2026-01]` - Package tcap provides simple and painless handling of TCAP(Transaction Capabilities Application Part) in SS7/SIGTRAN protocol stack.
- [openss7](http://www.openss7.org/) - An opensource development project (called OpenSS7) to provide a robust and GPL'ed SS7, SIGTRAN, ISDN and VoIP stack for Linux and other UN*X operating systems.
- [Extended jSS7](https://github.com/PAiC-team/Extended-jSS7) `[2023-07]` - Extended Java SS7 stack with MTP2/MTP3, ISUP, SCCP, TCAP, CAMEL (Phase I-IV) and MAP. Supports SIGTRAN (SCTP/M3UA) over IP.
- [signerl](https://gitea.osmocom.org/erlang/signerl/) - Erlang SS7 TCAP/MAP implementation. Originally from Motivity, continued within the Osmocom project. Hosted on **Osmocom Gitea**.
- [SigScale TCAP](https://github.com/sigscale/tcap) `[2026-06]` - SS7 Transaction Capabilities Application Part (TCAP) protocol stack in Erlang, used by MAP and CAP applications in mobile operator networks.
- [SigScale CSE](https://github.com/sigscale/cse) `[2026-04]` - Custom (CAMEL) Service Environment in Erlang. Part of the SigScale SS7 stack.
- [SigScale GTT](https://github.com/sigscale/gtt) `[2026-02]` - Global Title Translation (GTT) in Erlang. Part of the SigScale SS7 stack.
- [SigScale M3UA](https://github.com/sigscale/m3ua) `[2025-02]` - SIGTRAN M3UA protocol stack in Erlang. Part of the SigScale SS7 stack with companion [SCCP](https://github.com/sigscale/sccp), [MAP](https://github.com/sigscale/map), [CAP](https://github.com/sigscale/cap), and [INAP](https://github.com/sigscale/inap) modules.
- [osmo-dia2gsup](https://gitea.osmocom.org/erlang/osmo_dia2gsup) - Diameter-to-GSUP inter-working function in Erlang. Bridges Diameter-based AAA with Osmocom GSUP protocol. Hosted on **Osmocom Gitea**.
- [osmo_cap](https://gitea.osmocom.org/erlang/osmo_cap) - CAMEL Application Part (CAP) implementation in Erlang. Hosted on **Osmocom Gitea**.
- Additional RestComm sub-projects: [load-balancer](https://github.com/RestComm/load-balancer), [sctp](https://github.com/RestComm/sctp), [jain-slee.diameter](https://github.com/RestComm/jain-slee.diameter), [charging-server](https://github.com/RestComm/charging-server), [jain-slee.ss7](https://github.com/RestComm/jain-slee.ss7)

### Dataplane acceleration

- [fastswan](https://github.com/acassen/fastswan) `[2026-06]` - Linux Kernel XFRM/IPsec offload via eBPF/XDP. Relevant for mobile core SWu/N3IWF tunnels. From the gtp-guard/keepalived author.
- [xdp-fwd](https://github.com/acassen/xdp-fwd) `[2026-03]` - XDP Forwarding suite for high-performance packet processing via eBPF/XDP. From the gtp-guard/keepalived author.
- [socket-takeover](https://github.com/acassen/socket-takeover) `[2023-11]` - Live socket transfer between processes, engineered for zero-downtime upgrades of dataplane services such as gtp-guard.
- [fpp-vpp](https://github.com/travelping/fpp-vpp) `[2026-04]` - Foundation library used by Travelping's VPP-based subprojects (upg-vpp etc.) for VPP-based fastpath telco services.
- [Ligato](https://github.com/ligato/vpp-agent) `[2025-04]` - Controlplane agent for FD.io VPP
- [FD.io](https://fd.io) - FD.io is a vector processing engine (VPP). VPP processes a number of packets in parallel instead of one at a time thus significantly improving packet throughput.
- [OVS](http://www.openvswitch.org) - Open vSwitch is a production quality, multilayer virtual switch licensed under the open source Apache 2.0 license.
- [DPDK](https://www.dpdk.org) - DPDK is the Data Plane Development Kit that consists of libraries to accelerate packet processing workloads running on a wide variety of CPU architectures. [Vista Creek (FPGA-based baseband accelerator)](https://www.intel.com/content/www/us/en/wireline/products/programmable/applications/nfv.html) support has been added to [DPDK](https://doc.dpdk.org/guides/bbdevs/fpga_lte_fec.html).

### Others

- ⚠️ [open-nFAPI](https://github.com/cisco/open-nFAPI) `[2018-08]` - Open-nFAPI is implementation of the Small Cell Forum's network functional API or nFAPI for short. nFAPI defines a network protocol that is used to connect a Physical Network Function (PNF) running LTE Layer 1 to a Virtual Network Function (VNF) running LTE layer 2 and above.
- [CSDR](https://github.com/simonyiszk/csdr) `[2024-02]` - csdr is a command line tool to carry out DSP tasks for Software Defined Radio.
- [DiagLibrary](https://github.com/sanjaywave/DiagLibrary) `[2016-08]` -  a JNI library that implement a DIAG protocol parser under C code to be used under Android or Linux.
- [5G Trace visualizer](https://github.com/telekom/5g-trace-visualizer) `[2023-08]` - DT set of Python scripts allow you to convert pcap, pcapng or pdml 5G protocol traces (Wireshark, tcpdump, ...) into SVG sequence diagrams.
- [sigshark](https://github.com/2b-as/sigshark) `[2026-01]` - Sigshark makes working with SS7 TCAP (MAP/CAP) and Diameter signaling pcap files easier. Its features include "flattening" (putting each SCTP chunk in its own packet) and transaction sorting/grouping.
- ⚠️ [ipccdownloader](https://github.com/mrlnc/ipcc-downloader) `[2025-03]` - Download IPCC Carrier Profiles
- [4g-speed](https://github.com/jake-cryptic/4g-speed) `[2021-10]` - 4G Theoretical Speed Calculator | FDD & TDD Support
- [MCC_MNC](https://github.com/P1sec/MCC_MNC) `[2026-03]` - Accurate MCC/MNC data as JSON and Python dicts, providing MNO public information. From P1 Security.
- [phonenumber-normalizer](https://github.com/telekom/phonenumber-normalizer) `[2026-07]` - Phone number normalization to E.164 and national formats in Go. From Deutsche Telekom.
- [OpenAPI-Dissector](https://github.com/telekom/OpenAPI-Dissector) `[2025-10]` - Experimental Wireshark dissector generator from OpenAPI specs, useful for 5G SBI protocol analysis. From Deutsche Telekom.
- [RTPproxy](https://github.com/sippy/rtpproxy) `[2026-07]` - High-performance RTP stream proxy, works with OpenSIPS, Kamailio, and Sippy B2BUA for VoIP/VoLTE media relay.
- [RLS-wireshark-dissector](https://github.com/nextmn/RLS-wireshark-dissector) `[2026-06]` - Wireshark dissector for the Radio Link Simulation Protocol from UERANSIM. From NextMN.
- [gsmtapv3](https://gitea.osmocom.org/peremen/gsmtapv3) - GSMTAPv3 specification proposal and reference code for next-generation cellular packet capture format. Hosted on **Osmocom Gitea**.
- [osmo-gsm-shark](https://gitea.osmocom.org/nhofmeyr/osmo-gsm-shark) - Network trace tool that summarizes mobile network activity from pcap captures. Hosted on **Osmocom Gitea**.
- [the-things-stack-docker](https://github.com/xoseperez/the-things-stack-docker) `[2025-10]` - The Things Stack LoRaWAN Network Server (Open Source Edition) on a Raspberry Pi using docker
- [IoT-SAFE-APDU-library](https://github.com/Orange-OpenSource/IoT-SAFE-APDU-library) `[2021-07]` - APDU library to communicate with a GSMA IoT SAFE applet ( https://www.gsma.com/iot/iot-safe)
- [bg96](https://github.com/fasferraz/bg96) `[2023-10]` - IoT Quectel BG96 AT Command tool
- [sdn-traffic-routing](https://github.com/niloysh/sdn-traffic-routing) `[2018-12]` - Sway: Traffic-Aware QoS Routing in Software-Defined IoT
- [Orange-ExpLoRer-Kit-for-LoRa](https://github.com/Orange-OpenSource/Orange-ExpLoRer-Kit-for-LoRa) `[2020-06]` - The LoRa® Explorer Kit is a development board powered by Microchip that allows easy and quick prototyping of IoT obje...
- [rainy](https://github.com/s5uishida/rainy) `[2023-09]` - rainy - a tiny tool for iot data collection and monitoring
- [xr-telemetry-m2m-web](https://github.com/cisco/xr-telemetry-m2m-web) `[2016-07]` - A small web app to explore the IOS-XR internal data model, for streaming telemetry or other automation uses
- [lorawan-app-connect](https://github.com/MultiTechSystems/lorawan-app-connect) `[2025-08]` - Default application example mPower application and server API implementation for a distributed LoRaWAN network
- [lorawan-stack-migrate](https://github.com/TheThingsNetwork/lorawan-stack-migrate) `[2026-07]` - Migrate devices from other LoRaWAN Network Servers to The Things Stack
- [sonair-dataset](https://github.com/wineslab/sonair-dataset) `[2025-12]` - Dataset for the paper D. Uvaydov, D. Unal, K. Enhos, E. Demirors and T. Melodia, "SonAIr: Real-Time Deep Learning For...
- [iotContinuum](https://github.com/Orange-OpenSource/iotContinuum) `[2025-07]` - Development kit is provided by IoT Continuum to developers who are willing to start from scratch cellular IoT project...
- [xr-telemetry-m2m-lib](https://github.com/cisco/xr-telemetry-m2m-lib) `[2016-02]` - Libraries for interacting with the IOS-XR M2M service.
- [utracker](https://codeberg.org/b00bl1k/utracker) - A firmware project based on the uwan library that allows you to create a LoRaWAN device Hosted on **Codeberg**.
- [TinyGSM](https://github.com/vshymanskyy/TinyGSM) `[2026-06]` - Small Arduino library for GSM/LTE/NB-IoT modules that just works.
- [SIM7000-LTE-Shield](https://github.com/botletics/SIM7000-LTE-Shield) `[2026-05]` - Botletics SIM7000 LTE CAT-M1/NB-IoT shield and library for Arduino.
- [lwcell](https://github.com/MaJerle/lwcell) `[2026-06]` - Lightweight cellular modem AT-command host library.
- [FreeRTOS-Cellular-Interface](https://github.com/FreeRTOS/FreeRTOS-Cellular-Interface) `[2026-07]` - FreeRTOS implementation of the 3GPP TS 27.007 AT cellular interface.
- [pcap2uml](https://github.com/dgudtsov/pcap2uml) `[2025-08]` - Call-flow visualizer for HTTP, SIP, Diameter, GSM MAP and CAMEL from pcap.
- [3gpp-documentation](https://github.com/emanuelfreitas/3gpp-documentation) `[2025-11]` - Organized index of 3GPP documentation.


## Infrastructure

### NFV, Openstack

- [Openstack Kolla](https://github.com/openstack/kolla) `[2026-07]` - Production ready containers and Ansible tools for deploying an Openstack cluster to run NFV functions.
- ⚠️ [SNAPS-openstack](https://github.com/cablelabs/snaps-openstack) `[2021-09]` - Openstack deployment to be used on SNAPS booted machine from Cablelabs.
- [OPNFV](https://www.opnfv.org/software/downloads) - The OPNFV project addresses a number of aspects in the development of a consistent virtualisation platform including common hardware requirements, software architecture, MANO and applications.

### Containers, Kubernetes

- [Kubernetes KubeADM](https://kubernetes.io/docs/reference/setup-tools/kubeadm/kubeadm/) - Deployment tool to create Kubernetes cluster.
- [Intel Multus CNI plugin](https://github.com/intel/multus-cni) `[2026-07]` - Multus CNI is a container network interface (CNI) plugin for Kubernetes that enables attaching multiple network interfaces to pods from Intel.
- [Intel SRVIOV/DPDK CNI plugin](https://github.com/intel/sriov-cni) `[2026-07]` - SR-IOV CNI plugin works with SR-IOV device plugin for VF allocation for a container.
- ⚠️ [Nokia Danm](https://github.com/nokia/danm/) `[2026-07]` - TelCo grade network management in a Kubernetes cluster from Nokia.
- ⚠️ [SNAPS-kubernetes](https://github.com/cablelabs/snaps-kubernetes) `[2021-12]` - Kubernetes deployment to be used on SNAPS booted machine from Cablelabs.
- [Free5GC on kubeCORD](https://github.com/sufuf3/kube5GC) `[2019-05]` - This project is for deploying Free5GC on kubeCORD.
- ⚠️ [CNCF CNF-Testbed](https://github.com/cncf/cnf-testbed) `[2026-03]` - The CNCF CNF Testbed provides reference code and test cases for running networking code on Kubernetes and OpenStack using emerging cloud native technologies in the Telecom domain.
- [towards5gs-helm](https://github.com/Orange-OpenSource/towards5gs-helm) `[2024-10]` - Helm charts for deploying free5GC and other 5G network functions on Kubernetes. From Orange.
- [free5gc-helm](https://github.com/free5gc/free5gc-helm) `[2026-06]` - Official Helm charts for deploying free5GC on Kubernetes.
- [open5gs-operator](https://github.com/Gradiant/open5gs-operator) `[2026-06]` - Kubernetes operator for deploying and managing Open5GS. From Gradiant.
- [Project Sylva](https://gitlab.com/sylva-projects/sylva) `[2026-06]` - Production-grade Telco Cloud Stack under Linux Foundation Europe. Common cloud software framework for VNF/CNF, backed by Orange, Deutsche Telekom, Vodafone, Telefonica. Hosted on **GitLab**.
- [aether-cni](https://github.com/omec-project/aether-cni) `[2026-07]` - Container image bundling the Kubernetes CNI plugins used in Aether SD-Core, tuned specifically for UPF in DPDK mode.
- [OAI Helm Chart Catalog](https://gitlab.eurecom.fr/oai/orchestration/charts) `[2026-06]` - Official Helm chart catalog for deploying OAI 5G Core and RAN network functions on Kubernetes. Hosted on **GitLab (Eurecom)**.


- ⚠️ [~~NeoNephos-Katalis~~](https://github.com/telekom/NeoNephos-Katalis) `[2025-03]` - Katalis is inspired by the word "Catalyst", symbolizing transformation, acceleration, and orchestration—key concepts in federated Telco and Kubernetes infrastructure.
- [loxilb](https://github.com/loxilb-io/loxilb) `[2026-07]` - eBPF-based cloud-native load-balancer for Kubernetes, edge and telco (5G service mesh, SCTP/GTP aware).
- [cloud-native-telco](https://github.com/swisscom/cloud-native-telco) `[2026-04]` - Swisscom's documentation of their cloud-native telco transformation with Kubernetes and automation, including conference talks and reference material.
### Baremetal management

- ⚠️ [SNAPS-boot](https://github.com/cablelabs/snaps-boot) `[2019-09]` - Baremetal cluster management solution to prepare for a Openstack or k8s deployment from Cablelabs.
- [MAAS](https://maas.io) - Self-service, remote installation of Windows, CentOS, ESXi and Ubuntu on real servers turns your data center into a bare-metal cloud - Metal As A Service.

## Orchestration

- [5g-sharp-orchestrator](https://github.com/Ethon-Shield/5g-sharp-orchestrator) `[2025-04]` - tool that serves as a comprehensive wrapper for configuring, deploying and monitoring 5G open-source network components, simplifying the orchestration process.
- [ETSI Open Source MANO (OSM)](https://osm.etsi.org/) - ETSI-hosted NFV Management and Orchestration (MANO) stack for multi-cloud Telco orchestration, with network slicing support (eMBB, URLLC, mMTC).
- [Open Baton](https://openbaton.github.io/) - ETSI NFV MANO compliant framework with TOSCA support and network slicing via SDN.
- [Nephio](https://github.com/nephio-project/nephio) `[2026-04]` - Kubernetes-based automation platform for deploying and managing 5G Network Functions and underlying infrastructure. Linux Foundation project.
- [TeraFlowSDN](https://labs.etsi.org/rep/tfs/controller) - Cloud-native SDN orchestrator and controller for transport networks from ETSI. IP-optical convergence, telemetry, closed-loop automation. Hosted on **ETSI Labs**.
- [OpenCAPIF](https://labs.etsi.org/rep/ocf/capif) - Open source 3GPP Common API Framework (CAPIF) for managing API exposure/consumption in 5G networks. Hosted on **ETSI Labs**.
- [OpenSlice](https://osl.etsi.org/) - Open source OSS for delivering Network Slice as a Service (NSaaS). Implements ETSI ZSM and TMF OpenAPIs. Hosted on **ETSI Labs**.
- [OpenOP](https://oop.etsi.org/) - Open-source Operator Platform for Telco Cloud network federation and 6G experimentation. Exposes CAMARA APIs. Hosted on **ETSI Labs**. Reference components: [Federation Manager](https://labs.etsi.org/rep/oop/code/federation-manager), [Service Resource Manager](https://labs.etsi.org/rep/oop/code/service-resource-manager), [Open Exposure Gateway](https://labs.etsi.org/rep/oop/code/open-exposure-gateway).
- [TeraFlowSDN NSC](https://labs.etsi.org/rep/tfs/nsc) - Network Slice Controller architecture and implementation that complements TeraFlowSDN, providing 3GPP/IETF-aligned slice lifecycle management across transport segments. Hosted on **ETSI Labs**.
- [OpenCAPIF SDK](https://labs.etsi.org/rep/ocf/sdk) - Python/Go SDK for OpenCAPIF (originally produced inside the EU 6G-SANDBOX project) for API providers and invokers. Hosted on **ETSI Labs**.
- [Nephoran Intent Operator](https://github.com/thc1006/nephoran-intent-operator) `[2026-03]` - LLM-enhanced Nephio R5 + O-RAN automation system that turns natural-language intents into KRM packages for telecom NF orchestration.
- [OpenOP Open Exposure Gateway](https://labs.etsi.org/rep/oop/code/open-exposure-gateway) - OpenOP component implementing the CAMARA Edge Cloud management API. Hosted on **ETSI Labs**.

## Lab & Testbeds

### Ready-to-Use Environments

- ⚠️ [Open5GS-VoLTE](https://github.com/miaoski/docker_open5gs) `[2021-05]` - Install-and-run lab for Open5GS + Kamailio IMS VoLTE study. _Consider using [herlesupreeth/docker_open5gs](https://github.com/herlesupreeth/docker_open5gs) instead._
- [Open5GS Docker](https://github.com/herlesupreeth/docker_open5gs) `[2026-06]` - Docker files to build and run open5gs in a docker by Herle Supreeth.
- [rapid5gs](https://github.com/joshualambert/rapid5gs) `[2026-07]` - Configuration, setup, and maintenance toolkit for Open5GS.
- [Open5gs-K8s-VyOS](https://dev.to/infinitydon/virtual-4g-simulation-using-kubernetes-and-gns3-3b7k) - This tutorial is about how to deploy a virtual 4G stack using GNS3 and Kubernetes.
- [mobile-env](https://github.com/stefanbschneider/mobile-env) `[2026-01]` - An open, minimalist Gym environment for autonomous coordination in wireless mobile networks.
- [OpenAICellular](https://openaicellular.github.io/oaic/quickstart.html) - OAIC is an open-source effort led by a consortium of academic institutions to provide fully open-source software architecture, library, and toolset that encompass both the AI controllers (OAIC-C) as well as an AI testing framework (OAIC-T).
- [sample configs](https://github.com/s5uishida/sample_config_misc_for_mobile_network) `[2026-02]` - Sample Configurations and Miscellaneous for Mobile Network.
- [free5gc-compose](https://github.com/free5gc/free5gc-compose) `[2026-06]` - Docker Compose files for deploying the full free5GC 5G core stack.
- [free5GLabs](https://github.com/free5gc/free5GLabs) `[2026-04]` - Hands-on labs to guide building 5G networks with free5GC.
- [ETSI MEC Sandbox](https://labs.etsi.org/rep/mec/etsi-mec-sandbox) - Interactive environment for learning and experimenting with ETSI MEC service APIs. Hosted on **ETSI Labs**.
- [open5gs-k8s](https://github.com/niloysh/open5gs-k8s) `[2026-03]` - Open5GS 5G Core on Kubernetes with Helm charts and deployment guides.
- [docker-open5gs (Borjis131)](https://github.com/Borjis131/docker-open5gs) `[2025-11]` - Open5GS 5G Core container images with Docker Compose deployments and Helm charts for Kubernetes.
- [oai-cn5g-fed](https://gitlab.eurecom.fr/oai/cn5g/oai-cn5g-fed) `[2026-07]` - Federation of OAI CN 5G repositories. Docker Compose deployment for the full OAI 5G core. Hosted on **GitLab (Eurecom)**.
- [NextMN testbed](https://github.com/nextmn/testbed) `[2026-07]` - Ready-to-use testbed for the NextMN project with SRv6, UPF, and 5G simulators.
- [free5gc-k8s](https://github.com/niloysh/free5gc-k8s) `[2024-05]` - free5GC 5G Core on Kubernetes with Helm charts and deployment guides.
- [testbed-automator](https://github.com/niloysh/testbed-automator) `[2025-10]` - Scripts for automating deployment of 5G testbeds with Open5GS, free5GC, and UERANSIM.
- [aether-onramp](https://github.com/opennetworkinglab/aether-onramp) `[2026-07]` - Ansible-driven installer for deploying the Aether 5G stack (SD-Core, RAN, monitoring) on bare metal. Official Aether quick-start path.
- [5G-Monarch](https://github.com/niloysh/5g-monarch) `[2026-01]` - Companion repo for the 5G-MoNArch paper on monitoring/observability of cloud-native 5G deployments on Kubernetes.
- [T-5GS](https://github.com/T-5GS/T-5GS) `[2025-12]` - Near-realistic open-source 5G testbed for multi-core network interoperability and multi-tenant scenarios, built on PacketRusher and Open5GS.
- [free5gc/IPTV](https://github.com/free5gc/IPTV) `[2023-01]` - Sample 5G application demonstrating IPTV-style multicast/streaming traffic over a free5GC deployment.
- [OAI Raytracing Channel Emulator](https://gitlab.eurecom.fr/oai/raytracing-channel-emulator) `[2026-07]` - Ray-tracing-based wireless channel emulator integrated with OpenAirInterface for realistic 5G NR PHY testing. Hosted on **GitLab (Eurecom)**.
- [Open5GS-srsRAN deployment guide](https://github.com/ngkore/Open5GS-srsRAN) `[2026-03]` - End-to-end deployment guide for Open5GS 5G Core with srsRAN and srsUE. From NGKore.
- [frush](https://github.com/free-ran-ue/frush) `[2026-07]` - Bash-like interactive shell for operating free-ran-ue and validating 5G core (free5GC) behavior. Companion: [fru-helm](https://github.com/free-ran-ue/fru-helm), [fru-compose](https://github.com/free-ran-ue/fru-compose).
- [install_eupf](https://github.com/s5uishida/install_eupf) `[2026-02]` - Step-by-step host install for eUPF (eBPF/XDP UPF) for 5GC labs.
- [install_oai_upf](https://github.com/s5uishida/install_oai_upf) `[2026-06]` - Step-by-step host install for OAI-CN5G-UPF (eBPF/XDP) for 5GC labs.
- [install_goupf](https://github.com/s5uishida/install_goupf) `[2026-03]` - Step-by-step host install for free5GC's go-upf user-plane.
- [install_vpp_upf_dpdk](https://github.com/s5uishida/install_vpp_upf_dpdk) `[2026-03]` - Step-by-step host install for UPG-VPP (DPDK/VPP UPF). Companion guide series with the eUPF/OAI-UPF/goupf installers.
- [build_srsran_5g_zmq](https://github.com/s5uishida/build_srsran_5g_zmq) `[2026-05]` - Build srsRAN_Project (5G) with ZeroMQ for end-to-end RFsim labs against Open5GS / free5GC.
- [open5Gcube](https://github.com/open5Gcube/open5Gcube) `[2026-07]` - Modular framework for building mobile network laboratories.
- [OAI-UERANSIM](https://github.com/AIDY-F2N/OAI-UERANSIM) `[2025-11]` - Deploy the OAI 5G core plus UERANSIM gNB and UEs on a Kubernetes cluster.
- [ocudu-gpu-channel](https://github.com/zhouyou-gu/ocudu-gpu-channel) `[2026-06]` - GPU-accelerated, ZMQ-native channel emulator that drops between srsRAN/OCUDU radios and applies CUDA channel models within the 5G NR slot deadline.
- [StormSIM](https://github.com/lvdund/StormSIM) `[2026-07]` - Large scalable 5G UE/gNB emulator.
- [virtuallte](https://github.com/GaetanF/virtuallte) `[2026-06]` - Userspace virtual 5G/LTE UE (User Equipment).
- [open5G2GO](https://github.com/Waveriders-Collective/open5G2GO) `[2026-03]` - Homelab toolkit for private 5G SA and 4G LTE networks, built on Open5GS.
- [5g-charts](https://github.com/Gradiant/5g-charts) `[2026-01]` - Helm charts for deploying 5G technologies. From Gradiant.
- [containerlab-cellular](https://github.com/giros-dit/containerlab-cellular) `[2026-04]` - Containerlab scenarios for spinning up cellular mobile network topologies.

### Remote control

- [OpenSTF](https://openstf.io) - Enable remote control of phone over ADB over an HTML5 interfaces.
- [Vyzor](http://vysor.io) - A window to your Android, streaming Android UI through ADB in a Google Chrome Browser app.

### GPS, Time

- ⚠️ [GPS-SDR-SIM](https://github.com/osqzss/gps-sdr-sim) `[2025-01]` - GPS signal generator with a SDR radio and ephemeris files.
- [Tools for MT3339](https://github.com/f5eng/mt3339-utils) `[2023-01]` - Ephemeris injector for MT3339-based GPS chipset

## Testing

- [SIPp](https://github.com/SIPp/sipp) `[2026-07]` - SIP protocol test tool and traffic generator. Industry-standard for SIP load testing and conformance.
- [voip_perf](https://github.com/jchavanton/voip_perf) `[2026-03]` - SIP performance testing tool for VoIP infrastructure benchmarking.
- [gossipper](https://github.com/sipcapture/gossipper) `[2026-07]` - Go reimplementation of SIPp for modern SIP load testing.
- [ntt](https://github.com/nokia/ntt) `[2026-07]` - TTCN-3 test framework.
- [Eclipse Titan TTCN3](https://projects.eclipse.org/projects/tools.titan) - Eclipse Titan is a TTCN-3 compilation and execution environment with an  Eclipse-based IDE.
- [TTCN3vscode](https://github.com/nokia/vscode-ttcn3) `[2026-07]` - TTCN-3 vs code plugin
- [ixia-c](https://github.com/open-traffic-generator/ixia-c) `[2026-07]` - Ixia-c is a modern, powerful and API-driven traffic generator designed to cater to the needs of hyperscalers, network hardware vendors and hobbyists alike.
- ⚠️ [srsRAN_matlab](https://github.com/srsran/srsRAN_matlab) `[2026-03]` - MATLAB-based PHY-layer testing and verification tools for srsRAN. From SRS.
- [Telcometer](https://github.com/itsMohammadHeidari/Telcometer) `[2024-10]` - Diameter Credit-Control Application Load Testing script powered by [Grafana K6](https://github.com/grafana/k6)
- [Sionna](https://github.com/NVlabs/sionna) `[2026-07]` - GPU-accelerated open-source library from NVIDIA for link-level simulation of communication systems. Covers OFDM, MIMO, LDPC, Polar codes, and ray tracing for 5G/6G research.
- [Simu5G](https://simu5g.org/) - OMNeT++ based 5G network simulator for end-to-end performance evaluation.
- [ns-3 LTE/NR](https://gitlab.com/nsnam/ns-3-dev) `[2026-07]` - Discrete-event network simulator with LTE and 5G NR modules. Main development on **GitLab**.
- [5G-LENA](https://gitlab.com/cttc-lena/nr) `[2026-07]` - ns-3 NR module for 5G New Radio simulation (PHY/MAC/OFDMA, MIMO, NR-U, NR V2X). From CTTC OpenSim. [NR-U extension](https://gitlab.com/cttc-lena/nr-u). Hosted on **GitLab**.
- [Wireshark](https://gitlab.com/wireshark/wireshark) `[2026-07]` - Essential protocol analyzer with dissectors for GSMTAP, Diameter, GTP, S1AP, NGAP, SS7/TCAP and more. Main development on **GitLab**.
- [Seagull](https://gull.sourceforge.net/) - Multi-protocol traffic generator for IMS testing: Diameter (RFC3588) over TCP/SCTP, TCAP (over SS7/Sigtran), XCAP, Radius. From HP. [SourceForge](https://sourceforge.net/projects/gull/).
- [ETSI Forge Test Suites](https://forge.etsi.org/rep/explore/projects) - Official ETSI test suites in TTCN-3 and Robot Framework for telecom protocols (Diameter, GTP, S1AP, NAS, MEC, NFV). Hosted on **ETSI Forge (GitLab)**.
- [ETSI 5G Core NAS Test Suite](https://forge.etsi.org/rep/int/5g-core/nas) - Official ETSI INT test suite for 5G NAS conformance testing. Hosted on **ETSI Forge**.
- [ETSI 5G Core NGAP Test Suite](https://forge.etsi.org/rep/int/5g-core/ngap) - Official ETSI INT test suite for NGAP conformance testing on the N2 interface. Hosted on **ETSI Forge**.
- [Nokia Moler](https://github.com/nokia/moler) `[2026-07]` - Python library for building automated tests of network equipment. From Nokia.
- [twampy](https://github.com/nokia/twampy) `[2026-03]` - Python tools for TWAMP and STAMP (Two-Way Active Measurement Protocol) network performance measurement. From Nokia.
- [5g-traffic-generator](https://github.com/niloysh/5g-traffic-generator) `[2025-09]` - Tool for sending GTP-U packets with configurable TEID and QFI values. Useful for exercising UPFs and 5G data-plane setups.
- [CoreNetworkTrafficGenerator](https://github.com/tariromukute/CoreNetworkTrafficGenerator) `[2026-04]` - 5G Core traffic generator emulating gNodeB and UEs (control + user plane), with eBPF/BCC SCTP metrics. Validated against Open5GS, free5GC, and OAI.
- [petrel](https://github.com/lwlee2608/petrel) `[2024-11]` - Diameter load generator from the diameter-rs / xk6-diameter author, focused on high-throughput Diameter benchmarking.
- [seet](https://github.com/fonoster/seet) `[2024-09]` - SIP end-to-end test orchestrator coordinating multiple SIP user-agents for complex multi-leg test scenarios. From Fonoster.
- [sipp-js](https://github.com/fonoster/sipp-js) `[2023-10]` - JavaScript wrapper around SIPp making it easy to script SIP load and conformance tests from Node.js / TypeScript.
- [ETSI INT 5GC NGAP test suite](https://forge.etsi.org/rep/int/5g-core/ngap) - TTCN-3 conformance/interoperability test suite for 3GPP NGAP (N2) from ETSI TC INT. Companion [NAS test suite](https://forge.etsi.org/rep/int/5g-core/nas) and [Emergency Services over 5G IOP](https://forge.etsi.org/rep/int/vx5g/emergency-5g-iop). Hosted on **ETSI Forge (GitLab)**.
- [C-V2X Interoperability Testing Tool](https://github.com/usnistgov/C-V2XInteroperabilityTestingTool) `[2026-03]` - Automated Cellular Vehicle-to-Everything (C-V2X) interoperability testing tool. From NIST.
- [5GNRad](https://github.com/usnistgov/5GNRad) `[2026-02]` - 5G NR Integrated Sensing And Communication (ISAC) link-level simulator in MATLAB. From NIST.
- [das-schiff-network-operator](https://github.com/telekom/das-schiff-network-operator) `[2026-07]` - Kubernetes-operator to declaratively manage EVPN-to-the-Host deployments using custom resources.
- [snmp-collector](https://github.com/sigscale/snmp-collector) `[2023-10]` - SNMP Manager for 3GPP Alarm IRP
- [5GC-Bench](https://github.com/panitsasi/5GC-Bench) `[2025-12]` - Modular benchmarking framework to stress-test 5G core control- and user-plane VNFs under synthetic and realistic workloads.
- [UE-based 5G Pentesting Framework](https://github.com/Barkhausen-Institut/UE-based-5G-Pentesting-Framework) `[2025-09]` - Functional and security testing of 5G networks from the UE perspective. From the Barkhausen Institut.
- [5G-Gibbon](https://github.com/Suffix30/5G-Gibbon) `[2025-12]` - 5G/4G LTE core network security testing toolkit with red- and blue-team capabilities.
- [MNSF](https://github.com/noz-co-id/MNSF) `[2026-04]` - Mobile Network Security Framework: SDR-based security testing across 2G-5G using OpenBTS, Osmocom, Open5GS and srsRAN.
- [SF5G](https://github.com/sfn-tools/sf5g) `[2025-12]` - Baseband security research toolkit ("Something From 5G").
- [edaf](https://github.com/samiemostafavi/edaf) `[2026-04]` - End-to-end delay analytics framework for 5G-and-beyond networks.
- Additional travelping sub-projects: [docker-pcap](https://github.com/travelping/docker-pcap), [ergw-gtp-c-node](https://github.com/travelping/ergw-gtp-c-node)

## AI & Machine Learning

AI and machine learning tools for telecom networks, covering foundation models, physical layer optimization, network management, and security.

### Telecom LLMs & AI Assistants

- [Eclipse LMOS](https://github.com/eclipse-lmos) `[2026-04]` - Open-source multi-agent AI platform deployed by Deutsche Telekom for Frag Magenta customer service. Eclipse Foundation project.
- [Tele-LLMs](https://github.com/Ali-maatouk/Tele-LLMs) `[2025-04]` - Series of open-source LLMs (1B-8B params) specialized in telecom. Trained on 2.5B tokens from arXiv, 3GPP, Wikipedia. From Yale.
- [Telco-RAG](https://github.com/netop-team/Telco-RAG) `[2024-09]` - RAG framework specialized for 3GPP documents. Addresses challenges of retrieval-augmented generation on highly technical telecom standards.
- [3GPP Expert Skill](https://github.com/lugasia/3gpp-skill) `[2026-04]` - Claude Code skill providing deep 3GPP expertise across all generations (2G–6G), protocol stacks, core network, security, and deployment planning.
- [3GPP MCP Server](https://github.com/edhijlu/3gpp-mcp-server) `[2025-09]` - MCP server enabling AI assistants (Claude, VSCode) to search 3GPP specifications via the TSpec-LLM dataset.
- [TeleQnA](https://github.com/netop-team/TeleQnA) `[2024-01]` - Benchmark dataset (10K multiple-choice questions) for evaluating LLM telecom knowledge. Part of GSMA Open-Telco LLM Benchmarks.
- [Telco-AIX](https://github.com/open-experiments/Telco-AIX) `[2026-04]` - Applied AI experiments for telecom: self-healing networks (AutoNet), MCP-based diagnostic agents, GenAI for NOC.
- [teddi-mcp](https://forge.3gpp.org/rep/reimes/teddi-mcp) - MCP server for ETSI's TEDDI (Terms and Definitions Database Interactive). Search 3GPP/ETSI terms programmatically from AI assistants. Hosted on **3GPP Forge**.
- [MobiLLM](https://github.com/5GSEC/MobiLLM) `[2025-09]` - Domain-specific LLM for cellular security from the 5GSEC group. Trained for analyzing and reasoning about 5G/cellular security incidents and threats.
- [The AI Telco Engineer](https://github.com/NVlabs/the-ai-telco-engineer) `[2026-04]` - NVIDIA Research repo prototyping LLM/agent workflows for telecom engineering tasks (network design, troubleshooting). Companion to NVIDIA's wider AI-RAN push.
- [Chat3GPP](https://github.com/huangl22/Chat3GPP) `[2025-01]` - Open-source RAG framework purpose-built for 3GPP documents, combining hybrid retrieval (BM25 + HNSW + RRF) and BGE-M3 reranking without fine-tuning.
- [telco-network-configuration](https://github.com/bubbleran/telco-network-configuration) `[2025-06]` - Agentic AI workflow blueprint that recommends close-to-optimal RAN parameter configurations at a cell site. Showcases LLM-driven RAN parameter tuning.
- [OpenSlice MCP Server](https://labs.etsi.org/rep/osl/code/org.etsi.osl.mcp.server) - Model Context Protocol server exposing OpenSlice (network-slice / TMF Open API) operations to LLM agents. Hosted on **ETSI Labs**.
- [agentran](https://github.com/wineslab/agentran) `[2026-05]` - Multi-agent framework for AI-RAN control. From WINES Lab.
- [llm-shark](https://github.com/kinghighland/llm-shark-release) `[2026-07]` - LLM-powered flowshark for 4G/5G/IMS signaling diagnosis.
- [talk-to-pcap](https://github.com/Sagar-Mashal/talk-to-pcap) `[2025-11]` - AI-powered natural-language interface for 3GPP LTE/5G pcap analysis.
- [claude-phone](https://github.com/theNetworkChuck/claude-phone) `[2026-01]` - Voice interface for Claude Code over SIP/3CX.
- [exten_bot](https://github.com/estvita/exten_bot) `[2025-09]` - Speech-to-speech OpenAI Realtime VoIP bot as a SIP extension.

See also: [specpilot](#learning-resources) (AI-powered 3GPP spec assistant), [3gpp-crawler](#learning-resources) (3GPP FTP crawler), [GSMA Open-Telco LLM Benchmarks](https://huggingface.co/GSMA) (TeleYAML, TeleLogs, TeleMATH on HuggingFace).

### AI for Physical Layer & RF

- [DeepMIMO](https://github.com/DeepMIMO/DeepMIMO) `[2026-06]` - Ray-tracing dataset toolchain for mmWave and massive MIMO ML research. Python and MATLAB. Also: [DeepMIMO-5GNR](https://github.com/DeepMIMO/DeepMIMO-5GNR).
- [OpenDPD](https://github.com/lab-emi/OpenDPD) `[2026-07]` - PyTorch end-to-end learning framework for power amplifier modeling and digital pre-distortion. pip-installable.
- [HBF-Net](https://github.com/HamedHojatian/HBF-Net) `[2023-07]` - Unsupervised deep learning for massive MIMO hybrid beamforming.
- [deep-learning-channel-estimation](https://github.com/emilbjornson/deep-learning-channel-estimation) `[2021-02]` - Deep learning channel estimation in massive MIMO under hardware non-linearities. IEEE OJCOMS. From Bjornson.
- [TorchSig](https://github.com/TorchDSP/torchsig) `[2026-06]` - PyTorch signal processing ML toolkit. 60+ signal types, pretrained models, modulation families (FSK, QAM, PSK, OFDM).
- [RFML](https://github.com/brysef/rfml) `[2024-09]` - Radio Frequency Machine Learning with PyTorch. Automatic modulation classification, DeepSig dataset loaders, adversarial training.
- [on-device-ai-comm](https://github.com/abman23/on-device-ai-comm) `[2024-05]` - On-device AI/LLM communication system integrating a pre-trained LLM with 5G-NR PHY over 3GPP CDL channels.
- [Instant Radio Maps](https://github.com/NVlabs/instant-rm) `[2024-07]` - Fast and differentiable radio map generation using neural radiance field techniques. From NVIDIA Research.
- [diff-rt](https://github.com/NVlabs/diff-rt) `[2024-05]` - Sionna RT differentiable ray tracing research code for learning wireless propagation. From NVIDIA.
- [Sionna RT](https://github.com/NVlabs/sionna-rt) `[2026-06]` - Standalone differentiable ray tracing package extracted from NVIDIA Sionna for ML wireless propagation research.
- [Sionna Large Radio Maps](https://github.com/NVlabs/sionna-large-radio-maps) `[2026-02]` - Large-scale wireless coverage map simulation built on Sionna RT, producing city-scale radio maps for ML training and planning research.
- [SALAD](https://github.com/NVlabs/salad) `[2025-10]` - Self-Adaptive Link Adaptation for wireless communications. ML-based MCS/link adaptation research code from NVIDIA.
- [LibIQ](https://github.com/wineslab/lib-iq) `[2026-03]` - Modular Python library for analyzing, visualizing, and classifying I/Q time-series in wireless systems. From WiNES Lab.
- [DeepBeam](https://github.com/wineslab/deepbeam) `[2025-12]` - Deep waveform learning for coordination-free beam management in mmWave networks (ACM MobiHoc 2021 code). From WiNES Lab.
- [open-cloud-semantic-ran](https://github.com/6G-Cloud-RnE-Open-Hub/open-cloud-semantic-ran) `[2025-09]` - Software implementations of semantic PHY-RAN systems (cloud-native semantic communications RAN). Early 6G research code.
- [Sionna PlutoSDR](https://github.com/rikluost/sionna-PlutoSDR) `[2025-09]` - Adalm PlutoSDR interface for NVIDIA Sionna with full-duplex 1T1R operation on a single SDR. Bridges Sionna research with commodity SDR hardware.
- [OpenGERT](https://github.com/serhatadik/OpenGERT) `[2025-09]` - Open-source Geometry Extraction tool for Sionna Ray-Tracing including ray-tracing sensitivity analysis. Useful for building 3D scenes for Sionna RT.
- [CASTRO-5G](https://codeberg.org/gomezcuba/CASTRO-5G) `[2026-04]` - Python toolkit (Univ. Vigo) for sparse multipath 5G channel simulation, compressed-sensing channel estimation, mmWave link adaptation and ISAC location signal processing. GPLv3. Hosted on **Codeberg**.

### O-RAN AI/ML

- [O-RAN SC AIMLFW](https://docs.o-ran-sc.org/projects/o-ran-sc-aiml-fw-aiml-dashboard/en/latest/) - Modular ML pipeline for O-RAN: feature extraction, model training, storage and serving via Kubeflow/KServe. Hosted on **O-RAN SC Gerrit**.
- [O-RAN SC RIC ML xApps](https://wiki.o-ran-sc.org/display/RICAPP) - Suite of ML-based Near-RT RIC xApps: Anomaly Detection (UE classification), QoE Prediction (throughput forecasting), Traffic Steering (ML-informed handover). Hosted on **O-RAN SC Gerrit**.
- [5G-Spector](https://github.com/5GSEC/5G-Spector) `[2024-11]` - O-RAN compliant runtime intrusion detection xApp for L3 (RRC/NAS) cellular attack detection.
- [MobiWatch](https://github.com/5GSEC/MobiWatch) `[2025-08]` - O-RAN xApp using unsupervised deep learning to detect L3 cellular anomalies and attacks.
- [MobiFlow-Auditor](https://github.com/5GSEC/MobiFlow-Auditor) `[2026-07]` - O-RAN compliant xApp providing fine-grained, security-aware statistics monitoring over 5G RAN and UEs. Telemetry source for the MobiWatch detection xApp.
- [MobieXpert](https://github.com/5GSEC/MobieXpert) `[2025-07]` - First signature-based L3 cellular attack-detection xApp for O-RAN, complementing the deep-learning MobiWatch.
- [oai-anomaly-detection](https://github.com/teo-tsou/oai-anomaly-detection) `[2025-05]` - AI/ML framework for 5G anomaly detection plus closed-loop RB allocation and UE connectivity management on OpenAirInterface and FlexRIC.
- [MalO-RAN](https://github.com/wineslab/mal-o-ran) `[2026-03]` - Framework for evaluating data poisoning attacks on O-RAN AI-based xApps. From WiNES Lab.
- [ns-O-RAN-Gym](https://github.com/wineslab/ns-o-ran-gym) `[2025-04]` - Gymnasium-based RL environment for O-RAN with Traffic Steering and Energy Saving scenarios. From WiNES Lab.

### Network Optimization & Slicing

- [DeepCoMP](https://github.com/CN-UPB/DeepCoMP) `[2023-07]` - Dynamic multi-cell selection for cooperative multipoint (CoMP) using multi-agent deep RL.
- [Network Slicing Gym](https://github.com/jjalcaraz-upct/network-slicing) `[2024-11]` - OpenAI Gym environment for network slicing with model-based RL agent. Compatible with Stable-Baselines.
- [DeepNetSlice](https://github.com/AlexPasqua/DeepNetSlice) `[2024-05]` - RL tool for network slice placement (VNF placement). PyTorch + Stable-Baselines3. IEEE ICMLCN 2024.
- [DRL-GNN](https://github.com/knowledgedefinednetworking/DRL-GNN) `[2023-05]` - Combined DRL + GNN architecture for network routing optimization. Generalizes over arbitrary topologies.
- [RouteNet](https://github.com/knowledgedefinednetworking/demo-routenet) `[2023-03]` - GNN architecture for network performance modeling (delay, jitter, loss prediction). ACM SIGCOMM'19. See also [RouteNet-Fermi](https://github.com/BNN-UPC/RouteNet-Fermi).

### Simulation & RL Environments

- [ns3-gym](https://github.com/tkn-tub/ns3-gym) `[2026-02]` - OpenAI Gym integration with ns-3 for RL in networking research.
- [ns3-ai](https://github.com/hust-diangroup/ns3-ai) `[2026-07]` - Python-C++ bridge enabling AI frameworks (TensorFlow, PyTorch) to interact with ns-3 simulations.
- [RFRL Gym](https://github.com/vtnsi/rfrl-gym) `[2025-02]` - RL training environment for wireless communications: dynamic spectrum access, jamming scenarios.
- [ns3sionna](https://github.com/tkn-tub/ns3sionna) `[2025-12]` - ns-3 module bringing realistic Sionna ray-tracing channel simulation to ns-3.
- [ns-O-RAN-ns3-mmwave](https://github.com/wineslab/ns-o-ran-ns3-mmwave) `[2025-03]` - ns-O-RAN integration with the ns-3 mmWave module providing O-RAN E2 simulation on top of mmWave 5G/NR scenarios. From WiNES Lab.
- [ns3-iboran](https://github.com/Orange-OpenSource/ns3-iboran) `[2026-07]` - ns-3-based Open RAN simulation environment with native support for intent-based orchestration. From Orange.

### Datasets & Benchmarks

- [5GMdata](https://github.com/lasseufpa/5gm-data) `[2022-05]` - Datasets and code for ML in 5G mmWave MIMO systems involving mobility.
- [ColO-RAN Dataset](https://github.com/wineslab/colosseum-oran-coloran-dataset) `[2024-09]` - Open dataset for ML-based xApps in O-RAN closed-loop control. DRL-based RAN slicing/scheduling. From WiNES Lab / IEEE TMC.
- [NetworkModelingDatasets](https://github.com/BNN-UPC/NetworkModelingDatasets) `[2025-10]` - Datasets for network modeling simulated with OMNet++. Companion to the RouteNet family.
- [TelecomTS](https://github.com/Ali-maatouk/TelecomTS) `[2026-05]` - Multi-modal telecom dataset from the Tele-LLMs team.
- [MM-TelcoBench](https://github.com/gagan-iitb/MM-TelcoBench) `[2025-11]` - Multimodal telecom benchmark for LLM evaluation: network operations, troubleshooting, PCAP analysis, 5G faults.
- [RANalyzer Dataset](https://github.com/wineslab/RANalyzer-Dataset) `[2026-04]` - End-to-end 5G performance measurement dataset useful for training and evaluating performance-prediction models. From WiNES Lab.
- [BostonTwin](https://github.com/wineslab/boston_twin) `[2025-07]` - Digital-twin dataset and API of Boston for ray-tracing-based wireless coverage and network simulation research. From WiNES Lab.
- [TeleTwin](https://github.com/ngkore/TeleTwin) `[2026-02]` - Digital twin of telecom towers. Web-based 3D visualization platform for telecom infrastructure modelling. From NGKore.
- [Colosseum O-RAN ComMag Dataset](https://github.com/wineslab/colosseum-oran-commag-dataset) `[2024-12]` - Dataset for the IEEE ComMag paper "Intelligence and Learning in O-RAN for Data-driven NextG Cellular Networks" from WiNES Lab.
- [5GDatasets](https://github.com/DLTeamTUC/5GDatasets) `[2025-07]` - Public 5G security datasets (PCAPs, CSVs, AMF logs) covering flooding, fuzzing and replay attacks against control- and user-plane. Generated on Open5GS, OAI, and Amarisoft cores.
- [deepsense-spectrum-sensing-datasets](https://github.com/wineslab/deepsense-spectrum-sensing-datasets) `[2025-12]` - Dataset for the paper D. Uvaydov, S. D’Oro, F. Restuccia and T. Melodia, "DeepSense: Fast Wideband Spectrum Sensing T...
- [Infernos](https://github.com/sippy/Infernos) `[2025-10]` - Real-time multi-modal inference server for interacting with humans and other intelligences around

---

## Security

### Security Exploitation/fuzzing Frameworks

- ⚠️ [SigPloit](https://github.com/SigPloiter/SigPloit) `[2019-12]` - Telecom Signaling Exploitation Framework - SS7, GTP, Diameter & SIP.
- [5GC_API_parse](https://github.com/PentHertz/5GC_API_parse) `[2021-07]` - 5GC API parse is a BurpSuite extension allowing to assess 5G core network functions, by parsing the OpenAPI 3.0 not supported by previous OpenAPI extension in Burp, and generating requests for intrusion tests purposes.
- [FirmWire](https://github.com/FirmWire/FirmWire) `[2026-07]` - FirmWire is a full-system baseband firmware emulation platform for fuzzing, debugging, and root-cause analysis of smartphone baseband firmwares.
- [5Ghoul](https://github.com/asset-group/5ghoul-5g-nr-attacks) `[2026-03]` - 5G NR attack and fuzzing framework targeting Qualcomm and MediaTek 5G baseband implementations.
- [hexagon_fuzz](https://github.com/srlabs/hexagon_fuzz) `[2025-10]` - A fuzzing framework for Qualcomm Hexagon baseband firmware using QEMU system emulation, from SRLabs.
- [SIPVicious](https://github.com/EnableSecurity/sipvicious) `[2026-07]` - SIP/VoIP security testing toolset for auditing SIP-based VoIP systems.
- [SIMurai](https://github.com/tomasz-lisowski/simurai) `[2024-08]` - SIM card fuzzer and security research tool (USENIX Security 2024). From the author of swSIM/swICC.
- [SentryPeer](https://github.com/SentryPeer/SentryPeer) `[2026-07]` - SIP honeypot for detecting and preventing VoIP fraud with peer-to-peer threat intelligence sharing. Also on [Codeberg](https://codeberg.org/SentryPeer/SentryPeer).
- [sip-honeypot](https://github.com/0xNslabs/sip-honeypot) `[2025-12]` - Low-interaction SIP honeypot in Python for monitoring VoIP scanning traffic.
- [Sni5Gect](https://github.com/asset-group/Sni5Gect-5GNR-sniffing-and-exploitation) `[2026-06]` - 5G NR sniffer and downlink injector framework with Wireshark support. From the 5Ghoul team.
- [LLFuzz](https://github.com/SysSec-KAIST/LLFuzz) `[2026-03]` - Over-the-air dynamic testing framework for cellular baseband lower layers (PDCP, RLC, MAC, PHY). Found 11 unknown memory corruptions. USENIX Security 2025. From KAIST.
- [CITesting](https://github.com/SysSec-KAIST/CITesting) `[2025-10]` - Systematic testing of context integrity violations in LTE core networks. ACM CCS '25 Distinguished Paper. From KAIST.
- [BaseBridge](https://github.com/FirmWire/BaseBridge) `[2025-05]` - FirmWire extension that bridges emulation and over-the-air testing by restoring connection state from physical phone memory dumps. Up to 5x fuzzing coverage boost.
- [ShannonLoader](https://github.com/FirmWire/ShannonLoader) `[2026-07]` - Ghidra plugin for reverse engineering Samsung Shannon baseband firmware.
- [5G_ciphered_NAS_decipher_tool](https://github.com/PentHertz/5G_ciphered_NAS_decipher_tool) `[2025-11]` - Python tool to decipher 5G ciphered NAS messages and export to Wireshark pcap. From PentHertz.
- [gea-implementation](https://github.com/P1sec/gea-implementation) `[2026-03]` - GEA-1 and GEA-2 (GPRS Encryption Algorithm) stream cipher implementations in C, Python, and Rust. From P1 Security.
- [BaseSpec](https://github.com/SysSec-KAIST/BaseSpec) `[2021-03]` - Comparing cellular L3 protocol messages between 3GPP spec documents and baseband firmware implementations. From the LTESniffer team at KAIST.
- [DoLTEst](https://github.com/SysSec-KAIST/DoLTEst) `[2022-08]` - Negative testing framework for finding non-standard-compliant bugs in LTE protocol implementations of UEs. From KAIST.
- [Mirage](https://github.com/PentHertz/mirage) `[2025-04]` - Powerful and modular framework for security analysis of wireless communications (Bluetooth, Wi-Fi, Zigbee, and more). From PentHertz.
- [WatchingTheWatchers](https://github.com/SysSec-KAIST/WatchingTheWatchers) `[2024-03]` - Tools for video identification on LTE networks. From KAIST.
- [FISSURE](https://sourceforge.net/projects/fissure.mirror/) - RF and reverse engineering framework for signal intelligence, protocol analysis, and attack detection. Hosted on **SourceForge**.
- ⚠️ [Daedalus](https://github.com/IQTLabs/Daedalus) `[2024-05]` - Defensive response options for securing a 5G core network. From IQT Labs.
- [CVE-2025-36911 exploit](https://github.com/PentHertz/CVE-2025-36911-exploit) `[2026-01]` - Exploit for CVE-2025-36911 in Python for security testing. From PentHertz.
- [DIKEUE](https://github.com/SyNSec-den/DIKEUE) `[2023-06]` - Automated testing framework for LTE/5G UE protocol noncompliance. USENIX Security 2021.
- [hermes-spec-to-fsm](https://github.com/SyNSec-den/hermes-spec-to-fsm) `[2024-10]` - Extract finite state machines from 3GPP spec prose for protocol verification and fuzzing.
- [simurai-usenixsec2024-ae](https://github.com/tomasz-lisowski/simurai-usenixsec2024-ae) `[2026-05]` - Artifact evaluation code for the SIMurai SIM fuzzer USENIX Security 2024 paper.
- [pqproto](https://github.com/ngkore/pqproto) `[2025-10]` - Practical framework for experimenting with post-quantum cryptography in security protocols.
- [security-intents](https://github.com/5GSEC/security-intents) `[2024-03]` - Repository of 5G security intent templates in standard format for automated policy enforcement.
- [blue-merle](https://github.com/srlabs/blue-merle) `[2025-06]` - Enhances anonymity and reduces forensic traceability of 4G mobile Wi-Fi routers (IMEI change, MAC randomization). From SRLabs.
- [5GC_API_Pentest](https://github.com/PentHertz/5GC_API_Pentest) `[2025-12]` - Burp Suite extension for 5G Core SBI security testing with automated NF discovery, IMSI enumeration, OAuth2 workflows, and OpenAPI fuzzing. Successor to 5GC_API_parse. From PentHertz.
- [shannon_modem_loader](https://github.com/alexander-pick/shannon_modem_loader) `[2025-01]` - Samsung Exynos/Shannon baseband firmware loader for IDA Pro 8.x/9.x. Enables reverse engineering of Shannon modem firmware.
- [URH-NG](https://github.com/PentHertz/urh-ng) `[2026-07]` - Universal Radio Hacker Next Generation. Investigate wireless protocols, demodulate/decode signals, and analyze RF communications. Successor to URH. From PentHertz.
- [sigover_gen_sample](https://github.com/SysSec-KAIST/sigover_gen_sample) `[2022-05]` - Signal overshadowing sample generator for LTE broadcast signals. Companion to sigover_injector. From KAIST.
- [5GBaseChecker](https://github.com/SyNSec-den/5GBaseChecker) `[2025-01]` - Differential-testing security analysis framework for the control plane of 5G basebands. Evaluated on 17 commercial 5G basebands and 2 open-source UEs; uncovered 22 issues. USENIX Security '24.
- [py5sig](https://github.com/ANSSI-FR/py5sig) `[2025-11]` - ANSSI-published Python tool that auto-builds 5G signalling messages and fuzzes the SBI interfaces of a 5G core.
- [5Greplay](https://github.com/Montimage/5Greplay) `[2026-03]` - Tool for modifying and replaying captured 5G protocol traffic, enabling attack injection and fuzzing of 5G core/RAN deployments. From Montimage.
- [FuzzyDoo](https://github.com/gabrielepongelli/FuzzyDoo) `[2026-01]` - Mutation-based, structure-aware fuzzer purpose-built for 5G core networks (NGAP/NAS/PFCP/SBI).
- [U-Fuzz](https://github.com/asset-group/U-Fuzz) `[2025-07]` - Universal fuzzing framework for IoT/wireless protocols from the ASSET group, targeting stateful protocol stacks across radio technologies.
- [ORANClaw](https://github.com/asset-group/ORANClaw-E2-MitM-Fuzzing) `[2026-05]` - Fuzzes the O-RAN E2 interface via a MitM setup between RIC and E2 nodes. From the ASSET group.
- [AirBugCatcher](https://github.com/asset-group/air-bug-catcher) `[2024-12]` - Detection of bugs in over-the-air wireless protocol implementations. From the ASSET group.
- [FirmKit](https://github.com/SysSec-KAIST/FirmKit) `[2022-07]` - IoT firmware vulnerability analysis tool based on binary code similarity (BCSA). From the KAIST group behind BaseSpec/LTESniffer.
- [extractor](https://github.com/srlabs/extractor) `[2025-11]` - SRLabs Android firmware image extraction tool. Companion utility to their baseband and modem research workflow.
- [SentryFlow](https://github.com/5GSEC/SentryFlow) `[2025-05]` - 5G API observability and security platform monitoring SBA/HTTP2 5GC API traffic for anomalies and abuse.
- [nimbus](https://github.com/5GSEC/nimbus) `[2025-08]` - Intent-driven security automation framework for 5G/cloud-native deployments from the 5GSEC group.
- [Loris](https://github.com/SyNSec-den/Loris) `[2026-04]` - Stateful fuzzing framework for commercial baseband firmware (analyzer + emulator + fuzzer). IEEE S&P 2025. From the SyNSec group at PSU.
- [InvaRAN](https://github.com/SyNSec-den/INVARAN) `[2026-03]` - Invariant-guided logical testing of O-RAN controllers. Trace instrumentation, Daikon-based invariant inference, and grammar-aware fuzzing for xApps. From the SyNSec group.
- [closed-loop-5g-resilience](https://github.com/Montimage/closed-loop-5g-resilience) `[2026-03]` - Research prototype of a closed-loop resilience framework for 5G core networks: monitoring, alert-driven mitigation, non-regression testing. From Montimage.
- [advisories](https://github.com/EnableSecurity/advisories) `[2026-02]` - Security advisories published by Enable Security
- [CVE-2025-36911-exploit](https://github.com/PentHertz/CVE-2025-36911-exploit) `[2026-01]` - Exploit of the CVE-2025-36911 vulnerability in Python for testing our own equipment
- [sniffmap](https://github.com/P1sec/sniffmap) `[2014-12]` - sniffmap: Map of probable Internet network interception
- [pqproto](https://github.com/ngkore/pqproto) `[2025-10]` - Practical framework for experimenting with PQC in security protocols using OpenSSL and other open source libraries.
- [security-intents](https://github.com/5GSEC/security-intents) `[2024-03]` - Repository to hold security intents in standard template format.
- [E2IBS-5G-Authentication](https://github.com/SyNSec-den/E2IBS-5G-Authentication)
- [5g-threat-detector](https://github.com/SyNSec-den/5g-threat-detector)
- [MobiDojo](https://github.com/5GSEC/MobiDojo) `[2025-09]` - Virtual security combat platform for 5G with one-click OAI-based deployment and a web GUI for protocol-level security testing, no RF hardware required. From the 5GSEC group.
- [sippts](https://github.com/Pepelux/sippts) `[2026-06]` - Set of tools to audit SIP-based VoIP systems (scanning, enumeration, brute-force, interception). Companion to SIPVicious.
- [OTABase](https://github.com/OTABase/OTABase) `[2025-09]` - Over-the-air testing framework for detecting memory crashes in commercial LTE basebands.
- [AppleC4000](https://github.com/nlitsme/AppleC4000) `[2025-11]` - Tools for reverse engineering the Apple C4000 baseband firmware.

### IMSI Catcher Detection

- [Rayhunter](https://github.com/EFForg/rayhunter) `[2026-07]` - Rust tool to detect cell site simulators (IMSI catchers) on an Orbic mobile hotspot, from the EFF.
- [IMSI-catcher](https://github.com/Oros42/IMSI-catcher) `[2026-06]` - Python tool using gr-gsm to display IMSI numbers of cellphones around you.
- [Android-IMSI-Catcher-Detector](https://github.com/CellularPrivacy/Android-IMSI-Catcher-Detector) `[2026-07]` - Android app to detect IMSI catchers, StingRays, and silent SMS.
- [SentryRadio](https://github.com/fzer0x/SentryRadio) `[2026-03]` - Android forensic tool (Xposed/Magisk/KSU) to detect IMSI catchers, cell site simulators, suspicious network downgrades and silent SMS.
- [IMSICatcherDetector (Marlin)](https://github.com/eylonK14/IMSICatcherDetector) `[2025-08]` - Detects IMSI-catchers/Stingrays via statistical analysis of identity-exposing messages, implementing the Marlin methodology from NDSS 2025 (claimed 99.9% detection rate).
- [Tower-Hunter](https://github.com/Ringmast4r/Tower-Hunter) `[2026-01]` - Cell tower logger and anomaly detector for Linux mobile devices. Logs tower data with GPS, monitors cellular connections, and flags suspicious base stations.
- [rayhunter-enhanced](https://github.com/drinkingc0ffee/rayhunter-enhanced) `[2025-07]` - Enhanced fork of EFF Rayhunter providing roughly 3x cellular data coverage for IMSI-catcher detection on Quectel modems.
- [raypager](https://github.com/tschakram/raypager) `[2026-05]` - Rayhunter port for the GL-E750V2 (Mudi V2) travel router, integrating OpenCelliD and Blue Merle as part of a Chasing-Your-Tail counter-surveillance ecosystem.
- [GSM-Cipher-Sensor](https://github.com/mclab-hbrs/GSM-Cipher-Sensor) `[2025-06]` - SDR-based sensor that captures GSM Cipher Mode Command messages to detect weak/absent A5 encryption (an IMSI-catcher indicator).
- [SS7-Diameter-ShadowCell](https://github.com/zencefilefendi/SS7-Diameter-ShadowCell) `[2026-05]` - Cellular network anomaly detection platform against SS7/Diameter tracking and IMSI catchers.
- [Norypt-IMSI-Catcher](https://github.com/norypt-prv/Norypt-IMSI-Catcher) `[2026-04]` - Passive cellular security monitor for the TP-Link M7350 hotspot detecting IMSI catchers, 2G downgrades, and null ciphers.

### Security Research & Reports

- [Positive Technologies Telecom Reports](https://www.ptsecurity.com/ww-en/analytics/telecom-attacks/) - In-depth reports on SS7, Diameter, and GTP vulnerabilities in mobile networks.
- [Mobilesecurity.be](https://www.yourdigitalresearch.be/research/) - Academic mobile security research and publications.

### Videos and papers

- [Exploiting Possible 5G Vulnerabilities](https://blog.3g4g.co.uk/2019/10/exploiting-possible-5g-vulnerabilities.html) a blog post on the 3G/4G blog about the latest HITB talk describing attack in 5G.
- [USENIX19 Hiding in Plain Signal:Physical Signal Overshadowing Attack on LTE](https://www.usenix.org/system/files/sec19-yang-hojoon.pdf) - SigOver - Overriding LTE broadcast message using signal capture effect and good enough time synchronization.
- [HITB talk : 4G LTE Man in the Middle Attack with a Hacked Femtocell](https://gsec.hitb.org/materials/sg2019/D2%20-%204G%20LTE%20Man%20in%20the%20Middle%20Attacks%20with%20a%20Hacked%20Femtocell%20-%20Xiaodong%20Zou.pdf) - high level talk on hacking 4G smallcell, sourcing, tools, opportunities including on S1 gateway.
- [Vulnerabilities in 5G](https://infosec.sintef.no/en/informasjonssikkerhet/2019/08/new-vulnerabilities-in-5g-security-architecture-countermeasures/) New vulnerabilities in 5G Security Architecture & Countermeasures.
- [QPSI-2019-LTEFuzz](https://www.youtube.com/watch?v=1ns46Uy1lM0&feature=youtu.be) - Security analysis of the LTE control plane with LTEFuzz, talk regarded at QPSI Product Security Summit.
- [LTEInspector: A Systematic Approach for Adversarial Testing of 4G LTE](https://www.youtube.com/watch?v=Cf6-O63vVdI) - Talk about LTE vulnerability research at NDSS 2018.
- [SS7: Locate. Track. Manipulate.](https://media.ccc.de/v/31c3_-_6249_-_en_-_saal_1_-_201412271715_-_ss7_locate_track_manipulate_-_tobias_engel) - Talk about SS7 vulnerability at 31C3.
- [SS7map : mapping vulnerability of the international mobile roaming infrastructure](https://media.ccc.de/v/31c3_-_6531_-_en_-_saal_6_-_201412272300_-_ss7map_mapping_vulnerability_of_the_international_mobile_roaming_infrastructure_-_laurent_ghigonis_-_alexandre_de_oliveira) - Talk about SS7 vulnerability and introduction to [SS7map](https://ss7map.p1sec.com/) at 31C3.
- [Advanced interconnect attacks](https://media.ccc.de/v/camp2015-6785-advanced_interconnect_attacks) - Talk about GTP interconnection security at Chaos Communication Camp 2015.
- [Mobile Data Interception from the Interconnection Link](https://media.ccc.de/v/34c3-8879-mobile_data_interception_from_the_interconnection_link) - Talk about Diameter interconnection security at 34C3.
- [On the Challenges of Automata Reconstruction in LTE Networks](https://www.syssec.ruhr-uni-bochum.de/media/emma/veroeffentlichungen/2021/06/02/LTE-Automata-WiSec21.pdf) - In this paper, the authors explore active automata learning for 4G/LTE protocol state machines. [video](https://www.youtube.com/watch?v=0OERPpdeJi8)
- [SS7 and SIGTRAN in 2G/3G networks](https://people.osmocom.org/tnt/osmodevcall/osmodevcall-20210514-laforge-ss7-sigtran_h264_420.mp4) - An introduction to SS7/SIGTRAN stack, including the history, use cases, roles of each layer, and how SS7-speaking equipment works.
- [Hiding in plain signal: Physical signal overshadowing attack on LTE](https://syssec.kaist.ac.kr/pub/2019/sec19-yang-hojoon.pdf) - n this paper, for the first time, we present a signal injection attack that exploits the funda- mental weaknesses of broadcast messages in LTE and mod- ifies a transmitted signal over the air.

### Writeups

- [GSM capture, analysis and decoding](http://domonkos.tomcsanyi.net/?p=418) - Four-post series on GSM cellular signal analysis.

## Learning Resources

### Documentation & Standards

- [ShareTechNote](http://www.sharetechnote.com/) - An impressive repository of knowledge for the cellular telco world. Highly recommended for beginners.
- [Techplayon](https://www.techplayon.com/) - Excellent 4G/5G tutorials with clear diagrams and explanations.
- [EventHelix](https://www.eventhelix.com/lte/) - Protocol sequence diagrams for LTE/5G signaling flows.
- [3GPP specs](http://www.3gpp.org/ftp/Specs/html-info/36-series.htm) - Official 3GPP specifications.
- [GSMA Specifications](https://www.gsma.com/solutions-and-impact/technologies/networks/gsma_resources/) - Official GSMA specs for eSIM, roaming, interconnect, and more.
- [Getsi](https://getsi.org/) - Easy search engine for 3GPP specs.
- [speX](https://spex.cor-net.org) - Accessible 3GPP specs (PDF, DOC, HTML), [can be self-hosted](https://github.com/CoRfr/spex-3gpp).
- [3gpp.guru](https://3gpp.guru) - Look up 3GPP abbreviations.
- [3GPP-overall-architecture](https://github.com/nickel0/3GPP-Overall-Architecture) `[2021-11]` - Very detailed, high-res PDF of the overall 3GPP architecture.
- [Wireless frequency bands](http://niviuk.free.fr/) - Come for the frequency calculator, stay for the other cellular resources.
- [RCS on iOS Support Tracker](https://cupboardunderscore.github.io/ios-rcs/) - Tracks which mobile carriers worldwide support RCS messaging on iOS devices, organized by country.
- [CNTT](https://cntt-n.github.io/CNTT/) - Reference specifications for NFVI from Vodafone, Telstra, Orange, and others.
- [tool3rd](https://github.com/proj3rd/tool3rd) `[2026-02]` - Assistant for 3GPP telecommunication development.
- [3gpp-citations](https://github.com/martisak/3gpp-citations) `[2023-11]` - 3GPP Bibtex entry generator.
- [SA5 MnS APIs](https://forge.3gpp.org/rep/sa5/MnS) - 3GPP SA5 Management and Orchestration OpenAPI specifications and YANG data models. Hosted on **3GPP Forge**.
- [Introduce to 5GC](https://github.com/ianchen0119/Introduce-to-5GC) `[2022-07]` - 5GC & Cloud Native handbook (Traditional Chinese).
- [eUICC and eSIM Developer Manual](https://euicc-manual.osmocom.org) - Comprehensive eSIM developer documentation.
- [specpilot](https://github.com/herlesupreeth/specpilot) `[2025-08]` - AI-powered 3GPP specification assistant. From the author of docker_open5gs.
- [3gpp-crawler](https://forge.3gpp.org/rep/reimes/3gpp-crawler) - CLI tool to crawl 3GPP FTP server, cache TDocs data, return structured JSON/YAML. Hosted on **3GPP Forge**.
- [teddi-mcp](https://forge.3gpp.org/rep/reimes/teddi-mcp) - CLI and FastMCP server for ETSI's TEDDI (Terms and Definitions Database Interactive). Search 3GPP/ETSI terms programmatically. Hosted on **3GPP Forge**.
- [5G_APIs](https://forge.3gpp.org/rep/all/5G_APIs) - Official 3GPP 5G API definitions (OpenAPI/Swagger). REL-20. Hosted on **3GPP Forge**.
- [3GPP Meeting Tools](https://github.com/telekom/3gpp-meeting-tools) `[2026-07]` - Deutsche Telekom-maintained tools for the day-to-day execution of 3GPP meetings (TDoc handling, agenda parsing). Useful for delegates.
- [MNO List](https://github.com/CursedHardware/mno-list) `[2026-03]` - Curated list of mobile network operators with metadata, broader than the canonical PLMN list. Useful for SIM/eSIM tooling.
- [Telco-Spaghetti](https://codeberg.org/leecowdrey/Telco-Spaghetti) `[2026-03]` - SVG architecture posters illustrating real-world telco OSS/BSS and 4G/5G access/transport "spaghetti". Handy didactic reference. Hosted on **Codeberg**.
- [SA3-LI formal language specifications](https://forge.3gpp.org/rep/sa3/li) - Authoritative repo for 3GPP SA3-LI lawful-interception XSD/JSON schemas and formal-language specs (TS 33.128 family). Hosted on **3GPP Forge**.

### Blogs

- [Nick vs Networking](https://nickvsnetworking.com/category/plmn/) - Telecommunications network engineering, from legacy to cutting-edge.
- [The 3G4G Blog](https://blog.3g4g.co.uk) - Latest news and information on 3G, 4G, 5G wireless technologies.
- [How LTE Stuff Works?](https://howltestuffworks.blogspot.com/) - In-depth blog on 4G/5G by a 3GPP Engineer.
- [Yoshiyuki Kurauchi](https://wmnsk.com/posts/) - Blog posts by a telecom/networking/security enthusiast.
- [Frédéric Launay](http://blogs.univ-poitiers.fr/f-launay/) - 🇫🇷 French blog on 4G/5G mobile networks.
- [GTP-Guard articles](https://gtp-guard.org/articles/) - Design deep-dives on GTP-Guard and high-performance 5G UPF internals (XDP, PFCP, CPU scheduling) by the author of gtp-guard/keepalived. Notable posts:
  - [5G UPF: Smart Session Placement](https://gtp-guard.org/articles/5g-upf-smart-session-placement/) `[2026-04]` - Trend-based, multi-metric CPU scheduling using a Weighted Score Composite over sessions/load/bandwidth/PPS with constraint-based hard limits for SLA differentiation.
  - [5G UPF: From Flow Steering to Session Affinity](https://gtp-guard.org/articles/5g-upf-from-flow-steering-to-session-affinity/) `[2026-04]` - Integrates range partitioning into PFCP so session creation becomes a line-rate scheduling decision, aligning TEID, IP pool, and CPU resources via `range-partition`, `flow-steering-policy`, and `cpu-sched-group` objects.
  - [Per-Core CPU Load Measurement](https://gtp-guard.org/articles/cpu_load_measurement/) `[2026-04]` - Why `/proc` metrics miss inline XDP/NAPI softirq work, and how GTP-Guard uses `PERF_COUNT_HW_REF_CPU_CYCLES` hardware counters for accurate per-core load.
  - [5G UPF: Pump Up the Volume!](https://gtp-guard.org/articles/5g-upf-pump-up-the-volume/) `[2026-03]` - Hardware foundations for 800 Gbps UPF throughput: NIC queue pinning, IRQ affinity, and range-partitioning math over TEID/IP sub-prefixes.

### Presentations & Slides

- [Kubernetes networking in the telco space](https://wiki.lfnetworking.org/download/attachments/328197/KubernetesNetworkingInTheTelcoSpace-Csatari.pdf?version=1&modificationDate=1522083330000&api=v2)
- [How the CCC Camp 2019 LTE network works](http://people.osmocom.org/laforge/slides/cccamp2019-how_the_camp_lte_works.pdf) - Reusing commercial Ericsson 4G units.

### YouTube Channels

- [Penthertz](https://www.youtube.com/@Penthertz) - RF Hacking, Software-Defined Radio, tips and tricks.

## Organizations

Key organizations driving open source telecom development:

- [Osmocom](https://osmocom.org) - Umbrella for numerous open source mobile communications projects. Great presentations at [OsmoDevCon](https://osmocom.org/projects/osmo-dev-con/wiki/OsmoDevCon) and [OsmoDevCall](https://osmocom.org/projects/osmo-dev-con/wiki/OsmoDevCall).
- [Telecom Infra Project](https://www.telecominfraproject.com) - Facebook-initiated project, the OpenCompute of telecom.
- [3GPP Forge](https://forge.3gpp.org/rep/explore) - Official code forge for the 3GPP organization.
- [O-RAN Alliance](https://www.o-ran.org/) - Open Radio Access Network standards.
- [ETSI Forge](https://forge.etsi.org/) - Official ETSI code forge hosting test suites, APIs and reference implementations for telecom standards (NFV, MEC, TTCN-3). Hosted on **GitLab**.
- [ETSI Labs](https://labs.etsi.org/) - ETSI's development platform hosting open source implementations: TeraFlowSDN, OpenCAPIF, OpenSlice, OpenOP, and more. Hosted on **GitLab**.
- [Libre Space Foundation](https://libre.space/) - Non-profit for open source hardware and software in space, including SatNOGS ground station network and UPSat satellite.

## Community

### Discord

- [Open5GS](https://discord.gg/M9ARcyvV) - Open5GS community chat.

### Reddit

- [r/cellulartechnology](https://reddit.com/r/cellulartechnology) - Community discussions on cellular technology and mobile networks.
- [r/RTLSDR](https://reddit.com/r/RTLSDR) - SDR community with cellular signal reception discussions.

### Slack

- [Magma](https://slack.magmacore.org/) - Magma project community.

### Mailing Lists

- [OpenBSC / Osmocom](https://lists.osmocom.org/mailman/listinfo/openbsc)
- [Osmocom Discourse Forum](https://discourse.osmocom.org/)
- [OAI-user](http://lists.eurecom.fr/sympa/arc/openair5g-user) / [OAI-devel](http://lists.eurecom.fr/sympa/arc/openair5g-devel)
- [OAI Core Network](http://lists.eurecom.fr/sympa/arc/openaircn-user)
- [Magma-dev](https://groups.google.com/forum/#!forum/magma-dev) / [Magma-announce](https://groups.google.com/forum/#!forum/magma-announce)

### Notable GitHub Issues & Discussions

- [SCTP Kubernetes support](https://github.com/kubernetes/community/pull/2276)
- [SRSENB: Add SIB7 (GERAN neighbor) support](https://github.com/srsLTE/srsLTE/pull/361)

## Related Lists

- [awesome-5g](https://github.com/calee0219/awesome-5g) `[2026-02]` - 5G-specific projects and resources.
- [awesome-rtc-hacking](https://github.com/EnableSecurity/awesome-rtc-hacking) `[2026-06]` - Curated list of VoIP, WebRTC, and VoLTE security resources. From the SIPVicious team.
- [awesome-ai-oran](https://github.com/LynchXLQ/awesome-ai-oran) `[2026-03]` - Curated list of AI/ML research papers and tools for O-RAN. Covers DRL, GNN, LLMs, and more applied to O-RAN.
- [Paper-with-Code (Wireless DL)](https://github.com/ML4Comm-Netw/Paper-with-Code-of-Wireless-communication-Based-on-DL) `[2023-07]` - Massive curated collection of deep learning papers with code for wireless communication.
- [RIS-Codes-Collection](https://github.com/ken0225/RIS-Codes-Collection) `[2026-06]` - Complete collection of codes for RIS/IRS research including DL/RL approaches for beamforming and channel estimation.
- [GNN-Communication-Networks](https://github.com/jwwthu/GNN-Communication-Networks) `[2026-06]` - Curated collection of GNN research for communication networks. Covers traffic prediction, routing, spectrum sensing.
- [Cellular-Security-Papers](https://github.com/onehouwong/Cellular-Security-Papers) `[2026-03]` - Collection of papers, repos, talks, and tools for cellular security and privacy.

## Contributing

Contributions welcome! Please read the contribution guidelines first. Open a PR or issue to add new resources.

## License

[MIT](LICENSE)
