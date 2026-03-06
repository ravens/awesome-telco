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
- [GlobalPlatformPro](https://github.com/martinpaljak/GlobalPlatformPro) `[2026-01]` - CLI tool to load and manage applets on JavaCards, by Martin Paljak.
- [ARA-M Applet](https://github.com/bertrandmartel/aram-applet) `[2018-02]` - ARA-M implementation for JavaCards by Bertrand Martel.
- ⚠️ [HelloSTK2](https://github.com/mrlnc/HelloSTK2) `[2025-01]` - Guide to build and install SIM-Toolkit applets.
- [SUPI with pysim](https://gist.github.com/mrlnc/01d6300f1904f154d969ff205136b753) - Notes on enabling SUPI with pysim.
- [asterix](https://github.com/suma12/asterix) `[2019-06]` - Framework for smartcard communication based on pyscard.
- [SimServerAndroid](https://github.com/zhuowei/SimServerAndroid) `[2022-07]` - Get SIM card ICCID and run 3G Authentication over ADB shell.
- [ScapySMS](https://github.com/mnemonic-no/ScapySMS) `[2021-10]` - Scapy implementation of SMS-SUBMIT and (U)SIM Application Toolkit command packets.
- [USIM-https-server](https://github.com/fasferraz/USIM-https-server) `[2025-12]` - USIM HTTPS server API exposing AKA authentication over HTTP. Useful for lab/testing setups.
- [swicc-pcsc](https://github.com/tomasz-lisowski/swicc-pcsc) `[2025-12]` - PC/SC IFD handler bridging swICC-based software SIM cards to PC/SC applications. Companion to swSIM/swICC.

### eSIM / eUICC

- [eUICC and eSIM Developer Manual](https://euicc-manual.osmocom.org) - Comprehensive eSIM developer documentation from Osmocom.
- [Known eSIM Test Profiles](https://euicc-manual.osmocom.org/docs/rsp/known-test-profile/) - List of known test profiles for eSIM/eUICC testing and development.
- [lpac](https://github.com/estkme-group/lpac) `[2026-01]` - C-language implementation of a Consumer eSIM LPAd. Download/activate/deactivate profiles on eUICC.
- [EasyLPAC](https://github.com/creamlike1024/EasyLPAC) `[2025-09]` - lpac GUI Frontend for Linux and macOS.
- [OpenEUICC](https://github.com/estkme-group/openeuicc) `[2026-03]` - Fully open-source eSIM LPA (Local Profile Assistant) implementation for Android. System privilege required. Also available as [Magisk module](https://github.com/hzy132/OpenEUICC_for_Magisk).
- [LPAd SM-DP+ Connector](https://github.com/Truphone/LPAd_SM-DPPlus_Connector) `[2023-05]` - Local Profile Assistant for Device (LPAd) SM-DP+ Connector.
- [Generic-eUICC-Test-Profile](https://github.com/GSMATerminals/Generic-eUICC-Test-Profile-for-Device-Testing-Public) `[2025-06]` - Standardized test profiles for embedded UICCs.
- [ISD-R Access Provider](https://github.com/cheeriotb/ISD-R-AccessProvider) `[2021-01]` - Content provider for communicating with ISD-R in soldered eSIM on Android (Pixel4).
- [rlpa-server](https://github.com/estkme-group/rlpa-server) `[2024-07]` - Remote LPA Server for eSIM profile management, from the lpac team.
- [MiniLPA](https://github.com/EsimMoe/MiniLPA) `[2024-12]` - Professional cross-platform LPA UI for eSIM/eUICC management (GSMA SGP.22), built with Java Swing.
- [NekokoLPA](https://github.com/iebb/NekokoLPA) `[2026-01]` - Open-source LPA software for managing eSIM profiles on Android and iOS.

### SIM Emulation & Virtualization

- [swSIM](https://github.com/tomasz-lisowski/swsim) `[2024-07]` - A software-only SIM card.
- [swICC](https://github.com/tomasz-lisowski/swicc) `[2024-07]` - Framework for creating smart cards (ICC-based cards with contacts).
- [vsmartcard](https://github.com/frankmorgner/vsmartcard) `[2025-06]` - Umbrella project for emulation of smart card readers or smart cards.
- [Onomondo UICC](https://github.com/onomondo/onomondo-uicc) `[2025-12]` - Pure software implementation/emulation of SIM/UICC/USIM functionalities.
- [osmo-remsim](https://osmocom.org/projects/osmo-remsim/wiki) - Forward SIM card traffic to a remote SIM card via TCP/IP.
- [mobile-atlas](https://github.com/sbaresearch/mobile-atlas) `[2025-11]` - Geographically decouple SIM card and modem for scalable measurement platforms.

### VoLTE/VoWiFi & Carrier Privileges

- [CoIMS_Wiki](https://github.com/herlesupreeth/CoIMS_Wiki) `[2025-10]` - Guide for overriding IMS settings to enable VoLTE/VoWiFi using Carrier Privileges. Companion app: [CoIMS](https://play.google.com/store/apps/details?id=com.sherle.coims).


## User Equipment

### 4G

- [srsUE](https://github.com/srslte/srslte) `[2026-01]` - UE 4G modem part of the srsLTE project.
- [srsUE PR external NAS](https://github.com/srsLTE/srsLTE/pull/474) `[2026-01]` - a PR for srsLTE for external NAS message injection.
- [OAI UE](https://gitlab.eurecom.fr/oai/openairinterface5g/wikis/home) `[2026-02]` - Open Air Interface RAN 4G eNB/ 5G gNB to use on SDR-based radios.
- [Amarisoft](https://www.amarisoft.com) - Commercial UE Emulator by Amarisoft, company co-founded by [Bellard](https://bellard.org) on his original LTE software modem [work](https://bellard.org/lte/).
- [LTE-CellScanner](https://github.com/Evrytania/LTE-Cell-Scanner) `[2019-02]` - This is a collection of tools to locate and track LTE basestation cells using very low performance RF front ends.
- [LTE-CellScanner-SDR-X](https://github.com/JiaoXianjun/LTE-Cell-Scanner) `[2024-01]` - An OpenCL accelerated TDD/FDD LTE Scanner (from rtlsdr/hackRF/bladeRF A/D samples to PDSCH output and RRC SIB messages decoded).
- [S1APTester](https://github.com/magma/S1APTester) `[2022-12]` - A test tool that simulates the s1aptest functionality of a LTE network.

### 2G

- [OsmocomBB](https://osmocom.org/projects/baseband/wiki) - Open Source implementation of a 2G Mobile Station, including baseband firmware/PHY, L2, L3, etc.  Works with phones using TI Calypso chipset; SDR PHY is work-in-progress
- [FreeCalypso](https://www.freecalypso.org/) - Volunteer project building software derived from leaked source code for the TI calypso project

### Diagnostics, Monitor mode

- [SCAT](https://github.com/fgsect/scat) `[2026-01]` - this application parses diagnostic messages of Qualcomm and Samsung baseband through USB, and generates a stream of GSMTAP packet containing cellular control plane messages.
- [QCSuper](https://github.com/P1sec/QCSuper) `[2026-01]` - QCSuper is a tool communicating with Qualcomm-based phones and modems, allowing to capture raw 2G/3G/4G radio frames, among other things.
- [Network Signal Guru](http://m.qtrun.com/en/) - Android app able to parse Diag output from QC modem and display a lot of data for engineering field work.
- [SnoopSnitch](https://github.com/srlabs/snoopsnitch) `[2026-03]` - Android app that collects and analyzes mobile radio data to detect fake base stations, user tracking, and OTA updates via the DIAG protocol on a rooted phone. From SRLabs.
- [Diag-parser](https://github.com/moiji-mobile/diag-parser) `[2017-11]` - Parse the Qualcomm DIAG format and convert 2G, 3G and 4G radio messages to Osmocom GSMTAP for analysis in wireshark and other utilities.
- [LTE_monitor_c2xx](https://github.com/P1sec/LTE_monitor_c2xx) `[2014-11]` - The purpose of LTE_monitor_c2xx is to provide a LTE message debugging solution for Samsung C2xx-based chipsets.
- [XGoldmon](https://github.com/2b-as/xgoldmon) `[2013-12]` - xgoldmon is a small tool to convert the messages output by the USB logging mode of phones with Intel/Infineon XGold baseband processor.
- [Modmobmap](https://github.com/PentHertz/Modmobmap) `[2025-12]` - Map 2G/3G/4G and more cellular networks in real live with a simple smart phone, pretty much like osmocomBB monitoring feature.
- [Modmobjam](https://github.com/PentHertz/Modmobjam) `[2023-04]` - A smart jamming proof of concept for mobile equipments that could be powered with Modmobmap tool.
- [LTESniffer](https://github.com/SysSec-KAIST/LTESniffer) `[2024-10]` - An Open-source LTE Downlink/Uplink Eavesdropper
- [FALCON](https://github.com/falkenber9/falcon) `[2023-10]` - FALCON - Fast Analysis of LTE Control channels.
- [osmo-qcdiag](https://osmocom.org/projects/osmo-qcdiag/wiki) - Osmocom project for decoding Qualcomm DIAG messages. Use @hoernchen/gsmtap@ branch to feed 2G/3G/4G/SIM messages from DIAG into wireshark ia GSMTAP.
- [mbn-mcfg-tools](https://github.com/sbaresearch/mbn-mcfg-tools) `[2024-07]` - Tools for parsing, extracting, and packing Qualcomm MBN MCFG (Modem Configuration) files. From the mobile-atlas team at SBA Research.

## Radio Access Network

### RRH

- [O-RAN Software and seed code](https://o-ran-sc.org) - The O-RAN Software Community (SC) is a collaboration between the O-RAN Alliance and Linux Foundation with the mission to support the creation of software for the Radio Access Network (RAN). Introduction to O-RAN in a [LF video](https://www.youtube.com/watch?v=iJyb0pCWDKo).
- [srsRAN O-RAN SC RIC](https://github.com/srsran/oran-sc-ric) `[2025-10]` - Simplified O-RAN SC RIC deployment with improved usability and xApp examples, from the srsRAN team.
- [FlexRIC](https://gitlab.eurecom.fr/mosaic5g/flexric) `[2026-02]` - O-RAN Alliance compliant Near-RT RIC and E2 Agent with xApp SDK in C/C++ and Python. Sub-200µs latency. Part of MOSAIC5G/OAI. Hosted on **GitLab (Eurecom)**.
- [ProtO-RU](https://github.com/NUS-CIR/ProtO-RU) `[2025-12]` - Software implementation of an O-RAN split-7.2 compatible Radio Unit using SDRs. From NUS.

### 5G

- ⚠️ [srsRAN_Project](https://github.com/srsran/srsRAN_Project) `[2026-01]` - A complete ORAN-native 5G RAN solution. _Archived Feb 2026; successor is [OCUDU](https://ocudu.org/), a Linux Foundation project for open-source AI-RAN._
- [OAI NR](https://gitlab.eurecom.fr/oai/openairinterface5g/wikis/5g-nr-development-and-releases) `[2026-02]` - 5GNR related branch of the OAI code. You can follow the [weekly updates](https://trello.com/c/XBVaaHIO/26-5g-nr) to stay up to date.
- [UERANSIM](https://github.com/aligungr/UERANSIM) `[2025-10]` - UERANSIM is the state-of-the-art 5G UE and RAN (gNodeB) simulator. The project can be used for testing 5G Core Network and studying 5G System.
- ⚠️ [Software gNB for free5GC](https://github.com/Srajdax/gnb) `[2020-11]` - The gNB function was built on the model of the other free5GC CN functions using all the pattern and helper class defined by the free5GC team.
- [5G-tools.com](https://5g-tools.com/) - 5G-tools.com is devoted to modern standards of wireless communications, such as 5G, 4G, etc. Main mission of site to give engineers the useful software tools to create a wireless network
- ⚠️ [corescope](https://github.com/srsran/corescope) `[2021-12]` - CoreScope combines gNodeB and UE components without any radio transmission.
- [my5G-RANTester](https://github.com/my5G/my5G-RANTester) `[2024-04]` - my5G-RANTester is a gNB/UE simulator for testing 3GPP standards and stressing a 5G core.
- [free5GRAN](https://github.com/IMTSDRLab/free5GRAN) `[2021-10]` - free5GRAN is an open-source 5G RAN stack. The current version includes a receiver which decodes MIB & SIB1 data. It also acts as a cell scanner. free5GRAN works in SA mode. From Telecom Paris 5G laboratory - Institut Polytechnique de Paris.
- [pfm](https://github.com/arv-sajeev/pfm) `[2021-11]` - Implemented a prototype of gNB-CU-UP a network element of 5G Radio Network. Using DPDK, a set of data-plane processing libraries and NIC drivers for high speed packet processing applications.
- [PacketRusher](https://github.com/HewlettPackard/PacketRusher) `[2025-12]` - High performance 5G UE/gNB Simulator and CP/UP load tester. PacketRusher is an open-source tool dedicated to the performance testing and automatic validation of 5G Core Networks using simulated UE (user equipment) and gNodeB (5G base station). From Valentin D'Emmanuele - France.
- [py3gpp](https://github.com/catkira/py3gpp) `[2024-11]` - A Python package for 5G-NR simulations.
- [RFSwift](https://github.com/PentHertz/RF-Swift) `[2026-02]` -  powerful multi-platform RF toolbox that deploys specialized radio tools in seconds on Linux, Windows, and macOS. Provdes telecom_4G_5GNSA_* family of telecoms tools.
- [NVIDIA Aerial](https://github.com/NVIDIA/aerial-cuda-accelerated-ran) `[2025-12]` - SDK for building commercial-grade, AI-native, 3GPP and O-RAN compliant 5G/6G gNB software on NVIDIA GPU-accelerated platforms.
- [alsoran](https://github.com/nplrkn/alsoran) `[2025-06]` - 5G gNodeB Centralized Unit (gNB-CU) written in Rust. From the author of qcore.
- [gnbsim (SD-Core)](https://github.com/omec-project/gnbsim) `[2026-02]` - gNB and UE simulator for testing 5G core networks, from the SD-Core/OMEC project.
- [free-ran-ue](https://github.com/free-ran-ue/free-ran-ue) `[2026-02]` - Next-generation open-source 5G RAN/UE simulator for free5GC with web frontend, multi-UE and ULCL support. Written in Go.
- [NIST O-RAN Testbed Automation](https://github.com/usnistgov/O-RAN-Testbed-Automation) `[2026-02]` - Turn-key automation for deploying 5G O-RAN testbeds. Supports Open5GS, OAI, free5GC, srsRAN, multiple UPFs and xApps. From NIST.
- [ns-O-RAN-flexric](https://github.com/Orange-OpenSource/ns-O-RAN-flexric) `[2025-07]` - RAN simulator with E2 termination compliant with FlexRIC. Supports E2AP v1.01, KPM v3, RC v1.01. From Orange.
- [ns3-oran](https://github.com/usnistgov/ns3-oran) `[2025-11]` - ns-3 module for modeling O-RAN-like behavior with Near-RT RIC, E2 reporting, and ML model support. From NIST.
- [sim-ns3-o-ran-e2](https://github.com/o-ran-sc/sim-ns3-o-ran-e2) `[2025-11]` - ns-3 module with O-RAN-compliant E2 interface support. From O-RAN SC.

### 4G

- [OAI eNB/ gNB](https://gitlab.eurecom.fr/oai/openairinterface5g/wikis/home) `[2026-02]` - Open Air Interface RAN 4G eNB / 5G NR gNB to use on SDR-based radios.
- [srsLTE](https://github.com/srsran/srsRAN_4G) `[2026-01]` - srsLTE eNB 4G to use on SDR-based radios.
- ⚠️ [LTE-ciphercheck](https://github.com/mrlnc/LTE-ciphercheck) `[2022-09]` - srsLTE derivative to check for cipher configuration of an LTE network - test across the 256 possibilities using an SDR radio.
- ⚠️ [OpenLTE](https://sourceforge.net/projects/openlte/) - OpenLTE is an open source implementation of the 3GPP LTE specifications from Ben Wojtowicz. GNU Radio applications for LTE downlink/uplink with RTL-SDR, HackRF, USRP. Hosted on **SourceForge**. _Last updated 2021._
- ⚠️ [Cisco 4G nFAPI](https://github.com/cisco/open-nFAPI) `[2018-08]` - Open-nFAPI is implementation of the Small Cell Forum's network functional API or nFAPI for short. nFAPI defines a network protocol that is used to connect a Physical Network Function (PNF) running LTE Layer 1 to a Virtual Network Function (VNF) running LTE layer 2 and above.
- [CrocodileHunter](https://github.com/EFForg/crocodilehunter) `[2023-02]` - Crocodile Hunter is a tool to hunt fake eNodeBs, also known commonly as hailstorm, stingray, cell site simulators, or IMSI catchers. It works by listening for broadcast messages from all of the 4G stations in the area, inferring their location, and looking for unusual activity. From the EFF.
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

### PHY
- [gr-osmoSDR](https://osmocom.org/projects/gr-osmosdr) - Unified gnuradio input/output block for a variety of SDR devices, including FUNcube Dongle, OsmoSDR, RTL-SDR, MSi2500, SDRplay, SDR-IQ, AirSpy, rad10, HackRF, bladeRF, USSRP/UHD, UMtrx, RedPitaya, FreeSRP.
- [gr-gsm](https://github.com/ptrkrysik/gr-gsm) `[2025-03]` - GNU Radio blocks and tools for receiving GSM transmissions.
- [USRP B210](https://www.ettus.com/all-products/UB210-KIT/) - SDR Radio kit compatible with most of the SDR-based software modem implementations.
- [LimeSDR](https://limemicro.com/products/boards/limesdr/) - Affordable full-duplex SDR board, popular for srsRAN and OAI experimentation.
- [BladeRF](https://www.nuand.com/) - USB 3.0 SDR platform compatible with open source cellular stacks.
- [Kalibrate](https://github.com/steve-m/kalibrate-rtl) `[2023-08]` - Kalibrate, or kal, can scan for GSM base stations in a given frequency band and can use those GSM base stations to calculate the local oscillator frequency offset.
- [rtl-sdr](https://github.com/osmocom/rtl-sdr) `[2026-01]` - Library for turning a RTL2832-based DVB dongle into a Software Defined Receiver. Foundational for low-cost SDR-based cellular signal reception.
- ⚠️ [open5G_phy](https://github.com/catkira/open5G_phy) `[2025-04]` - A resource-efficient, customizable, synthesizable 5G NR lower PHY written in Verilog for FPGA targets.
- [neural_rx](https://github.com/NVlabs/neural_rx) `[2025-12]` - Real-time inference of 5G NR multi-user MIMO neural receivers from NVIDIA Research.
- [zynq_timestamping](https://github.com/srsran/zynq_timestamping) `[2026-02]` - Open source Zynq FPGA timestamping for precise SDR timing in 5G RAN deployments. From SRS.
- [DragonOS](https://sourceforge.net/projects/dragonos-focal/) - Debian/Ubuntu-based Linux distro with 30+ pre-installed SDR tools (GNU Radio, gr-gsm, GQRX, etc.) for RF analysis, spectrum monitoring and telecom security. Hosted on **SourceForge**.
- [Gqrx SDR](https://www.gqrx.dk/) - Open source SDR receiver powered by GNU Radio, supporting RTL-SDR, HackRF, LimeSDR, USRP and more. [SourceForge](https://sourceforge.net/projects/gqrx/).


## Core Network

### 5G

- [Open5GS](https://open5gs.org) `[2025-12]` - 5G, R14 4G EPC core with independent MME, HSS, SGW, PGW, PCRF, UPF, SMF, NRF functions. Follow-up of NextEPC. [github](https://github.com/open5gs)
- [OAI 5GCN](https://gitlab.eurecom.fr/oai/cn5g) - OAI(Open Air Interface) was initially developed by EURECOM, provides a 3GPP-Compliant 5G SA Core Network.
- ⚠️ [travelping-vpp](https://github.com/travelping/vpp) `[2021-01]` - UPF plugins implements a GTP-U user plane based on 3GPP TS 23.214 and 3GPP TS 29.244 Release 15, adding UPF as a plugin to VPP.
- ⚠️ [IITB 5G SBA PoC](https://github.com/iithnewslab/SBA-gRPC-5G) `[2019-08]` - Prototyping and Load Balancing the Service Based Architecture of 5G Core using NFV - [research paper from IITB](https://github.com/iithnewslab/SBA-gRPC-5G/blob/master/Presentation_Netsoft19_gRPC_5G.pdf)
- [Free5GC](https://www.free5gc.org/) `[2025-12]` - The free5GC is an open-source project for 5th generation (5G) mobile core network hosted by [CS Lab](https://cslab.cs.nycu.edu.tw/). Written in Golang. Associated github projects: [PER parser/encoder](https://github.com/free5gc/aper), [AMF](https://github.com/free5gc/amf).
- [5GC Swagger APIS](https://github.com/jdegre/5GC_APIs) `[2024-06]` - RESTful APIs of main Network Functions in the 3GPP 5G Core Network. R16.
- [5G GTP kernel driver](https://github.com/free5gc/gtp5g) `[2026-03]` - gtp5g is a customized Linux kernel module 5G GTP-U to handle packet by PFCP IEs such as PDR and FAR. Per 3GPP TS 29.281 and 3GPP TS 29.244.
- [UPF (OMEC)](https://github.com/omec-project/upf) `[2026-03]` - 4G/5G Mobile Core User Plane from the OMEC/SD-Core project. Successor to upf-epc.
- [OpenUPF](https://github.com/5GOpenUPF/openupf) `[2021-05]` - A 3GPP R16 compliant open source 5G core UPF (User Plane Function).
- [Katana Slice Manager](https://github.com/medianetlab/katana-slice_manager) `[2023-05]` - Katana Slice Manager is a central software component responsible for controlling all the devices comprising the network, providing an interface for creating, modifying, monitoring and deleting slices.
- [my5G-core](https://github.com/my5G/my5G-core) `[2021-01]` - Currently, my5G-core is a fork of the free5GC project, with some extensions to facilitate the deployment.
- [III-5GC-Free-Trial](https://github.com/III-5GC/III-5GC-Free-Trial) `[2021-05]` - The basic III-5GC is a free trial for lab research, prototype product testing and simple 5G end-to-end demonstration.
- [upf-bpf](https://github.com/navarrothiago/upf-bpf) `[2024-09]` - An open source C++ library powered by eBPF/XDP for user plane in mobile core network (5G/LTE).
- [5G_CN](https://github.com/wnlUc3m/5G_CN) `[2019-08]` - This is a basic implementation of a 5G Core Network supporting 4G LTE control signalling.
- [openupf](https://github.com/5GOpenUPF/openupf) `[2021-05]` - A 3GPP R16 compliant open source 5G core UPF (User Plane Function).
- [upf-xdp](https://github.com/801room/upf-xdp) `[2021-01]` -  it shows the possibility of using xdp to implement 5g upf.
- [SD-Core](https://opennetworking.org/sd-core/) - A 4G/5G core that is based on [OMEC](https://www.opennetworking.org/omec/) for 4G, and a fork of [Free5GC](https://www.free5gc.org/) for 5G. Has implementations for AMF,SMF,PCF,UDM,AUSF,NSSF and a P4 based UPF. [github](https://github.com/omec-project/amf)
- [Magma](https://github.com/magma/magma) `[2026-01]` - Rearchitected core network with access gateway (MME+P/SGW), federation gateway for auth (S6a) and billing (Gx, Gy). Initiated by FB on a the OAI EPC code base.
- ⚠️ [5GCoreNetSDK](https://github.com/5GCoreNet/5GCoreNetSDK) `[2023-06]` - 5GCoreNetSDK is a fully-featured Golang SDK for developing inside 5GC (Release-18).
- [eupf](https://github.com/edgecomllc/eupf) `[2026-02]` - Open Source UPF built on eBPF.
- [UPG-VPP](https://github.com/travelping/upg-vpp) `[2026-02]` - High-performance User Plane Gateway (UPG) based on FD.io VPP from Travelping.
- [qcore](https://github.com/nplrkn/qcore) `[2026-01]` - The world's most lightweight 5G Core (probably)
- [NEF_emulator](https://github.com/medianetlab/NEF_emulator) `[2025-02]` - Configurable emulated environment for providing 3GPP Network Exposure Function (NEF) APIs. Enables testing of network applications against 5GC exposure capabilities.
- [Ella Core](https://github.com/ellanetworks/core) `[2026-03]` - Lightweight 5G core for private networks. Single binary with embedded DB, web UI, REST API, and OpenTelemetry. Written in Go.
- [UnifyAir Core](https://github.com/unifyair/unifyair-core) `[2025-11]` - 5G Core Network Functions (AMF, UPF, SMF) implementation in Rust, based on 3GPP Release 17.
- [HEXAeBPF](https://github.com/coranlabs/HEXAeBPF) `[2025-10]` - eBPF-defined interoperable 5G Core (eDC).
- [NextMN-UPF](https://github.com/nextmn/UPF) `[2026-03]` - Experimental user-space 5G UPF in Go. Interoperable with free5GC and UERANSIM.
- [go-upf](https://github.com/free5gc/go-upf) `[2026-03]` - Go-based UPF implementation for free5GC.

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
- [gtp-guard](https://github.com/acassen/gtp-guard) `[2026-02]` - The main goal of this project is to provide robust and secure extensions to GTP protocol (GPRS Tunneling Protocol).

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

### OSS/BSS

- [Sigscale OCS](https://github.com/sigscale/ocs) `[2026-01]` - SigScale OCS includes a 3GPP AAA server function for authentication, authorization and accounting (AAA) of subscribers using DIAMETER or RADIUS protocols.
- [Bodastage CE](https://gitlab.com/bts-ce/bts-ce) `[2019-05]` - Boda Telecom Suite - Community Edition (BTS-CE) is an open source vendor-agnostic telecommunication network management platform. Hosted on **GitLab**.
- [CGRateS](https://github.com/cgrates/cgrates) `[2026-01]` - Real-time Charging System for Telecom & ISP environments. Cloud-ready micro-services with CDR mediation, LCR, fraud detection and multi-tenant support.
- [BillRun](https://github.com/BillRun/system) `[2026-02]` - Open source Telecom BSS: CDR mediation, real-time OCS, rating/charging (prepaid, postpaid, roaming, wholesale), and fraud detection.
- [OpenCDRRate](https://sourceforge.net/p/opencdrrate/home/Home/) - Scalable CDR rating, taxation and invoicing system for telecom/VoIP. Hosted on **SourceForge**.
- [jBilling](https://sourceforge.net/projects/jbilling/) - Open source enterprise billing system in Java with CDR mediation module for telecom. Hosted on **SourceForge**.

## Interconnect

### SBC, IMS

- [Freeswitch](https://freeswitch.org/confluence/display/FREESWITCH/Python_SBC) - Popular SIP stack that could be used as Session Border Controller (SBC)
- [IMS Clearwater](http://www.projectclearwater.org) - Clearwater is an open source implementation of IMS (the IP Multimedia Subsystem).
- [Kamailio](https://www.kamailio.org) - SIP stack used for VoLTE and SBC.
- [go-eventsocket](https://github.com/fiorix/go-eventsocket) `[2024-09]` - FreeSWITCH Event Socket library for the Go programming language.
- [Asterisk](https://github.com/asterisk/asterisk) `[2026-02]` - The most widely deployed open-source PBX and telephony engine. SIP, PJSIP, WebRTC, conferencing, and IVR.
- [PJSIP](https://github.com/pjsip/pjproject) `[2026-02]` - Free and open-source multimedia communication library implementing SIP, SDP, RTP, STUN, TURN, and ICE. Foundation for many VoIP/IMS clients.
- [HOMER](https://github.com/sipcapture/homer) `[2026-01]` - 100% Open-Source SIP/VoIP/RTC packet capture and monitoring platform. Essential for VoLTE/VoWiFi troubleshooting.
- [Routr](https://github.com/fonoster/routr) `[2026-02]` - A programmable, cloud-native SIP server for building modern telephony systems.
- [OpenSIPS](https://opensips.org/) - GPL multi-functional SIP server: proxy, registrar, load balancer, SBC, NAT traversal. Former OpenSER. [SourceForge (legacy)](https://sourceforge.net/projects/opensips/) / [GitHub](https://github.com/OpenSIPS/opensips).
- [OpenIMSs](https://github.com/VoicenterTeam/openimss) `[2023-10]` - Open source environment for real-life development of IMS-based 4G/5G/NR voice/video/data/RCS services. Extends docker_open5gs.
- [FusionPBX](https://www.fusionpbx.com/) - Multi-tenant PBX and voice switch for FreeSWITCH with IVR, call center, provisioning and more. [SourceForge](https://sourceforge.net/directory/pbx/).
- [DjangoPBX](https://codeberg.org/DjangoPBX/DjangoPBX) `[2026-02]` - Full-featured domain-based multi-tenant PBX driven by Django and FreeSWITCH with REST API, call center, and provisioning. Hosted on **Codeberg**.
- [Sofia-SIP](https://github.com/freeswitch/sofia-sip) `[2025-11]` - Open-source SIP User-Agent library (RFC3261 compliant) maintained by FreeSWITCH. Originally from Nokia Research Center.
- [OpalVOIP](https://sourceforge.net/projects/opalvoip/) - C++ multi-platform VoIP library supporting H.323, SIP, and IAX2. Used by Ekiga softphone. Hosted on **SourceForge**.

### SS7

- [Restcomm SS7](https://github.com/restcomm/jss7) `[2024-06]` - Open Source Java SS7 stack that allows Java apps to communicate with legacy SS7 communications equipment.
- [SigFW](https://github.com/P1sec/SigFW) `[2024-10]` - Open Source Signaling Firewall for SS7, Diameter filtering, antispoof and antisniff.
- [yate](https://github.com/yatevoip/yate) `[2026-01]` - Open Source Telephony engine with support of MTP2/MTP3 over TDM, M2PA, M2UA, M3UA, SCCP, TCAP

### SMPP / SMS Gateways

- [go-smpp](https://github.com/fiorix/go-smpp) `[2022-11]` - This is an implementation of SMPP 3.4 for Go, based on the original smpp34 from Kevin Patel.
- [Selenium SMPPSim](http://www.seleniumsoftware.com/downloads.html) - (software disappeared) - possible mirror [here](https://github.com/haifzhan/SMPPSim).
- [smppgui](https://github.com/ukarim/smppgui) `[2025-07]` - SMPP gui client
- [Kannel](https://www.kannel.org/) - Compact and powerful open source WAP and SMS gateway, used globally for SMS delivery at scale. [SourceForge](https://sourceforge.net/projects/kannelrelease/).
- [Jasmin SMS Gateway](https://github.com/jookies/jasmin) `[2024-06]` - Open source SMS gateway in Python/Twisted with SMPP and HTTP APIs, message routing/filtering, and real-time billing.

## Satellite Communication
- [Hughes_OneWeb_Monitor](https://github.com/nickvsnetworking/Hughes_OneWeb_Monitor) `[2025-04]` - Hughes OneWeb Terminal Prometheus Exporter
- [SatNOGS](https://gitlab.com/librespacefoundation/satnogs) - Open Source Global Satellite Ground Station Network focused on LEO satellites, from the Libre Space Foundation. Hosted on **GitLab**.
- [gr-leo](https://gitlab.com/librespacefoundation/gr-leo) `[2025-10]` - GNU Radio Out-of-Tree module simulating the telecommunication channel between orbiting satellites and ground stations, from Libre Space Foundation / ESA SDR Makerspace. Hosted on **GitLab**.
- [OpenSN](https://github.com/OpenSN-Library/OpenSN-Library) `[2026-01]` - Open source library for emulating LEO satellite networks. Container-based, 5-10x faster than StarryNet.
- [Satellite-Open-Source](https://github.com/jwwthu/Satellite-Open-Source) `[2026-03]` - Curated collection of open source code and data for satellite communication research.
- [GNSS-SDR](https://sourceforge.net/projects/gnss-sdr/) - Open source software-defined GNSS (Global Navigation Satellite Systems) receiver written in C++ and based on GNU Radio. Hosted on **SourceForge**.

## Protocols

### ASN1-based, S1AP/NGAP

- [Pycrate](https://github.com/pycrate-org/pycrate) `[2025-12]` - A Python library to ease the development of encoders and decoders for various protocols and file formats, especially telecom ones. Provides an ASN.1 compiler and a CSN.1 runtime.
- [pycrate-rs](https://github.com/EFForg/pycrate-rs) `[2025-12]` - Rust telecom protocol parser generated from pycrate. From the EFF (Rayhunter project).
- [bazel-pycrate](https://github.com/ravens/bazel-pycrate) `[2023-07]` - A bazel-based pycrate ready jupyter notebook env
- [hampi](https://github.com/gabhijit/hampi) `[2025-08]` - The Goal of this project is to implement an ASN.1 Compiler in Rust which can generate Rust bindings for different ASN.1 specifications.
- [Eclipse Titan TTCN-3 (core)](https://gitlab.eclipse.org/eclipse/titan/titan.core/) - Open source TTCN-3 compiler and runtime from Ericsson/Eclipse, with built-in ASN.1 BER/PER/XML codecs. Used for telecom protocol conformance testing. Hosted on **GitLab (Eclipse)**.

### NAS 4G/5G and Milenage

- [mts-nas](https://github.com/ericsson-mts/mts-nas) `[2023-04]` - Project to decode/encode Non-Access Stratum (NAS) protocol.
- [LTE-security](https://fabricioapps.blogspot.com/2012/05/lte-security.html) - a Windows application that implements all the security procedures for LTE referred in Annex A and Annex B of 3GPP 33.401. Last update in 2020, direct [link](https://www.dropbox.com/s/adpa2yuac99riqt/LTE%20Security%203.3.zip?dl=0)
- [milenage](https://github.com/emakeev/milenage) `[2020-10]` - Go implementation of milenage ciphers.
- [nas-5gs](https://github.com/hzane/nas-5gs) `[2020-02]` - Routines for Non-Access-Stratum (NAS) protocol for NAS-NR(5GS).
- [oxirush-nas](https://github.com/linouxis9/oxirush-nas) `[2025-03]` - A Rust Library that allows the decoding/encoding of NAS-5G messages. From Valentin D'Emmanuele - France.
- [CryptoMobile](https://github.com/P1sec/CryptoMobile) `[2023-01]` - C implementations with Python bindings for mobile network cryptographic algorithms (Milenage, TUAK, Kasumi, SNOW, ZUC). From P1 Security.
- [milenage (Go)](https://github.com/wmnsk/milenage) `[2025-12]` - MILENAGE algorithm implementation in Go for 3G/4G/5G AKA authentication.

### GTP/PFCP

- [Kernel GTP-U](https://osmocom.org/projects/linux-kernel-gtp-u) - This is an implementation of the GTP-U (user plane) inside the Linux kernel.
- [go-gtp](https://github.com/wmnsk/go-gtp) `[2026-01]` - Package gtp provides simple and painless handling of GTP(GPRS Tunneling Protocol), implemented in the Go Programming Language.
- [go-pfcp](https://github.com/wmnsk/go-pfcp) `[2026-01]` - PFCP(Packet Forwarding Control Protocol) is a signaling protocol used in mobile networking infrastructure(LTE EPC, 5GC) to realize CUPS architecture(Control and User Plane Separation, not a printing system) defined in 3GPP TS29.244.
- [gtplib](https://github.com/travelping/gtplib) `[2025-09]` - Erlang GTPv1/GTPv2 library.
- [gtpv2](https://github.com/blorticus/gtpv2) `[2021-09]` - GPRS Tunneling Protocol Library for golang.
- [scapy-gtp](https://github.com/secdev/scapy/blob/master/scapy/contrib/gtp.py) `[2026-01]` - Scapy (A interactive packet manipulation program) GTP layer. Spec: 3GPP TS 29.060 and 3GPP TS 29.274. Some IEs: 3GPP TS 24.008.
- [gtp_dialer](https://github.com/fasferraz/gtp_dialer) `[2025-11]` - GTPv1/GTPv2 Dialer
- [nwGTPv2](https://sourceforge.net/projects/nwgtpv2/) - Free and open source implementation of eGTP (GTPv2) control plane, supporting S11, S5, S8 EPC interfaces. Also provides nwEPC SAE-Gateway framework. Hosted on **SourceForge**.
- [pfcpsim](https://github.com/omec-project/pfcpsim) `[2026-03]` - PFCP client simulator for UPF testing. From the SD-Core/OMEC project.
- [pfcplib](https://github.com/travelping/pfcplib) `[2025-08]` - Erlang library for encoding/decoding PFCP frames per 3GPP TS 29.244. From Travelping.
- [OpenGGSN](https://sourceforge.net/projects/ggsn/) - Open source Gateway GPRS Support Node (GGSN) with SGSN emulator for core network testing. Maintained within Osmocom. Hosted on **SourceForge**.

### SCTP

- [sctp](https://github.com/ishidawataru/sctp) `[2025-11]` - Stream Control Transmission Protocol (SCTP) in Go.
- [usrsctp](https://github.com/sctplab/usrsctp) `[2025-10]` - This is a userland SCTP stack supporting FreeBSD, Linux, Mac OS X and Windows.
- [PySCTP](https://github.com/P1sec/pysctp) `[2024-09]` - PySCTP - SCTP bindings for Python.
- [MTS: Multiprotocol Test Tool](https://github.com/ericsson-mts/mts) `[2023-11]` - MTS (Multi-protocol Test Suite) is a multi-protocol testing tool specially designed for telecom IP-based architectures (see above "Features" section for more details).
- [scapy-sctp](https://github.com/secdev/scapy/blob/master/scapy/layers/sctp.py) `[2026-01]` - Scapy (A interactive packet manipulation program) SCTP layer.
- [ellora](https://github.com/gabhijit/ellora/) `[2023-11]` - Rust SCTP Toolkit. The Goal of this project is to make safe bindings for Linux SCTP stack that can be used within Rust's `async` ecosystem.
- [sctplb](https://github.com/omec-project/sctplb) `[2026-03]` - SCTP Load Balancer for 5G core networks. From the SD-Core/OMEC project.

### VoWiFi/VoLTE

- [SWu-IKEv2](https://github.com/fasferraz/SWu-IKEv2) `[2026-02]` - SWu client emulator in Python that establishes an IKEv2/IPSec tunnel with an ePDG, implementing both control plane (IKEv2) and user plane (IPSec).
- [osmo-epdg](https://gitea.osmocom.org/erlang/osmo-epdg) - Implement an ePDG with an embedded AAA server. osmo-ePDG also requires a modify strongswan.
- [NWu-Non3GPP-5GC](https://github.com/fasferraz/NWu-Non3GPP-5GC) `[2024-09]` - NWu IKEv2/IPSec dialer for 5GC N3IWF (Non-3GPP Interworking Function). From the author of eNB s1 emulator and gtp_dialer.
- [GBA_ME](https://github.com/fasferraz/GBA_ME) `[2025-11]` - Generic Bootstrapping Architecture (GBA) ME emulator in Python. From fasferraz.


### Diameter

- [go-diameter](https://github.com/fiorix/go-diameter) `[2025-07]` - Package go-diameter is an implementation of the Diameter Base Protocol RFC 6733 and a stack for the Go programming language.
- [jdiameter](https://github.com/RestComm/jdiameter/) `[2024-01]` - RestComm jDiameter provides an Open Source Java implementation of the Diameter standard for Authentication, Authorization, and Accounting (AAA).
- ⚠️ [diafuzzer](https://github.com/Orange-OpenSource/diafuzzer) `[2019-10]` - Diameter fuzzer, based on specifications of Diameter applications following rfc 3588 / 6733 from Orange.
- [bromelia](https://github.com/heimiricmr/bromelia) `[2024-05]` - A Python micro framework for building Diameter protocol applications.
- [freeDiameter](http://www.freediameter.net/) - Open source implementation of the Diameter protocol (RFC 6733). Extensible platform for AAA with modular architecture. Also available on [GitLab (Eurecom)](https://gitlab.eurecom.fr/oai/freediameter).
- [Open Diameter](https://sourceforge.net/projects/diameter/) - Open source C++ implementation of the Diameter protocol, licensed under GPLv2/LGPLv2. Hosted on **SourceForge**.
- [eradius](https://github.com/travelping/eradius) `[2026-01]` - Erlang RADIUS server framework. From Travelping.

### SS7/SIGTRAN

- [go-m3ua](https://github.com/wmnsk/go-m3ua) `[2026-01]` - Package m3ua provides easy and painless handling of M3UA protocol in pure Golang.
- [go-sccp](https://github.com/wmnsk/go-sccp) `[2025-06]` - Package sccp provides simple and painless handling of SCCP(Signaling Connection Control Part) in SS7/SIGTRAN stack, implemented in the Go Programming Language.
- [libosmo-sccp](https://git.osmocom.org/libosmo-sccp/) - SCCP Library
- [go-tcap](https://github.com/wmnsk/go-tcap) `[2026-01]` - Package tcap provides simple and painless handling of TCAP(Transaction Capabilities Application Part) in SS7/SIGTRAN protocol stack.
- [openss7](http://www.openss7.org/) - An opensource development project (called OpenSS7) to provide a robust and GPL'ed SS7, SIGTRAN, ISDN and VoIP stack for Linux and other UN*X operating systems.
- [Extended jSS7](https://github.com/PAiC-team/Extended-jSS7) `[2023-07]` - Extended Java SS7 stack with MTP2/MTP3, ISUP, SCCP, TCAP, CAMEL (Phase I-IV) and MAP. Supports SIGTRAN (SCTP/M3UA) over IP.
- [signerl](https://gitea.osmocom.org/erlang/signerl/) - Erlang SS7 TCAP/MAP implementation. Originally from Motivity, continued within the Osmocom project. Hosted on **Osmocom Gitea**.
- [SigScale TCAP](https://github.com/sigscale/tcap) `[2025-01]` - SS7 Transaction Capabilities Application Part (TCAP) protocol stack in Erlang, used by MAP and CAP applications in mobile operator networks.

### Dataplane acceleration

- [fastswan](https://github.com/acassen/fastswan) `[2026-02]` - Linux Kernel XFRM/IPsec offload via eBPF/XDP. Relevant for mobile core SWu/N3IWF tunnels. From the gtp-guard/keepalived author.
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
- [MCC_MNC](https://github.com/P1sec/MCC_MNC) `[2024-07]` - Accurate MCC/MNC data as JSON and Python dicts, providing MNO public information. From P1 Security.
- [phonenumber-normalizer](https://github.com/telekom/phonenumber-normalizer) `[2026-01]` - Phone number normalization to E.164 and national formats in Go. From Deutsche Telekom.
- [OpenAPI-Dissector](https://github.com/telekom/OpenAPI-Dissector) `[2025-10]` - Experimental Wireshark dissector generator from OpenAPI specs, useful for 5G SBI protocol analysis. From Deutsche Telekom.
- [RTPproxy](https://github.com/sippy/rtpproxy) `[2026-01]` - High-performance RTP stream proxy, works with OpenSIPS, Kamailio, and Sippy B2BUA for VoIP/VoLTE media relay.


## Infrastructure

### NFV, Openstack

- [Openstack Kolla](https://github.com/openstack/kolla) `[2026-01]` - Production ready containers and Ansible tools for deploying an Openstack cluster to run NFV functions.
- ⚠️ [SNAPS-openstack](https://github.com/cablelabs/snaps-openstack) `[2021-09]` - Openstack deployment to be used on SNAPS booted machine from Cablelabs.
- [OPNFV](https://www.opnfv.org/software/downloads) - The OPNFV project addresses a number of aspects in the development of a consistent virtualisation platform including common hardware requirements, software architecture, MANO and applications.

### Containers, Kubernetes

- [Kubernetes KubeADM](https://kubernetes.io/docs/reference/setup-tools/kubeadm/kubeadm/) - Deployment tool to create Kubernetes cluster.
- [Intel Multus CNI plugin](https://github.com/intel/multus-cni) `[2026-01]` - Multus CNI is a container network interface (CNI) plugin for Kubernetes that enables attaching multiple network interfaces to pods from Intel.
- [Intel SRVIOV/DPDK CNI plugin](https://github.com/intel/sriov-cni) `[2026-01]` - SR-IOV CNI plugin works with SR-IOV device plugin for VF allocation for a container.
- ⚠️ [Nokia Danm](https://github.com/nokia/danm/) `[2022-09]` - TelCo grade network management in a Kubernetes cluster from Nokia.
- ⚠️ [SNAPS-kubernetes](https://github.com/cablelabs/snaps-kubernetes) `[2021-12]` - Kubernetes deployment to be used on SNAPS booted machine from Cablelabs.
- [Free5GC on kubeCORD](https://github.com/sufuf3/kube5GC) `[2019-05]` - This project is for deploying Free5GC on kubeCORD.
- ⚠️ [CNCF CNF-Testbed](https://github.com/cncf/cnf-testbed) `[2024-02]` - The CNCF CNF Testbed provides reference code and test cases for running networking code on Kubernetes and OpenStack using emerging cloud native technologies in the Telecom domain.
- [towards5gs-helm](https://github.com/Orange-OpenSource/towards5gs-helm) `[2024-10]` - Helm charts for deploying free5GC and other 5G network functions on Kubernetes. From Orange.
- [free5gc-helm](https://github.com/free5gc/free5gc-helm) `[2026-02]` - Official Helm charts for deploying free5GC on Kubernetes.

### Baremetal management

- ⚠️ [SNAPS-boot](https://github.com/cablelabs/snaps-boot) `[2019-09]` - Baremetal cluster management solution to prepare for a Openstack or k8s deployment from Cablelabs.
- [MAAS](https://maas.io) - Self-service, remote installation of Windows, CentOS, ESXi and Ubuntu on real servers turns your data center into a bare-metal cloud - Metal As A Service.

## Orchestration

- [5g-sharp-orchestrator](https://github.com/Ethon-Shield/5g-sharp-orchestrator) `[2025-04]` - tool that serves as a comprehensive wrapper for configuring, deploying and monitoring 5G open-source network components, simplifying the orchestration process.
- [ETSI Open Source MANO (OSM)](https://osm.etsi.org/) - ETSI-hosted NFV Management and Orchestration (MANO) stack for multi-cloud Telco orchestration, with network slicing support (eMBB, URLLC, mMTC).
- [Open Baton](https://openbaton.github.io/) - ETSI NFV MANO compliant framework with TOSCA support and network slicing via SDN.
- [Nephio](https://github.com/nephio-project/nephio) `[2026-02]` - Kubernetes-based automation platform for deploying and managing 5G Network Functions and underlying infrastructure. Linux Foundation project.

## Lab & Testbeds

### Ready-to-Use Environments

- ⚠️ [Open5GS-VoLTE](https://github.com/miaoski/docker_open5gs) `[2021-05]` - Install-and-run lab for Open5GS + Kamailio IMS VoLTE study. _Consider using [herlesupreeth/docker_open5gs](https://github.com/herlesupreeth/docker_open5gs) instead._
- [Open5GS Docker](https://github.com/herlesupreeth/docker_open5gs) `[2026-02]` - Docker files to build and run open5gs in a docker by Herle Supreeth.
- [Open5gs-K8s-VyOS](https://dev.to/infinitydon/virtual-4g-simulation-using-kubernetes-and-gns3-3b7k) - This tutorial is about how to deploy a virtual 4G stack using GNS3 and Kubernetes.
- [mobile-env](https://github.com/stefanbschneider/mobile-env) `[2026-01]` - An open, minimalist Gym environment for autonomous coordination in wireless mobile networks.
- [OpenAICellular](https://openaicellular.github.io/oaic/quickstart.html) - OAIC is an open-source effort led by a consortium of academic institutions to provide fully open-source software architecture, library, and toolset that encompass both the AI controllers (OAIC-C) as well as an AI testing framework (OAIC-T).
- [sample configs](https://github.com/s5uishida/sample_config_misc_for_mobile_network) `[2026-01]` - Sample Configurations and Miscellaneous for Mobile Network.
- [free5gc-compose](https://github.com/free5gc/free5gc-compose) `[2026-02]` - Docker Compose files for deploying the full free5GC 5G core stack.
- [free5GLabs](https://github.com/free5gc/free5GLabs) `[2026-03]` - Hands-on labs to guide building 5G networks with free5GC.
- [open5gs-k8s](https://github.com/niloysh/open5gs-k8s) `[2025-12]` - Open5GS 5G Core on Kubernetes with Helm charts and deployment guides.
- [docker-open5gs (Borjis131)](https://github.com/Borjis131/docker-open5gs) `[2025-11]` - Open5GS 5G Core container images with Docker Compose deployments and Helm charts for Kubernetes.

### Remote control

- [OpenSTF](https://openstf.io) - Enable remote control of phone over ADB over an HTML5 interfaces.
- [Vyzor](http://vysor.io) - A window to your Android, streaming Android UI through ADB in a Google Chrome Browser app.

### GPS, Time

- ⚠️ [GPS-SDR-SIM](https://github.com/osqzss/gps-sdr-sim) `[2025-01]` - GPS signal generator with a SDR radio and ephemeris files.
- [Tools for MT3339](https://github.com/f5eng/mt3339-utils) `[2023-01]` - Ephemeris injector for MT3339-based GPS chipset

## Testing

- [ntt](https://github.com/nokia/ntt) `[2025-10]` - TTCN-3 test framework.
- [Eclipse Titan TTCN3](https://projects.eclipse.org/projects/tools.titan) - Eclipse Titan is a TTCN-3 compilation and execution environment with an  Eclipse-based IDE.
- [TTCN3vscode](https://github.com/nokia/vscode-ttcn3) `[2026-01]` - TTCN-3 vs code plugin
- [ixia-c](https://github.com/open-traffic-generator/ixia-c) `[2026-01]` - Ixia-c is a modern, powerful and API-driven traffic generator designed to cater to the needs of hyperscalers, network hardware vendors and hobbyists alike.
- [srsRAN_matlab](https://github.com/srsran/srsRAN_matlab) `[2026-01]` - MATLAB-based PHY-layer testing and verification tools for srsRAN. From SRS.
- [Telcometer](https://github.com/itsMohammadHeidari/Telcometer) `[2024-10]` - Diameter Credit-Control Application Load Testing script powered by [Grafana K6](https://github.com/grafana/k6)
- [Sionna](https://github.com/NVlabs/sionna) `[2025-12]` - GPU-accelerated open-source library from NVIDIA for link-level simulation of communication systems. Covers OFDM, MIMO, LDPC, Polar codes, and ray tracing for 5G/6G research.
- [Simu5G](https://simu5g.org/) - OMNeT++ based 5G network simulator for end-to-end performance evaluation.
- [ns-3 LTE/NR](https://gitlab.com/nsnam/ns-3-dev) `[2026-02]` - Discrete-event network simulator with LTE and 5G NR modules. Main development on **GitLab**.
- [5G-LENA](https://gitlab.com/cttc-lena/nr) `[2026-02]` - ns-3 NR module for 5G New Radio simulation (PHY/MAC/OFDMA, MIMO, NR-U, NR V2X). From CTTC OpenSim. [NR-U extension](https://gitlab.com/cttc-lena/nr-u). Hosted on **GitLab**.
- [Wireshark](https://gitlab.com/wireshark/wireshark) `[2026-02]` - Essential protocol analyzer with dissectors for GSMTAP, Diameter, GTP, S1AP, NGAP, SS7/TCAP and more. Main development on **GitLab**.
- [Seagull](https://gull.sourceforge.net/) - Multi-protocol traffic generator for IMS testing: Diameter (RFC3588) over TCP/SCTP, TCAP (over SS7/Sigtran), XCAP, Radius. From HP. [SourceForge](https://sourceforge.net/projects/gull/).
- [ETSI Forge Test Suites](https://forge.etsi.org/rep/explore/projects) - Official ETSI test suites in TTCN-3 and Robot Framework for telecom protocols (Diameter, GTP, S1AP, NAS, MEC, NFV). Hosted on **ETSI Forge (GitLab)**.

## Security

### Security Exploitation/fuzzing Frameworks

- ⚠️ [SigPloit](https://github.com/SigPloiter/SigPloit) `[2019-12]` - Telecom Signaling Exploitation Framework - SS7, GTP, Diameter & SIP.
- [5GC_API_parse](https://github.com/PentHertz/5GC_API_parse) `[2021-07]` - 5GC API parse is a BurpSuite extension allowing to assess 5G core network functions, by parsing the OpenAPI 3.0 not supported by previous OpenAPI extension in Burp, and generating requests for intrusion tests purposes.
- [FirmWire](https://github.com/FirmWire/FirmWire) `[2026-01]` - FirmWire is a full-system baseband firmware emulation platform for fuzzing, debugging, and root-cause analysis of smartphone baseband firmwares.
- [5Ghoul](https://github.com/asset-group/5ghoul-5g-nr-attacks) `[2025-11]` - 5G NR attack and fuzzing framework targeting Qualcomm and MediaTek 5G baseband implementations.
- [hexagon_fuzz](https://github.com/srlabs/hexagon_fuzz) `[2025-10]` - A fuzzing framework for Qualcomm Hexagon baseband firmware using QEMU system emulation, from SRLabs.
- [SIPVicious](https://github.com/EnableSecurity/sipvicious) `[2026-01]` - SIP/VoIP security testing toolset for auditing SIP-based VoIP systems.
- [SIMurai](https://github.com/tomasz-lisowski/simurai) `[2024-08]` - SIM card fuzzer and security research tool (USENIX Security 2024). From the author of swSIM/swICC.
- [SentryPeer](https://github.com/SentryPeer/SentryPeer) `[2026-02]` - SIP honeypot for detecting and preventing VoIP fraud with peer-to-peer threat intelligence sharing. Also on [Codeberg](https://codeberg.org/SentryPeer/SentryPeer).
- [Sni5Gect](https://github.com/asset-group/Sni5Gect-5GNR-sniffing-and-exploitation) `[2026-01]` - 5G NR sniffer and downlink injector framework with Wireshark support. From the 5Ghoul team.
- [LLFuzz](https://github.com/SysSec-KAIST/LLFuzz) `[2026-02]` - Over-the-air dynamic testing framework for cellular baseband lower layers (PDCP, RLC, MAC, PHY). Found 11 unknown memory corruptions. USENIX Security 2025. From KAIST.
- [CITesting](https://github.com/SysSec-KAIST/CITesting) `[2026-01]` - Systematic testing of context integrity violations in LTE core networks. ACM CCS '25 Distinguished Paper. From KAIST.
- [BaseBridge](https://github.com/FirmWire/BaseBridge) `[2026-01]` - FirmWire extension that bridges emulation and over-the-air testing by restoring connection state from physical phone memory dumps. Up to 5x fuzzing coverage boost.
- [ShannonLoader](https://github.com/FirmWire/ShannonLoader) `[2026-02]` - Ghidra plugin for reverse engineering Samsung Shannon baseband firmware.
- [5G_ciphered_NAS_decipher_tool](https://github.com/PentHertz/5G_ciphered_NAS_decipher_tool) `[2025-11]` - Python tool to decipher 5G ciphered NAS messages and export to Wireshark pcap. From PentHertz.
- [gea-implementation](https://github.com/P1sec/gea-implementation) `[2026-02]` - GEA-1 and GEA-2 (GPRS Encryption Algorithm) stream cipher implementations in C, Python, and Rust. From P1 Security.
- [BaseSpec](https://github.com/SysSec-KAIST/BaseSpec) `[2021-03]` - Comparing cellular L3 protocol messages between 3GPP spec documents and baseband firmware implementations. From the LTESniffer team at KAIST.
- [DoLTEst](https://github.com/SysSec-KAIST/DoLTEst) `[2022-08]` - Negative testing framework for finding non-standard-compliant bugs in LTE protocol implementations of UEs. From KAIST.
- ⚠️ [Daedalus](https://github.com/IQTLabs/Daedalus) `[2024-05]` - Defensive response options for securing a 5G core network. From IQT Labs.
- [blue-merle](https://github.com/srlabs/blue-merle) `[2025-06]` - Enhances anonymity and reduces forensic traceability of 4G mobile Wi-Fi routers (IMEI change, MAC randomization). From SRLabs.
- [5GC_API_Pentest](https://github.com/PentHertz/5GC_API_Pentest) `[2025-12]` - Burp Suite extension for 5G Core SBI security testing with automated NF discovery, IMSI enumeration, OAuth2 workflows, and OpenAPI fuzzing. Successor to 5GC_API_parse. From PentHertz.

### IMSI Catcher Detection

- [Rayhunter](https://github.com/EFForg/rayhunter) `[2026-02]` - Rust tool to detect cell site simulators (IMSI catchers) on an Orbic mobile hotspot, from the EFF.
- [IMSI-catcher](https://github.com/Oros42/IMSI-catcher) `[2025-12]` - Python tool using gr-gsm to display IMSI numbers of cellphones around you.
- [Android-IMSI-Catcher-Detector](https://github.com/CellularPrivacy/Android-IMSI-Catcher-Detector) `[2026-01]` - Android app to detect IMSI catchers, StingRays, and silent SMS.

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
- [Introduce to 5GC](https://github.com/ianchen0119/Introduce-to-5GC) `[2022-07]` - 5GC & Cloud Native handbook (Traditional Chinese).
- [eUICC and eSIM Developer Manual](https://euicc-manual.osmocom.org) - Comprehensive eSIM developer documentation.
- [specpilot](https://github.com/herlesupreeth/specpilot) `[2025-09]` - AI-powered 3GPP specification assistant. From the author of docker_open5gs.

### Blogs

- [Nick vs Networking](https://nickvsnetworking.com/category/plmn/) - Telecommunications network engineering, from legacy to cutting-edge.
- [The 3G4G Blog](https://blog.3g4g.co.uk) - Latest news and information on 3G, 4G, 5G wireless technologies.
- [How LTE Stuff Works?](https://howltestuffworks.blogspot.com/) - In-depth blog on 4G/5G by a 3GPP Engineer.
- [Yoshiyuki Kurauchi](https://wmnsk.com/posts/) - Blog posts by a telecom/networking/security enthusiast.
- [Frédéric Launay](http://blogs.univ-poitiers.fr/f-launay/) - 🇫🇷 French blog on 4G/5G mobile networks.

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

## Contributing

Contributions welcome! Please read the contribution guidelines first. Open a PR or issue to add new resources.

## License

[MIT](LICENSE)
