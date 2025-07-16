# Abstract

Low-Power Wide Area Networks (LPWANs) are communication networks designed for long-range data transmission for low-bandwidth, low-power devices such as IoT sensors. The low cost and low power consumption of LPWANs make them ideal for distributed IoT systems. LoRaWAN networks, based on the LoRa radio modulation technology, are the most adopted type of non-cellular LPWAN for IoT applications. In smart city solutions, LoRaWAN coverage and transmission ranges are affected by several factors including building obstacles, and the location of LoRaWAN gateways.

Through this project, we are not only able to test the coverage and transmission range of three LoRaWANs in the city of Munich, but also provide technical support and decision-making basis for urban digitization and IoT deployment, with clear engineering value and application prospects.

# Introduction




## LPWAN & LoRaWan
### LPWAN

Low Power Wide Area Networks (LPWANs) are a class of wireless communication networks designed to provide long-range, low-energy connectivity for large numbers of distributed sensing nodes. Its nodes are typically powered by batteries or energy harvesting and communicate at low rates (~300 bps to 50 kbps) to extend device range.

LPWAN nodes are connected to a LAN or the Internet through a gateway, and data

The plot above compares the LoRaWAN performance of two nodes operating at different Spreading Factors (SF): TTN1 at SF12 and TTN2 at SF7. The data was collected in room 0126, located very close to a TTN gateway.

Despite SF12 being designed for long-range and poor signal conditions, the success rate of TTN2-SF07 is slightly higher (65.01% overall, 69.23% in the last 5 minutes) compared to TTN1-SF12 (60.73% overall, 68.85% in the last 5 minutes). This result is consistent with the indoor, short-distance test environment, where high data rate and low airtime (as provided by SF7) lead to reduced channel occupancy and fewer collisions.

Furthermore, TTN2-SF07 exhibits stronger RSSI (around -45 dBm) and higher SNR (around 9–11 dB) compared to TTN1-SF12, which maintains lower RSSI (around -55 dBm) and slightly lower SNR. This suggests that under close-range conditions, using a lower spreading factor like SF7 not only ensures higher transmission efficiency but also achieves better signal quality and reliability.

These observations highlight the importance of choosing the appropriate spreading factor based on deployment context, with SF7 being advantageous in short-range, low-interference indoor environments like this one.

is typically forwarded by the gateway to a web server. The small size and low cost of this type of network device makes it suitable for large-scale IoT applications.

Typical representatives include LoRaWAN, NB-IoT, and Sigfox.

### LoRaWan

LoRaWAN is an LPWAN communication protocol and network architecture developed by the LoRa Alliance, a non-profit organization with more than 330 members, which employs LoRa modulation technology at the physical layer and enables upstream and downstream communication through multi-frequency points and channel hopping. It communicates in the license-free ISM band, which in Europe is concentrated at 868 MHz, without spectrum licensing fees, but the band is also often occupied by other devices (e.g., weather stations, remote controls, etc.), which can cause channel interference.

Low Power Wide Area Networks (LPWANs) are a class of wireless communication networks designed to provide long-range, low-energy connectivity to a large number of distributed sensing nodes. Its nodes are typically powered by batteries or energy harvesting and communicate at low rates (~300 bps to 50 kbps) to extend device range.LPWAN nodes are connected to a LAN or the Internet through a gateway, and data is typically forwarded by the gateway to a web server. The small size and low cost of this type of network device makes it suitable for large-scale IoT applications.

Typical representatives include LoRaWAN, NB-IoT, and Sigfox.

### LoRaWANs in Munich: A Parallel Pattern

​With the development of smart cities, low-power wide-area networks (LPWANs) have become the key infrastructure for city-level IoT deployment. Among them, LoRaWAN, as a representative technology, plays an increasingly important role in urban monitoring, resource management and data collection due to its advantages of long range, low power consumption and flexible deployment.

Now Munich's LPWAN development framework blends utility operations with community-driven innovation: Stadtwerke München (SWM) has partnered with Vantage Towers to build a citywide private LoRaWAN network, with around 80 gateways currently deployed for a variety of smart city scenarios such as groundwater monitoring, substation management, and building and energy system monitoring. Scenarios. 

In addition, community networks such as TTN and Helium are also expanding rapidly in Munich, providing more open network access and complementary coverage to form a multi-layered urban IoT network ecosystem.​​

### SWM:  Stadtwerke München

SWM is the Munich municipal utility company (Stadtwerke München) and its LoRaWAN network is part of the city's smart city strategy. As a key operator of local infrastructure, SWM owns a large number of power towers and high-rise buildings in the city, which enables it to establish high-density, high-altitude LoRa network nodes in Munich and the surrounding area for stable and extensive network coverage.
Unlike community-based networks, SWM's LoRaWAN network operates at a commercial level with a closed authorization access mechanism, primarily serving city administrations, utility companies, and enterprise customers. SWM's network enables long-term, reliable collection of data on water meters, electricity meters, energy consumption, environmental parameters, etc. It is one of the most reliable and suitable LoRaWAN networks for city-level applications in Munich.
With its emphasis on stability and data security, the SWM network is ideally suited for formal deployment projects with high reliability requirements, such as municipal monitoring, building energy management and infrastructure condition assessment.​

### TTN: The Things Network

The Things Network (TTN) is a global open source LoRaWAN networking platform with the core idea of “building an Internet of Things for everyone”.
In Munich, the TTN network is built and maintained by local universities, tech enthusiasts, developer communities, and some research institutes, forming an open LoRaWAN network ecosystem centered in the city's core and technology parks. Many of the gateways are deployed on university campuses, makerspaces, research labs, and even on the rooftops of individual homes. While the density and quality of deployment of these gateways varies, overall there is still good coverage in the center of Munich, the main TUM campus and some of the innovation districts.
The advantages of the TTN network are that it is free, open and easy to access, making it ideal for prototyping, academic research, teaching experiments and student projects. At the same time, however, the network's coverage and stability are limited by voluntary maintenance by community members and the lack of commercial support guarantees that performance fluctuations may occur in mission-critical or data-transfer-intensive scenarios.
