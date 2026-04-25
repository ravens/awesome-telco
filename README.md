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
- [Commercial](#commercial) - Companies and commercial offerings

---

## SIM Cards

### SIM/USIM Tools & Hardware

- [PySIM](https://osmocom.org/projects/pysim/wiki) `[2025-12]` - Set of tools to read/explore/decode and program (write) SIM/USIM/ISIM cards. Essential for managing programmable SIM cards.
- [sysmoISIM-SJA5](https://www.sysmocom.de/products/sim/sysmoisim-sja5/) - Latest generation programmable SIM/UICC/USIM/ISIM card with 3GPP Release 17 support. Ideal for lab/research networks.
- [sysmo-usim-tool](https://gitea.sysmocom.de/sysmocom/sysmo-usim-tool) - Utility for managing proprietary bits of sysmoUSIM/sysmoISIM programmable cards.
- [SIMTrace2](https://osmocom.org/projects/simtrace2) - Hardware device + firmware to trace communication between phone and SIM card. Supports card-side emulation. Works with [ngff-cardem](https://osmocom.org/projects/ngff-cardem/wiki).
- [SIMTester](https://opensource.srlabs.de/projects/simtester) - Assess SIM card security: cryptanalytic attack surface and application attack surface.
- [GlobalPlatformPro](https://github.com/martinpaljak/GlobalPlatformPro) `[2026-03]` - CLI tool to load and manage applets on JavaCards, by Martin Paljak.
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
- [apdu4j](https://github.com/martinpaljak/apdu4j) `[2026-04]` - APDU-level smart card communication library for Java. PC/SC and remote JSON interfaces. From the GlobalPlatformPro author.
- [UiccBrowser](https://github.com/cheeriotb/UiccBrowser) `[2026-04]` - Android app to browse the file system of a UICC/eUICC via the OMAPI. From the ISD-R-AccessProvider author.
- [sim-toolkit-refresh](https://github.com/cheeriotb/sim-toolkit-refresh) `[2026-01]` - Java Card applet implementing the SIM Toolkit REFRESH proactive command for SIM/STK testing on Android.
- [osmocom-sim-tools (mirror)](https://github.com/cheeriotb/osmocom-sim-tools) `[2025-07]` - Active fork of Osmocom sim-tools with additional features for sysmoUSIM/sysmoISIM cards.

### eSIM / eUICC

- [eUICC and eSIM Developer Manual](https://euicc-manual.osmocom.org) - Comprehensive eSIM developer documentation from Osmocom.
- [Known eSIM Test Profiles](https://euicc-manual.osmocom.org/docs/rsp/known-test-profile/) - List of known test profiles for eSIM/eUICC testing and development.
- [lpac](https://github.com/estkme-group/lpac) `[2026-03]` - C-language implementation of a Consumer eSIM LPAd. Download/activate/deactivate profiles on eUICC.
- [EasyLPAC](https://github.com/creamlike1024/EasyLPAC) `[2026-03]` - lpac GUI Frontend for Linux and macOS.
- [OpenEUICC](https://github.com/estkme-group/openeuicc) `[2026-03]` - Fully open-source eSIM LPA (Local Profile Assistant) implementation for Android. System privilege required. Also available as [Magisk module](https://github.com/hzy132/OpenEUICC_for_Magisk).
- [LPAd SM-DP+ Connector](https://github.com/Truphone/LPAd_SM-DPPlus_Connector) `[2023-05]` - Local Profile Assistant for Device (LPAd) SM-DP+ Connector.
- [Generic-eUICC-Test-Profile](https://github.com/GSMATerminals/Generic-eUICC-Test-Profile-for-Device-Testing-Public) `[2025-06]` - Standardized test profiles for embedded UICCs.
- [ISD-R Access Provider](https://github.com/cheeriotb/ISD-R-AccessProvider) `[2021-01]` - Content provider for communicating with ISD-R in soldered eSIM on Android (Pixel4).
- [rlpa-server](https://github.com/estkme-group/rlpa-server) `[2024-07]` - Remote LPA Server for eSIM profile management, from the lpac team.
- [MiniLPA](https://github.com/EsimMoe/MiniLPA) `[2024-12]` - Professional cross-platform LPA UI for eSIM/eUICC management (GSMA SGP.22), built with Java Swing.
- [NekokoLPA](https://github.com/iebb/NekokoLPA) `[2026-01]` - Open-source LPA software for managing eSIM profiles on Android and iOS.
- [eUICC Probe](https://github.com/CursedHardware/euicc-probe) `[2026-04]` - eUICC diagnostic and probing tool in Kotlin. Inspect eUICC capabilities and profile information.
- [OpenRSP](https://github.com/Blockchain-Powered-eSIM/OpenRSP) `[2026-04]` - Open source Remote SIM Provisioning implementation for eSIM profile management.
- [Onomondo SoftSIM](https://github.com/onomondo/nrf-softsim) `[2026-04]` - SoftSIM integration for Nordic Semiconductor nRF91 Series. Software-based SIM for IoT. From Onomondo.
- [smdpp](https://github.com/ianchen0119/smdpp) `[2026-01]` - Early-stage open SM-DP+ (Subscription Manager Data Preparation+) implementation for eSIM remote provisioning research.
- [onomondo-eim](https://github.com/onomondo/onomondo-eim) `[2026-03]` - Open implementation of an eIM (eUICC IoT Manager) per GSMA SGP.31 for IoT eSIM remote provisioning. From Onomondo.
- [onomondo-ipa](https://github.com/onomondo/onomondo-ipa) `[2026-02]` - IoT Profile Assistant (IPA) implementation per SGP.32 providing on-device functions for SGP.32 eUICC provisioning by an SM-DP+. From Onomondo.
- [euicc-go](https://github.com/damonto/euicc-go) `[2026-04]` - Pure-Go implementation of the eUICC profile management protocol (SGP.22). Building block for LPA tooling.
- [notccid](https://github.com/estkme-group/notccid) `[2026-03]` - ESTKme-RED reader protocol, the non-CCID protocol used by the ESTKme programmable eSIM reader/writer hardware.
- [NekokoLPA2](https://github.com/iebb/NekokoLPA2) `[2026-04]` - Second-generation cross-platform open-source LPA UI for eSIM management on Android/iOS, by the original NekokoLPA author.
- [remocard](https://github.com/iebb/remocard) `[2026-04]` - Remote OMAPI companion app for NekokoLPA2, exposing a phone's secure element/eUICC over the network for remote LPA operations.
- [SecureElementAccessBypass](https://github.com/EsimMoe/SecureElementAccessBypass) `[2026-03]` - Android module to bypass SE ARA & ARF access restrictions for full SE access. Used in eUICC/SIM research on locked-down devices.
- [gsma-sgp22-asn1](https://github.com/CursedHardware/gsma-sgp22-asn1) `[2026-04]` - Standalone GSMA SGP.22 ASN.1 schema definitions extracted for use in eSIM tooling and codegen.
- [eSIM Wallet](https://github.com/Blockchain-Powered-eSIM/eSIM-Wallet) `[2025-12]` - Mobile eSIM wallet app, the user-facing companion to OpenRSP. From the Blockchain-Powered-eSIM project.
- [TSMS](https://github.com/BSI-Bund/TSMS) `[2026-02]` - German BSI reference Java API and OpenAPI spec for a Trusted Service Management System (BSI-TR-03165), used to install and personalize JavaCard applets on smartphone secure elements.

### SIM Emulation & Virtualization

- [swSIM](https://github.com/tomasz-lisowski/swsim) `[2026-02]` - A software-only SIM card.
- [swICC](https://github.com/tomasz-lisowski/swicc) `[2026-02]` - Framework for creating smart cards (ICC-based cards with contacts).
- [vsmartcard](https://github.com/frankmorgner/vsmartcard) `[2026-03]` - Umbrella project for emulation of smart card readers or smart cards.
- [Onomondo UICC](https://github.com/onomondo/onomondo-uicc) `[2026-03]` - Pure software implementation/emulation of SIM/UICC/USIM functionalities.
- [osmo-remsim](https://osmocom.org/projects/osmo-remsim/wiki) - Forward SIM card traffic to a remote SIM card via TCP/IP.
- [mobile-atlas](https://github.com/sbaresearch/mobile-atlas) `[2025-11]` - Geographically decouple SIM card and modem for scalable measurement platforms.
- [softsim-quecopen-unisoc-lte](https://github.com/onomondo/softsim-quecopen-unisoc-lte) `[2026-03]` - Onomondo SoftSIM integration for Quectel LTE modules using the UNISOC SDK, extending SoftSIM beyond the Nordic nRF91.

### VoLTE/VoWiFi & Carrier Privileges

- [CoIMS_Wiki](https://github.com/herlesupreeth/CoIMS_Wiki) `[2025-10]` - Guide for overriding IMS settings to enable VoLTE/VoWiFi using Carrier Privileges. Companion app: [CoIMS](https://play.google.com/store/apps/details?id=com.sherle.coims).
- [pixel_ims_module](https://github.com/cxOrz/pixel_ims_module) `[2024-04]` - Magisk module that enables VoLTE, VoNR, and Wi-Fi Calling on rooted Pixel devices by modifying carrier config boolean flags.
- [aram-cardlet](https://github.com/cheeriotb/aram-cardlet) `[2025-02]` - Sample Java Card ARA-M applet for the Android Secure Element CTS, useful for carrier-privilege experimentation on SIMs.
- [App ARA-M Calculator](https://github.com/EsimMoe/AppARA-MCalculator) `[2026-02]` - Helper to compute the App ARA-M hash needed for Android carrier-privilege rules and SE access entries.


## User Equipment

### 4G

- [srsUE](https://github.com/srslte/srslte) `[2026-01]` - UE 4G modem part of the srsLTE project.
- [srsUE PR external NAS](https://github.com/srsLTE/srsLTE/pull/474) `[2026-01]` - a PR for srsLTE for external NAS message injection.
- [OAI UE](https://gitlab.eurecom.fr/oai/openairinterface5g/wikis/home) `[2026-03]` - Open Air Interface RAN 4G eNB/ 5G gNB to use on SDR-based radios.
- [Amarisoft](https://www.amarisoft.com) - Commercial UE Emulator by Amarisoft, company co-founded by [Bellard](https://bellard.org) on his original LTE software modem [work](https://bellard.org/lte/).
- [LTE-CellScanner](https://github.com/Evrytania/LTE-Cell-Scanner) `[2019-02]` - This is a collection of tools to locate and track LTE basestation cells using very low performance RF front ends.
- [LTE-CellScanner-SDR-X](https://github.com/JiaoXianjun/LTE-Cell-Scanner) `[2024-01]` - An OpenCL accelerated TDD/FDD LTE Scanner (from rtlsdr/hackRF/bladeRF A/D samples to PDSCH output and RRC SIB messages decoded).
- [S1APTester](https://github.com/magma/S1APTester) `[2022-12]` - A test tool that simulates the s1aptest functionality of a LTE network.

### 2G

- [OsmocomBB](https://osmocom.org/projects/baseband/wiki) - Open Source implementation of a 2G Mobile Station, including baseband firmware/PHY, L2, L3, etc.  Works with phones using TI Calypso chipset; SDR PHY is work-in-progress
- [FreeCalypso](https://www.freecalypso.org/) - Volunteer project building software derived from leaked source code for the TI calypso project

### Diagnostics, Monitor mode

- [SCAT](https://github.com/fgsect/scat) `[2026-02]` - this application parses diagnostic messages of Qualcomm and Samsung baseband through USB, and generates a stream of GSMTAP packet containing cellular control plane messages.
- [QCSuper](https://github.com/P1sec/QCSuper) `[2026-03]` - QCSuper is a tool communicating with Qualcomm-based phones and modems, allowing to capture raw 2G/3G/4G radio frames, among other things.
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
- [TowerCollector](https://github.com/zamojski/TowerCollector) `[2026-04]` - Android contributor app for OpenCellID and BeaconDB. Records GPS-tagged GSM/UMTS/LTE/5G cell observations and uploads them to open cell databases.
- [gsm-parser](https://github.com/srlabs/gsm-parser) `[2025-11]` - SRLabs GSM/UMTS parser used by the SnoopSnitch backend for analyzing baseband logs and signaling.

## Radio Access Network

### RRH

- [O-RAN Software and seed code](https://o-ran-sc.org) - The O-RAN Software Community (SC) is a collaboration between the O-RAN Alliance and Linux Foundation with the mission to support the creation of software for the Radio Access Network (RAN). Introduction to O-RAN in a [LF video](https://www.youtube.com/watch?v=iJyb0pCWDKo).
- [srsRAN O-RAN SC RIC](https://github.com/srsran/oran-sc-ric) `[2025-10]` - Simplified O-RAN SC RIC deployment with improved usability and xApp examples, from the srsRAN team.
- [FlexRIC](https://gitlab.eurecom.fr/mosaic5g/flexric) `[2026-03]` - O-RAN Alliance compliant Near-RT RIC and E2 Agent with xApp SDK in C/C++ and Python. Sub-200µs latency. Part of MOSAIC5G/OAI. Hosted on **GitLab (Eurecom)**.
- [ProtO-RU](https://github.com/NUS-CIR/ProtO-RU) `[2026-02]` - Software implementation of an O-RAN split-7.2 compatible Radio Unit using SDRs. From NUS.
- [xDevSM](https://github.com/wineslab/xDevSM) `[2026-03]` - Open-source framework for O-RAN E2 service models that simplifies xApp development for OSC Near-RT RIC. Supports KPM V3. From WiNES Lab / Northeastern University.
- [Colosseum Near-RT RIC](https://github.com/wineslab/colosseum-near-rt-ric) `[2025-12]` - Minimal O-RAN SC Near-RT RIC adapted for the Colosseum wireless network emulator. Supports concurrent multi-base-station and multi-xApp connections. From WiNES Lab.
- [xFAPI](https://github.com/coranlabs/xFAPI) `[2025-10]` - Facilitating interoperability in Open RAN via xFAPI interface. From CoRAN Labs.
- [O-RAN SC O-DU L2](https://github.com/o-ran-sc/o-du-l2) `[2026-03]` - O-RAN Software Community Distributed Unit Layer 2 implementation. Reference O-DU high with F1/E2 interfaces.
- [SCOPE](https://github.com/wineslab/colosseum-scope) `[2026-03]` - Open and Softwarized Prototyping Platform for NextG Systems on the Colosseum wireless network emulator. From WiNES Lab (ACM MobiSys).
- [ORANSlice](https://github.com/wineslab/ORANSlice) `[2026-03]` - Open-source 5G network slicing platform for O-RAN with xApp-based slice management. From WiNES Lab (ACM MobiCom'24).
- [dApp Framework](https://github.com/wineslab/dApp-framework) `[2026-03]` - Framework for distributed Apps (dApps) for O-RAN beyond the xApp/rApp model. From WiNES Lab.
- [dApp Library](https://github.com/wineslab/dApp-library) `[2026-04]` - Library counterpart to dApp-framework providing building blocks for writing dApps that run inside the O-RAN DU/CU. From WiNES Lab.
- [OSC RIC xApp Template](https://github.com/5GSEC/OSC-RIC-xApp-Template) `[2026-02]` - Python xApp development template for the O-RAN SC Near-RT RIC with SDL/RMR/E2 scaffolding. Useful starting point for new xApp authors.
- [OAI O1 Adapter](https://gitlab.eurecom.fr/oai/o1-adapter) - O-RAN O1/NETCONF adapter for OpenAirInterface gNB enabling integration with O-RAN SMOs. Hosted on **GitLab (Eurecom)**.
- [ai-ran-dgx-spark](https://github.com/rcbarke/ai-ran-dgx-spark) `[2025-12]` - Deployment automation for NVIDIA Aerial AI-RAN on the DGX Spark platform. Useful for getting Aerial running on GPU AI-RAN testbeds.

### 5G

- ⚠️ [srsRAN_Project](https://github.com/srsran/srsRAN_Project) `[2026-02]` - A complete ORAN-native 5G RAN solution. _Archived Feb 2026; successor is [OCUDU](https://ocudu.org/), a Linux Foundation project for open-source AI-RAN._
- [OAI NR](https://gitlab.eurecom.fr/oai/openairinterface5g/wikis/5g-nr-development-and-releases) `[2026-03]` - 5GNR related branch of the OAI code. You can follow the [weekly updates](https://trello.com/c/XBVaaHIO/26-5g-nr) to stay up to date.
- [UERANSIM](https://github.com/aligungr/UERANSIM) `[2025-10]` - UERANSIM is the state-of-the-art 5G UE and RAN (gNodeB) simulator. The project can be used for testing 5G Core Network and studying 5G System.
- ⚠️ [Software gNB for free5GC](https://github.com/Srajdax/gnb) `[2020-11]` - The gNB function was built on the model of the other free5GC CN functions using all the pattern and helper class defined by the free5GC team.
- [5G-tools.com](https://5g-tools.com/) - 5G-tools.com is devoted to modern standards of wireless communications, such as 5G, 4G, etc. Main mission of site to give engineers the useful software tools to create a wireless network
- ⚠️ [corescope](https://github.com/srsran/corescope) `[2021-12]` - CoreScope combines gNodeB and UE components without any radio transmission.
- [my5G-RANTester](https://github.com/my5G/my5G-RANTester) `[2024-04]` - my5G-RANTester is a gNB/UE simulator for testing 3GPP standards and stressing a 5G core.
- [free5GRAN](https://github.com/IMTSDRLab/free5GRAN) `[2021-10]` - free5GRAN is an open-source 5G RAN stack. The current version includes a receiver which decodes MIB & SIB1 data. It also acts as a cell scanner. free5GRAN works in SA mode. From Telecom Paris 5G laboratory - Institut Polytechnique de Paris.
- [pfm](https://github.com/arv-sajeev/pfm) `[2021-11]` - Implemented a prototype of gNB-CU-UP a network element of 5G Radio Network. Using DPDK, a set of data-plane processing libraries and NIC drivers for high speed packet processing applications.
- [PacketRusher](https://github.com/HewlettPackard/PacketRusher) `[2026-02]` - High performance 5G UE/gNB Simulator and CP/UP load tester. PacketRusher is an open-source tool dedicated to the performance testing and automatic validation of 5G Core Networks using simulated UE (user equipment) and gNodeB (5G base station). From Valentin D'Emmanuele - France.
- [py3gpp](https://github.com/catkira/py3gpp) `[2024-11]` - A Python package for 5G-NR simulations.
- [RFSwift](https://github.com/PentHertz/RF-Swift) `[2026-03]` -  powerful multi-platform RF toolbox that deploys specialized radio tools in seconds on Linux, Windows, and macOS. Provdes telecom_4G_5GNSA_* family of telecoms tools.
- [NVIDIA Aerial](https://github.com/NVIDIA/aerial-cuda-accelerated-ran) `[2025-12]` - SDK for building commercial-grade, AI-native, 3GPP and O-RAN compliant 5G/6G gNB software on NVIDIA GPU-accelerated platforms.
- [NVIDIA Aerial Framework](https://github.com/NVIDIA/aerial-framework) `[2025-12]` - Python toolchain for generating GPU-accelerated 5G/6G pipelines. MLIR-TensorRT compilation and real-time runtime. Companion to Aerial SDK.
- [alsoran](https://github.com/nplrkn/alsoran) `[2025-06]` - 5G gNodeB Centralized Unit (gNB-CU) written in Rust. From the author of qcore.
- [gnbsim (SD-Core)](https://github.com/omec-project/gnbsim) `[2026-03]` - gNB and UE simulator for testing 5G core networks, from the SD-Core/OMEC project.
- [free-ran-ue](https://github.com/free-ran-ue/free-ran-ue) `[2026-03]` - Next-generation open-source 5G RAN/UE simulator for free5GC with web frontend, multi-UE and ULCL support. Written in Go.
- [NIST O-RAN Testbed Automation](https://github.com/usnistgov/O-RAN-Testbed-Automation) `[2026-02]` - Turn-key automation for deploying 5G O-RAN testbeds. Supports Open5GS, OAI, free5GC, srsRAN, multiple UPFs and xApps. From NIST.
- [ns-O-RAN-flexric](https://github.com/Orange-OpenSource/ns-O-RAN-flexric) `[2025-07]` - RAN simulator with E2 termination compliant with FlexRIC. Supports E2AP v1.01, KPM v3, RC v1.01. From Orange.
- [ns3-oran](https://github.com/usnistgov/ns3-oran) `[2025-11]` - ns-3 module for modeling O-RAN-like behavior with Near-RT RIC, E2 reporting, and ML model support. From NIST.
- [sim-ns3-o-ran-e2](https://github.com/o-ran-sc/sim-ns3-o-ran-e2) `[2025-11]` - ns-3 module with O-RAN-compliant E2 interface support. From O-RAN SC.
- [NextMN-SRv6](https://github.com/nextmn/SRv6) `[2026-03]` - Experimental SRv6 MUP Endpoint Behaviors implementation (RFC 9433) for mobile user plane. From NextMN.
- [NextMN-UE-Lite](https://github.com/nextmn/UE-Lite) `[2026-03]` - Experimental 5G UE simulator from the NextMN project. Companion to [gNB-Lite](https://github.com/nextmn/gNB-Lite) and [CP-Lite](https://github.com/nextmn/CP-Lite).
- [Sionna Research Kit](https://github.com/NVlabs/sionna-rk) `[2026-03]` - GPU-accelerated research platform for AI-RAN from NVIDIA. Extends Sionna for AI-native radio access network research.

### 4G

- [OAI eNB/ gNB](https://gitlab.eurecom.fr/oai/openairinterface5g/wikis/home) `[2026-03]` - Open Air Interface RAN 4G eNB / 5G NR gNB to use on SDR-based radios.
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

### TETRA

- [osmo-tetra](https://gitea.osmocom.org/tetra/osmo-tetra) - TETRA PHY/MAC layer implementation in C/Python. Supports receiving and decoding TETRA signals with SDR hardware (USRP, HackRF). Hosted on **Osmocom Gitea**.

### Analog / 1G

- [osmocom-analog](https://gitea.osmocom.org/cellular-infrastructure/osmocom-analog) - Analog cellular network implementations: A-Netz, B-Netz, C-Netz, NMT, AMPS, TACS, and more. Hosted on **Osmocom Gitea**.

### PHY
- [gr-osmoSDR](https://osmocom.org/projects/gr-osmosdr) - Unified gnuradio input/output block for a variety of SDR devices, including FUNcube Dongle, OsmoSDR, RTL-SDR, MSi2500, SDRplay, SDR-IQ, AirSpy, rad10, HackRF, bladeRF, USSRP/UHD, UMtrx, RedPitaya, FreeSRP.
- [gr-gsm](https://github.com/ptrkrysik/gr-gsm) `[2025-03]` - GNU Radio blocks and tools for receiving GSM transmissions.
- [USRP B210](https://www.ettus.com/all-products/UB210-KIT/) - SDR Radio kit compatible with most of the SDR-based software modem implementations.
- [LimeSDR](https://limemicro.com/products/boards/limesdr/) - Affordable full-duplex SDR board, popular for srsRAN and OAI experimentation.
- [BladeRF](https://www.nuand.com/) - USB 3.0 SDR platform compatible with open source cellular stacks.
- [Kalibrate](https://github.com/steve-m/kalibrate-rtl) `[2023-08]` - Kalibrate, or kal, can scan for GSM base stations in a given frequency band and can use those GSM base stations to calculate the local oscillator frequency offset.
- [rtl-sdr](https://github.com/osmocom/rtl-sdr) `[2026-02]` - Library for turning a RTL2832-based DVB dongle into a Software Defined Receiver. Foundational for low-cost SDR-based cellular signal reception.
- ⚠️ [open5G_phy](https://github.com/catkira/open5G_phy) `[2025-04]` - A resource-efficient, customizable, synthesizable 5G NR lower PHY written in Verilog for FPGA targets.
- [neural_rx](https://github.com/NVlabs/neural_rx) `[2025-12]` - Real-time inference of 5G NR multi-user MIMO neural receivers from NVIDIA Research.
- [zynq_timestamping](https://github.com/srsran/zynq_timestamping) `[2023-01]` - Open source Zynq FPGA timestamping for precise SDR timing in 5G RAN deployments. From SRS.
- [CyberEther](https://github.com/PentHertz/CyberEther) `[2026-03]` - High-performance GPU-accelerated signal processing and visualization framework. Runs anywhere. From PentHertz.
- [osmo-fl2k](https://gitea.osmocom.org/sdr/osmo-fl2k) - Turns USB 3.0 VGA adapters (FL2000-based) into low-cost SDR transmitters. Hosted on **Osmocom Gitea**.
- [gr-fosphor](https://gitea.osmocom.org/sdr/gr-fosphor) - GNU Radio spectrum visualization block with GPU-accelerated real-time waterfall display. Hosted on **Osmocom Gitea**.
- [GeoLibCov](https://github.com/Orange-OpenSource/GeoLibCov) `[2026-02]` - Geographic library for cell coverage modelling and topography generation. From Orange.
- [DragonOS](https://sourceforge.net/projects/dragonos-focal/) - Debian/Ubuntu-based Linux distro with 30+ pre-installed SDR tools (GNU Radio, gr-gsm, GQRX, etc.) for RF analysis, spectrum monitoring and telecom security. Hosted on **SourceForge**.
- [Gqrx SDR](https://www.gqrx.dk/) - Open source SDR receiver powered by GNU Radio, supporting RTL-SDR, HackRF, LimeSDR, USRP and more. [SourceForge](https://sourceforge.net/projects/gqrx/).


## Core Network

### 5G

- [Open5GS](https://open5gs.org) `[2025-12]` - 5G, R14 4G EPC core with independent MME, HSS, SGW, PGW, PCRF, UPF, SMF, NRF functions. Follow-up of NextEPC. [github](https://github.com/open5gs)
- [OAI 5GCN](https://gitlab.eurecom.fr/oai/cn5g) - OAI(Open Air Interface) was initially developed by EURECOM, provides a 3GPP-Compliant 5G SA Core Network.
- ⚠️ [travelping-vpp](https://github.com/travelping/vpp) `[2021-01]` - UPF plugins implements a GTP-U user plane based on 3GPP TS 23.214 and 3GPP TS 29.244 Release 15, adding UPF as a plugin to VPP.
- ⚠️ [IITB 5G SBA PoC](https://github.com/iithnewslab/SBA-gRPC-5G) `[2019-08]` - Prototyping and Load Balancing the Service Based Architecture of 5G Core using NFV - [research paper from IITB](https://github.com/iithnewslab/SBA-gRPC-5G/blob/master/Presentation_Netsoft19_gRPC_5G.pdf)
- [Free5GC](https://www.free5gc.org/) `[2026-03]` - The free5GC is an open-source project for 5th generation (5G) mobile core network hosted by [CS Lab](https://cslab.cs.nycu.edu.tw/). Written in Golang. Associated github projects: [PER parser/encoder](https://github.com/free5gc/aper), [AMF](https://github.com/free5gc/amf).
- [5GC Swagger APIS](https://github.com/jdegre/5GC_APIs) `[2024-06]` - RESTful APIs of main Network Functions in the 3GPP 5G Core Network. R16.
- [5G GTP kernel driver](https://github.com/free5gc/gtp5g) `[2026-03]` - gtp5g is a customized Linux kernel module 5G GTP-U to handle packet by PFCP IEs such as PDR and FAR. Per 3GPP TS 29.281 and 3GPP TS 29.244.
- [UPF (OMEC)](https://github.com/omec-project/upf) `[2026-03]` - 4G/5G Mobile Core User Plane from the OMEC/SD-Core project. Successor to upf-epc.
- [OpenUPF](https://github.com/5GOpenUPF/openupf) `[2021-05]` - A 3GPP R16 compliant open source 5G core UPF (User Plane Function).
- [Katana Slice Manager](https://github.com/medianetlab/katana-slice_manager) `[2026-03]` - Katana Slice Manager is a central software component responsible for controlling all the devices comprising the network, providing an interface for creating, modifying, monitoring and deleting slices.
- [my5G-core](https://github.com/my5G/my5G-core) `[2021-01]` - Currently, my5G-core is a fork of the free5GC project, with some extensions to facilitate the deployment.
- [III-5GC-Free-Trial](https://github.com/III-5GC/III-5GC-Free-Trial) `[2021-05]` - The basic III-5GC is a free trial for lab research, prototype product testing and simple 5G end-to-end demonstration.
- [upf-bpf](https://github.com/navarrothiago/upf-bpf) `[2024-09]` - An open source C++ library powered by eBPF/XDP for user plane in mobile core network (5G/LTE).
- [5G_CN](https://github.com/wnlUc3m/5G_CN) `[2019-08]` - This is a basic implementation of a 5G Core Network supporting 4G LTE control signalling.
- [openupf](https://github.com/5GOpenUPF/openupf) `[2021-05]` - A 3GPP R16 compliant open source 5G core UPF (User Plane Function).
- [upf-xdp](https://github.com/801room/upf-xdp) `[2021-01]` -  it shows the possibility of using xdp to implement 5g upf.
- [SD-Core](https://opennetworking.org/sd-core/) - A 4G/5G core that is based on [OMEC](https://www.opennetworking.org/omec/) for 4G, and a fork of [Free5GC](https://www.free5gc.org/) for 5G. Has implementations for AMF,SMF,PCF,UDM,AUSF,NSSF and a P4 based UPF. [github](https://github.com/omec-project/amf)
- [Magma](https://github.com/magma/magma) `[2026-03]` - Rearchitected core network with access gateway (MME+P/SGW), federation gateway for auth (S6a) and billing (Gx, Gy). Initiated by FB on a the OAI EPC code base.
- ⚠️ [5GCoreNetSDK](https://github.com/5GCoreNet/5GCoreNetSDK) `[2023-06]` - 5GCoreNetSDK is a fully-featured Golang SDK for developing inside 5GC (Release-18).
- [eupf](https://github.com/edgecomllc/eupf) `[2026-02]` - Open Source UPF built on eBPF.
- [UPG-VPP](https://github.com/travelping/upg-vpp) `[2026-03]` - High-performance User Plane Gateway (UPG) based on FD.io VPP from Travelping.
- [qcore](https://github.com/nplrkn/qcore) `[2026-03]` - The world's most lightweight 5G Core (probably)
- [NEF_emulator](https://github.com/medianetlab/NEF_emulator) `[2025-02]` - Configurable emulated environment for providing 3GPP Network Exposure Function (NEF) APIs. Enables testing of network applications against 5GC exposure capabilities.
- [Ella Core](https://github.com/ellanetworks/core) `[2026-03]` - Lightweight 5G core for private networks. Single binary with embedded DB, web UI, REST API, and OpenTelemetry. Written in Go.
- [UnifyAir Core](https://github.com/unifyair/unifyair-core) `[2025-11]` - 5G Core Network Functions (AMF, UPF, SMF) implementation in Rust, based on 3GPP Release 17.
- [HEXAeBPF](https://github.com/coranlabs/HEXAeBPF) `[2025-10]` - eBPF-defined interoperable 5G Core (eDC).
- [NextMN-UPF](https://github.com/nextmn/UPF) `[2026-03]` - Experimental user-space 5G UPF in Go. Interoperable with free5GC and UERANSIM.
- [go-upf](https://github.com/free5gc/go-upf) `[2026-03]` - Go-based UPF implementation for free5GC.
- [SigScale CHF](https://github.com/sigscale/chf) `[2025-10]` - 3GPP 5GC Charging Function (CHF) in Erlang. Part of the SigScale telecom stack.
- [QORE](https://github.com/coranlabs/QORE) `[2025-11]` - Quantum Secure Core: Beyond 5G Core integrated with Post-Quantum Cryptography and QRNG. From CoRAN Labs.
- ⚠️ [SEPP](https://github.com/ellanetworks/sepp) `[2025-08]` - Open source 5G Security Edge Protection Proxy. From Ella Networks.
- [free5gc n3iwue](https://github.com/free5gc/n3iwue) `[2026-01]` - N3IWF UE simulator for non-3GPP access testing. From the free5GC project.
- [upf_p4_poc](https://github.com/801room/upf_p4_poc) `[2026-03]` - Proof of concept for 5G UPF based on P4 programmable data plane. From the upf-xdp author.
- [NWDAF](https://github.com/net-ty/mnc_NWDAF) `[2026-02]` - Network Data Analytics Function (NWDAF) implementation in Go.
- [OAI CN5G NWDAF](https://gitlab.eurecom.fr/oai/cn5g/oai-cn5g-nwdaf) - OpenAirInterface NWDAF with AnLF and MTLF separation per 3GPP Release 17. Hosted on **GitLab (Eurecom)**.
- [closed-loop-nwdaf](https://github.com/fatemeshafiee/closed-loop-nwdaf) `[2025-12]` - NWDAF integrated with OAI and Open5GS for closed-loop security automation. ML model provisioning via MLflow.
- [OAI CN5G LMF](https://gitlab.eurecom.fr/oai/cn5g/oai-cn5g-lmf) - OpenAirInterface Location Management Function for 5G positioning (UL-TDoA). Hosted on **GitLab (Eurecom)**.
- [nokia 5G Network Emulator](https://github.com/nokia/5g-network-emulator) `[2026-02]` - 5G network emulator from Nokia.
- [SD-Core Helm Charts](https://github.com/omec-project/sdcore-helm-charts) `[2026-04]` - Official Helm charts for packaging and deploying the SD-Core 5G core (Aether/OMEC).
- [UE-non3GPP](https://github.com/LABORA-INF-UFG/UE-non3GPP) `[2025-02]` - Open-source User Equipment for non-3GPP access via N3IWF. Useful for testing 5G core untrusted/trusted Wi-Fi access flows.
- [opncell](https://github.com/opncell/opncell) `[2026-02]` - OPNsense plugin that adds private 5G/LTE network capability out-of-the-box by integrating Open5GS with the OPNsense firewall.
- [OAI CN5G AMF](https://gitlab.eurecom.fr/oai/cn5g/oai-cn5g-amf) - OpenAirInterface 5G Access and Mobility Management Function (AMF). Active C++ implementation, Apache 2.0. Hosted on **GitLab (Eurecom)**. Companion NFs: [SMF](https://gitlab.eurecom.fr/oai/cn5g/oai-cn5g-smf), [UPF](https://gitlab.eurecom.fr/oai/cn5g/oai-cn5g-upf), [NRF](https://gitlab.eurecom.fr/oai/cn5g/oai-cn5g-nrf), [AUSF](https://gitlab.eurecom.fr/oai/cn5g/oai-cn5g-ausf), [UDM](https://gitlab.eurecom.fr/oai/cn5g/oai-cn5g-udm), [UDR](https://gitlab.eurecom.fr/oai/cn5g/oai-cn5g-udr), [PCF](https://gitlab.eurecom.fr/oai/cn5g/oai-cn5g-pcf), [NSSF](https://gitlab.eurecom.fr/oai/cn5g/oai-cn5g-nssf), [NEF](https://gitlab.eurecom.fr/oai/cn5g/oai-cn5g-nef).

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
- [gtp-guard](https://github.com/acassen/gtp-guard) `[2026-03]` - The main goal of this project is to provide robust and secure extensions to GTP protocol (GPRS Tunneling Protocol).
- [osmo-s1gw](https://gitea.osmocom.org/erlang/osmo-s1gw) - S1AP gateway/proxy in Erlang for 4G LTE. Bridges eNB-facing and CN-facing IP networks. Hosted on **Osmocom Gitea**.
- [osmo-upf](https://gitea.osmocom.org/cellular-infrastructure/osmo-upf) - Osmocom UPF (User Plane Function) in C with PFCP session management. Hosted on **Osmocom Gitea**.

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

### OSS/BSS

- [Sigscale OCS](https://github.com/sigscale/ocs) `[2026-03]` - SigScale OCS includes a 3GPP AAA server function for authentication, authorization and accounting (AAA) of subscribers using DIAMETER or RADIUS protocols.
- [Bodastage CE](https://gitlab.com/bts-ce/bts-ce) `[2019-05]` - Boda Telecom Suite - Community Edition (BTS-CE) is an open source vendor-agnostic telecommunication network management platform. Hosted on **GitLab**.
- [CGRateS](https://github.com/cgrates/cgrates) `[2026-03]` - Real-time Charging System for Telecom & ISP environments. Cloud-ready micro-services with CDR mediation, LCR, fraud detection and multi-tenant support.
- [BillRun](https://github.com/BillRun/system) `[2026-03]` - Open source Telecom BSS: CDR mediation, real-time OCS, rating/charging (prepaid, postpaid, roaming, wholesale), and fraud detection.
- [SigScale CGF](https://github.com/sigscale/cgf) `[2025-08]` - 3GPP Charging Gateway Function (CGF) in Erlang. Part of the SigScale telecom stack.
- [SigScale HSS](https://github.com/sigscale/hss) `[2025-12]` - 3GPP Home Subscriber Server (HSS) in Erlang. Part of the SigScale telecom stack.
- [Kuwaiba](https://sourceforge.net/projects/kuwaiba/) - Enterprise-grade open source network inventory and CMDB for telecom. Supports 5G, GPON, SDH, MPLS topologies. Hosted on **SourceForge**.
- [Nokia OSSMediator](https://github.com/nokia/OSSMediator) `[2026-02]` - OSS Mediator for telecom network management. From Nokia.
- [free5gc cdrFileParser](https://github.com/free5gc/cdrFileParser) `[2025-05]` - TS 32.297 CDR file decoder CLI. From the free5GC project.
- [OpenCDRRate](https://sourceforge.net/p/opencdrrate/home/Home/) - Scalable CDR rating, taxation and invoicing system for telecom/VoIP. Hosted on **SourceForge**.
- [jBilling](https://sourceforge.net/projects/jbilling/) - Open source enterprise billing system in Java with CDR mediation module for telecom. Hosted on **SourceForge**.

## Interconnect

### SBC, IMS

- [Freeswitch](https://freeswitch.org/confluence/display/FREESWITCH/Python_SBC) - Popular SIP stack that could be used as Session Border Controller (SBC)
- [IMS Clearwater](http://www.projectclearwater.org) - Clearwater is an open source implementation of IMS (the IP Multimedia Subsystem).
- [Kamailio](https://www.kamailio.org) - SIP stack used for VoLTE and SBC.
- [go-eventsocket](https://github.com/fiorix/go-eventsocket) `[2024-09]` - FreeSWITCH Event Socket library for the Go programming language.
- [Asterisk](https://github.com/asterisk/asterisk) `[2026-03]` - The most widely deployed open-source PBX and telephony engine. SIP, PJSIP, WebRTC, conferencing, and IVR.
- [PJSIP](https://github.com/pjsip/pjproject) `[2026-03]` - Free and open-source multimedia communication library implementing SIP, SDP, RTP, STUN, TURN, and ICE. Foundation for many VoIP/IMS clients.
- [HOMER](https://github.com/sipcapture/homer) `[2026-02]` - 100% Open-Source SIP/VoIP/RTC packet capture and monitoring platform. Essential for VoLTE/VoWiFi troubleshooting.
- [Routr](https://github.com/fonoster/routr) `[2026-03]` - A programmable, cloud-native SIP server for building modern telephony systems.
- [OpenSIPS](https://opensips.org/) - GPL multi-functional SIP server: proxy, registrar, load balancer, SBC, NAT traversal. Former OpenSER. [SourceForge (legacy)](https://sourceforge.net/projects/opensips/) / [GitHub](https://github.com/OpenSIPS/opensips).
- [OpenIMSs](https://github.com/VoicenterTeam/openimss) `[2023-10]` - Open source environment for real-life development of IMS-based 4G/5G/NR voice/video/data/RCS services. Extends docker_open5gs.
- [FusionPBX](https://www.fusionpbx.com/) - Multi-tenant PBX and voice switch for FreeSWITCH with IVR, call center, provisioning and more. [SourceForge](https://sourceforge.net/directory/pbx/).
- [DjangoPBX](https://codeberg.org/DjangoPBX/DjangoPBX) `[2026-02]` - Full-featured domain-based multi-tenant PBX driven by Django and FreeSWITCH with REST API, call center, and provisioning. Hosted on **Codeberg**.
- [Sofia-SIP](https://github.com/freeswitch/sofia-sip) `[2026-03]` - Open-source SIP User-Agent library (RFC3261 compliant) maintained by FreeSWITCH. Originally from Nokia Research Center.
- [OpalVOIP](https://sourceforge.net/projects/opalvoip/) - C++ multi-platform VoIP library supporting H.323, SIP, and IAX2. Used by Ekiga softphone. Hosted on **SourceForge**.
- [OpenSIPS IMS CE](https://github.com/OpenSIPS/opensips-ims-ce) `[2025-03]` - IMS CSCF (P-CSCF, I-CSCF, S-CSCF) compliant with 3GPP TS 124 228 for VoLTE. Docker-based, designed to work on top of Open5GS.
- [rtpengine](https://github.com/sipwise/rtpengine) `[2026-04]` - Kernel-assisted high-performance RTP/RTCP media proxy for Kamailio, OpenSIPS and other SIP proxies. Handles transcoding, recording, DTLS-SRTP. From Sipwise.
- [sipgo](https://github.com/emiago/sipgo) `[2026-04]` - SIP library for building fast SIP services in Go. Full RFC3261 stack with transport, transaction and dialog layers.
- [LibreSBC](https://github.com/hnimminh/libresbc) `[2026-04]` - Open source Session Border Controller built on FreeSWITCH. Multi-tenant, clustering, REST API, WebUI.
- [drachtio-server](https://github.com/drachtio/drachtio-server) `[2026-04]` - SIP call processing server controllable via Node.js. Companion [signaling resource framework](https://github.com/drachtio/drachtio-srf). Used for building telephony apps.
- [Sippy B2BUA](https://github.com/sippy/b2bua) `[2026-04]` - RFC3261-compliant SIP Back-to-Back User Agent in Python. Works with RTPproxy, OpenSIPS, Kamailio. Go port: [go-b2bua](https://github.com/sippy/go-b2bua).
- [Restcomm Media Server](https://github.com/RestComm/media-core) `[2026-03]` - Java media server for real-time communications. SIP-based conferencing, IVR, transcoding and announcements.
- [Kamailio IMS Config](https://github.com/herlesupreeth/Kamailio_IMS_Config) `[2026-04]` - Fixed Kamailio IMS configuration files for basic VoLTE calling. Companion to docker_open5gs.
- [DVRTC](https://github.com/EnableSecurity/DVRTC) `[2026-04]` - Damn Vulnerable Real-Time Communications: intentionally vulnerable VoIP/WebRTC platform for security training (SIP, RTP, TURN). From the SIPVicious team.
- [libsrtp](https://github.com/cisco/libsrtp) `[2026-04]` - Reference open-source SRTP/SRTCP library originally from Cisco, widely used in WebRTC, SIP and IMS media stacks.
- [FHoSS (maintained fork)](https://github.com/herlesupreeth/FHoSS) `[2026-04]` - Maintained fork of OpenIMSCore's FHoSS HSS with bug-fixes and added VoLTE/VoWiFi features.
- [aringo](https://github.com/cgrates/aringo) `[2026-03]` - Asterisk ARI connector in Go, maintained by the CGRateS team. Useful glue for integrating Asterisk with rating/CDR pipelines.
- [beswitched](https://codeberg.org/tychosoft/beswitched) `[2026-04]` - eXosip-based SIP key-system/softswitch by David Sugar (GNU Bayonne author) targeting residential and small-office deployments. C++20, AGPLv3. Hosted on **Codeberg**.

### SS7

- [Restcomm SS7](https://github.com/restcomm/jss7) `[2024-06]` - Open Source Java SS7 stack that allows Java apps to communicate with legacy SS7 communications equipment.
- [Restcomm USSD Gateway](https://github.com/RestComm/ussdgateway) `[2026-03]` - Open source USSD Gateway based on Restcomm jSS7 stack. MAP-based USSD services over SS7/SIGTRAN.
- [SigFW](https://github.com/P1sec/SigFW) `[2024-10]` - Open Source Signaling Firewall for SS7, Diameter filtering, antispoof and antisniff.
- [yate](https://github.com/yatevoip/yate) `[2026-03]` - Open Source Telephony engine with support of MTP2/MTP3 over TDM, M2PA, M2UA, M3UA, SCCP, TCAP

### SMPP / SMS Gateways

- [go-smpp](https://github.com/fiorix/go-smpp) `[2022-11]` - This is an implementation of SMPP 3.4 for Go, based on the original smpp34 from Kevin Patel.
- [Selenium SMPPSim](http://www.seleniumsoftware.com/downloads.html) - (software disappeared) - possible mirror [here](https://github.com/haifzhan/SMPPSim).
- [smppgui](https://github.com/ukarim/smppgui) `[2025-07]` - SMPP gui client
- [Kannel](https://www.kannel.org/) - Compact and powerful open source WAP and SMS gateway, used globally for SMS delivery at scale. [SourceForge](https://sourceforge.net/projects/kannelrelease/).
- [Jasmin SMS Gateway](https://github.com/jookies/jasmin) `[2024-06]` - Open source SMS gateway in Python/Twisted with SMPP and HTTP APIs, message routing/filtering, and real-time billing.
- [Kamex](https://github.com/vaska94/Kamex) `[2026-01]` - Modernized fork of Kannel with WAP removed. 16,000+ msg/sec, SMPP 3.3/3.4/5.0, EMI/UCP, HTTP, Prometheus metrics, Kubernetes health checks.

## Satellite Communication
- [Hughes_OneWeb_Monitor](https://github.com/nickvsnetworking/Hughes_OneWeb_Monitor) `[2025-04]` - Hughes OneWeb Terminal Prometheus Exporter
- [SatNOGS](https://gitlab.com/librespacefoundation/satnogs) - Open Source Global Satellite Ground Station Network focused on LEO satellites, from the Libre Space Foundation. Hosted on **GitLab**.
- [gr-leo](https://gitlab.com/librespacefoundation/gr-leo) `[2025-10]` - GNU Radio Out-of-Tree module simulating the telecommunication channel between orbiting satellites and ground stations, from Libre Space Foundation / ESA SDR Makerspace. Hosted on **GitLab**.
- [OpenSN](https://github.com/OpenSN-Library/OpenSN-Library) `[2026-01]` - Open source library for emulating LEO satellite networks. Container-based, 5-10x faster than StarryNet.
- [Satellite-Open-Source](https://github.com/jwwthu/Satellite-Open-Source) `[2026-03]` - Curated collection of open source code and data for satellite communication research.
- [Hypatia](https://github.com/snkas/hypatia) `[2024-05]` - LEO satellite network simulation framework with ns-3 packet-level simulation and CesiumJS visualization. Supports Starlink and Kuiper constellations. Published at ACM IMC 2020.
- [LEOViz](https://github.com/clarkzjw/LEOViz) `[2026-01]` - LEO satellite constellation measurement and visualization tool for Starlink/OneWeb. Grafana/CesiumJS integration. From University of Victoria.
- [GNSS-SDR](https://sourceforge.net/projects/gnss-sdr/) - Open source software-defined GNSS (Global Navigation Satellite Systems) receiver written in C++ and based on GNU Radio. Hosted on **SourceForge**.
- [OAI-5G-NR-NTN](https://github.com/ngkore/OAI-5G-NR-NTN) `[2026-04]` - Deployment guide and configurations for OpenAirInterface 5G NR over Non-Terrestrial Networks using RFsimulator with both GEO and LEO satellite scenarios.
- [starlink-grpc-tools](https://github.com/sparky8512/starlink-grpc-tools) `[2026-04]` - De-facto reference Python toolkit for talking to the SpaceX Starlink user terminal's local gRPC API: stats, history, alerts, Prometheus/InfluxDB exporters.
- [starlink_exporter](https://github.com/clarkzjw/starlink_exporter) `[2026-01]` - Self-contained Prometheus exporter and Grafana stack for Starlink dish telemetry. Companion to LEOViz from the same author.
- [LeoHoSim_MATLAB](https://github.com/jtlee-97/LeoHoSim_MATLAB_2024) `[2026-02]` - Time-stepped MATLAB simulator for 5G NTN with a 600 km LEO constellation (per 3GPP TR 38.821) and a hybrid handover mechanism for handheld UEs.
- [sdr-o-ran-platform](https://github.com/thc1006/sdr-o-ran-platform) `[2026-04]` - SDR + cloud-native O-RAN research platform for satellite NTN with AI/ML (DRL) optimization and quantum-safe (NIST PQC) cryptography.

## Protocols

### ASN1-based, S1AP/NGAP

- [Pycrate](https://github.com/pycrate-org/pycrate) `[2025-12]` - A Python library to ease the development of encoders and decoders for various protocols and file formats, especially telecom ones. Provides an ASN.1 compiler and a CSN.1 runtime.
- [pycrate-rs](https://github.com/EFForg/pycrate-rs) `[2025-07]` - Rust telecom protocol parser generated from pycrate. From the EFF (Rayhunter project).
- [bazel-pycrate](https://github.com/ravens/bazel-pycrate) `[2023-07]` - A bazel-based pycrate ready jupyter notebook env
- [hampi](https://github.com/gabhijit/hampi) `[2025-08]` - The Goal of this project is to implement an ASN.1 Compiler in Rust which can generate Rust bindings for different ASN.1 specifications.
- [Eclipse Titan TTCN-3 (core)](https://gitlab.eclipse.org/eclipse/titan/titan.core/) - Open source TTCN-3 compiler and runtime from Ericsson/Eclipse, with built-in ASN.1 BER/PER/XML codecs. Used for telecom protocol conformance testing. Hosted on **GitLab (Eclipse)**.
- [oxirush-ngap](https://github.com/linouxis9/oxirush-ngap) `[2026-04]` - Auto-generated Rust APER codec for 5G NGAP from official 3GPP ASN.1 definitions. Companion to oxirush-nas.

### NAS 4G/5G and Milenage

- [mts-nas](https://github.com/ericsson-mts/mts-nas) `[2023-04]` - Project to decode/encode Non-Access Stratum (NAS) protocol.
- [LTE-security](https://fabricioapps.blogspot.com/2012/05/lte-security.html) - a Windows application that implements all the security procedures for LTE referred in Annex A and Annex B of 3GPP 33.401. Last update in 2020, direct [link](https://www.dropbox.com/s/adpa2yuac99riqt/LTE%20Security%203.3.zip?dl=0)
- [milenage](https://github.com/emakeev/milenage) `[2020-10]` - Go implementation of milenage ciphers.
- [nas-5gs](https://github.com/hzane/nas-5gs) `[2020-02]` - Routines for Non-Access-Stratum (NAS) protocol for NAS-NR(5GS).
- [oxirush-nas](https://github.com/linouxis9/oxirush-nas) `[2025-03]` - A Rust Library that allows the decoding/encoding of NAS-5G messages. From Valentin D'Emmanuele - France.
- [CryptoMobile](https://github.com/P1sec/CryptoMobile) `[2023-01]` - C implementations with Python bindings for mobile network cryptographic algorithms (Milenage, TUAK, Kasumi, SNOW, ZUC). From P1 Security.
- [milenage (Go)](https://github.com/wmnsk/milenage) `[2025-05]` - MILENAGE algorithm implementation in Go for 3G/4G/5G AKA authentication.

### GTP/PFCP

- [Kernel GTP-U](https://osmocom.org/projects/linux-kernel-gtp-u) - This is an implementation of the GTP-U (user plane) inside the Linux kernel.
- [go-gtp](https://github.com/wmnsk/go-gtp) `[2026-03]` - Package gtp provides simple and painless handling of GTP(GPRS Tunneling Protocol), implemented in the Go Programming Language.
- [go-pfcp](https://github.com/wmnsk/go-pfcp) `[2026-01]` - PFCP(Packet Forwarding Control Protocol) is a signaling protocol used in mobile networking infrastructure(LTE EPC, 5GC) to realize CUPS architecture(Control and User Plane Separation, not a printing system) defined in 3GPP TS29.244.
- [gtplib](https://github.com/travelping/gtplib) `[2025-09]` - Erlang GTPv1/GTPv2 library.
- [gtpv2](https://github.com/blorticus/gtpv2) `[2021-09]` - GPRS Tunneling Protocol Library for golang.
- [scapy-gtp](https://github.com/secdev/scapy/blob/master/scapy/contrib/gtp.py) `[2026-03]` - Scapy (A interactive packet manipulation program) GTP layer. Spec: 3GPP TS 29.060 and 3GPP TS 29.274. Some IEs: 3GPP TS 24.008.
- [gtp_dialer](https://github.com/fasferraz/gtp_dialer) `[2025-11]` - GTPv1/GTPv2 Dialer
- [nwGTPv2](https://sourceforge.net/projects/nwgtpv2/) - Free and open source implementation of eGTP (GTPv2) control plane, supporting S11, S5, S8 EPC interfaces. Also provides nwEPC SAE-Gateway framework. Hosted on **SourceForge**.
- [pfcpsim](https://github.com/omec-project/pfcpsim) `[2026-03]` - PFCP client simulator for UPF testing. From the SD-Core/OMEC project.
- [pfcplib](https://github.com/travelping/pfcplib) `[2024-06]` - Erlang library for encoding/decoding PFCP frames per 3GPP TS 29.244. From Travelping.
- [OpenGGSN](https://sourceforge.net/projects/ggsn/) - Open source Gateway GPRS Support Node (GGSN) with SGSN emulator for core network testing. Maintained within Osmocom. Hosted on **SourceForge**.
- [NextMN go-pfcp-networking](https://github.com/nextmn/go-pfcp-networking) `[2026-01]` - PFCP networking functionalities on top of go-pfcp. From the NextMN project.
- [libosmo-pfcp](https://gitea.osmocom.org/osmocom/libosmo-pfcp) - C library for PFCP protocol encoding/decoding and session endpoint management. Hosted on **Osmocom Gitea**.
- [gtp-load-gen](https://gitea.osmocom.org/cellular-infrastructure/gtp-load-gen) - High-performance GTP-U load generator using Linux io_uring. Hosted on **Osmocom Gitea**.
- [gtp-rs](https://github.com/ErvinsK/gtp-rs) `[2025-12]` - Pure Rust implementation of 3GPP GTP (GTPv1 and GTPv2) protocols.
- [free5gc gtp5g-tracer](https://github.com/free5gc/gtp5g-tracer) `[2025-10]` - Debug gtp5g kernel module using eBPF. From the free5GC project.
- [rs-pfcp](https://github.com/xandlom/rs-pfcp) `[2026-04]` - Rust implementation of the PFCP protocol (3GPP TS 29.244), modeled on go-pfcp. Includes an interop test harness against the Go reference.

### SCTP

- [sctp](https://github.com/ishidawataru/sctp) `[2025-11]` - Stream Control Transmission Protocol (SCTP) in Go.
- [usrsctp](https://github.com/sctplab/usrsctp) `[2025-10]` - This is a userland SCTP stack supporting FreeBSD, Linux, Mac OS X and Windows.
- [PySCTP](https://github.com/P1sec/pysctp) `[2026-02]` - PySCTP - SCTP bindings for Python.
- [MTS: Multiprotocol Test Tool](https://github.com/ericsson-mts/mts) `[2023-11]` - MTS (Multi-protocol Test Suite) is a multi-protocol testing tool specially designed for telecom IP-based architectures (see above "Features" section for more details).
- [scapy-sctp](https://github.com/secdev/scapy/blob/master/scapy/layers/sctp.py) `[2026-03]` - Scapy (A interactive packet manipulation program) SCTP layer.
- [ellora](https://github.com/gabhijit/ellora/) `[2023-11]` - Rust SCTP Toolkit. The Goal of this project is to make safe bindings for Linux SCTP stack that can be used within Rust's `async` ecosystem.
- [sctplb](https://github.com/omec-project/sctplb) `[2026-03]` - SCTP Load Balancer for 5G core networks. From the SD-Core/OMEC project.

### VoWiFi/VoLTE

- [SWu-IKEv2](https://github.com/fasferraz/SWu-IKEv2) `[2025-10]` - SWu client emulator in Python that establishes an IKEv2/IPSec tunnel with an ePDG, implementing both control plane (IKEv2) and user plane (IPSec).
- [osmo-epdg](https://gitea.osmocom.org/erlang/osmo-epdg) - Implement an ePDG with an embedded AAA server. osmo-ePDG also requires a modified [strongswan-epdg](https://gitea.osmocom.org/ims-volte-vowifi/strongswan-epdg). Hosted on **Osmocom Gitea**.
- [ims-client](https://gitea.osmocom.org/septs/ims-client) - IMS client with SWu (VoWiFi) protocol in PHP. Hosted on **Osmocom Gitea**.
- [NWu-Non3GPP-5GC](https://github.com/fasferraz/NWu-Non3GPP-5GC) `[2024-09]` - NWu IKEv2/IPSec dialer for 5GC N3IWF (Non-3GPP Interworking Function). From the author of eNB s1 emulator and gtp_dialer.
- [GBA_ME](https://github.com/fasferraz/GBA_ME) `[2023-10]` - Generic Bootstrapping Architecture (GBA) ME emulator in Python. From fasferraz.
- [vowifi-epdg-scanning](https://github.com/sbaresearch/vowifi-epdg-scanning) `[2026-04]` - VoWiFi ePDG scanning toolkit and dataset from SBA Research, used to enumerate and probe operator ePDG endpoints worldwide.
- [vowifi-sms](https://github.com/dmitzsaz/vowifi-sms) `[2025-10]` - Go-based VoWiFi (IMS/ePDG) client capable of registering to a carrier IMS over Wi-Fi and receiving SMS without an active mobile connection.
- [carrier_wifi_http_server](https://github.com/herlesupreeth/carrier_wifi_http_server) `[2026-04]` - Server hosting the carrier certificate used by handsets to encrypt the IMSI when authenticating to WLAN (Hotspot 2.0) and ePDG (VoWiFi).
- [free5gc/ike](https://github.com/free5gc/ike) `[2026-04]` - free5GC's standalone IKEv2 implementation used by N3IWF/TNGF. Reusable as a Go IKE library outside free5GC.


### Diameter

- [go-diameter](https://github.com/fiorix/go-diameter) `[2026-03]` - Package go-diameter is an implementation of the Diameter Base Protocol RFC 6733 and a stack for the Go programming language.
- [jdiameter](https://github.com/RestComm/jdiameter/) `[2024-01]` - RestComm jDiameter provides an Open Source Java implementation of the Diameter standard for Authentication, Authorization, and Accounting (AAA).
- ⚠️ [diafuzzer](https://github.com/Orange-OpenSource/diafuzzer) `[2019-10]` - Diameter fuzzer, based on specifications of Diameter applications following rfc 3588 / 6733 from Orange.
- [bromelia](https://github.com/heimiricmr/bromelia) `[2024-05]` - A Python micro framework for building Diameter protocol applications.
- [freeDiameter](http://www.freediameter.net/) - Open source implementation of the Diameter protocol (RFC 6733). Extensible platform for AAA with modular architecture. Also available on [GitLab (Eurecom)](https://gitlab.eurecom.fr/oai/freediameter).
- [Open Diameter](https://sourceforge.net/projects/diameter/) - Open source C++ implementation of the Diameter protocol, licensed under GPLv2/LGPLv2. Hosted on **SourceForge**.
- [eradius](https://github.com/travelping/eradius) `[2026-03]` - Erlang RADIUS server framework. From Travelping.
- [prometheus_diameter_collector](https://github.com/travelping/prometheus_diameter_collector) `[2024-04]` - Diameter Prometheus.io collector for monitoring Diameter signaling. From Travelping.
- [xk6-diameter](https://github.com/lwlee2608/xk6-diameter) `[2026-03]` - k6 extension for Diameter protocol load testing. Written in Go.
- [diameter-rs](https://github.com/lwlee2608/diameter-rs) `[2025-12]` - Rust implementation of the Diameter Protocol (RFC 6733).
- [SigScale RADIUS](https://github.com/sigscale/radierl) `[2025-02]` - RADIUS protocol stack for Erlang with EAP and DIAMETER transport support. Part of the SigScale telecom stack.

### SS7/SIGTRAN

- [go-m3ua](https://github.com/wmnsk/go-m3ua) `[2026-01]` - Package m3ua provides easy and painless handling of M3UA protocol in pure Golang.
- [go-sccp](https://github.com/wmnsk/go-sccp) `[2025-06]` - Package sccp provides simple and painless handling of SCCP(Signaling Connection Control Part) in SS7/SIGTRAN stack, implemented in the Go Programming Language.
- [libosmo-sccp](https://git.osmocom.org/libosmo-sccp/) - SCCP Library
- [go-tcap](https://github.com/wmnsk/go-tcap) `[2026-01]` - Package tcap provides simple and painless handling of TCAP(Transaction Capabilities Application Part) in SS7/SIGTRAN protocol stack.
- [openss7](http://www.openss7.org/) - An opensource development project (called OpenSS7) to provide a robust and GPL'ed SS7, SIGTRAN, ISDN and VoIP stack for Linux and other UN*X operating systems.
- [Extended jSS7](https://github.com/PAiC-team/Extended-jSS7) `[2023-07]` - Extended Java SS7 stack with MTP2/MTP3, ISUP, SCCP, TCAP, CAMEL (Phase I-IV) and MAP. Supports SIGTRAN (SCTP/M3UA) over IP.
- [signerl](https://gitea.osmocom.org/erlang/signerl/) - Erlang SS7 TCAP/MAP implementation. Originally from Motivity, continued within the Osmocom project. Hosted on **Osmocom Gitea**.
- [SigScale TCAP](https://github.com/sigscale/tcap) `[2025-01]` - SS7 Transaction Capabilities Application Part (TCAP) protocol stack in Erlang, used by MAP and CAP applications in mobile operator networks.
- [SigScale CSE](https://github.com/sigscale/cse) `[2026-03]` - Custom (CAMEL) Service Environment in Erlang. Part of the SigScale SS7 stack.
- [SigScale GTT](https://github.com/sigscale/gtt) `[2026-02]` - Global Title Translation (GTT) in Erlang. Part of the SigScale SS7 stack.
- [SigScale M3UA](https://github.com/sigscale/m3ua) `[2025-02]` - SIGTRAN M3UA protocol stack in Erlang. Part of the SigScale SS7 stack with companion [SCCP](https://github.com/sigscale/sccp), [MAP](https://github.com/sigscale/map), [CAP](https://github.com/sigscale/cap), and [INAP](https://github.com/sigscale/inap) modules.
- [osmo-dia2gsup](https://gitea.osmocom.org/erlang/osmo_dia2gsup) - Diameter-to-GSUP inter-working function in Erlang. Bridges Diameter-based AAA with Osmocom GSUP protocol. Hosted on **Osmocom Gitea**.
- [osmo_cap](https://gitea.osmocom.org/erlang/osmo_cap) - CAMEL Application Part (CAP) implementation in Erlang. Hosted on **Osmocom Gitea**.

### Dataplane acceleration

- [fastswan](https://github.com/acassen/fastswan) `[2026-02]` - Linux Kernel XFRM/IPsec offload via eBPF/XDP. Relevant for mobile core SWu/N3IWF tunnels. From the gtp-guard/keepalived author.
- [xdp-fwd](https://github.com/acassen/xdp-fwd) `[2026-03]` - XDP Forwarding suite for high-performance packet processing via eBPF/XDP. From the gtp-guard/keepalived author.
- [socket-takeover](https://github.com/acassen/socket-takeover) `[2026-04]` - Live socket transfer between processes, engineered for zero-downtime upgrades of dataplane services such as gtp-guard.
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
- [phonenumber-normalizer](https://github.com/telekom/phonenumber-normalizer) `[2026-01]` - Phone number normalization to E.164 and national formats in Go. From Deutsche Telekom.
- [OpenAPI-Dissector](https://github.com/telekom/OpenAPI-Dissector) `[2025-10]` - Experimental Wireshark dissector generator from OpenAPI specs, useful for 5G SBI protocol analysis. From Deutsche Telekom.
- [RTPproxy](https://github.com/sippy/rtpproxy) `[2026-03]` - High-performance RTP stream proxy, works with OpenSIPS, Kamailio, and Sippy B2BUA for VoIP/VoLTE media relay.
- [RLS-wireshark-dissector](https://github.com/nextmn/RLS-wireshark-dissector) `[2026-02]` - Wireshark dissector for the Radio Link Simulation Protocol from UERANSIM. From NextMN.
- [gsmtapv3](https://gitea.osmocom.org/peremen/gsmtapv3) - GSMTAPv3 specification proposal and reference code for next-generation cellular packet capture format. Hosted on **Osmocom Gitea**.
- [osmo-gsm-shark](https://gitea.osmocom.org/nhofmeyr/osmo-gsm-shark) - Network trace tool that summarizes mobile network activity from pcap captures. Hosted on **Osmocom Gitea**.


## Infrastructure

### NFV, Openstack

- [Openstack Kolla](https://github.com/openstack/kolla) `[2026-03]` - Production ready containers and Ansible tools for deploying an Openstack cluster to run NFV functions.
- ⚠️ [SNAPS-openstack](https://github.com/cablelabs/snaps-openstack) `[2021-09]` - Openstack deployment to be used on SNAPS booted machine from Cablelabs.
- [OPNFV](https://www.opnfv.org/software/downloads) - The OPNFV project addresses a number of aspects in the development of a consistent virtualisation platform including common hardware requirements, software architecture, MANO and applications.

### Containers, Kubernetes

- [Kubernetes KubeADM](https://kubernetes.io/docs/reference/setup-tools/kubeadm/kubeadm/) - Deployment tool to create Kubernetes cluster.
- [Intel Multus CNI plugin](https://github.com/intel/multus-cni) `[2026-03]` - Multus CNI is a container network interface (CNI) plugin for Kubernetes that enables attaching multiple network interfaces to pods from Intel.
- [Intel SRVIOV/DPDK CNI plugin](https://github.com/intel/sriov-cni) `[2026-03]` - SR-IOV CNI plugin works with SR-IOV device plugin for VF allocation for a container.
- ⚠️ [Nokia Danm](https://github.com/nokia/danm/) `[2022-09]` - TelCo grade network management in a Kubernetes cluster from Nokia.
- ⚠️ [SNAPS-kubernetes](https://github.com/cablelabs/snaps-kubernetes) `[2021-12]` - Kubernetes deployment to be used on SNAPS booted machine from Cablelabs.
- [Free5GC on kubeCORD](https://github.com/sufuf3/kube5GC) `[2019-05]` - This project is for deploying Free5GC on kubeCORD.
- ⚠️ [CNCF CNF-Testbed](https://github.com/cncf/cnf-testbed) `[2026-03]` - The CNCF CNF Testbed provides reference code and test cases for running networking code on Kubernetes and OpenStack using emerging cloud native technologies in the Telecom domain.
- [towards5gs-helm](https://github.com/Orange-OpenSource/towards5gs-helm) `[2024-10]` - Helm charts for deploying free5GC and other 5G network functions on Kubernetes. From Orange.
- [free5gc-helm](https://github.com/free5gc/free5gc-helm) `[2026-03]` - Official Helm charts for deploying free5GC on Kubernetes.
- [Project Sylva](https://gitlab.com/sylva-projects/sylva) - Production-grade Telco Cloud Stack under Linux Foundation Europe. Common cloud software framework for VNF/CNF, backed by Orange, Deutsche Telekom, Vodafone, Telefonica. Hosted on **GitLab**.
- [aether-cni](https://github.com/omec-project/aether-cni) `[2026-04]` - Container image bundling the Kubernetes CNI plugins used in Aether SD-Core, tuned specifically for UPF in DPDK mode.
- [OAI Helm Chart Catalog](https://gitlab.eurecom.fr/oai/orchestration/charts) - Official Helm chart catalog for deploying OAI 5G Core and RAN network functions on Kubernetes. Hosted on **GitLab (Eurecom)**.

### Baremetal management

- ⚠️ [SNAPS-boot](https://github.com/cablelabs/snaps-boot) `[2019-09]` - Baremetal cluster management solution to prepare for a Openstack or k8s deployment from Cablelabs.
- [MAAS](https://maas.io) - Self-service, remote installation of Windows, CentOS, ESXi and Ubuntu on real servers turns your data center into a bare-metal cloud - Metal As A Service.

## Orchestration

- [5g-sharp-orchestrator](https://github.com/Ethon-Shield/5g-sharp-orchestrator) `[2025-04]` - tool that serves as a comprehensive wrapper for configuring, deploying and monitoring 5G open-source network components, simplifying the orchestration process.
- [ETSI Open Source MANO (OSM)](https://osm.etsi.org/) - ETSI-hosted NFV Management and Orchestration (MANO) stack for multi-cloud Telco orchestration, with network slicing support (eMBB, URLLC, mMTC).
- [Open Baton](https://openbaton.github.io/) - ETSI NFV MANO compliant framework with TOSCA support and network slicing via SDN.
- [Nephio](https://github.com/nephio-project/nephio) `[2026-02]` - Kubernetes-based automation platform for deploying and managing 5G Network Functions and underlying infrastructure. Linux Foundation project.
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
- [Open5GS Docker](https://github.com/herlesupreeth/docker_open5gs) `[2026-03]` - Docker files to build and run open5gs in a docker by Herle Supreeth.
- [Open5gs-K8s-VyOS](https://dev.to/infinitydon/virtual-4g-simulation-using-kubernetes-and-gns3-3b7k) - This tutorial is about how to deploy a virtual 4G stack using GNS3 and Kubernetes.
- [mobile-env](https://github.com/stefanbschneider/mobile-env) `[2026-01]` - An open, minimalist Gym environment for autonomous coordination in wireless mobile networks.
- [OpenAICellular](https://openaicellular.github.io/oaic/quickstart.html) - OAIC is an open-source effort led by a consortium of academic institutions to provide fully open-source software architecture, library, and toolset that encompass both the AI controllers (OAIC-C) as well as an AI testing framework (OAIC-T).
- [sample configs](https://github.com/s5uishida/sample_config_misc_for_mobile_network) `[2026-02]` - Sample Configurations and Miscellaneous for Mobile Network.
- [free5gc-compose](https://github.com/free5gc/free5gc-compose) `[2026-03]` - Docker Compose files for deploying the full free5GC 5G core stack.
- [free5GLabs](https://github.com/free5gc/free5GLabs) `[2026-03]` - Hands-on labs to guide building 5G networks with free5GC.
- [ETSI MEC Sandbox](https://labs.etsi.org/rep/mec/etsi-mec-sandbox) - Interactive environment for learning and experimenting with ETSI MEC service APIs. Hosted on **ETSI Labs**.
- [open5gs-k8s](https://github.com/niloysh/open5gs-k8s) `[2026-03]` - Open5GS 5G Core on Kubernetes with Helm charts and deployment guides.
- [docker-open5gs (Borjis131)](https://github.com/Borjis131/docker-open5gs) `[2025-11]` - Open5GS 5G Core container images with Docker Compose deployments and Helm charts for Kubernetes.
- [oai-cn5g-fed](https://gitlab.eurecom.fr/oai/cn5g/oai-cn5g-fed) - Federation of OAI CN 5G repositories. Docker Compose deployment for the full OAI 5G core. Hosted on **GitLab (Eurecom)**.
- [NextMN testbed](https://github.com/nextmn/testbed) `[2026-03]` - Ready-to-use testbed for the NextMN project with SRv6, UPF, and 5G simulators.
- [free5gc-k8s](https://github.com/niloysh/free5gc-k8s) `[2026-03]` - free5GC 5G Core on Kubernetes with Helm charts and deployment guides.
- [testbed-automator](https://github.com/niloysh/testbed-automator) `[2025-12]` - Scripts for automating deployment of 5G testbeds with Open5GS, free5GC, and UERANSIM.
- [aether-onramp](https://github.com/opennetworkinglab/aether-onramp) `[2026-04]` - Ansible-driven installer for deploying the Aether 5G stack (SD-Core, RAN, monitoring) on bare metal. Official Aether quick-start path.
- [5G-Monarch](https://github.com/niloysh/5g-monarch) `[2026-03]` - Companion repo for the 5G-MoNArch paper on monitoring/observability of cloud-native 5G deployments on Kubernetes.
- [T-5GS](https://github.com/T-5GS/T-5GS) `[2025-12]` - Near-realistic open-source 5G testbed for multi-core network interoperability and multi-tenant scenarios, built on PacketRusher and Open5GS.
- [free5gc/IPTV](https://github.com/free5gc/IPTV) `[2026-01]` - Sample 5G application demonstrating IPTV-style multicast/streaming traffic over a free5GC deployment.
- [OAI Raytracing Channel Emulator](https://gitlab.eurecom.fr/oai/raytracing-channel-emulator) - Ray-tracing-based wireless channel emulator integrated with OpenAirInterface for realistic 5G NR PHY testing. Hosted on **GitLab (Eurecom)**.

### Remote control

- [OpenSTF](https://openstf.io) - Enable remote control of phone over ADB over an HTML5 interfaces.
- [Vyzor](http://vysor.io) - A window to your Android, streaming Android UI through ADB in a Google Chrome Browser app.

### GPS, Time

- ⚠️ [GPS-SDR-SIM](https://github.com/osqzss/gps-sdr-sim) `[2025-01]` - GPS signal generator with a SDR radio and ephemeris files.
- [Tools for MT3339](https://github.com/f5eng/mt3339-utils) `[2023-01]` - Ephemeris injector for MT3339-based GPS chipset

## Testing

- [ntt](https://github.com/nokia/ntt) `[2026-03]` - TTCN-3 test framework.
- [Eclipse Titan TTCN3](https://projects.eclipse.org/projects/tools.titan) - Eclipse Titan is a TTCN-3 compilation and execution environment with an  Eclipse-based IDE.
- [TTCN3vscode](https://github.com/nokia/vscode-ttcn3) `[2026-03]` - TTCN-3 vs code plugin
- [ixia-c](https://github.com/open-traffic-generator/ixia-c) `[2026-03]` - Ixia-c is a modern, powerful and API-driven traffic generator designed to cater to the needs of hyperscalers, network hardware vendors and hobbyists alike.
- [srsRAN_matlab](https://github.com/srsran/srsRAN_matlab) `[2026-01]` - MATLAB-based PHY-layer testing and verification tools for srsRAN. From SRS.
- [Telcometer](https://github.com/itsMohammadHeidari/Telcometer) `[2024-10]` - Diameter Credit-Control Application Load Testing script powered by [Grafana K6](https://github.com/grafana/k6)
- [Sionna](https://github.com/NVlabs/sionna) `[2026-03]` - GPU-accelerated open-source library from NVIDIA for link-level simulation of communication systems. Covers OFDM, MIMO, LDPC, Polar codes, and ray tracing for 5G/6G research.
- [Simu5G](https://simu5g.org/) - OMNeT++ based 5G network simulator for end-to-end performance evaluation.
- [ns-3 LTE/NR](https://gitlab.com/nsnam/ns-3-dev) `[2026-03]` - Discrete-event network simulator with LTE and 5G NR modules. Main development on **GitLab**.
- [5G-LENA](https://gitlab.com/cttc-lena/nr) `[2026-03]` - ns-3 NR module for 5G New Radio simulation (PHY/MAC/OFDMA, MIMO, NR-U, NR V2X). From CTTC OpenSim. [NR-U extension](https://gitlab.com/cttc-lena/nr-u). Hosted on **GitLab**.
- [Wireshark](https://gitlab.com/wireshark/wireshark) `[2026-03]` - Essential protocol analyzer with dissectors for GSMTAP, Diameter, GTP, S1AP, NGAP, SS7/TCAP and more. Main development on **GitLab**.
- [Seagull](https://gull.sourceforge.net/) - Multi-protocol traffic generator for IMS testing: Diameter (RFC3588) over TCP/SCTP, TCAP (over SS7/Sigtran), XCAP, Radius. From HP. [SourceForge](https://sourceforge.net/projects/gull/).
- [ETSI Forge Test Suites](https://forge.etsi.org/rep/explore/projects) - Official ETSI test suites in TTCN-3 and Robot Framework for telecom protocols (Diameter, GTP, S1AP, NAS, MEC, NFV). Hosted on **ETSI Forge (GitLab)**.
- [ETSI 5G Core NAS Test Suite](https://forge.etsi.org/rep/int/5g-core/nas) - Official ETSI INT test suite for 5G NAS conformance testing. Hosted on **ETSI Forge**.
- [ETSI 5G Core NGAP Test Suite](https://forge.etsi.org/rep/int/5g-core/ngap) - Official ETSI INT test suite for NGAP conformance testing on the N2 interface. Hosted on **ETSI Forge**.
- [Nokia Moler](https://github.com/nokia/moler) `[2026-03]` - Python library for building automated tests of network equipment. From Nokia.
- [twampy](https://github.com/nokia/twampy) `[2026-03]` - Python tools for TWAMP and STAMP (Two-Way Active Measurement Protocol) network performance measurement. From Nokia.
- [5g-traffic-generator](https://github.com/niloysh/5g-traffic-generator) `[2025-09]` - Tool for sending GTP-U packets with configurable TEID and QFI values. Useful for exercising UPFs and 5G data-plane setups.
- [CoreNetworkTrafficGenerator](https://github.com/tariromukute/CoreNetworkTrafficGenerator) `[2026-04]` - 5G Core traffic generator emulating gNodeB and UEs (control + user plane), with eBPF/BCC SCTP metrics. Validated against Open5GS, free5GC, and OAI.
- [petrel](https://github.com/lwlee2608/petrel) `[2026-04]` - Diameter load generator from the diameter-rs / xk6-diameter author, focused on high-throughput Diameter benchmarking.
- [seet](https://github.com/fonoster/seet) `[2026-02]` - SIP end-to-end test orchestrator coordinating multiple SIP user-agents for complex multi-leg test scenarios. From Fonoster.
- [sipp-js](https://github.com/fonoster/sipp-js) `[2025-09]` - JavaScript wrapper around SIPp making it easy to script SIP load and conformance tests from Node.js / TypeScript.
- [ETSI INT 5GC NGAP test suite](https://forge.etsi.org/rep/int/5g-core/ngap) - TTCN-3 conformance/interoperability test suite for 3GPP NGAP (N2) from ETSI TC INT. Companion [NAS test suite](https://forge.etsi.org/rep/int/5g-core/nas) and [Emergency Services over 5G IOP](https://forge.etsi.org/rep/int/vx5g/emergency-5g-iop). Hosted on **ETSI Forge (GitLab)**.

## AI & Machine Learning

AI and machine learning tools for telecom networks, covering foundation models, physical layer optimization, network management, and security.

### Telecom LLMs & AI Assistants

- [Eclipse LMOS](https://github.com/eclipse-lmos) `[2026-04]` - Open-source multi-agent AI platform deployed by Deutsche Telekom for Frag Magenta customer service. Eclipse Foundation project.
- [Tele-LLMs](https://github.com/Ali-maatouk/Tele-LLMs) `[2026-03]` - Series of open-source LLMs (1B-8B params) specialized in telecom. Trained on 2.5B tokens from arXiv, 3GPP, Wikipedia. From Yale.
- [Telco-RAG](https://github.com/netop-team/Telco-RAG) `[2024-09]` - RAG framework specialized for 3GPP documents. Addresses challenges of retrieval-augmented generation on highly technical telecom standards.
- [3GPP Expert Skill](https://github.com/lugasia/3gpp-skill) `[2026-04]` - Claude Code skill providing deep 3GPP expertise across all generations (2G–6G), protocol stacks, core network, security, and deployment planning.
- [3GPP MCP Server](https://github.com/edhijlu/3gpp-mcp-server) `[2025-09]` - MCP server enabling AI assistants (Claude, VSCode) to search 3GPP specifications via the TSpec-LLM dataset.
- [TeleQnA](https://github.com/netop-team/TeleQnA) `[2026-04]` - Benchmark dataset (10K multiple-choice questions) for evaluating LLM telecom knowledge. Part of GSMA Open-Telco LLM Benchmarks.
- [Telco-AIX](https://github.com/open-experiments/Telco-AIX) `[2026-04]` - Applied AI experiments for telecom: self-healing networks (AutoNet), MCP-based diagnostic agents, GenAI for NOC.
- [teddi-mcp](https://forge.3gpp.org/rep/reimes/teddi-mcp) - MCP server for ETSI's TEDDI (Terms and Definitions Database Interactive). Search 3GPP/ETSI terms programmatically from AI assistants. Hosted on **3GPP Forge**.
- [MobiLLM](https://github.com/5GSEC/MobiLLM) `[2025-10]` - Domain-specific LLM for cellular security from the 5GSEC group. Trained for analyzing and reasoning about 5G/cellular security incidents and threats.
- [The AI Telco Engineer](https://github.com/NVlabs/the-ai-telco-engineer) `[2026-04]` - NVIDIA Research repo prototyping LLM/agent workflows for telecom engineering tasks (network design, troubleshooting). Companion to NVIDIA's wider AI-RAN push.
- [Chat3GPP](https://github.com/huangl22/Chat3GPP) `[2025-01]` - Open-source RAG framework purpose-built for 3GPP documents, combining hybrid retrieval (BM25 + HNSW + RRF) and BGE-M3 reranking without fine-tuning.
- [telco-network-configuration](https://github.com/bubbleran/telco-network-configuration) `[2025-06]` - Agentic AI workflow blueprint that recommends close-to-optimal RAN parameter configurations at a cell site. Showcases LLM-driven RAN parameter tuning.
- [OpenSlice MCP Server](https://labs.etsi.org/rep/osl/code/org.etsi.osl.mcp.server) - Model Context Protocol server exposing OpenSlice (network-slice / TMF Open API) operations to LLM agents. Hosted on **ETSI Labs**.

See also: [specpilot](#learning-resources) (AI-powered 3GPP spec assistant), [3gpp-crawler](#learning-resources) (3GPP FTP crawler), [GSMA Open-Telco LLM Benchmarks](https://huggingface.co/GSMA) (TeleYAML, TeleLogs, TeleMATH on HuggingFace).

### AI for Physical Layer & RF

- [DeepMIMO](https://github.com/DeepMIMO/DeepMIMO) `[2026-04]` - Ray-tracing dataset toolchain for mmWave and massive MIMO ML research. Python and MATLAB. Also: [DeepMIMO-5GNR](https://github.com/DeepMIMO/DeepMIMO-5GNR).
- [OpenDPD](https://github.com/lab-emi/OpenDPD) `[2026-04]` - PyTorch end-to-end learning framework for power amplifier modeling and digital pre-distortion. pip-installable.
- [HBF-Net](https://github.com/HamedHojatian/HBF-Net) `[2026-04]` - Unsupervised deep learning for massive MIMO hybrid beamforming.
- [deep-learning-channel-estimation](https://github.com/emilbjornson/deep-learning-channel-estimation) `[2026-02]` - Deep learning channel estimation in massive MIMO under hardware non-linearities. IEEE OJCOMS. From Bjornson.
- [TorchSig](https://github.com/TorchDSP/torchsig) `[2026-04]` - PyTorch signal processing ML toolkit. 60+ signal types, pretrained models, modulation families (FSK, QAM, PSK, OFDM).
- [RFML](https://github.com/brysef/rfml) `[2026-04]` - Radio Frequency Machine Learning with PyTorch. Automatic modulation classification, DeepSig dataset loaders, adversarial training.
- [on-device-ai-comm](https://github.com/abman23/on-device-ai-comm) `[2026-04]` - On-device AI/LLM communication system integrating a pre-trained LLM with 5G-NR PHY over 3GPP CDL channels.
- [Sionna RT](https://github.com/NVlabs/sionna-rt) `[2026-04]` - Standalone differentiable ray tracing package extracted from NVIDIA Sionna for ML wireless propagation research.
- [Sionna Large Radio Maps](https://github.com/NVlabs/sionna-large-radio-maps) `[2026-04]` - Large-scale wireless coverage map simulation built on Sionna RT, producing city-scale radio maps for ML training and planning research.
- [SALAD](https://github.com/NVlabs/salad) `[2026-04]` - Self-Adaptive Link Adaptation for wireless communications. ML-based MCS/link adaptation research code from NVIDIA.
- [LibIQ](https://github.com/wineslab/lib-iq) `[2026-03]` - Modular Python library for analyzing, visualizing, and classifying I/Q time-series in wireless systems. From WiNES Lab.
- [DeepBeam](https://github.com/wineslab/deepbeam) `[2026-03]` - Deep waveform learning for coordination-free beam management in mmWave networks (ACM MobiHoc 2021 code). From WiNES Lab.
- [open-cloud-semantic-ran](https://github.com/6G-Cloud-RnE-Open-Hub/open-cloud-semantic-ran) `[2025-09]` - Software implementations of semantic PHY-RAN systems (cloud-native semantic communications RAN). Early 6G research code.
- [Sionna PlutoSDR](https://github.com/rikluost/sionna-PlutoSDR) `[2025-09]` - Adalm PlutoSDR interface for NVIDIA Sionna with full-duplex 1T1R operation on a single SDR. Bridges Sionna research with commodity SDR hardware.
- [OpenGERT](https://github.com/serhatadik/OpenGERT) `[2025-09]` - Open-source Geometry Extraction tool for Sionna Ray-Tracing including ray-tracing sensitivity analysis. Useful for building 3D scenes for Sionna RT.
- [CASTRO-5G](https://codeberg.org/gomezcuba/CASTRO-5G) `[2026-04]` - Python toolkit (Univ. Vigo) for sparse multipath 5G channel simulation, compressed-sensing channel estimation, mmWave link adaptation and ISAC location signal processing. GPLv3. Hosted on **Codeberg**.

### O-RAN AI/ML

- [O-RAN SC AIMLFW](https://docs.o-ran-sc.org/projects/o-ran-sc-aiml-fw-aiml-dashboard/en/latest/) - Modular ML pipeline for O-RAN: feature extraction, model training, storage and serving via Kubeflow/KServe. Hosted on **O-RAN SC Gerrit**.
- [O-RAN SC RIC ML xApps](https://wiki.o-ran-sc.org/display/RICAPP) - Suite of ML-based Near-RT RIC xApps: Anomaly Detection (UE classification), QoE Prediction (throughput forecasting), Traffic Steering (ML-informed handover). Hosted on **O-RAN SC Gerrit**.
- [5G-Spector](https://github.com/5GSEC/5G-Spector) `[2024-11]` - O-RAN compliant runtime intrusion detection xApp for L3 (RRC/NAS) cellular attack detection.
- [MobiWatch](https://github.com/5GSEC/MobiWatch) `[2025-08]` - O-RAN xApp using unsupervised deep learning to detect L3 cellular anomalies and attacks.
- [MobiFlow-Auditor](https://github.com/5GSEC/MobiFlow-Auditor) `[2026-01]` - O-RAN compliant xApp providing fine-grained, security-aware statistics monitoring over 5G RAN and UEs. Telemetry source for the MobiWatch detection xApp.
- [MobieXpert](https://github.com/5GSEC/MobieXpert) `[2026-01]` - First signature-based L3 cellular attack-detection xApp for O-RAN, complementing the deep-learning MobiWatch.
- [oai-anomaly-detection](https://github.com/teo-tsou/oai-anomaly-detection) `[2025-05]` - AI/ML framework for 5G anomaly detection plus closed-loop RB allocation and UE connectivity management on OpenAirInterface and FlexRIC.
- [MalO-RAN](https://github.com/wineslab/mal-o-ran) `[2026-03]` - Framework for evaluating data poisoning attacks on O-RAN AI-based xApps. From WiNES Lab.
- [ns-O-RAN-Gym](https://github.com/wineslab/ns-o-ran-gym) - Gymnasium-based RL environment for O-RAN with Traffic Steering and Energy Saving scenarios. From WiNES Lab.

### Network Optimization & Slicing

- [DeepCoMP](https://github.com/CN-UPB/DeepCoMP) `[2026-04]` - Dynamic multi-cell selection for cooperative multipoint (CoMP) using multi-agent deep RL.
- [Network Slicing Gym](https://github.com/jjalcaraz-upct/network-slicing) `[2026-03]` - OpenAI Gym environment for network slicing with model-based RL agent. Compatible with Stable-Baselines.
- [DeepNetSlice](https://github.com/AlexPasqua/DeepNetSlice) `[2026-02]` - RL tool for network slice placement (VNF placement). PyTorch + Stable-Baselines3. IEEE ICMLCN 2024.
- [DRL-GNN](https://github.com/knowledgedefinednetworking/DRL-GNN) - Combined DRL + GNN architecture for network routing optimization. Generalizes over arbitrary topologies.
- [RouteNet](https://github.com/knowledgedefinednetworking/demo-routenet) `[2026-03]` - GNN architecture for network performance modeling (delay, jitter, loss prediction). ACM SIGCOMM'19. See also [RouteNet-Fermi](https://github.com/BNN-UPC/RouteNet-Fermi).

### Simulation & RL Environments

- [ns3-gym](https://github.com/tkn-tub/ns3-gym) `[2026-02]` - OpenAI Gym integration with ns-3 for RL in networking research.
- [ns3-ai](https://github.com/hust-diangroup/ns3-ai) - Python-C++ bridge enabling AI frameworks (TensorFlow, PyTorch) to interact with ns-3 simulations.
- [RFRL Gym](https://github.com/vtnsi/rfrl-gym) `[2026-03]` - RL training environment for wireless communications: dynamic spectrum access, jamming scenarios.
- [ns3sionna](https://github.com/tkn-tub/ns3sionna) `[2026-03]` - ns-3 module bringing realistic Sionna ray-tracing channel simulation to ns-3.
- [ns-O-RAN-ns3-mmwave](https://github.com/wineslab/ns-o-ran-ns3-mmwave) `[2026-04]` - ns-O-RAN integration with the ns-3 mmWave module providing O-RAN E2 simulation on top of mmWave 5G/NR scenarios. From WiNES Lab.

### Datasets & Benchmarks

- [5GMdata](https://github.com/lasseufpa/5gm-data) `[2026-04]` - Datasets and code for ML in 5G mmWave MIMO systems involving mobility.
- [ColO-RAN Dataset](https://github.com/wineslab/colosseum-oran-coloran-dataset) - Open dataset for ML-based xApps in O-RAN closed-loop control. DRL-based RAN slicing/scheduling. From WiNES Lab / IEEE TMC.
- [NetworkModelingDatasets](https://github.com/BNN-UPC/NetworkModelingDatasets) `[2026-03]` - Datasets for network modeling simulated with OMNet++. Companion to the RouteNet family.
- [TelecomTS](https://github.com/Ali-maatouk/TelecomTS) `[2026-04]` - Multi-modal telecom dataset from the Tele-LLMs team.
- [MM-TelcoBench](https://github.com/gagan-iitb/MM-TelcoBench) `[2025-11]` - Multimodal telecom benchmark for LLM evaluation: network operations, troubleshooting, PCAP analysis, 5G faults.
- [RANalyzer Dataset](https://github.com/wineslab/RANalyzer-Dataset) `[2026-04]` - End-to-end 5G performance measurement dataset useful for training and evaluating performance-prediction models. From WiNES Lab.
- [BostonTwin](https://github.com/wineslab/boston_twin) `[2026-04]` - Digital-twin dataset and API of Boston for ray-tracing-based wireless coverage and network simulation research. From WiNES Lab.
- [Colosseum O-RAN ComMag Dataset](https://github.com/wineslab/colosseum-oran-commag-dataset) `[2026-03]` - Dataset for the IEEE ComMag paper "Intelligence and Learning in O-RAN for Data-driven NextG Cellular Networks" from WiNES Lab.
- [5GDatasets](https://github.com/DLTeamTUC/5GDatasets) `[2025-07]` - Public 5G security datasets (PCAPs, CSVs, AMF logs) covering flooding, fuzzing and replay attacks against control- and user-plane. Generated on Open5GS, OAI, and Amarisoft cores.

---

## Security

### Security Exploitation/fuzzing Frameworks

- ⚠️ [SigPloit](https://github.com/SigPloiter/SigPloit) `[2019-12]` - Telecom Signaling Exploitation Framework - SS7, GTP, Diameter & SIP.
- [5GC_API_parse](https://github.com/PentHertz/5GC_API_parse) `[2021-07]` - 5GC API parse is a BurpSuite extension allowing to assess 5G core network functions, by parsing the OpenAPI 3.0 not supported by previous OpenAPI extension in Burp, and generating requests for intrusion tests purposes.
- [FirmWire](https://github.com/FirmWire/FirmWire) `[2026-01]` - FirmWire is a full-system baseband firmware emulation platform for fuzzing, debugging, and root-cause analysis of smartphone baseband firmwares.
- [5Ghoul](https://github.com/asset-group/5ghoul-5g-nr-attacks) `[2026-03]` - 5G NR attack and fuzzing framework targeting Qualcomm and MediaTek 5G baseband implementations.
- [hexagon_fuzz](https://github.com/srlabs/hexagon_fuzz) `[2025-10]` - A fuzzing framework for Qualcomm Hexagon baseband firmware using QEMU system emulation, from SRLabs.
- [SIPVicious](https://github.com/EnableSecurity/sipvicious) `[2026-03]` - SIP/VoIP security testing toolset for auditing SIP-based VoIP systems.
- [SIMurai](https://github.com/tomasz-lisowski/simurai) `[2024-08]` - SIM card fuzzer and security research tool (USENIX Security 2024). From the author of swSIM/swICC.
- [SentryPeer](https://github.com/SentryPeer/SentryPeer) `[2026-03]` - SIP honeypot for detecting and preventing VoIP fraud with peer-to-peer threat intelligence sharing. Also on [Codeberg](https://codeberg.org/SentryPeer/SentryPeer).
- [Sni5Gect](https://github.com/asset-group/Sni5Gect-5GNR-sniffing-and-exploitation) `[2026-03]` - 5G NR sniffer and downlink injector framework with Wireshark support. From the 5Ghoul team.
- [LLFuzz](https://github.com/SysSec-KAIST/LLFuzz) `[2026-03]` - Over-the-air dynamic testing framework for cellular baseband lower layers (PDCP, RLC, MAC, PHY). Found 11 unknown memory corruptions. USENIX Security 2025. From KAIST.
- [CITesting](https://github.com/SysSec-KAIST/CITesting) `[2025-10]` - Systematic testing of context integrity violations in LTE core networks. ACM CCS '25 Distinguished Paper. From KAIST.
- [BaseBridge](https://github.com/FirmWire/BaseBridge) `[2025-05]` - FirmWire extension that bridges emulation and over-the-air testing by restoring connection state from physical phone memory dumps. Up to 5x fuzzing coverage boost.
- [ShannonLoader](https://github.com/FirmWire/ShannonLoader) `[2026-01]` - Ghidra plugin for reverse engineering Samsung Shannon baseband firmware.
- [5G_ciphered_NAS_decipher_tool](https://github.com/PentHertz/5G_ciphered_NAS_decipher_tool) `[2025-11]` - Python tool to decipher 5G ciphered NAS messages and export to Wireshark pcap. From PentHertz.
- [gea-implementation](https://github.com/P1sec/gea-implementation) `[2026-02]` - GEA-1 and GEA-2 (GPRS Encryption Algorithm) stream cipher implementations in C, Python, and Rust. From P1 Security.
- [BaseSpec](https://github.com/SysSec-KAIST/BaseSpec) `[2021-03]` - Comparing cellular L3 protocol messages between 3GPP spec documents and baseband firmware implementations. From the LTESniffer team at KAIST.
- [DoLTEst](https://github.com/SysSec-KAIST/DoLTEst) `[2022-08]` - Negative testing framework for finding non-standard-compliant bugs in LTE protocol implementations of UEs. From KAIST.
- [Mirage](https://github.com/PentHertz/mirage) `[2025-04]` - Powerful and modular framework for security analysis of wireless communications (Bluetooth, Wi-Fi, Zigbee, and more). From PentHertz.
- [WatchingTheWatchers](https://github.com/SysSec-KAIST/WatchingTheWatchers) `[2024-03]` - Tools for video identification on LTE networks. From KAIST.
- [FISSURE](https://sourceforge.net/projects/fissure.mirror/) - RF and reverse engineering framework for signal intelligence, protocol analysis, and attack detection. Hosted on **SourceForge**.
- ⚠️ [Daedalus](https://github.com/IQTLabs/Daedalus) `[2024-05]` - Defensive response options for securing a 5G core network. From IQT Labs.
- [blue-merle](https://github.com/srlabs/blue-merle) `[2025-06]` - Enhances anonymity and reduces forensic traceability of 4G mobile Wi-Fi routers (IMEI change, MAC randomization). From SRLabs.
- [5GC_API_Pentest](https://github.com/PentHertz/5GC_API_Pentest) `[2025-12]` - Burp Suite extension for 5G Core SBI security testing with automated NF discovery, IMSI enumeration, OAuth2 workflows, and OpenAPI fuzzing. Successor to 5GC_API_parse. From PentHertz.
- [shannon_modem_loader](https://github.com/alexander-pick/shannon_modem_loader) `[2026-02]` - Samsung Exynos/Shannon baseband firmware loader for IDA Pro 8.x/9.x. Enables reverse engineering of Shannon modem firmware.
- [URH-NG](https://github.com/PentHertz/urh-ng) `[2026-04]` - Universal Radio Hacker Next Generation. Investigate wireless protocols, demodulate/decode signals, and analyze RF communications. Successor to URH. From PentHertz.
- [sigover_gen_sample](https://github.com/SysSec-KAIST/sigover_gen_sample) `[2025-09]` - Signal overshadowing sample generator for LTE broadcast signals. Companion to sigover_injector. From KAIST.
- [5GBaseChecker](https://github.com/SyNSec-den/5GBaseChecker) `[2025-01]` - Differential-testing security analysis framework for the control plane of 5G basebands. Evaluated on 17 commercial 5G basebands and 2 open-source UEs; uncovered 22 issues. USENIX Security '24.
- [py5sig](https://github.com/ANSSI-FR/py5sig) `[2025-11]` - ANSSI-published Python tool that auto-builds 5G signalling messages and fuzzes the SBI interfaces of a 5G core.
- [5Greplay](https://github.com/Montimage/5Greplay) `[2026-03]` - Tool for modifying and replaying captured 5G protocol traffic, enabling attack injection and fuzzing of 5G core/RAN deployments. From Montimage.
- [FuzzyDoo](https://github.com/gabrielepongelli/FuzzyDoo) `[2026-01]` - Mutation-based, structure-aware fuzzer purpose-built for 5G core networks (NGAP/NAS/PFCP/SBI).
- [U-Fuzz](https://github.com/asset-group/U-Fuzz) `[2026-04]` - Universal fuzzing framework for IoT/wireless protocols from the ASSET group, targeting stateful protocol stacks across radio technologies.
- [ORANClaw](https://github.com/asset-group/ORANClaw-E2-MitM-Fuzzing) `[2026-04]` - Fuzzes the O-RAN E2 interface via a MitM setup between RIC and E2 nodes. From the ASSET group.
- [AirBugCatcher](https://github.com/asset-group/air-bug-catcher) `[2026-04]` - Detection of bugs in over-the-air wireless protocol implementations. From the ASSET group.
- [FirmKit](https://github.com/SysSec-KAIST/FirmKit) `[2026-04]` - IoT firmware vulnerability analysis tool based on binary code similarity (BCSA). From the KAIST group behind BaseSpec/LTESniffer.
- [extractor](https://github.com/srlabs/extractor) `[2026-04]` - SRLabs Android firmware image extraction tool. Companion utility to their baseband and modem research workflow.
- [SentryFlow](https://github.com/5GSEC/SentryFlow) `[2025-07]` - 5G API observability and security platform monitoring SBA/HTTP2 5GC API traffic for anomalies and abuse.
- [nimbus](https://github.com/5GSEC/nimbus) `[2026-01]` - Intent-driven security automation framework for 5G/cloud-native deployments from the 5GSEC group.

### IMSI Catcher Detection

- [Rayhunter](https://github.com/EFForg/rayhunter) `[2026-03]` - Rust tool to detect cell site simulators (IMSI catchers) on an Orbic mobile hotspot, from the EFF.
- [IMSI-catcher](https://github.com/Oros42/IMSI-catcher) `[2025-12]` - Python tool using gr-gsm to display IMSI numbers of cellphones around you.
- [Android-IMSI-Catcher-Detector](https://github.com/CellularPrivacy/Android-IMSI-Catcher-Detector) `[2026-02]` - Android app to detect IMSI catchers, StingRays, and silent SMS.
- [SentryRadio](https://github.com/fzer0x/SentryRadio) `[2026-04]` - Android forensic tool (Xposed/Magisk/KSU) to detect IMSI catchers, cell site simulators, suspicious network downgrades and silent SMS.
- [IMSICatcherDetector (Marlin)](https://github.com/eylonK14/IMSICatcherDetector) `[2025-08]` - Detects IMSI-catchers/Stingrays via statistical analysis of identity-exposing messages, implementing the Marlin methodology from NDSS 2025 (claimed 99.9% detection rate).
- [Tower-Hunter](https://github.com/Ringmast4r/Tower-Hunter) `[2026-01]` - Cell tower logger and anomaly detector for Linux mobile devices. Logs tower data with GPS, monitors cellular connections, and flags suspicious base stations.
- [rayhunter-enhanced](https://github.com/drinkingc0ffee/rayhunter-enhanced) `[2025-07]` - Enhanced fork of EFF Rayhunter providing roughly 3x cellular data coverage for IMSI-catcher detection on Quectel modems.
- [raypager](https://github.com/tschakram/raypager) `[2026-04]` - Rayhunter port for the GL-E750V2 (Mudi V2) travel router, integrating OpenCelliD and Blue Merle as part of a Chasing-Your-Tail counter-surveillance ecosystem.

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
- [3GPP Meeting Tools](https://github.com/telekom/3gpp-meeting-tools) `[2026-01]` - Deutsche Telekom-maintained tools for the day-to-day execution of 3GPP meetings (TDoc handling, agenda parsing). Useful for delegates.
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

## Commercial

Companies offering products/services around open source telco tech:

> **Disclaimer:** The commercial products and services listed below are provided for reference only. This list does not constitute an endorsement, affiliation, or recommendation. Users should independently verify suitability and terms before engaging with any vendor.

- [sysmocom](https://www.sysmocom.de) - Products, support, and services for open source telecom, including Osmocom.
- [open-cells](https://open-cells.com) - 4G and 5G full open source testbed solutions.
- [5ber eSIM](http://esim.5ber.com) - Physical SIM card that stores up to 15 eSIM profiles (GSMA compliant).
- [esim.me](https://esim.me) - Physical SIM + app combo for loading up to 15 eSIM profiles.
- [PikaSim](https://pikasim.com/reseller) - Privacy-first eSIM Reseller API. Purchase travel eSIMs for 190+ countries programmatically with webhooks and no customer data required.

---

## Related Lists

- [awesome-5g](https://github.com/calee0219/awesome-5g) `[2026-02]` - 5G-specific projects and resources.
- [awesome-rtc-hacking](https://github.com/EnableSecurity/awesome-rtc-hacking) `[2025-07]` - Curated list of VoIP, WebRTC, and VoLTE security resources. From the SIPVicious team.
- [awesome-ai-oran](https://github.com/LynchXLQ/awesome-ai-oran) `[2026-03]` - Curated list of AI/ML research papers and tools for O-RAN. Covers DRL, GNN, LLMs, and more applied to O-RAN.
- [Paper-with-Code (Wireless DL)](https://github.com/ML4Comm-Netw/Paper-with-Code-of-Wireless-communication-Based-on-DL) `[2026-04]` - Massive curated collection of deep learning papers with code for wireless communication.
- [RIS-Codes-Collection](https://github.com/ken0225/RIS-Codes-Collection) `[2026-04]` - Complete collection of codes for RIS/IRS research including DL/RL approaches for beamforming and channel estimation.
- [GNN-Communication-Networks](https://github.com/jwwthu/GNN-Communication-Networks) `[2026-04]` - Curated collection of GNN research for communication networks. Covers traffic prediction, routing, spectrum sensing.
- [Cellular-Security-Papers](https://github.com/onehouwong/Cellular-Security-Papers) `[2026-04]` - Collection of papers, repos, talks, and tools for cellular security and privacy.

## Contributing

Contributions welcome! Please read the contribution guidelines first. Open a PR or issue to add new resources.

## License

[MIT](LICENSE)
