# awesome-telco

A curated list of telco resources and projects.
Consult [awesome-5g](https://github.com/calee0219/awesome-5g) for 5G specific projects, which is probably more up to date on the matter than this one.

## Contents

- [SIM: USIM, SIM, eSIM](#SIMCards)
- [UE: phones, modems apps](#UE)
- [RAN: 2G, 3G, 4G, 5G](#RAN)
- [Core: EPC, MME, SGW, PGW](#Core)
- [Interco: IMS, SBC, Diameter](#interco)
- [Protocols: Libraries, Frameworks](#Protocols)
- [Satellite Communication: Monitoring and tooling](#Satcom)
- [Infrastructure: SDN and NFV management software](#Infrastructure)
- [Orchestration: Automation and integration software](#Orchestration)
- [Lab: tooling for telco labs](#Lab)
- [Testing : TTCN3 and others testing frameworks](#Testing)
- [Security: Papers and talks around telco security](#Security)
- [Blogs: Telco-related personal blogs](#Blogs)
- [Organizations: Orgs and forums working on telcos hardware/software](#Organizations)
- [Docs: Documentations and standards](#Docs)
- [Decks: Powerpoints and great slides](#Slides)
- [Tweets: Relevant tweets and link to social networks](#Tweets)
- [Issues: interesting issues on bugtrackers](#Issues)
- [Mailings-lists : ML, slack and other forums](#Mailing-lists)
- [Commercial Services around open source tech](#Commercial)

## SIMCards

- [PySIM](https://osmocom.org/projects/pysim/wiki) - Set of tools to read / explore / decode and program (write) SIM/USIM/ISIM cards. Useful to manage and program modifiable SIM cards such as the sysmocom ones.
- [sysmoISIM-SJA5](https://www.sysmocom.de/products/sim/sysmoisim-sja5/) - latest generation of programmable/modifiable SIM/UICC/USIM/ISIM card with support up to 3GPP Release 17. Ideal for any type of lab/research network (irrespective of RAN/CN vendor).
- [SIMTrace2](https://osmocom.org/projects/simtrace2) - Osmocom SIMtrace2 is a hardware device and associated firmware + host software to trace the communication between phone and SIM card.  Also supports emulating the card-side of the ISO7816 interface.  Firmware now also supports other hardware like [ngff-cardem](https://osmocom.org/projects/ngff-cardem/wiki)
- [SIMTester](https://opensource.srlabs.de/projects/simtester) - SIMtester assess SIM card security in two dimensions : Cryptanalytic attack surface, Application attack surface.
- [Njiwa - M2M UICC](https://github.com/brucedchen1991/njiwa) - Njiwa (Swahili for homing pigeon) is an implementation of the GSMA's Embedded SIM Remote Provisioning Manager for M2M devices. (Note: original repo is missing, replacing by a fork).
- [LPAd SM-DP+ Connector](https://github.com/Truphone/LPAd_SM-DPPlus_Connector) - Local Profile Assistant for Device (LPAd) - LPAd SM-DP+ Connector
- [sysmo-usim-tool](https://gitea.sysmocom.de/sysmocom/sysmo-usim-tool) - Utility for managing proprietary bits of sysmoUSIM/sysmoISIM programmable cards
- [GlobalPlatformPro](https://github.com/martinpaljak/GlobalPlatformPro) -  A tool to load and manage SIM applets on compatible JavaCards from command line from MArtin Paljak.
- [ARA-M Applet](https://github.com/bertrandmartel/aram-applet) -  ARA-M implementation for JavaCards by Bertrand Martel.
- [CoIMS_wiki](https://github.com/herlesupreeth/CoIMS_Wiki) - Guide for overriding IMS settings to force enable VoLTE/VoWiFi using Carrier Privileges, with its companion app on the Google Play store [CoIMS](https://play.google.com/store/apps/details?id=com.sherle.coims).
- [HelloSTK2](https://github.com/mrlnc/HelloSTK2) - My 2021's guide to HelloSTK [...] but maybe this "guide" helps you to build and install SIM-Toolkit applets.
- [Generic-eUICC-Test-Profile](https://github.com/GSMATerminals/Generic-eUICC-Test-Profile-for-Device-Testing-Public) - [...] to normalize the way in which Test Profiles for embedded UICCs will be available, and configurable, for industry standardised testing.
- [SUPI with pysim](https://gist.github.com/mrlnc/01d6300f1904f154d969ff205136b753) - Notes on enabling SUPI with pysim.
- [ScapySMS](https://github.com/mnemonic-no/ScapySMS) - A Scapy implementation of SMS-SUBMIT and (U)SIM Application Toolkit command packets.
- [ISD-R Access Provider](https://github.com/cheeriotb/ISD-R-AccessProvider) - This application contains a tiny content provider for communicating with ISD-R in eSIM soldered on Android device (developed for Pixel4).
- [asterix](https://github.com/suma12/asterix) - asterix is a framework for communication with smartcards based on pyscard.
- [SimServerAndroid](https://github.com/zhuowei/SimServerAndroid) - Gets SIM card ICCID/runs 3G Authentication over ADB shell.
- [swSIM](https://github.com/tomasz-lisowski/swsim) - A software-only SIM card.
- [swICC](https://github.com/tomasz-lisowski/swicc) - A framework for creating smart cards (ICC-based cards with contacts).
- [vsmartcard](https://github.com/frankmorgner/vsmartcard) - umbrella project for emulation of smart card readers or smart cards.
- [OpenEUICC](https://gitea.angry.im/PeterCxy/OpenEUICC) - (WIP) eSIM LPA (Local Profile Assistant) implementation for Android. System privilege required.
– [mobile-atlas](https://github.com/sbaresearch/mobile-atlas) - MobileAtlas implements the promising approach to geographically decouple SIM card and modem, which boosts the scalability and flexibility of the measurement platform.
- [osmo-remsim](https://osmocom.org/projects/osmo-remsim/wiki) - software suite permitting forwarding of SIM card traffic to a _remote_ SIM card (via TCP/IP).
- [lpac](https://github.com/estkme-group/lpac) - C-language implementation of a Consumer eSIM LPAd.  Can be used to download/activate/deactivate profiles on eUICC.
- [Onomondo UICC](https://github.com/onomondo/onomondo-uicc) - This repository contains a pure software implementation/emulation of the most relevant SIM/UICC/USIM functionalities.
- [EasyLPAC](https://github.com/creamlike1024/EasyLPAC) - lpac GUI Frontend for linux and OSX.


## UE

### 4G

- [srsUE](https://github.com/srslte/srslte) - UE 4G modem part of the srsLTE project.
- [srsUE PR external NAS](https://github.com/srsLTE/srsLTE/pull/474) - a PR for srsLTE for external NAS message injection.
- [OAI UE](https://gitlab.eurecom.fr/oai/openairinterface5g/wikis/home) - Open Air Interface RAN 4G eNB/ 5G gNB to use on SDR-based radios.
- [Amarisoft](https://www.amarisoft.com) - Commercial UE Emulator by Amarisoft, company co-founded by [Bellard](https://bellard.org) on his original LTE software modem [work](https://bellard.org/lte/).
- [LTE-CellScanner](https://github.com/Evrytania/LTE-Cell-Scanner) - This is a collection of tools to locate and track LTE basestation cells using very low performance RF front ends.
- [LTE-CellScanner-SDR-X](https://github.com/JiaoXianjun/LTE-Cell-Scanner) - An OpenCL accelerated TDD/FDD LTE Scanner (from rtlsdr/hackRF/bladeRF A/D samples to PDSCH output and RRC SIB messages decoded).
- [S1APTester](https://github.com/facebookexperimental/S1APTester) - A test tool that simulates the s1aptest functionality of a LTE network.

### 2G

- [OsmocomBB](https://osmocom.org/projects/baseband/wiki) - Open Source implementation of a 2G Mobile Station, including baseband firmware/PHY, L2, L3, etc.  Works with phones using TI Calypso chipset; SDR PHY is work-in-progress
- [FreeCalypso](https://www.freecalypso.org/) - Volunteer project building software derived from leaked source code for the TI calypso project

### Diagnostics, Monitor mode

- [SCAT](https://github.com/fgsect/scat) - this application parses diagnostic messages of Qualcomm and Samsung baseband through USB, and generates a stream of GSMTAP packet containing cellular control plane messages.
- [QCSuper](https://github.com/P1sec/QCSuper) - QCSuper is a tool communicating with Qualcomm-based phones and modems, allowing to capture raw 2G/3G/4G radio frames, among other things.
- [Network Signal Guru](http://m.qtrun.com/en/) - Android app able to parse Diag output from QC modem and display a lot of data for engineering field work.
- [Snoopsnitch](https://opensource.srlabs.de/projects/snoopsnitch)  - an opensource project focused on collecting data on existing network by performing passive and active tests and recovering the event through the DIAG protocol on a rooted Android phone.
- [Diag-parser](https://github.com/moiji-mobile/diag-parser) - Parse the Qualcomm DIAG format and convert 2G, 3G and 4G radio messages to Osmocom GSMTAP for analysis in wireshark and other utilities.
- [LTE_monitor_c2xx](https://github.com/P1sec/LTE_monitor_c2xx) - The purpose of LTE_monitor_c2xx is to provide a LTE message debugging solution for Samsung C2xx-based chipsets.
- [XGoldmon](https://github.com/2b-as/xgoldmon) - xgoldmon is a small tool to convert the messages output by the USB logging mode of phones with Intel/Infineon XGold baseband processor.
- [Modmobmap](https://github.com/PentHertz/Modmobmap) - Map 2G/3G/4G and more cellular networks in real live with a simple smart phone, pretty much like osmocomBB monitoring feature.
- [Modmobjam](https://github.com/PentHertz/Modmobjam) - A smart jamming proof of concept for mobile equipments that could be powered with Modmobmap tool.
- [LTESniffer](https://github.com/SysSec-KAIST/LTESniffer) - An Open-source LTE Downlink/Uplink Eavesdropper
- [FALCON](https://github.com/falkenber9/falcon) - FALCON - Fast Analysis of LTE Control channels.
- [osmo-qcdiag](https://osmocom.org/projects/osmo-qcdiag/wiki) - Osmocom project for decoding Qualcomm DIAG messages. Use @hoernchen/gsmtap@ branch to feed 2G/3G/4G/SIM messages from DIAG into wireshark ia GSMTAP.

## RAN

### RRH

- [O-RAN Software and seed code](https://o-ran-sc.org) - The O-RAN Software Community (SC) is a collaboration between the O-RAN Alliance and Linux Foundation with the mission to support the creation of software for the Radio Access Network (RAN). Introduction to O-RAN in a [LF video](https://www.youtube.com/watch?v=iJyb0pCWDKo).

### 5G

- [srsRAN_Project](https://github.com/srsran/srsRAN_Project) - A complete ORAN-native 5G RAN solution.
- [OAI NR](https://gitlab.eurecom.fr/oai/openairinterface5g/wikis/5g-nr-development-and-releases) - 5GNR related branch of the OAI code. You can follow the [weekly updates](https://trello.com/c/XBVaaHIO/26-5g-nr) to stay up to date.
- [UERANSIM](https://github.com/aligungr/UERANSIM) - UERANSIM is the state-of-the-art 5G UE and RAN (gNodeB) simulator. The project can be used for testing 5G Core Network and studying 5G System.
- [Software gNB for free5GC](https://github.com/Srajdax/gnb) - The gNB function was built on the model of the other free5GC CN functions using all the pattern and helper class defined by the free5GC team.
- [~~gnbsim~~](https://github.com/hhorai/gnbsim) - gnbsim is a 5G SA gNB/UE (Release 16) simulator for testing 5GC system. The project is aimed to understand 5GC system more efficiently than just reading 3GPP standard documents. _The original repo is not available. See [the forked repo](https://github.com/AlohaLuo/gnbsim-backup) instead._
- [5G-tools.com](https://5g-tools.com/) - 5G-tools.com is devoted to modern standards of wireless communications, such as 5G, 4G, etc. Main mission of site to give engineers the useful software tools to create a wireless network
- [corescope](https://github.com/srsran/corescope) - CoreScope combines gNodeB and UE components without any radio transmission.
- [my5G-RANTester](https://github.com/my5G/my5G-RANTester) - my5G-RANTester is a gNB/UE simulator for testing 3GPP standards and stressing a 5G core.
- [free5GRAN](https://github.com/free5G/free5GRAN) - free5GRAN is an open-source 5G RAN stack. The current version includes a receiver which decodes MIB & SIB1 data. It also acts as a cell scanner. free5GRAN works in SA mode. From Telecom Paris 5G laboratory - Institut Polytechnique de Paris.
- [pfm](https://github.com/arv-sajeev/pfm) - Implemented a prototype of gNB-CU-UP a network element of 5G Radio Network. Using DPDK, a set of data-plane processing libraries and NIC drivers for high speed packet processing applications.
- [PacketRusher](https://github.com/HewlettPackard/PacketRusher) - High performance 5G UE/gNB Simulator and CP/UP load tester. PacketRusher is an open-source tool dedicated to the performance testing and automatic validation of 5G Core Networks using simulated UE (user equipment) and gNodeB (5G base station). From Valentin D'Emmanuele - France.
- [py3gpp](https://github.com/catkira/py3gpp) - A Python package for 5G-NR simulations.
- [RFSwift](https://github.com/PentHertz/RF-Swift) -  powerful multi-platform RF toolbox that deploys specialized radio tools in seconds on Linux, Windows, and macOS. Provdes telecom_4G_5GNSA_* family of telecoms tools.

### 4G

- [OAI eNB/ gNB](https://gitlab.eurecom.fr/oai/openairinterface5g/wikis/home) - Open Air Interface RAN 4G eNB / 5G NR gNB to use on SDR-based radios.
- [srsLTE](https://github.com/srslte/srslte) - srsLTE eNB 4G to use on SDR-based radios.
- [LTE-ciphercheck](https://github.com/mrlnc/LTE-ciphercheck) - srsLTE derivative to check for cipher configuration of an LTE network - test across the 256 possibilities using an SDR radio.
- [OpenLTE](http://openlte.sourceforge.net) - OpenLTE is an open source implementation of the 3GPP LTE specifications from Ben Wojtowicz.
- [Cisco 4G nFAPI](https://github.com/cisco/open-nFAPI) - Open-nFAPI is implementation of the Small Cell Forum's network functional API or nFAPI for short. nFAPI defines a network protocol that is used to connect a Physical Network Function (PNF) running LTE Layer 1 to a Virtual Network Function (VNF) running LTE layer 2 and above.
- [CrocodileHunter](https://github.com/EFForg/crocodilehunter) - Crocodile Hunter is a tool to hunt fake eNodeBs, also known commonly as hailstorm, stingray, cell site simulators, or IMSI catchers. It works by listening for broadcast messages from all of the 4G stations in the area, inferring their location, and looking for unusual activity. From the EFF.
- [eNB s1 emulator](https://github.com/fasferraz/eNB) - This is an eNB emulator application done in python3 to interact with MME (S1AP) and SGW (S1-U). This application can be used to perform and simulate several EMM and ESM procedures, including user plane traffic. This application was tested with real MMEs (lab environment).
- [radisys_lte_enb_for_qualcomm_fsm9955](https://github.com/laf0rge/radisys_lte_enb_for_qualcomm_fsm9955) - Radisys Open Source code for a LTE eNB on Qualcomm FSM9955
- [sigover_injector](https://github.com/SysSec-KAIST/sigover_injector) - A tool for SigOver, signal overshadowing attack on the LTE broadcast signals in physical domain.

### 3G

- [OpenUMTS](https://github.com/RangeNetworks/OpenBTS-UMTS) - 3G NodeB
- [openbts-UMTS](https://github.com/PentHertz/OpenBTS-UMTS) - updated dependency and code to run OpenBTS-UMTS in 2023. Docker image available [here](https://hub.docker.com/r/penthertz/openbts-umts)
- [OsmoHNodeB](https://osmocom.org/projects/osmo-hnodeb) - Open Source implementation of the upper layers (RANAP/RUA/HNBAP/GTP/RTP) of a hNodeB.  Not usable standalone, requires lower-layer (RRC/RLC/MAC/PHY).

### 2G

- [OpenBTS](http://openbts.org) - 2G BTS with SDR-based radios.
- [YateBTS](https://wiki.yatebts.com/index.php/Main_Page) - 2G BTS with SDR-based radios.
- [OsmoTRX](https://osmocom.org/projects/osmotrx) - fork of OpenBTS tranceiver to use on SDR-based radios.
- [OsmoBTS](https://osmocom.org/projects/osmobts) - Open Source GSM BTS (Base Transceiver Station) with A-bis/IP interface.
- [OsmoPCU](https://osmocom.org/projects/osmopcu/wiki/OsmoPCU) - Open source GPRS PCU (Packet Control Unit) with Gb/IP interface. Supports OsmoBTS as well as Ericsson RBS2000/RBS6000.
- [OsmoBSC](https://osmocom.org/projects/osmobsc/wiki) - Open Source BSC (Base Station Controller) with Abis/E1 and Abis/IP support. Works with OsmoBTS, nanoBTS and various Nokia, Ericsson and Siemens BTS models.

### PHY
- [gr-osmoSDR](https://osmocom.org/projects/gr-osmosdr) - Unified gnuradio input/output block for a variety of SDR devices, including FUNcube Dongle, OsmoSDR, RTL-SDR, MSi2500, SDRplay, SDR-IQ, AirSpy, rad10, HackRF, bladeRF, USSRP/UHD, UMtrx, RedPitaya, FreeSRP.
- [USRP B210](https://www.ettus.com/all-products/UB210-KIT/) - SDR Radio kit compatible with most of the SDR-based software modem implementations.
- [Kalibrate](https://github.com/steve-m/kalibrate-rtl) - Kalibrate, or kal, can scan for GSM base stations in a given frequency band and can use those GSM base stations to calculate the local oscillator frequency offset.


## Core

### 5G

- [Open5GS](https://open5gs.org) - 5G, R14 4G EPC core with independent MME, HSS, SGW, PGW, PCRF, UPF, SMF, NRF functions. Follow-up of NextEPC. [github](https://github.com/open5gs)
- [OAI 5GCN](https://gitlab.eurecom.fr/oai/cn5g) - OAI(Open Air Interface) was initially developed by EURECOM, provides a 3GPP-Compliant 5G SA Core Network.
- [travelping-vpp](https://github.com/travelping/vpp) - UPF plugins implements a GTP-U user plane based on 3GPP TS 23.214 and 3GPP TS 29.244 Release 15, adding UPF as a plugin to VPP.
- [IITB 5G SBA PoC](https://github.com/iithnewslab/SBA-gRPC-5G) - Prototyping and Load Balancing the Service Based Architecture of 5G Core using NFV - [research paper from IITB](https://github.com/iithnewslab/SBA-gRPC-5G/blob/master/Presentation_Netsoft19_gRPC_5G.pdf)
- [Free5GC](https://www.free5gc.org/) - The free5GC is an open-source project for 5th generation (5G) mobile core network hosted by [CS Lab](https://cslab.cs.nycu.edu.tw/). Written in Golang. Associated github projects: [PER parser/encoder](https://github.com/free5gc/aper), [AMF](https://github.com/free5gc/amf).
- [5GC Swagger APIS](https://github.com/jdegre/5GC_APIs) - RESTful APIs of main Network Functions in the 3GPP 5G Core Network. R16.
- [5G GTP kernel driver](https://github.com/PrinzOwO/gtp5g) - gtp5g is a customized Linux kernel module 5G GTP-U to handle packet by PFCP IEs such as PDR and FAR. About more detail IEs, there are more information in 3GPP TS 29.281 and 3GPP TS 29.244.
- [UPF-EPC](https://github.com/omec-project/upf-epc) - UPF-EPC is a revised version of ngic-rtc's dp. it uses BESS as dataplane.
- [OpenUPF](https://github.com/5GOpenUPF/openupf) - A 3GPP R16 compliant open source 5G core UPF (User Plane Function).
- [Katana Slice Manager](https://github.com/medianetlab/katana-slice_manager) - Katana Slice Manager is a central software component responsible for controlling all the devices comprising the network, providing an interface for creating, modifying, monitoring and deleting slices.
- [my5G-core](https://github.com/my5G/my5G-core) - Currently, my5G-core is a fork of the free5GC project, with some extensions to facilitate the deployment.
- [III-5GC-Free-Trial](https://github.com/III-5GC/III-5GC-Free-Trial) - The basic III-5GC is a free trial for lab research, prototype product testing and simple 5G end-to-end demonstration.
- [upf-bpf](https://github.com/navarrothiago/upf-bpf) - An open source C++ library powered by eBPF/XDP for user plane in mobile core network (5G/LTE).
- [5G_CN](https://github.com/wnlUc3m/5G_CN) - This is a basic implementation of a 5G Core Network supporting 4G LTE control signalling.
- [openupf](https://github.com/5GOpenUPF/openupf) - A 3GPP R16 compliant open source 5G core UPF (User Plane Function).
- [upf-xdp](https://github.com/801room/upf-xdp) -  it shows the possibility of using xdp to implement 5g upf.
- [SD-Core](https://opennetworking.org/sd-core/) - A 4G/5G core that is based on [OMEC](https://www.opennetworking.org/omec/) for 4G, and a fork of [Free5GC](https://www.free5gc.org/) for 5G. Has implementations for AMF,SMF,PCF,UDM,AUSF,NSSF and a P4 based UPF. [github](https://github.com/omec-project/amf)
- [Magma](https://github.com/facebookincubator/magma) - Rearchitected core network with access gateway (MME+P/SGW), federation gateway for auth (S6a) and billing (Gx, Gy). Initiated by FB on a the OAI EPC code base.
- [5GCoreNetSDK](https://github.com/5GCoreNet/5GCoreNetSDK) - 5GCoreNetSDK is a fully-featured Golang SDK for developing inside 5GC (Release-18).
- [eupf](https://github.com/edgecomllc/eupf) - Open Source UPF built on eBPF.
- [qcore](https://github.com/nplrkn/qcore) - The world's most lightweight 5G Core (probably)

### 4G

- [OAI EPC](https://github.com/OPENAIRINTERFACE/openair-cn/wiki) - MME and HSS functions from the OAI projects.
- [NextEPC](https://nextepc.org) - R13 4G EPC core with independent MME, HSS, SGW, PGW, PCRF functions. [github](https://github.com/nextepc/)
- [Magma](https://github.com/facebookincubator/magma) - Rearchitected core network with access gateway (MME+P/SGW), federation gateway for auth (S6a) and billing (Gx, Gy). Initiated by FB on a the OAI EPC code base.
- [C3PO](https://github.com/omec-project/c3po) - HSS, CDF, CTF, PCRF around Cassandra DB, and backed by hardware security through SGX from the [OMEC](https://www.opennetworking.org/omec/).
- [NGIC-RTC](https://github.com/omec-project/ngic-rtc) - Control User Plane Separated (CUPS) architecture 3GPP TS23501 based implementation of EPC Service and Packet Gateway functions (SGW, PGW) from the [OMEC](https://www.opennetworking.org/omec/).
- [OpenMME](https://github.com/omec-project/openmme) - OpenMME is a grounds up implementation of the Mobility Management Entity EPC S1 front end to the Cell Tower (eNB) from the [OMEC](https://www.opennetworking.org/omec/).
- [srsEPC](https://github.com/srslte/srslte) - light-weight LTE core network implementation with MME, HSS and S/P-GW.
- [corenet](https://github.com/mitshell/corenet) - Minimal 3G and LTE / EPC core network using Pycrate library.
- [erGW](https://github.com/travelping/ergw) - This is a 3GPP GGSN and PDN-GW implemented in Erlang.
- [vEPC IITB](https://github.com/networkedsystemsIITB/NFV_LTE_EPC) - vEPC is a simple virtualized form of Long Term Evolution Evolved Packet Core (LTE EPC) from IITB india.
- [pyHSS](https://gitlab.com/nickvsnetworking/pyhss) - PyHSS is a simple Home Subscriber Server (HSS) used by LTE (4G) Evolved Packet Core (EPC) networks, written in Python. 3GPP network elements like the MME and PCRF communicate with the HSS via the DIAMETER protocol, with some extensions defined by 3GPP.
- [coreswitch](https://github.com/coreswitch/coreswitch) - coreswitch is an open soruce project for EPC (Evolved Packet Core) of LTE and 5G infrastructure. Right now we are implementing MME (Mobility Management Entity).
- [SGs](https://github.com/fasferraz/SGs) - This is a MSS SGs SCTP Server written in python3 that can be used with a MME to test some SGs features, like IMSI Attach, Location Update, SMS (Sending/Receiving/Alerting) or Paging (for SMS or CS-Fallback).
- [dra-guard](https://github.com/acassen/dra-guard) - DRA-Guard is a SCTP proxy offering access to Diameter payload.
- [gtp-guard](https://github.com/acassen/gtp-guard) - The main goal of this project is to provide robust and secure extensions to GTP protocol (GPRS Tunneling Protocol).

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

- [Sigscale OCS](https://github.com/sigscale/ocs) - SigScale OCS includes a 3GPP AAA server function for authentication, authorization and accounting (AAA) of subscribers using DIAMETER or RADIUS protocols.
- [Bodastage CE](http://www.bodastage.org) - Boda Telecom Suite - Community Edition (BTS-CE) is an open source telecommunication network management platform for various RAN providers. [github](https://github.com/bodastage/bts-ce)

## Interco

### SBC, IMS

- [Freeswitch](https://freeswitch.org/confluence/display/FREESWITCH/Python_SBC) - Popular SIP stack that could be used as Session Border Controller (SBC)
- [IMS Clearwater](http://www.projectclearwater.org) - Clearwater is an open source implementation of IMS (the IP Multimedia Subsystem).
- [Kamailio](https://www.kamailio.org) - SIP stack used for VoLTE and SBC.
- [go-eventsocket](https://github.com/fiorix/go-eventsocket) - FreeSWITCH Event Socket library for the Go programming language.

### SS7

- [Restcomm SS7](https://github.com/restcomm/jss7) - Open Source Java SS7 stack that allows Java apps to communicate with legacy SS7 communications equipment.
- [SigFW](https://github.com/P1sec/SigFW) - Open Source Signaling Firewall for SS7, Diameter filtering, antispoof and antisniff.
- [yate](https://github.com/yatevoip/yate) - Open Source Telephony engine with support of MTP2/MTP3 over TDM, M2PA, M2UA, M3UA, SCCP, TCAP

### SMPP

- [go-smpp](https://github.com/fiorix/go-smpp) - This is an implementation of SMPP 3.4 for Go, based on the original smpp34 from Kevin Patel.
- [Selenium SMPPSim](http://www.seleniumsoftware.com/downloads.html) - (software disappeared) - possible mirror [here](https://github.com/haifzhan/SMPPSim).
- [smppgui](https://github.com/ukarim/smppgui) - SMPP gui client

## Satellite Communication

### Ephemeris
- [Hughes_OneWeb_Monitor](https://github.com/nickvsnetworking/Hughes_OneWeb_Monitor) - Hughes OneWeb Terminal Prometheus Exporter 

## Protocols

### ASN1-based, S1AP/NGAP

- [Pycrate](https://github.com/pycrate-org/pycrate) - A Python library to ease the development of encoders and decoders for various protocols and file formats, especially telecom ones. Provides an ASN.1 compiler and a CSN.1 runtime.
- [bazel-pycrate](https://github.com/ravens/bazel-pycrate) - A bazel-based pycrate ready jupyter notebook env
- [hampi](https://github.com/gabhijit/hampi) - The Goal of this project is to implement an ASN.1 Compiler in Rust which can generate Rust bindings for different ASN.1 specifications.

### NAS 4G/5G and Milenage

- [mts-nas](https://github.com/ericsson-mts/mts-nas) - Project to decode/encode Non-Access Stratum (NAS) protocol.
- [LTE-security](https://fabricioapps.blogspot.com/2012/05/lte-security.html) - a Windows application that implements all the security procedures for LTE referred in Annex A and Annex B of 3GPP 33.401. Last update in 2020, direct [link](https://www.dropbox.com/s/adpa2yuac99riqt/LTE%20Security%203.3.zip?dl=0)
- [milenage](https://github.com/emakeev/milenage) - Go implementation of milenage ciphers.
- [nas-5gs](https://github.com/hzane/nas-5gs) - Routines for Non-Access-Stratum (NAS) protocol for NAS-NR(5GS).
- [oxirush-nas](https://github.com/linouxis9/oxirush-nas) - A Rust Library that allows the decoding/encoding of NAS-5G messages. From Valentin D'Emmanuele - France.

### GTP/PFCP

- [Kernel GTP-U](https://osmocom.org/projects/linux-kernel-gtp-u) - This is an implementation of the GTP-U (user plane) inside the Linux kernel.
- [go-gtp](https://github.com/wmnsk/go-gtp) - Package gtp provides simple and painless handling of GTP(GPRS Tunneling Protocol), implemented in the Go Programming Language.
- [go-pfcp](https://github.com/wmnsk/go-pfcp) - PFCP(Packet Forwarding Control Protocol) is a signaling protocol used in mobile networking infrastructure(LTE EPC, 5GC) to realize CUPS architecture(Control and User Plane Separation, not a printing system) defined in 3GPP TS29.244.
- [gtplib](https://github.com/travelping/gtplib) - Erlang GTPv1/GTPv2 library.
- [gtpv2](https://github.com/blorticus/gtpv2) - GPRS Tunneling Protocol Library for golang.
- [scapy-gtp](https://github.com/secdev/scapy/blob/master/scapy/contrib/gtp.py) - Scapy (A interactive packet manipulation program) GTP layer. Spec: 3GPP TS 29.060 and 3GPP TS 29.274. Some IEs: 3GPP TS 24.008.
- [gtp_dialer](https://github.com/fasferraz/gtp_dialer) - GTPv1/GTPv2 Dialer

### SCTP

- [sctp](https://github.com/ishidawataru/sctp) - Stream Control Transmission Protocol (SCTP) in Go.
- [usrsctp](https://github.com/sctplab/usrsctp) - This is a userland SCTP stack supporting FreeBSD, Linux, Mac OS X and Windows.
- [PySCTP](https://github.com/P1sec/pysctp) - PySCTP - SCTP bindings for Python.
- [MTS: Multiprotocol Test Tool](https://github.com/ericsson-mts/mts) - MTS (Multi-protocol Test Suite) is a multi-protocol testing tool specially designed for telecom IP-based architectures (see above "Features" section for more details).
- [scapy-sctp](https://github.com/secdev/scapy/blob/master/scapy/layers/sctp.py) - Scapy (A interactive packet manipulation program) SCTP layer.
- [ellora](https://github.com/gabhijit/ellora/) - Rust SCTP Toolkit. The Goal of this project is to make safe bindings for Linux SCTP stack that can be used within Rust's `async` ecosystem.

### VoWiFi/VoLTE

- [SWu-IKEv2](https://github.com/sysmocom/SWu-IKEv2) - This is a SWu client emulator done in python3 that establishes an IKEv2/IPSec tunnel with an ePDG. This application implements not only the control plane of SWu (IKEv2) but also the user plane (IPSec).
- [osmo-epdg](https://gitea.osmocom.org/erlang/osmo-epdg) - Implement an ePDG with an embedded AAA server. osmo-ePDG also requires a modify strongswan.


### Diameter

- [go-diameter](https://github.com/fiorix/go-diameter) - Package go-diameter is an implementation of the Diameter Base Protocol RFC 6733 and a stack for the Go programming language.
- [jdiameter](https://github.com/RestComm/jdiameter/) - RestComm jDiameter provides an Open Source Java implementation of the Diameter standard for Authentication, Authorization, and Accounting (AAA).
- [diafuzzer](https://github.com/Orange-OpenSource/diafuzzer) - Diameter fuzzer, based on specifications of Diameter applications following rfc 3588 / 6733 from Orange.
- [bromelia](https://github.com/heimiricmr/bromelia) - A Python micro framework for building Diameter protocol applications.

### SS7/SIGTRAN

- [go-m3ua](https://github.com/wmnsk/go-m3ua) - Package m3ua provides easy and painless handling of M3UA protocol in pure Golang.
- [go-sccp](https://github.com/wmnsk/go-sccp) - Package sccp provides simple and painless handling of SCCP(Signaling Connection Control Part) in SS7/SIGTRAN stack, implemented in the Go Programming Language.
- [libosmo-sccp](https://git.osmocom.org/libosmo-sccp/) - SCCP Library
- [go-tcap](https://github.com/wmnsk/go-tcap) - Package tcap provides simple and painless handling of TCAP(Transaction Capabilities Application Part) in SS7/SIGTRAN protocol stack.
- [openss7](http://www.openss7.org/) - An opensource development project (called OpenSS7) to provide a robust and GPL'ed SS7, SIGTRAN, ISDN and VoIP stack for Linux and other UN*X operating systems.

### Dataplane acceleration

- [Ligato](https://github.com/ligato/vpp-agent) - Controlplane agent for FD.io VPP
- [FD.io](https://fd.io) - FD.io is a vector processing engine (VPP). VPP processes a number of packets in parallel instead of one at a time thus significantly improving packet throughput.
- [OVS](http://www.openvswitch.org) - Open vSwitch is a production quality, multilayer virtual switch licensed under the open source Apache 2.0 license.
- [DPDK](https://www.dpdk.org) - DPDK is the Data Plane Development Kit that consists of libraries to accelerate packet processing workloads running on a wide variety of CPU architectures. [Vista Creek (FPGA-based baseband accelerator)](https://www.intel.com/content/www/us/en/wireline/products/programmable/applications/nfv.html) support has been added to [DPDK](https://doc.dpdk.org/guides/bbdevs/fpga_lte_fec.html).

### Others

- [open-nFAPI](https://github.com/cisco/open-nFAPI) - Open-nFAPI is implementation of the Small Cell Forum's network functional API or nFAPI for short. nFAPI defines a network protocol that is used to connect a Physical Network Function (PNF) running LTE Layer 1 to a Virtual Network Function (VNF) running LTE layer 2 and above.
- [CSDR](https://github.com/simonyiszk/csdr) - csdr is a command line tool to carry out DSP tasks for Software Defined Radio.
- [OGSLib](https://github.com/open5gs/ogslib) - state machine and utilities functions for NextEPC and Open5gs
- [DiagLibrary](https://github.com/sanjaywave/DiagLibrary) -  a JNI library that implement a DIAG protocol parser under C code to be used under Android or Linux.
- [5G Trace visualizer](https://github.com/telekom/5g-trace-visualizer) - DT set of Python scripts allow you to convert pcap, pcapng or pdml 5G protocol traces (Wireshark, tcpdump, ...) into SVG sequence diagrams.
- [sigshark](https://github.com/2b-as/sigshark) - Sigshark makes working with SS7 TCAP (MAP/CAP) and Diameter signaling pcap files easier. Its features include "flattening" (putting each SCTP chunk in its own packet) and transaction sorting/grouping.
- [ipccdownloader](https://github.com/mrlnc/ipcc-downloader) - Download IPCC Carrier Profiles
- [4g-speed](https://github.com/jake-cryptic/4g-speed) - 4G Theoretical Speed Calculator | FDD & TDD Support

Resources


## Infrastructure

### NFV, Openstack

- [Openstack Kolla](https://github.com/openstack/kolla) - Production ready containers and Ansible tools for deploying an Openstack cluster to run NFV functions.
- [SNAPS-openstack](https://github.com/cablelabs/snaps-openstack) - Openstack deployment to be used on SNAPS booted machine from Cablelabs.
- [OPNFV](https://www.opnfv.org/software/downloads) - The OPNFV project addresses a number of aspects in the development of a consistent virtualisation platform including common hardware requirements, software architecture, MANO and applications.

### Containers, Kubernetes

- [Kubernetes KubeADM](https://kubernetes.io/docs/reference/setup-tools/kubeadm/kubeadm/) - Deployment tool to create Kubernetes cluster.
- [Intel Multus CNI plugin](https://github.com/intel/multus-cni) - Multus CNI is a container network interface (CNI) plugin for Kubernetes that enables attaching multiple network interfaces to pods from Intel.
- [Intel SRVIOV/DPDK CNI plugin](https://github.com/intel/sriov-cni) - SR-IOV CNI plugin works with SR-IOV device plugin for VF allocation for a container.
- [Nokia Danm](https://github.com/nokia/danm/) - TelCo grade network management in a Kubernetes cluster from Nokia.
- [SNAPS-kubernetes](https://github.com/cablelabs/snaps-kubernetes) - Kubernetes deployment to be used on SNAPS booted machine from Cablelabs.
- [Free5GC on kubeCORD](https://github.com/sufuf3/kube5GC) - This project is for deploying Free5GC on kubeCORD.
- [CNCF CNF-Testbed](https://github.com/cncf/cnf-testbed) - The CNCF CNF Testbed provides reference code and test cases for running networking code on Kubernetes and OpenStack using emerging cloud native technologies in the Telecom domain. Provides simulated [network functions](https://github.com/cncf/cnf-testbed/tree/master/examples/network_functions).

### Baremetal management

- [SNAPS-boot](https://github.com/cablelabs/snaps-boot) - Baremetal cluster management solution to prepare for a Openstack or k8s deployment from Cablelabs.
- [MAAS](https://maas.io) - Self-service, remote installation of Windows, CentOS, ESXi and Ubuntu on real servers turns your data center into a bare-metal cloud - Metal As A Service.

## Orchestration

- [5g-sharp-orchestrator](https://github.com/Ethon-Shield/5g-sharp-orchestrator) - tool that serves as a comprehensive wrapper for configuring, deploying and monitoring 5G open-source network components, simplifying the orchestration process.

## Lab

### ready to use testbed (Docker, Vagrant etc.)

- [Open5GS-VoLTE](https://github.com/miaoski/docker_open5gs) - This repository is meant to be a install-and-run lab for Open5GS + Kamailio IMS VoLTE study, a follow-up project of Open5GS Tutorial: VoLTE Setup with Kamailio IMS and Open5GS, which is mainly contributed by Herle Supreeth.
- [Open5GS](https://github.com/herlesupreeth/docker_open5gs) - Docker files to build and run open5gs in a docker by Herle Supreeth.
- [Open5gs-K8s-VyOS](https://dev.to/infinitydon/virtual-4g-simulation-using-kubernetes-and-gns3-3b7k) - This tutorial is about how to deploy a virtual 4G stack using GNS3 and Kubernetes.
- [mobile-env](https://github.com/stefanbschneider/mobile-env) - An open, minimalist Gym environment for autonomous coordination in wireless mobile networks.
- [OpenAICellular](https://openaicellular.github.io/oaic/quickstart.html) - OAIC is an open-source effort led by a consortium of academic institutions to provide fully open-source software architecture, library, and toolset that encompass both the AI controllers (OAIC-C) as well as an AI testing framework (OAIC-T).
- [sample configs](https://github.com/s5uishida/sample_config_misc_for_mobile_network) - Sample Configurations and Miscellaneous for Mobile Network.

### Remote control

- [OpenSTF](https://openstf.io) - Enable remote control of phone over ADB over an HTML5 interfaces.
- [Vyzor](http://vysor.io) - A window to your Android, streaming Android UI through ADB in a Google Chrome Browser app.

### GPS, Time

- [GPS-SDR-SIM](https://github.com/osqzss/gps-sdr-sim) - GPS signal generator with a SDR radio and ephemeris files.
- [Tools for MT3339](https://github.com/f5eng/mt3339-utils) - Ephemeris injector for MT3339-based GPS chipset

## Testing

- [ntt](https://github.com/nokia/ntt) - TTCN-3 test framework.
- [Eclipse Titan TTCN3](https://projects.eclipse.org/projects/tools.titan) - Eclipse Titan is a TTCN-3 compilation and execution environment with an  Eclipse-based IDE.
- [TTCN3vscode](https://github.com/nokia/vscode-ttcn3) - TTCN-3 vs code plugin
- [ixia-c](https://github.com/open-traffic-generator/ixia-c) - Ixia-c is a modern, powerful and API-driven traffic generator designed to cater to the needs of hyperscalers, network hardware vendors and hobbyists alike.
- [Telcometer](https://github.com/itsMohammadHeidari/Telcometer) - Diameter Credit-Control Application Load Testing script powered by [Grafana K6](https://github.com/grafana/k6)

## Security

### Security Exploitation/fuzzing Frameworks

- [SigPloit](https://github.com/SigPloiter/SigPloit) - Telecom Signaling Exploitation Framework - SS7, GTP, Diameter & SIP.
- [5GC_API_parse](https://github.com/PentHertz/5GC_API_parse) - 5GC API parse is a BurpSuite extension allowing to assess 5G core network functions, by parsing the OpenAPI 3.0 not supported by previous OpenAPI extension in Burp, and generating requests for intrusion tests purposes.
- [FirmWire](https://github.com/FirmWire/FirmWire) - FirmWire is a full-system baseband firmware emulation platform for fuzzing, debugging, and root-cause analysis of smartphone baseband firmwares.

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

- [How the CCC Camp 2019 LTE network works](http://people.osmocom.org/laforge/slides/cccamp2019-how_the_camp_lte_works.pdf) - write up on reusing commercial Ericsson 4G units.
- [GSM capture, analysis and decoding](http://domonkos.tomcsanyi.net/?p=418) - four posts series on GSM cellular signal analysis.

## Blogs
- [Nick vs Networking](https://nickvsnetworking.com/category/plmn/) - So this blog focuses on telecommunications network engineering, from the very old (Shout out to the National Communications Museum), to very new and everything in between.
- [The 3G4G Blog](https://blog.3g4g.co.uk) - Latest news and information on 3G, 4G, 5G wireless and technologies in general.
- [Frédéric Launay - Les réseaux de mobiles 4G et 5G](http://blogs.univ-poitiers.fr/f-launay/) - [FR] Ce blog est un site de vulgarisation sur la téléphonie mobile de 4ème Génération ou 4G, du LTE et du web 2.O.
- [Yoshiyuki Kurauchi](https://wmnsk.com/posts/) - Blog posts by Yoshiyuki Kurauchi - A telecom / networking / security enthusiast.
- [How LTE Stuff Works?](https://howltestuffworks.blogspot.com/) - Blogs on 4G/5G by a 3GPP Engineer.

## Organizations

- [Osmocom](https://osmocom.org) Umbrella for numerous opensource mobile communications projects. Recordings of many great presentations can be found on their [OsmoDevCon](https://osmocom.org/projects/osmo-dev-con/wiki/OsmoDevCon) page (It's held online as [OsmoDevCall](https://osmocom.org/projects/osmo-dev-con/wiki/OsmoDevCall) lately).  They also have a web based [discourse forum](https://discourse.osmocom.org/)
- [Sysmocom](http://shop.sysmocom.de) Store frontend for [sysmocom](https://www.sysmocom.de), company providing product, support and services not only related to Osmocom.
- [Telecom Infra Project](https://www.telecominfraproject.com) - FB initiated project to create an equivalent of the OpenCompute project in the telco space.
- [3GPP Forge](https://forge.3gpp.org/rep/explore) - Forge for the 3GPP organization.

## Docs

- [Wireless frequency bands](http://niviuk.free.fr/) - Come for the frequency calculator, stay for the cellular other resources.
- [ShareTechNote](http://www.sharetechnote.com/) - an impressive repo of knowledge for the cellular telco world.
- [3GPP specs](http://www.3gpp.org/ftp/Specs/html-info/36-series.htm) - 3GPP specs.
- [CNTT](https://cntt-n.github.io/CNTT/) - set of reference specifications for NFVI coming from several telcos (Vodafone, Telstra, Orange mentionned as authors).
- [3gpp.guru](https://3gpp.guru) - look up 3GPP abbreviations
- [speX](https://spex.cor-net.org) - accessible 3GPP specs (PDF, DOC, HTML), [can be self-hosted](https://github.com/CoRfr/spex-3gpp)
- [tool3rd](https://github.com/proj3rd/tool3rd) - Assistant for 3GPP telecommunication development
- [3gpp-citations](https://github.com/martisak/3gpp-citations) - 3GPP Bibtex entry generator
- [3GPP-overall-architecture](https://github.com/nickel0/3GPP-Overall-Architecture) - very detailed, high-res PDF of the overall 3GPP architecture
- [Introduce to 5GC](https://github.com/ianchen0119/Introduce-to-5GC) - 5GC & Cloud Native handbook written in traditaional chinese
- [Getsi](https://getsi.org/) - Easy search engine for 3GPP specs
- [eUICC and eSIM Developer Manual](https://euicc-manual.osmocom.org)

## Slides

- [Kubernetes networking in the telco space](https://wiki.lfnetworking.org/download/attachments/328197/KubernetesNetworkingInTheTelcoSpace-Csatari.pdf?version=1&modificationDate=1522083330000&api=v2)

## Tweets

- [srsLTE 2G CSFB and PCAP fixes](https://twitter.com/LaF0rge/status/1158078169477292032)

## Issues

- [SCTP Kubernetes support](https://github.com/kubernetes/community/pull/2276)
- [SRSENB: Add SIB7 (GERAN neighbor) support](https://github.com/srsLTE/srsLTE/pull/361)

## Mailing-lists

- [OpenBSC](https://lists.osmocom.org/mailman/listinfo/openbsc)
- [OAI-user](http://lists.eurecom.fr/sympa/arc/openair5g-user)
- [OAI-devel](http://lists.eurecom.fr/sympa/arc/openair5g-devel)
- [OAI-corenetwork-user](http://lists.eurecom.fr/sympa/arc/openaircn-user)
- [OAI-corenetwork-devel](http://lists.eurecom.fr/sympa/arc/openaircn-devel)
- [magma-dev](https://groups.google.com/forum/#!forum/magma-dev)
- [magma-announce](https://groups.google.com/forum/#!forum/magma-announce)

## YouTube channels

- [penhertz](https://www.youtube.com/@Penthertz) - Official YT channel of Penthertz to talk about RF Hacking, Software-Defined Radio, and other tips and tricks!.

## Slacks

- [Magma](https://slack.magmacore.org/)

## Discord

- [Open5gs](https://discord.gg/M9ARcyvV)

## Commercial 
- [open-cells](https://open-cells.com): 4G and 5G, full open source can implement any test bed using cellular network
- [sysmocom](https://www.sysmocom.de): sysmocom fills a gap in the telecommunications market for development, products and services.
- [5ber esim](http://esim.5ber.com) - 5ber.eSIM card is a physical SIM card that complies with the GSMA standards that can store up to 15 eSIM profiles at the same time.
- [esim.me](https://esim.me) - physical sim card combined with a proprietary app that enable to load up to 15 eSIM on the physical sim card.

## License

[MIT](LICENSE)
