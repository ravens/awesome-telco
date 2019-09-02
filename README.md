# awesome-telco
A curated list of telco resources and projects.

## Contents

- [SIM: USIM, SIM, eSIM](#SIMCards)
- [UE: phones, modems apps](#UE)
- [RAN: 2G, 3G, 4G, 5G](#RAN)
- [Core: EPC, MME, SGW, PGW](#Core)
- [Interco: IMS, SBC, Diameter](#interco)
- [Protocols: Libraries, Frameworks](#Protocols)
- [Infrastructure: SDN and NFV management software](#Infrastructure)
- [Security: Papers and talks around telco security](#Security)
- [Organizations: Orgs and forums working on telcos hardware/software](#Organizations)
- [Docs: Documentations and standards](#Docs)
- [Decks: Powerpoints and great slides](#Slides)
- [Tweets: Relevant tweets and link to social networks](#Tweets)
- [Issues: interesting issues on bugtrackers](#Issues)
- [Mailings-lists : ML, slack and other forums](#Mailing-lists)
- [Lab: tooling for telco labs](#Lab)

## SIMCards
- [PySIM](https://github.com/osmocom/pysim) - Tool to program sim card. Useful to manage and program blank SIM cards such as the sysmocom ones.
- [SIMTrace](http://osmocom.org/projects/simtrace) - Osmocom SIMtrace is a hardware device and associated firmware + host software to trace the communication between phone and SIM card.
- [SIMTester](https://opensource.srlabs.de/projects/simtester) - SIMtester assess SIM card security in two dimensions : Cryptanalytic attack surface, Application attack surface.

## UE

### 4G

- [srsUE](https://github.com/srslte/srslte) - UE 4G modem part of the srsLTE project.
- [OAI UE](https://gitlab.eurecom.fr/oai/openairinterface5g/wikis/home) - Open Air Interface RAN 4G eNB/ 5G gNB to use on SDR-based radios. 
- [Amarisoft](https://www.amarisoft.com) - Commercial UE Emulator by Amarisoft, company co-founded by [Bellard](https://bellard.org) on his original LTE software modem [work](https://bellard.org/lte/).
- [LTE-CellScanner](https://github.com/Evrytania/LTE-Cell-Scanner) - This is a collection of tools to locate and track LTE basestation cells using
very low performance RF front ends.
- [LTE-CellScanner-SDR-X](https://github.com/JiaoXianjun/LTE-Cell-Scanner) - An OpenCL accelerated TDD/FDD LTE Scanner (from rtlsdr/hackRF/bladeRF A/D samples to PDSCH output and RRC SIB messages decoded).


### Diagnostics, Monitor mode

- [SCAT](https://github.com/fgsect/scat) - this application parses diagnostic messages of Qualcomm and Samsung baseband through USB, and generates a stream of GSMTAP packet containing cellular control plane messages.
- [QCSuper](https://github.com/P1sec/QCSuper) - QCSuper is a tool communicating with Qualcomm-based phones and modems, allowing to capture raw 2G/3G/4G radio frames, among other things.
- [Network Signal Guru](http://m.qtrun.com/en/) - Android app able to parse Diag output from QC modem and display a lot of data for engineering field work.
- [Snoopsnitch](https://opensource.srlabs.de/projects/snoopsnitch)  - an opensource project focused on collecting data on existing network by performing passive and active tests and recovering the event through the DIAG protocol on a rooted Android phone.
- [Diag-parser](https://github.com/moiji-mobile/diag-parser) - Parse the Qualcomm DIAG format and convert 2G, 3G and 4G radio messages to Osmocom GSMTAP for analysis in wireshark and other utilities.
- [LTE_monitor_c2xx](https://github.com/P1sec/LTE_monitor_c2xx) - The purpose of LTE_monitor_c2xx is to provide a LTE message debugging solution for Samsung C2xx-based chipsets.
- [XGoldmon](https://github.com/2b-as/xgoldmon) - xgoldmon is a small tool to convert the messages output by the USB logging mode of phones with Intel/Infineon XGold baseband processor.

## RAN

### 4G

- [OAI eNB/ gNB](https://gitlab.eurecom.fr/oai/openairinterface5g/wikis/home) - Open Air Interface RAN 4G eNB / 5G NR gNB to use on SDR-based radios. 
- [srsLTE](https://github.com/srslte/srslte) - srsLTE eNB 4G to use on SDR-based radios. 
- [OpenLTE](http://openlte.sourceforge.net) - OpenLTE is an open source implementation of the 3GPP LTE specifications from Ben Wojtowicz.

### 3G

- [OpenUMTS](https://github.com/RangeNetworks/OpenBTS-UMTS) - 3G NodeB 

### 2G

- [OpenBTS](http://openbts.org) - 2G BTS with SDR-based radios.
- [YateBTS](https://wiki.yatebts.com/index.php/Main_Page) - 2G BTS with SDR-based radios.
- [OsmoTRX](http://osmocom.org/projects/osmotrx) - fork of OpenBTS tranceiver to use on SDR-based radios.
- [OsmoBTS](http://osmocom.org/projects/osmobts) - Open Source GSM BTS (Base Transceiver Station) with A-bis/IP interface.

### PHY 
- [gr-osmoSDR](http://osmocom.org/projects/gr-osmosdr) - Unified gnuradio input/output block for a variety of SDR devices, including FUNcube Dongle, OsmoSDR, RTL-SDR, MSi2500, SDRplay, SDR-IQ, AirSpy, rad10, HackRF, bladeRF, USSRP/UHD, UMtrx, RedPitaya, FreeSRP.
- [USRP B210](https://www.ettus.com/all-products/UB210-KIT/) - SDR Radio kit compatible with most of the SDR-based software modem implementations.
- [Kalibrate](https://github.com/steve-m/kalibrate-rtl) - Kalibrate, or kal, can scan for GSM base stations in a given frequency band and can use those GSM base stations to calculate the local oscillator frequency offset. 

## Core

### 4G

- [OAI EPC](https://github.com/OPENAIRINTERFACE/openair-cn/wiki) - MME and HSS functions from the OAI projects.
- [NextEPC](https://nextepc.org) - R13 4G EPC core with independent MME, HSS, SGW, PGW, PCRF functions. [github](https://github.com/nextepc/)
- [Open5gs](https://open5gs.org) - R14 4G EPC core with independent MME, HSS, SGW, PGW, PCRF functions. Follow-up of NextEPC. [github](https://github.com/open5gs)
- [Free5GC](https://bitbucket.org/nctu_5g/free5gc) - The free5GC is an open-source project for 5th generation (5G) mobile core network. Based on NextEPC.
- [Magma](https://github.com/facebookincubator/magma) - Rearchitected core network with access gateway (MME+P/SGW), federation gateway for auth (S6a) and billing (Gx, Gy). Initiated by FB on a the OAI EPC code base.
- [C3PO](https://github.com/omec-project/c3po) - HSS, CDF, CTF, PCRF around Cassandra DB, and backed by hardware security through SGX from the [OMEC](https://www.opennetworking.org/omec/).
- [NGIC-RTC](https://github.com/omec-project/ngic-rtc) - Control User Plane Separated (CUPS) architecture 3GPP TS23501 based implementation of EPC Service and Packet Gateway functions (SGW, PGW) from the [OMEC](https://www.opennetworking.org/omec/).
- [OpenMME](https://github.com/omec-project/openmme) - OpenMME is a grounds up implementation of the Mobility Management Entity EPC S1 front end to the Cell Tower (eNB) from the [OMEC](https://www.opennetworking.org/omec/).
- [srsEPC](https://github.com/srslte/srslte) - light-weight LTE core network implementation with MME, HSS and S/P-GW.
- [corenet](https://github.com/mitshell/corenet) - Minimal 3G and LTE / EPC core network using Pycrate library.
- [erGW](https://github.com/travelping/ergw) - This is a 3GPP GGSN and PDN-GW implemented in Erlang. 

### 3G

- [OsmoHNBGW](http://osmocom.org/projects/osmohnbgw) - An Open Source implenentation of a HNB-GW (HomeNodeB-Gateway), implementing the Iuh, IuCS and IuPS interfaces. It aggregates the Iuh links from femtocells (hNodeBs) and presents them as regular IuCS and IuPS towards MSC and SGSN.

### 2G 

- [OpenBSC](http://osmocom.org/projects/osmobsc) - OsmoBSC is an Open Source BSC (GSM Base Station Controller) with A-bis/IP and A/IP interface. It supports a variety of BTS Vendors/Models, including some Siemens, Nokia, Ericsson and ip.access models.
- [OsmoMSC](http://osmocom.org/projects/osmomsc) - It provides a 3GPP AoIP interface towards BSCs like OsmoBSC as well as 3GPP IuCS towards RNCs or HNB-GWs like OsmoHNBGW as well as GSUP towards OsmoHLR.

### OSS/BSS

- [Sigscale OCS](https://github.com/sigscale/ocs) - SigScale OCS includes a 3GPP AAA server function for authentication, authorization and accounting (AAA) of subscribers using DIAMETER or RADIUS protocols.
- [Bodastage CE](http://www.bodastage.org) - Boda Telecom Suite - Community Edition (BTS-CE) is an open source telecommunication network management platform for various RAN providers. [github](https://github.com/bodastage/bts-ce)

## Interco

### SBC, IMS

- [Freeswitch](https://freeswitch.org/confluence/display/FREESWITCH/Python_SBC) - Popular SIP stack that could be used as Session Border Controller (SBC)
- [IMS Clearwater](http://www.projectclearwater.org) - Clearwater is an open source implementation of IMS (the IP Multimedia Subsystem).
- [Kamalio](https://www.kamailio.org) - SIP stack used for VoLTE and SBC.

### SS7

- [Restcomm SS7](https://github.com/restcomm/jss7) - Open Source Java SS7 stack that allows Java apps to communicate with legacy SS7 communications equipment.
- [SigGW](https://github.com/P1sec/SigFW) - Open Source Signaling Firewall for SS7, Diameter filtering, antispoof and antisniff.

## Protocols

### GTP

- [Kernel GTP-U](http://osmocom.org/projects/linux-kernel-gtp-u) - This is an implementation of the GTP-U (user plane) inside the Linux kernel. 
- [go-GTP](https://github.com/wmnsk/go-gtp) - Package gtp provides simple and painless handling of GTP(GPRS Tunneling Protocol), implemented in the Go Programming Language.

### SCTP

- [go-SCTP](https://github.com/ishidawataru/sctp) - Stream Control Transmission Protocol (SCTP) in Go.
- [usrsctp](https://github.com/sctplab/usrsctp) - This is a userland SCTP stack supporting FreeBSD, Linux, Mac OS X and Windows.
- [PySCTP](https://github.com/P1sec/pysctp) - PySCTP - SCTP bindings for Python.

### Diameter

- [go-diameter](https://github.com/fiorix/go-diameter) - Package go-diameter is an implementation of the Diameter Base Protocol RFC 6733 and a stack for the Go programming language.
- [jdiameter](https://github.com/RestComm/jdiameter/) - RestComm jDiameter provides an Open Source Java implementation of the Diameter standard for Authentication, Authorization, and Accounting (AAA).

### SCCP

- [go-SCCP](https://github.com/wmnsk/go-sccp) - Package sccp provides simple and painless handling of SCCP(Signaling Connection Control Part) in SS7/SIGTRAN stack, implemented in the Go Programming Language.
- [libosmo-sccp](https://git.osmocom.org/libosmo-sccp/) - SCCP Library

### Dataplane acceleration

- [OVS](http://www.openvswitch.org) - Open vSwitch is a production quality, multilayer virtual switch licensed under the open source Apache 2.0 license.
- [FD.io](https://fd.io) - FD.io is a vector processing engine (VPP). VPP processes a number of packets in parallel instead of one at a time thus significantly improving packet throughput.
- [DPDK](https://www.dpdk.org) - DPDK is the Data Plane Development Kit that consists of libraries to accelerate packet processing workloads running on a wide variety of CPU architectures.

### Others

- [Pycrate](https://github.com/P1sec/pycrate) - the successor of the libmich library that is used to encode and decode data structures, including ASN.1 used in cellular protocol.
- [csdr](https://github.com/simonyiszk/csdr) - csdr is a command line tool to carry out DSP tasks for Software Defined Radio.
- [OGSLib](https://github.com/open5gs/ogslib) - state machine and utilities functions for NextEPC and Open5gs
- [DIAGLibrary](https://github.com/sanjaywave/DiagLibrary) -  a JNI library that implement a DIAG protocol parser under C code to be used under Android or Linux.


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

### Baremetal management

- [SNAPS-boot](https://github.com/cablelabs/snaps-boot) - Baremetal cluster management solution to prepare for a Openstack or k8s deployment from Cablelabs.
- [MAAS](https://maas.io) - Self-service, remote installation of Windows, CentOS, ESXi and Ubuntu on real servers turns your data center into a bare-metal cloud - Metal As A Service.

## Security

### Videos and papers

- [HITB talk : 4G LTE Man in the Middle Attack with a Hacked Femtocell](https://gsec.hitb.org/materials/sg2019/D2%20-%204G%20LTE%20Man%20in%20the%20Middle%20Attacks%20with%20a%20Hacked%20Femtocell%20-%20Xiaodong%20Zou.pdf) - high level talk on hacking 4G smallcell, sourcing, tools, opportunities including on S1 gateway.
- [Vulnerabilities in 5G](https://infosec.sintef.no/en/informasjonssikkerhet/2019/08/new-vulnerabilities-in-5g-security-architecture-countermeasures/) New vulnerabilities in 5G Security Architecture & Countermeasures.
- [QPSI-2019-LTEFuzz](https://www.youtube.com/watch?v=1ns46Uy1lM0&feature=youtu.be) - Security analysis of the LTE control plane with LTEFuzz, talk regarded at QPSI Product Security Summit.
- [LTEInspector: A Systematic Approach for Adversarial Testing of 4G LTE](https://www.youtube.com/watch?v=Cf6-O63vVdI) - Talk about LTE vulnerability research at NDSS 2018.
- [SS7: Locate. Track. Manipulate.](https://media.ccc.de/v/31c3_-_6249_-_en_-_saal_1_-_201412271715_-_ss7_locate_track_manipulate_-_tobias_engel) - Talk about SS7 vulnerability at 31C3.
- [SS7map : mapping vulnerability of the international mobile roaming infrastructure]() - Talk about SS7 vulnerability and introduction to [SS7map](https://ss7map.p1sec.com/) at 31C3.
- [Advanced interconnect attacks](https://media.ccc.de/v/camp2015-6785-advanced_interconnect_attacks) - Talk about GTP interconnection security at Chaos Communication Camp 2015.
- [Mobile Data Interception from the Interconnection Link](https://media.ccc.de/v/34c3-8879-mobile_data_interception_from_the_interconnection_link) - Talk about Diameter interconnection security at 34C3.

### Writeups

- [GSM capture, analysis and decoding](http://domonkos.tomcsanyi.net/?p=418) - four posts series on GSM cellular signal analysis.

## Organizations

- [Osmocom](http://osmocom.org) Umbrella for numerous opensource mobile communications projects.
- [Sysmocom](http://shop.sysmocom.de) Store frontend for [sysmocom](https://www.sysmocom.de), company providing product, support and services not only related to Osmocom.
- [Telecom Infra Project](https://www.telecominfraproject.com) - FB initiated project to create an equivalent of the OpenCompute project in the telco space.

## Docs

- [Wireless frequency bands](http://niviuk.free.fr/) - Come for the frequency calculator, stay for the cellular other resources.
- [ShareTechNote](http://www.sharetechnote.com/) - an impressive repo of knowledge for the cellular telco world.
- [3GPP specs](http://www.3gpp.org/ftp/Specs/html-info/36-series.htm) - 3GPP specs. 

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

## Lab

### remote control

- [OpenSTF](https://openstf.io) - Enable remote control of phone over ADB over an HTML5 interfaces. 
- [Vyzor](http://vysor.io) - A window to your Android, streaming Android UI through ADB in a Google Chrome Browser app.

### GPS, Time

- [GPS-SDR-SIM](https://github.com/osqzss/gps-sdr-sim) - GPS signal generator with a SDR radio and ephemeris files.
- [Tools for MT3339](https://github.com/f5eng/mt3339-utils) - Ephemeris injector for MT3339-based GPS chipset

## License

[MIT](LICENSE)
