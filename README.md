Abstract

Low-Power Wide Area Networks (LPWANs) are communication networks designed for long-range data transmission for low-bandwidth, low-power devices such as IoT sensors. The low cost and low power consumption of LPWANs make them ideal for distributed IoT systems. LoRaWAN networks, based on the LoRa radio modulation technology, are the most adopted type of non-cellular LPWAN for IoT applications. In smart city solutions, LoRaWAN coverage and transmission ranges are affected by several factors including building obstacles, and the location of LoRaWAN gateways.

Through this project, we are not only able to test the coverage and transmission range of three LoRaWANs in the city of Munich, but also provide technical support and decision-making basis for urban digitization and IoT deployment, with clear engineering value and application prospects.

Introduction




LPWAN & LoRaWan
LPWAN

Low Power Wide Area Networks (LPWANs) are a class of wireless communication networks designed to provide long-range, low-energy connectivity for large numbers of distributed sensing nodes. Its nodes are typically powered by batteries or energy harvesting and communicate at low rates (~300 bps to 50 kbps) to extend device range.

LPWAN nodes are connected to a LAN or the Internet through a gateway, and data

The plot above compares the LoRaWAN performance of two nodes operating at different Spreading Factors (SF): TTN1 at SF12 and TTN2 at SF7. The data was collected in room 0126, located very close to a TTN gateway.

Despite SF12 being designed for long-range and poor signal conditions, the success rate of TTN2-SF07 is slightly higher (65.01% overall, 69.23% in the last 5 minutes) compared to TTN1-SF12 (60.73% overall, 68.85% in the last 5 minutes). This result is consistent with the indoor, short-distance test environment, where high data rate and low airtime (as provided by SF7) lead to reduced channel occupancy and fewer collisions.

Furthermore, TTN2-SF07 exhibits stronger RSSI (around -45 dBm) and higher SNR (around 9–11 dB) compared to TTN1-SF12, which maintains lower RSSI (around -55 dBm) and slightly lower SNR. This suggests that under close-range conditions, using a lower spreading factor like SF7 not only ensures higher transmission efficiency but also achieves better signal quality and reliability.

These observations highlight the importance of choosing the appropriate spreading factor based on deployment context, with SF7 being advantageous in short-range, low-interference indoor environments like this one.

is typically forwarded by the gateway to a web server. The small size and low cost of this type of network device makes it suitable for large-scale IoT applications.

Typical representatives include LoRaWAN, NB-IoT, and Sigfox.

LoRaWan

LoRaWAN is an LPWAN communication protocol and network architecture developed by the LoRa Alliance, a non-profit organization with more than 330 members, which employs LoRa modulation technology at the physical layer and enables upstream and downstream communication through multi-frequency points and channel hopping. It communicates in the license-free ISM band, which in Europe is concentrated at 868 MHz, without spectrum licensing fees, but the band is also often occupied by other devices (e.g., weather stations, remote controls, etc.), which can cause channel interference.

Low Power Wide Area Networks (LPWANs) are a class of wireless communication networks designed to provide long-range, low-energy connectivity to a large number of distributed sensing nodes. Its nodes are typically powered by batteries or energy harvesting and communicate at low rates (~300 bps to 50 kbps) to extend device range.LPWAN nodes are connected to a LAN or the Internet through a gateway, and data is typically forwarded by the gateway to a web server. The small size and low cost of this type of network device makes it suitable for large-scale IoT applications.

Typical representatives include LoRaWAN, NB-IoT, and Sigfox.

LoRaWANs in Munich: A Parallel Pattern

​With the development of smart cities, low-power wide-area networks (LPWANs) have become the key infrastructure for city-level IoT deployment. Among them, LoRaWAN, as a representative technology, plays an increasingly important role in urban monitoring, resource management and data collection due to its advantages of long range, low power consumption and flexible deployment.

Now Munich's LPWAN development framework blends utility operations with community-driven innovation: Stadtwerke München (SWM) has partnered with Vantage Towers to build a citywide private LoRaWAN network, with around 80 gateways currently deployed for a variety of smart city scenarios such as groundwater monitoring, substation management, and building and energy system monitoring. Scenarios. 

In addition, community networks such as TTN and Helium are also expanding rapidly in Munich, providing more open network access and complementary coverage to form a multi-layered urban IoT network ecosystem.​​

SWM:  Stadtwerke München

SWM is the Munich municipal utility company (Stadtwerke München) and its LoRaWAN network is part of the city's smart city strategy. As a key operator of local infrastructure, SWM owns a large number of power towers and high-rise buildings in the city, which enables it to establish high-density, high-altitude LoRa network nodes in Munich and the surrounding area for stable and extensive network coverage.
Unlike community-based networks, SWM's LoRaWAN network operates at a commercial level with a closed authorization access mechanism, primarily serving city administrations, utility companies, and enterprise customers. SWM's network enables long-term, reliable collection of data on water meters, electricity meters, energy consumption, environmental parameters, etc. It is one of the most reliable and suitable LoRaWAN networks for city-level applications in Munich.
With its emphasis on stability and data security, the SWM network is ideally suited for formal deployment projects with high reliability requirements, such as municipal monitoring, building energy management and infrastructure condition assessment.​

TTN: The Things Network

The Things Network (TTN) is a global open source LoRaWAN networking platform with the core idea of “building an Internet of Things for everyone”.
In Munich, the TTN network is built and maintained by local universities, tech enthusiasts, developer communities, and some research institutes, forming an open LoRaWAN network ecosystem centered in the city's core and technology parks. Many of the gateways are deployed on university campuses, makerspaces, research labs, and even on the rooftops of individual homes. While the density and quality of deployment of these gateways varies, overall there is still good coverage in the center of Munich, the main TUM campus and some of the innovation districts.
The advantages of the TTN network are that it is free, open and easy to access, making it ideal for prototyping, academic research, teaching experiments and student projects. At the same time, however, the network's coverage and stability are limited by voluntary maintenance by community members and the lack of commercial support guarantees that performance fluctuations may occur in mission-critical or data-transfer-intensive scenarios.

​Helium

Helium is a decentralized wireless network project that is unique in that it uses blockchain incentives to attract users around the world to deploy LoRa hotspots, thus enabling the expansion of LoRaWAN networks worldwide.
In Munich, the Helium network has been growing rapidly in recent years, with many users already installing hotspots on their own initiative, especially in residential neighborhoods, shared office spaces and areas with a high concentration of startups. Compared to traditional networks, Helium is more flexible and open, allowing any LoRaWAN-compatible device to be used without registration or access fees, making it ideal for individual projects, distributed sensor deployments, or teams looking to conduct quick experiments.
Since the distribution of network nodes relies on user deployment, the quality and online status of hotspot devices are somewhat uncertain, so the network performance may vary greatly in different regions and time periods. Especially in industrial or urban projects with high data accuracy and high availability requirements, Helium's uncertainty can be a limiting factor. However, for low-frequency, low-power transmission tasks, such as air quality monitoring and location tracking, Helium provides a low-cost, easy-to-access solution.

Hardware
Components
Microcontroller: Seeeduino LoRaWAN+GPS: Seeeduino LoRaWAN | Seeed Studio Wiki

Seeeduino LoRaWAN is an Arduino development board with LoRaWan protocol embedded, through which you can get started quickly to experience LoRa's advantage in the field of IoT. Based on the communication module RHF76-052AM, Seeeduino LoRaWAN is compatible with LoRaWAN Class A/C and supports a variety of communication frequencies.

Base Shield: Seed BaseShield v2.0 Base Shield V2 | Seeed Studio Wiki

In this section we are looking at the Seeed BaseShield v2.0. A Base Shield is a piece of hardware that can increase the number and types of grove ports you can use with your microcontroller. The BaseShield is constructed in a way, that it can be placed on top of every Arduino-based board. The Seeed BaseShield v2.0 has four analog, seven digital, four I2C and one UART port. Additionally it still has the Arduino-styled Input/Output Pins where you could attach more hardware. The Shield can be operated with an 3.3V and 5V operating voltage, which can be selected with a switch.

Temperature, humidity sensor (DHT-11): Grove - Temperature&Humidity Sensor (DHT11) | Seeed Studio Wiki

This is a powerful sister version of our Grove - Temperature&Humidity Sensor Pro. It has more complete and accurate performance than the basic version. The detecting range of this sensor is 5% RH - 99% RH, and -40°C - 80°C. And its accuracy reaches up to 2% RH and 0.5°C. A professional choice for applications that have relatively strict requirements.

Hardware Setup

Step 1. Connect Grove - Temperature&Humidity Sensor Pro to port A2 of Seeeduino microcontroller. (Port could be changed based on users' requirement)

Step 2. Plug Grove - Base Shield into Seeeduino.

Step 3. Connect Seeeduino to PC via a USB cable.

Software Setup

Step 1. Download the Seeed DHT library from Github.

Step 2. Refer to How to install library to install library for Arduino.

Step 3. Restart the Arduino IDE. Open “ DHTtester” example via the path: File --> Examples --> Grove_Humidity_Temperature_Sensor-master --> DHTtester. Through this demo, we can read the temperature and relative humidity information of the environment.

Step 4. Upload the demo. If you do not know how to upload the code, please check How to upload code.

Step 5. Open the Serial Monitor of Arduino IDE by click Tool-> Serial Monitor. Or tap the ++ctrl+shift+m++ key at the same time. if every thing goes well, you will get the result.

Temperature&Humidity&Pressure&Gas Sensor (BME680): Grove - Temperature Humidity Pressure Gas Sensor(BME680) | Seeed Studio Wiki 

The Grove-Temperature&Humidity&Pressure&Gas Sensor(BME680) is a multiple function sensor which can measure temperature, pressure, humidity and gas at the same time. It is based on the BME680 module and you can use this sensor in your GPS, IoT devices or other device which needs those four parameters.

Grove LCD: 16*2 LCD Display (white in blue): Grove - 16x2 LCD | Seeed Studio Wiki

The Grove-LCD Backlight display is operating on 5V and 3.3V and can be attached to a microcontroller via an I2C Grove connector. We are using two different versions of the display, one with one background colour and one with an adjustable RGB background colour. Both versions have two rows of each 16 programmable character slots.

Grove - 16 x 2 LCD is a perfect I2C LCD display for Arduino and Raspberry Pi with high contrast and easy deployment. 16x2 means two lines and each line has 16 columns, 32 characters in total. With the help of Grove I2C connector, only 2 signal pins and 2 power pins are needed. You don't even need to care about how to connect these pins. Just plug it into the I2C interface on Seeeduino or Arduino/Raspberry Pi+baseshield via the Grove cable. There won't be complicated wiring, soldering, worrying about burning the LCD caused by the wrong current limiting resistor.

LCD Setup

Step 1. Download the Grove-LCD RGB Backlight Library from Github.

Step 2. Refer to How to install library to install library for Arduino.

Step 3. Restart the Arduino IDE. Open the example

Grove GPS - Air530: Grove - GPS (Air530) | Seeed Studio Wiki

It’s a high-performance, highly integrated multi-mode statelite positioning and navigation module. It supports GPS / Beidou / Glonass / Galileo / QZSS / SBAS, which makes it suitable for GNSS positioning applications such as car navigation, smart wear and drone.

Cost-effective
Highly integrated Multi-mode statelite positioning and navigation
Compact size for easy deployment
Tiny volume and low power consumption

GPS Setup

Step 1. Connect Grove - GPS to port D2 of Grove-Base Shield.(Port could be changed based on users' requirement)
Step 2. Plug Grove - Base Shield into Seeeduino.
Step 3. Connect Seeeduino to PC via a USB cable

We also can view data in Google Earth:

Step 1. Click File -> Database Export -> Google Earth KML

Step 2. This should launch Google Earth with the history that was captured by u-center(u-center | u-blox).

Step 3. Alternatively, data can be recorded by pressing the red circle on the toolbar which will then ask where you want to save the record.

Step 4. When we have captured enough data, click the black square to stop recording.

Step 5. We can then convert the .ubx file generated to KML by using uploading the ubx file to GPSVisualizer, and the location (Red spot) would be shown on the map.

LoRa EU868: 868MHz LORA Antenna 5dBi Gain Omni SMA Female Connector + RF Antenna Adapter Cable 

This 868 MHz LoRa antenna offers strong, reliable connectivity with a 5 dBi gain, ideal for applications like paging systems, elevator monitoring, LoRa gateways, and routers.

Made of solid copper with a gold-plated finish, it ensures durability and excellent signal transmission. The antenna measures 19.5 cm and folds to 17 cm at a 90-degree angle for flexible installation.

It includes an adapter cable for quick setup without special tools. Optimized for the 868 MHz band, the antenna delivers stable, clear signals, making it a valuable addition to communication systems, including Meshtastic projects and receiver stations.




LoRaWAN antenna RO8061: 21702NM

Outdoor Fiberglass Omni Antenna 806-960 & 1710-2170 MHz with N-Male

Pulse announces a new outdoor radome omni antenna for 3G operations. The frequency range covers 806-960 and 1710-2170 MHz with peak gain levels of 1.5 and 2.5 dBi delivered in the lower and higher frequency bands respectively. The white Pultruded Fiberglass radome is 216 mm (8.5 inches) in height, UV protected and IP-67 rated. It has been tested to wind loading of 150 mph. 




Temperature, humidity and gas sensor (BME680): Grove - Temperature Humidity Pressure Gas Sensor(BME680) | Seeed Studio Wiki

The Grove-Temperature&Humidity&Pressure&Gas Sensor(BME680) is a multiple function sensor which can measure temperature, pressure, humidity and gas at the same time. It is based on the BME680 module and you can use this sensor in your GPS, IoT devices or other device which needs those four parameters.




vhbw GPS Antenna ⁣GPS Antenne passend für Plus, Blue Media, Magellan, Navigon Navi u.a. - Mit Magnetfuß, 5 m, MMCX-Anschluss, sc | 201250008

This reliable GPS antenna is fully compatible with navigation systems such as Plus Navi, offering excellent signal amplification for accurate positioning even in remote or urban areas. Its durable construction, long robust cable, and magnetic base ensure easy installation, secure mounting, and consistent performance.


Powerful GPS antenna with SMA connector, very good reception, reliable signal strength
Flexible placement in the car | Magnetic base for secure hold on the dashboard, glove box, etc.
Precisely manufactured plug for particularly space-saving and easy installation
Cable length: 5 m. As a replacement or additional antenna for GPS navigation systems. Repair your navigation system yourself
Box contents: 1x GPS antenna, accessories and spare parts such as cables, antennas, adapters and much more. vhbw







Setting-up
Environment Initial Setting-up

(Libraries?code?)

Sensor Test




TTN Connection

The Things Network (TTN) is a community-driven, open LoRaWAN network that offers free public access to LoRaWAN infrastructure in many cities worldwide, including Munich.
It is based on The Things Stack and provides a flexible platform for developing and testing LoRaWAN applications.
Device registration, network access, and documentation are available through the official TTN console and website.

Incoming packages (using one of the keys below) are listed here: https://gi3.gis.lrg.tum.de/nodered/ui

DevID

	

DevEUI

	

AppEUI

	

AppKey

	

User


eui-8765182202e81e1e	8765182202E81E1E	E89CE2FC9061426D	F9BD9ACB7CF00A1B3FF8177909C52689	Group-15
eui-8765182202e81e02	8765182202E81E02	E89CE2FC9061426D	67210B34155881B1F4E33F39F65A7951	Group-15
SWM Connection

The Munich public utility company, Stadtwerke München (SWM), kindly provides access to their city-wide LoRaWAN network for use in this course. Their infrastructure ensures comprehensive road-level coverage across Munich.
All necessary details for accessing and using the SWM LoRaWAN network can be found on this page.

Incoming packages (using one of the keys below) are listed here: https://gi3.gis.lrg.tum.de/nodered/ui




DevID

	

DevEUI

	

AppEUI

	

AppKey

	

User


gi3-2020-dev-29	0009296F1A9F134F	70B3D57ED002F952	5AD62F6D46B8AF52B942EEFBDD867863	Group-15
gi3-2020-dev-30	00876EA598282BF6	70B3D57ED002F952	681E6474FE2E68769D0869BF0E83A12E	Group-15
Helium Connection




Documents
Levchenko, P., Bankov, D., Khorov, E., Lyakhov, A., 2022. Performance Comparison of NB-Fi, Sigfox, and LoRaWAN. Sensors 22, 9633. https://doi.org/10.3390/s22249633.
Borsos, D., Lajos, B., 2022. Challenges of LoRaWAN technology in smart city solutions. Interdisciplinary Description of Complex Systems 20, 1–10. https://doi.org/10.7906/indecs.20.1.1
Supervision
Methodology
Hardware Implementation
Hardware Setting-up
Showing Temperature and Humidity directly on LCD 

LCD should be connected via I2C port, while HT22 using D2 port

#include <Wire.h>
#include "rgb_lcd.h"
#include "Grove_Temperature_And_Humidity_Sensor.h"

// LCD setup
rgb_lcd lcd;
const int colorR = 0;
const int colorG = 128;
const int colorB = 255;

// DHT setup
#define DHTPIN 2
#define DHTTYPE DHT22
DHT dht(DHTPIN, DHTTYPE);
    
void setup() {
    lcd.begin(16, 2);
    lcd.setRGB(colorR, colorG, colorB);
    Serial.begin(9600);

    dht.begin();

    lcd.setCursor(0, 0);
    lcd.print("Temp & Humidity");
    lcd.setCursor(0, 1);
    lcd.print("Initializing...");
    delay(2000);
    lcd.clear();
}

void loop() {
    float temp_hum_val[2] = {0};

    if (!dht.readTempAndHumidity(temp_hum_val)) {
        float humidity = temp_hum_val[0];
        float temperature = temp_hum_val[1];

        Serial.print("Temp: ");
        Serial.print(temperature);
        Serial.print(" C, Humi: ");
        Serial.print(humidity);
        Serial.println(" %");

        // LCD clear
        lcd.clear();
        lcd.setCursor(0, 0);
        lcd.print("Temp: ");
        lcd.print(temperature, 1); // %.1f
        lcd.print("C");

        lcd.setCursor(0, 1);
        lcd.print("Humi: ");
        lcd.print(humidity, 1);
        lcd.print("%");
    } else {
        Serial.println("Failed to read from DHT sensor.");
        lcd.clear();
        lcd.setCursor(0, 0);
        lcd.print("Read failed");
    }

    delay(2000);
}




Receiving GPS data

There are 2 types of GPS antenna available, here is the example with Grove-GPS(Air530)

The correct receiving message should be like example below:

This GPS data shows a valid fix with accurate position and time. The coordinates (48.0892741° N, 11.3413825° E) place the device in southern Germany. The fix time is 09:51:15 UTC on June 8, 2025. Multiple satellites are in view, and the antenna is connected and working properly. Overall, the GPS is functioning normally.




But sometimes, if test happens in indoor area, there might be very bad GPS signal and cause strange value like example below:




vhbw GPS antenna may show no different data structure, but the accuracy could be better and it could receive data from more satellites

The only solution would be moving the antenna to an open space so that it could receive data from more GPS satellites.

#include <SoftwareSerial.h>
SoftwareSerial SoftSerial(4, 3);			// using D4 port to avoid conflicting with Temp&Humi sensor (Eg: SoftSerial(2, 3); using D2 port)
unsigned char buffer[64];                   // buffer array for data receive over serial port
int count=0;                                // counter for buffer array
void setup()
{
    SoftSerial.begin(9600);                 // the SoftSerial baud rate
    Serial.begin(9600);                     // the Serial port of Arduino baud rate.
}
 
void loop()
{
    if (SoftSerial.available())                     // if date is coming from software serial port ==> data is coming from SoftSerial shield
    {
        while(SoftSerial.available())               // reading data into char array
        {
            buffer[count++]=SoftSerial.read();      // writing data into array
            if(count == 64)break;
        }
        Serial.write(buffer,count);                 // if no data transmission ends, write buffer to hardware serial port
        clearBufferArray();                         // call clearBufferArray function to clear the stored data from the array
        count = 0;                                  // set counter of while loop to zero
    }
    if (Serial.available())                 // if data is available on hardware serial port ==> data is coming from PC or notebook
    SoftSerial.write(Serial.read());        // write it to the SoftSerial shield
}
 
 
void clearBufferArray()                     // function to clear buffer array
{
    for (int i=0; i<count;i++)
    {
        buffer[i]=NULL;
    }                      // clear all index of array with command NULL
}
Data collection
Connecting with TTN 

By following Cayenne Protocol, TTN could be connected 

After all data-stream being built, roaming could be seen in Node-RED Dashboard

Right now, only Tem&Humi sensor's data are thrown to TTN and will be updated every 1 minutes. (GPS data is still not available)




Name

	

GroupNo

	

Thing

	

DevEUI

	

Sensor

	

ObservedProperty

	

LppChannelNr

	

FROST Datastream IDs




TUM-Group15

(testing with SF-12)

	

15

	

TUM-Group15-TTN-01 (thing_iot_id: 529)

	

TTN: 8765182202E81E1E

	

Seeed BME680

	

Temperature [°C]

	

1

	

1440(TTN)   1501(SWM)




TUM-Group15-SWM-01(thing_iot_id: 571)

	

SWM: 0009296F1A9F134F

	

Humidity [%H]

	

2

	

1499(TTN)   1554(SWM)



	
	

vhbw GPS

	

lat/lon/height

	

3

	

1576(SWM)






TUM-Group15

(testing with SF-7)

	

15

	

TUM-Group15-TTN-02 (thing_iot_id: 597)

	

TTN:8765182202E81E02

	

Grove DHT-11

	

Temperature [°C]

	

1

	

1601(TTN)   1599(SWM)




TUM-Group15-SWM-02(thing_iot_id: 596)

	

SWM:00876EA598282BF6

	

Humidity [%H]

	

2

	

1602(TTN)   1600(SWM)




// Seeeduino LoRaWAN ------------------------------------------------------------
#define PIN_GROVE_POWER 38
#define SerialUSB Serial
#include <SoftwareSerial.h>
#include <TinyGPS++.h>
#include <LoRaWan.h>
#include <CayenneLPP.h>
#include <SoftwareSerial.h>
#include "seeed_bme680.h"
#include "rgb_lcd.h"

// BME680 I2C setup
#define IIC_ADDR uint8_t(0x76)  // BME should always connect to a I2C portal !!!
Seeed_BME680 bme680(IIC_ADDR);

// LCD setup
rgb_lcd lcd;
const int colorR = 0;
const int colorG = 128;
const int colorB = 255;

// LoRa keys
// TTN 1 (SF12)
#define DevEUI "8765182202E81E1E"
#define AppEUI "E89CE2FC9061426D"
#define AppKey "F9BD9ACB7CF00A1B3FF8177909C52689"
// SWM 1 (SF12)
// #define DevEUI "0009296F1A9F134F"
// #define AppEUI "70B3D57ED002F952"
// #define AppKey "5AD62F6D46B8AF52B942EEFBDD867863"

// CayenneLPP
CayenneLPP lpp(51);

// GNSS SoftSerial
SoftwareSerial SoftSerial(2, 3);  // RX=D2 (connect GNSS TX), TX=D3
TinyGPSPlus gps; 

// buffer for GNSS
unsigned char gnss_buffer[64];
int gnss_count = 0;

// buffer for LoRa
char buffer[256];

void clearGnssBufferArray() {
  for (int i = 0; i < gnss_count; i++) {
    gnss_buffer[i] = NULL;
  }
}

void setup() {
  pinMode(LED_BUILTIN, OUTPUT);
  // LCD init
  lcd.begin(16, 2);
  lcd.setRGB(colorR, colorG, colorB);
  lcd.setCursor(0, 0);
  lcd.print("LCD Start OK");
  delay(2000);
  lcd.clear();

  // GNSS SoftSerial
  SoftSerial.begin(9600);
  Serial.begin(9600);

  // Grove power
  pinMode(PIN_GROVE_POWER, OUTPUT);
  digitalWrite(PIN_GROVE_POWER, 1);

  // BME680 init
  while (!bme680.init()) {
    lcd.clear();
    lcd.setCursor(0, 0);
    lcd.print("BME680 fail");
    Serial.println("bme680 init failed ! can't find device!");
    delay(5000);
  }
  lcd.clear();
  lcd.setCursor(0, 0);
  lcd.print("BME680 ready");

  // LoRa init
  lora.init();
  memset(buffer, 0, 256);
  lora.getVersion(buffer, 256, 1);
  Serial.print(buffer);
  memset(buffer, 0, 256);
  lora.getId(buffer, 256, 1);
  Serial.print(buffer);

  lora.setId(NULL, DevEUI, AppEUI);
  lora.setKey(NULL, NULL, AppKey);

  lora.setDeciveMode(LWOTAA);
  lora.setDataRate(DR0, EU868);   // DR5 = SF7, DR0= SF12
  lora.setAdaptiveDataRate(false); // true: auto change the best SF; False: unchangeble SF
  lora.setPower(14);
  lora.setPort(33);

  lora.setDutyCycle(false);
  lora.setJoinDutyCycle(false);

  // Channels
  lora.setChannel(0, 868.1);
  lora.setChannel(1, 868.3);
  lora.setChannel(2, 868.5);
  lora.setChannel(3, 867.1);
  lora.setChannel(4, 867.3);
  lora.setChannel(5, 867.5);
  lora.setChannel(6, 867.7);
  lora.setChannel(7, 867.9);

  // LoRa Join
  lcd.clear();
  lcd.setCursor(0, 0);
  lcd.print("+JOIN: Start");
  delay(500);

  unsigned int nretries = 0;
  while (!lora.setOTAAJoin(JOIN, 20)) {
    nretries++;
    lcd.clear();
    lcd.setCursor(0, 0);
    lcd.print("+JOIN: Fail");
    lcd.setCursor(0, 1);
    lcd.print("Retry: ");
    lcd.print(nretries);
    Serial.println((String) "Join failed, retry: " + nretries);
    delay(2000);
  }

  lcd.clear();
  lcd.setCursor(0, 0);
  lcd.print("+JOIN: Done");
  Serial.println("Join successful!");
  delay(1000);
}

unsigned int nloops = 0;
void loop() {
  nloops++;
  Serial.println((String)"Loop " + nloops + "...");

  lpp.reset();

  // Read BME680 data
  if (bme680.read_sensor_data()) {
    Serial.println("BME680 read failed");
    lcd.clear();
    lcd.setCursor(0, 0);
    lcd.print("BME read fail");
    lpp.addTemperature(1, -999);
  } else {
    float temperature = bme680.sensor_result_value.temperature;
    float humidity = bme680.sensor_result_value.humidity;

    lpp.addTemperature(1, temperature);
    lpp.addRelativeHumidity(2, humidity);

    lcd.clear();
    lcd.setCursor(0, 0);
    lcd.print("T:");
    lcd.print(temperature, 1);
    lcd.print("C H:");
    lcd.print(humidity, 1);
    lcd.print("%");

    Serial.print("Temp: ");
    Serial.print(temperature);
    Serial.print(" C, Humi: ");
    Serial.print(humidity);
    Serial.println(" %");
  }

  // LoRa send
  bool result = lora.transferPacket(lpp.getBuffer(), lpp.getSize(), 10);

  if (result) {
    short length, rssi;
    char rx[256];
    length = lora.receivePacket(rx, 256, &rssi);
    if (length) {
      Serial.print("Length: "); Serial.println(length);
      Serial.print("RSSI: "); Serial.println(rssi);
      Serial.print("Data: ");
      for (unsigned char i = 0; i < length; i++) {
        Serial.print("0x");
        Serial.print(rx[i], HEX);
        Serial.print(" ");
      }
      int rx_data_asInteger = atoi(rx);
      Serial.println();
      Serial.println("Received data: " + String(rx_data_asInteger));
    }
    lcd.setCursor(0, 1);
    lcd.print("LoRa Sent OK");
  } else {
    lcd.setCursor(0, 1);
    lcd.print("LoRa Send Fail");
  }

  // GNSS SoftSerial bridge
  while (SoftSerial.available()) {
    gps.encode(SoftSerial.read());
  }

  if (gps.location.isUpdated()) {
    float lat = gps.location.lat();
    float lon = gps.location.lng();
    float alt = gps.altitude.meters();

    String locStr = String("Location: ") + String(lat, 6) + ", " + String(lon, 6) + ", " + String(alt, 2);
    Serial.println(locStr);

    lpp.addGPS(3, lat, lon, alt);
  }

  if (Serial.available()) {
    SoftSerial.write(Serial.read());
  }

  Serial.println((String)"Loop " + nloops + "...done!\n");
  delay(20000);
  
  digitalWrite(LED_BUILTIN, HIGH);  // turn the LED on (HIGH is the voltage level)
  delay(1000);                      // wait for a second
  digitalWrite(LED_BUILTIN, LOW);   // turn the LED off by making the voltage LOW
  delay(1000);                      // wait for a second
}



In the test, we use 2 indipendent microcontroller connecting the LoRa. In this case, 2 different DevEUIs should be used and they use different sensors. So that all the frost things and datastreams should be changed

// Seeeduino LoRaWAN ------------------------------------------------------------
#define PIN_GROVE_POWER 38
#define SerialUSB Serial

#include <LoRaWan.h>
#include "Grove_Temperature_And_Humidity_Sensor.h"
#include "rgb_lcd.h"
#include <CayenneLPP.h>
#include <SoftwareSerial.h>

// DHT11 setup
#define DHTPIN A2              // Using DHT11 as input
#define DHTTYPE DHT11
DHT dht(DHTPIN, DHTTYPE);

// LCD setup
rgb_lcd lcd;
const int colorR = 0;
const int colorG = 128;
const int colorB = 255;

// LoRa keys
// TTN 2 (SF7)
#define DevEUI "8765182202E81E02"
#define AppEUI "E89CE2FC9061426D"
#define AppKey "67210B34155881B1F4E33F39F65A7951"
// SWM 2 (SF7)
// #define DevEUI "00876EA598282BF6"
// #define AppEUI "70B3D57ED002F952"
// #define AppKey "681E6474FE2E68769D0869BF0E83A12E"


// CayenneLPP
CayenneLPP lpp(51);

// GNSS SoftSerial
SoftwareSerial SoftSerial(2, 3);  // RX=D2 (connect GNSS TX), TX=D3

// buffer for GNSS
unsigned char gnss_buffer[64];
int gnss_count = 0;

// buffer for LoRa
char buffer[256];

void clearGnssBufferArray() {
  for (int i = 0; i < gnss_count; i++) {
    gnss_buffer[i] = NULL;
  }
}

void setup() {
  // Grove power
  pinMode(PIN_GROVE_POWER, OUTPUT);
  digitalWrite(PIN_GROVE_POWER, HIGH);

  // LCD init
  lcd.begin(16, 2);
  lcd.setRGB(colorR, colorG, colorB);
  lcd.setCursor(0, 0);
  lcd.print("LCD Start OK");
  delay(2000);
  lcd.clear();

  // DHT init
  dht.begin();

  // GNSS SoftSerial
  SoftSerial.begin(9600);
  Serial.begin(9600);

  // LoRa init
  lora.init();
  memset(buffer, 0, 256);
  lora.getVersion(buffer, 256, 1);
  Serial.print(buffer);
  memset(buffer, 0, 256);
  lora.getId(buffer, 256, 1);
  Serial.print(buffer);

  lora.setId(NULL, DevEUI, AppEUI);
  lora.setKey(NULL, NULL, AppKey);

  lora.setDeciveMode(LWOTAA);
  lora.setDataRate(DR5, EU868); 	// DR5=SF7  DR0=SF12  
  lora.setAdaptiveDataRate(false);  // false: dont allow automatic change
  lora.setPower(14);
  lora.setPort(33);

  lora.setDutyCycle(false);
  lora.setJoinDutyCycle(false);

  // Channels
  lora.setChannel(0, 868.1);
  lora.setChannel(1, 868.3);
  lora.setChannel(2, 868.5);
  lora.setChannel(3, 867.1);
  lora.setChannel(4, 867.3);
  lora.setChannel(5, 867.5);
  lora.setChannel(6, 867.7);
  lora.setChannel(7, 867.9);

  // LoRa Join
  lcd.clear();
  lcd.setCursor(0, 0);
  lcd.print("+JOIN: Start");
  delay(500);

  unsigned int nretries = 0;
  while (!lora.setOTAAJoin(JOIN, 20)) {
    nretries++;
    lcd.clear();
    lcd.setCursor(0, 0);
    lcd.print("+JOIN: Fail");
    lcd.setCursor(0, 1);
    lcd.print("Retry: ");
    lcd.print(nretries);
    Serial.println((String) "Join failed, retry: " + nretries);
    delay(2000);
  }

  lcd.clear();
  lcd.setCursor(0, 0);
  lcd.print("+JOIN: Done");
  Serial.println("Join successful!");
  delay(1000);
}

unsigned int nloops = 0;
void loop() {
  nloops++;
  Serial.println((String)"Loop " + nloops + "...");

  lpp.reset();

  // Read temp & humi
  float temp_hum_val[2] = {0};
  float temperature = 0;
  float humidity = 0;

  if (!dht.readTempAndHumidity(temp_hum_val)) {
    humidity = temp_hum_val[0];
    temperature = temp_hum_val[1];

    lpp.addTemperature(1, temperature);
    lpp.addRelativeHumidity(2, humidity);
	
    lcd.clear();
    lcd.setCursor(0, 0);
    lcd.print("T: ");
    lcd.print(temperature, 1);
    lcd.print("C H:");

    // lcd.setCursor(0, 1);
    // lcd.print("Humid: ");
    lcd.print(humidity, 1);
    lcd.print(" %");

    Serial.print("Temp: ");
    Serial.print(temperature);
    Serial.print(" C, Humi: ");
    Serial.print(humidity);
    Serial.println(" %");

  } else {
    lcd.clear();
    lcd.setCursor(0, 0);
    lcd.print("DHT read fail");
    lpp.addTemperature(1, -999);
    Serial.println("Failed to read from DHT sensor.");
  }

  // LoRa send
  bool result = lora.transferPacket(lpp.getBuffer(), lpp.getSize(), 10);
  

  if (result) {
    short length, rssi;
    char rx[256];
    length = lora.receivePacket(rx, 256, &rssi);
    if (length) {
      Serial.print("Length: "); Serial.println(length);
      Serial.print("RSSI: "); Serial.println(rssi);
      Serial.print("Data: ");
      for (unsigned char i = 0; i < length; i++) {
        Serial.print("0x");
        Serial.print(rx[i], HEX);
        Serial.print(" ");
      }
      int rx_data_asInteger = atoi(rx);
      Serial.println();
      Serial.println("Received data: " + String(rx_data_asInteger));
    }
    lcd.setCursor(0, 1);
    lcd.print("LoRa Sent OK");
  } else {
    lcd.setCursor(0, 1);
    lcd.print("LoRa Send Fail");

  }

  // GNSS SoftSerial bridge
  if (SoftSerial.available()) {
    while (SoftSerial.available()) {
      gnss_buffer[gnss_count++] = SoftSerial.read();
      if (gnss_count == 64) break;
    }
    Serial.write(gnss_buffer, gnss_count);
    clearGnssBufferArray();
    gnss_count = 0;
  }

  if (Serial.available()) {
    SoftSerial.write(Serial.read());
  }

  Serial.println((String)"Loop " + nloops + "...done!\n");
  delay(20000);
}






After successfully connecting to TTN, data could be copied through gi3.gis.lrg.tum.de/frost/v1.1/Things(529)/Datastreams(1440)/Observations?  (Time in UTC)

{
  "value": [
    {
      "@iot.selfLink": "https://gi3.gis.lrg.tum.de/frost/v1.1/Observations(230669806)",
      "@iot.id": 230669806,
      "phenomenonTime": "2025-06-08T14:34:04.978203Z",
      "resultTime": "2025-06-08T14:34:04.959895Z",
      "result": 33.0,
      "Datastream@iot.navigationLink": "https://gi3.gis.lrg.tum.de/frost/v1.1/Observations(230669806)/Datastream",
      "FeatureOfInterest@iot.navigationLink": "https://gi3.gis.lrg.tum.de/frost/v1.1/Observations(230669806)/FeatureOfInterest"
    },
    {
      "@iot.selfLink": "https://gi3.gis.lrg.tum.de/frost/v1.1/Observations(230669809)",
      "@iot.id": 230669809,
      "phenomenonTime": "2025-06-08T14:34:04.978203Z",
      "resultTime": "2025-06-08T14:34:04.959895Z",
      "result": 31.5,
      "Datastream@iot.navigationLink": "https://gi3.gis.lrg.tum.de/frost/v1.1/Observations(230669809)/Datastream",
      "FeatureOfInterest@iot.navigationLink": "https://gi3.gis.lrg.tum.de/frost/v1.1/Observations(230669809)/FeatureOfInterest"
    }
  ],
  "@iot.nextLink": "https://gi3.gis.lrg.tum.de/frost/v1.1/Things(529)/Datastreams(1440)/Observations?$skip=100&$orderby=%40iot.id+asc&$skipFilter=%28%40iot.id+gt+230669809%29"
}
Connecting with SWM 

By following Cayenne Protocol, SWM could be connected 

After all data-stream being built, roaming could be seen in Node-RED Dashboard

Right now, only Tem&Humi sensor's data are thrown to SWM and will be updated every 1 minutes. (GPS data is still not available)

// Seeeduino LoRaWAN ------------------------------------------------------------
#define PIN_GROVE_POWER 38
#define SerialUSB Serial
#include <SoftwareSerial.h>
#include <TinyGPS++.h>
#include <LoRaWan.h>
#include <CayenneLPP.h>
#include <SoftwareSerial.h>
#include "seeed_bme680.h"
#include "rgb_lcd.h"

// BME680 I2C setup
#define IIC_ADDR uint8_t(0x76)
Seeed_BME680 bme680(IIC_ADDR);

// LCD setup
rgb_lcd lcd;
const int colorR = 0;
const int colorG = 128;
const int colorB = 255;

// LoRa keys
// TTN 1 (SF12)
// #define DevEUI "8765182202E81E1E"
// #define AppEUI "E89CE2FC9061426D"
// #define AppKey "F9BD9ACB7CF00A1B3FF8177909C52689"
// SWM 1 (SF12)
#define DevEUI "0009296F1A9F134F"
#define AppEUI "70B3D57ED002F952"
#define AppKey "5AD62F6D46B8AF52B942EEFBDD867863"

// CayenneLPP
CayenneLPP lpp(51);

// GNSS SoftSerial
SoftwareSerial SoftSerial(2, 3);  // RX=D2 (connect GNSS TX), TX=D3
TinyGPSPlus gps; 

// buffer for GNSS
unsigned char gnss_buffer[64];
int gnss_count = 0;

// buffer for LoRa
char buffer[256];

void clearGnssBufferArray() {
  for (int i = 0; i < gnss_count; i++) {
    gnss_buffer[i] = NULL;
  }
}

void setup() {
  // LCD init
  lcd.begin(16, 2);
  lcd.setRGB(colorR, colorG, colorB);
  lcd.setCursor(0, 0);
  lcd.print("LCD Start OK");
  delay(2000);
  lcd.clear();

  // GNSS SoftSerial
  SoftSerial.begin(9600);
  Serial.begin(9600);

  // Grove power
  pinMode(PIN_GROVE_POWER, OUTPUT);
  digitalWrite(PIN_GROVE_POWER, 1);

  // BME680 init
  while (!bme680.init()) {
    lcd.clear();
    lcd.setCursor(0, 0);
    lcd.print("BME680 fail");
    Serial.println("bme680 init failed ! can't find device!");
    delay(5000);
  }
  lcd.clear();
  lcd.setCursor(0, 0);
  lcd.print("BME680 ready");

  // LoRa init
  lora.init();
  memset(buffer, 0, 256);
  lora.getVersion(buffer, 256, 1);
  Serial.print(buffer);
  memset(buffer, 0, 256);
  lora.getId(buffer, 256, 1);
  Serial.print(buffer);

  lora.setId(NULL, DevEUI, AppEUI);
  lora.setKey(NULL, NULL, AppKey);

  lora.setDeciveMode(LWOTAA);
  lora.setDataRate(DR0, EU868);   // DR5 = SF7, DR0= SF12
  lora.setAdaptiveDataRate(false); // true: auto change the best SF; False: unchangeble SF
  lora.setPower(14);
  lora.setPort(33);

  lora.setDutyCycle(false);
  lora.setJoinDutyCycle(false);

  // Channels
  lora.setChannel(0, 868.1);
  lora.setChannel(1, 868.3);
  lora.setChannel(2, 868.5);
  lora.setChannel(3, 867.1);
  lora.setChannel(4, 867.3);
  lora.setChannel(5, 867.5);
  lora.setChannel(6, 867.7);
  lora.setChannel(7, 867.9);

  // LoRa Join
  lcd.clear();
  lcd.setCursor(0, 0);
  lcd.print("+JOIN: Start");
  delay(500);

  unsigned int nretries = 0;
  while (!lora.setOTAAJoin(JOIN, 20)) {
    nretries++;
    lcd.clear();
    lcd.setCursor(0, 0);
    lcd.print("+JOIN: Fail");
    lcd.setCursor(0, 1);
    lcd.print("Retry: ");
    lcd.print(nretries);
    Serial.println((String) "Join failed, retry: " + nretries);
    delay(2000);
  }

  lcd.clear();
  lcd.setCursor(0, 0);
  lcd.print("+JOIN: Done");
  Serial.println("Join successful!");
  delay(1000);
}

unsigned int nloops = 0;
void loop() {
  nloops++;
  Serial.println((String)"Loop " + nloops + "...");

  lpp.reset();

  // Read BME680 data
  if (bme680.read_sensor_data()) {
    Serial.println("BME680 read failed");
    lcd.clear();
    lcd.setCursor(0, 0);
    lcd.print("BME read fail");
    lpp.addTemperature(1, -999);
  } else {
    float temperature = bme680.sensor_result_value.temperature;
    float humidity = bme680.sensor_result_value.humidity;

    lpp.addTemperature(1, temperature);
    lpp.addRelativeHumidity(2, humidity);

    lcd.clear();
    lcd.setCursor(0, 0);
    lcd.print("T:");
    lcd.print(temperature, 1);
    lcd.print("C H:");
    lcd.print(humidity, 1);
    lcd.print("%");

    Serial.print("Temp: ");
    Serial.print(temperature);
    Serial.print(" C, Humi: ");
    Serial.print(humidity);
    Serial.println(" %");
  }

  // LoRa send
  bool result = lora.transferPacket(lpp.getBuffer(), lpp.getSize(), 10);

  if (result) {
    short length, rssi;
    char rx[256];
    length = lora.receivePacket(rx, 256, &rssi);
    if (length) {
      Serial.print("Length: "); Serial.println(length);
      Serial.print("RSSI: "); Serial.println(rssi);
      Serial.print("Data: ");
      for (unsigned char i = 0; i < length; i++) {
        Serial.print("0x");
        Serial.print(rx[i], HEX);
        Serial.print(" ");
      }
      int rx_data_asInteger = atoi(rx);
      Serial.println();
      Serial.println("Received data: " + String(rx_data_asInteger));
    }
    lcd.setCursor(0, 1);
    lcd.print("LoRa Sent OK");
  } else {
    lcd.setCursor(0, 1);
    lcd.print("LoRa Send Fail");
  }

  // GNSS SoftSerial bridge
  while (SoftSerial.available()) {
    gps.encode(SoftSerial.read());
  }

  if (gps.location.isUpdated()) {
    float lat = gps.location.lat();
    float lon = gps.location.lng();
    float alt = gps.altitude.meters();

    String locStr = String("Location: ") + String(lat, 6) + ", " + String(lon, 6) + ", " + String(alt, 2);
    Serial.println(locStr);

    lpp.addGPS(3, lat, lon, alt);
  }

  if (Serial.available()) {
    SoftSerial.write(Serial.read());
  }

  Serial.println((String)"Loop " + nloops + "...done!\n");
  delay(20000);
}

After successfully connecting to TTN, data could be copied throughgi3.gis.lrg.tum.de/frost/v1.1/Things(571)/Datastreams(1501)/Observations  (Time in UTC)




To better connecting with the SWM-LoRaWAN, specific testing place is chosen at 5th floor of TUM building (same floor as DachCaffe) 







LoRaWAN Frost Downlink

By using Frost, the required parameters could be downloaded seperatly. The file is

All data could be downloaded via URL link frost/Things()/Datastreams()/Observations?  (eg: base_url = "https://gi3.gis.lrg.tum.de/frost/v1.1/Things(529)/Datastreams(1440)/Observations?$orderby=%40iot.id+asc" )

 The python codes below could help:

import requests
import pandas as pd

base_url = "https://gi3.gis.lrg.tum.de/frost/v1.1/Things(529)/Datastreams(1440)/Observations?$orderby=%40iot.id+asc"

results = []
times = []

url = base_url
while url:
    print(f"Fetching: {url}")
    response = requests.get(url)
    if response.status_code != 200:
        print(f"Error: {response.status_code}")
        break

    data = response.json()
    for obs in data.get("value", []):
        results.append(obs.get("result"))
        times.append(obs.get("phenomenonTime"))

    url = data.get("@iot.nextLink")


df = pd.DataFrame({
    "phenomenonTime": times,
    "result": results
})

#  Save as Excel
output_file = "observations.xlsx"
df.to_excel(output_file, index=False)
print(f"Saved to {output_file}")


After that, by using Matlab, a nice could be easily plotted.










LoRaWAN package logging

The successfully transformed LoRaWAN packages could be seen via: gi3.gis.lrg.tum.de/log/all?dev_eui=eq.8765182202E81E1E

All details about the device logging is stored in a json-format file. Here is an example block of the data we receive.

[
    {
        "msg_id": "d45d9c84b6203929",
        "dev_eui": "8765182202E81E1E",
        "ts": "2025-06-15T13:45:33.629084+00:00",
        "network": "ttn",
        "decoded_payload": {
            "temperature_1": 27.2,
            "relative_humidity_2": 58.5
        },
        "confirmed": false,
        "fcnt": 44,
        "port": 33,
        "bandwidth": 125000,
        "frequency": 867700000,
        "spreading_factor": 7,
        "coding_rate": "",
        "time_over_air": "0.056576s",
        "gateway_eui": "B827EBFFFE42A733",
        "snr": 9.5,
        "rssi": -63,
        "lat": 48.149113,
        "lon": 11.568094,
        "alt": 516
    }
]

This record shows that device 8765182202E81E1E sent data via TTN on 2025-06-15 13:45:33 UTC.
The payload includes temperature 27.2°C and relative humidity 58.5%.
The message was transmitted at 867.7 MHz, 125 kHz bandwidth, using spreading factor 7.
Signal quality: SNR 9.5 dB, RSSI -63 dBm.
The data was unconfirmed, airtime was about 0.0566 seconds.
The device location was lat 48.149113, lon 11.568094, alt 516 m.

To better abstract and filter the data from json file, the following python codes could be used to store the data in excel for easier analysis:

import requests
import pandas as pd

url = "https://gi3.gis.lrg.tum.de/log/all?dev_eui=eq.8765182202E81E1E"

response = requests.get(url)
if response.status_code != 200:
    print(f"Error: HTTP {response.status_code}")
    exit()

data = response.json()

# Abstract usable data
records = []
for item in data:
    decoded = item.get("decoded_payload", {})
    records.append({
        "network": item.get("network"),
        "temperature_1": decoded.get("temperature_1"),
        "relative_humidity_2": decoded.get("relative_humidity_2"),
        "spreading_factor": item.get("spreading_factor"),
        "snr": item.get("snr"),
        "rssi": item.get("rssi"),
        "lat": item.get("lat"),
        "lon": item.get("lon"),
        "timestamp": item.get("ts")
    })

# transform DataFrame
df = pd.DataFrame(records)

# save as Excel
output_file = "device_log.xlsx"
df.to_excel(output_file, index=False)
print(f"Data saved into {output_file}")

And to better visualize the stored data, the following Matlab codes would be helpful to plot the received data:

clear; clc; close all

data = readtable('device_log.xlsx');
time = datetime(data.timestamp,'InputFormat', 'yyyy-MM-dd''T''HH:mm:ss.SSSSSSXXX','TimeZone', 'UTC');

% The time limitation could be set to better filter out the data during our measuring time.
t_start = datetime(2025,6,15,9,0,0, 'TimeZone', 'UTC');
t_end   = datetime(2025,6,15,11,0,0, 'TimeZone', 'UTC');

idx = (time >= t_start) & (time <= t_end);
time_filtered = time(idx);
temp_filtered = data.temperature_1(idx);
humi_filtered = data.relative_humidity_2(idx);
snr = data.snr(idx);
rssi = data.rssi(idx);

figure;
subplot(2,1,1)
plot(time_filtered, snr, '-o', 'LineWidth', 1.2);	%SNR
xlabel('Time (UTC)');
ylabel('SNR');
title('SNR between 2025-06-15 09:00 and 11:00 (UTC)');
subplot(2,1,2)
plot(time_filtered, rssi, '-o', 'LineWidth', 1.2);	%RSSI
xlabel('Time (UTC)');
ylabel('RSSI');
title('RSSI between 2025-06-15 09:00 and 11:00 (UTC)');
grid on;
ax = gca;
ax.XAxis.TickLabelFormat = 'HH:mm:ss';

figure;
subplot(2,1,1)
plot(time_filtered, temp_filtered, '-o', 'LineWidth', 1.2);	%Temperature
xlabel('Time (UTC)');
ylabel('Temperature');
title('Temperature between 2025-06-15 09:00 and 11:00 (UTC)');
subplot(2,1,2)
plot(time_filtered, humi_filtered, '-o', 'LineWidth', 1.2);	%Humidity
xlabel('Time (UTC)');
ylabel('Humidity');
title('Humidity between 2025-06-15 09:00 and 11:00 (UTC)');
grid on;
ax = gca;
ax.XAxis.TickLabelFormat = 'HH:mm:ss';


For our project, the SNR(Signal Noise Rate) and the RSSI(Received Signal Strength), both of which present how good the signal is.

Higher SNR means the signal is clearer compared to background noise, while a stronger (less negative) RSSI indicates a better signal strength at the receiver. Together, these values help us evaluate the quality and reliability of our LoRa communication.




Only the latest 1000 messages are sent to the gi3.gis.lrg.tum.de/log/all?dev_eui=eq.8765182202E81E1E, so there is temporal limitation. 

This method may not be ideal for continuous long-term monitoring, but already meets the request for our scenario.

Real time monitoring the LoRa signal quality

This Python script enables real-time monitoring of LoRaWAN signal quality by continuously retrieving log data from the TUM GIS server every 30 seconds. It focuses on a specific device (identified by dev_eui), filtering records to include only those from the current day and within a defined geographic tolerance to ensure relevant and precise analysis.

All timestamps are converted to Europe/Berlin local time, providing accurate time representation in the local timezone, including daylight saving time adjustments. The script dynamically updates plots of Signal-to-Noise Ratio (SNR) and Received Signal Strength Indicator (RSSI) over time, allowing users to visually track the stability and performance of the LoRaWAN communication link as new data arrives.

In addition, the script calculates and displays two key success rates to help evaluate network conditions and detect potential issues in near real time:

Overall success rate: The ratio of received packets to expected packets since the first packet of the test, based on a 20-second device sampling interval.

5-minute window success rate: The ratio of received packets to expected packets within the most recent 5-minute window, providing insight into short-term performance.

This tool supports validation of LoRaWAN network stability and reliability in real-world deployments and assists in optimizing communication parameters.

The second test was done continuously in 2 different locations, as shown in the figure below, the signal strength changed on different locations (SNR&RSSI).

# This Python script continuously fetches LoRaWAN log data from the TUM GIS server every 30 seconds. 
# It filters records for a specific device and location, and plots SNR and RSSI over time using Berlin local time. 
# The script also calculates and displays the overall and recent 5-minute success rates, 
# showing how many packets were successfully received compared to the expected number based on a 20-second sampling interval.

import requests
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from datetime import datetime, timedelta, timezone
from zoneinfo import ZoneInfo

local_tz = ZoneInfo("Europe/Berlin")

import time

URL = "https://gi3.gis.lrg.tum.de/log/all"
DEV_EUI = "0009296F1A9F134F"
LAT_TOL = 0.0001
LON_TOL = 0.0001
POLL_INTERVAL = 30
REFERENCE_LAT = None
REFERENCE_LON = None

SAMPLE_INTERVAL = 20

plt.ion()
fig, ax = plt.subplots(2, 1, figsize=(10, 6))
all_data = pd.DataFrame()

def fetch_data():
    try:
        response = requests.get(URL, timeout=10)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Request Failed: {e}")
        return []

def filter_data(data):
    filtered = []
    today_local = datetime.now(local_tz).date()
    global REFERENCE_LAT, REFERENCE_LON
    
    for item in data:
        if item.get("dev_eui") != DEV_EUI:
            continue
        
        ts_str = item.get("ts", "")
        try:
            ts_dt_utc = pd.to_datetime(ts_str, utc=True)
            ts_dt_local = ts_dt_utc.astimezone(local_tz)
        except Exception as e:
            print(f"Invalid timestamp: {ts_str}, error: {e}")
            continue
        
        if ts_dt_local.date() != today_local:
            continue
        
        lat = item.get("lat")
        lon = item.get("lon")
        
        if lat is None or lon is None:
            continue
        
        if REFERENCE_LAT is None:
            REFERENCE_LAT = lat
            REFERENCE_LON = lon
        
        if abs(lat - REFERENCE_LAT) > LAT_TOL or abs(lon - REFERENCE_LON) > LON_TOL:
            continue
        
        filtered.append({
            "timestamp": ts_dt_utc,
            "timestamp_local": ts_dt_local,
            "snr": item.get("snr"),
            "rssi": item.get("rssi"),
            "temperature": item.get("temperature_1"),
            "relative_humidity": item.get("relative_humidity_2")
        })
    return filtered

def update_plot(df, overall_rate, recent_rate):
    ax[0].clear()
    ax[1].clear()
    
    if df.empty:
        print("Currently no useful data")
        return
    
    df_sorted = df.sort_values("timestamp_local")
    ax[0].plot(df_sorted["timestamp_local"], df_sorted["snr"], marker='o')
    ax[0].set_title(f"SNR over time (Local time)")
    ax[0].set_ylabel("SNR (dB)")
    
    ax[1].plot(df_sorted["timestamp_local"], df_sorted["rssi"], marker='o', color='orange')
    ax[1].set_title(f"RSSI over time (Local time)")
    ax[1].set_ylabel("RSSI (dBm)")

    # time_format = mdates.DateFormatter('%H:%M:%S')
    time_format = mdates.DateFormatter('%H:%M:%S', tz=local_tz)

    ax[0].xaxis.set_major_formatter(time_format)
    ax[1].xaxis.set_major_formatter(time_format)

    fig.suptitle(f"SWM LoRaWAN Connection \n Successful Rate Overall: {overall_rate:.2%}, 5min: {recent_rate:.2%}", fontsize=14)

    
    plt.tight_layout()
    plt.draw()
    plt.pause(0.1)

while True:
    data = fetch_data()
    records = filter_data(data)
    if records:
        df_new = pd.DataFrame(records)
        all_data = pd.concat([all_data, df_new]).drop_duplicates(subset=["timestamp"])
    
    if not all_data.empty:
        all_data["timestamp"] = pd.to_datetime(all_data["timestamp"], utc=True)
        if "timestamp_local" not in all_data.columns:
            all_data["timestamp_local"] = all_data["timestamp"].dt.tz_convert(local_tz)

        # Overall success rate
        start_ts_overall = all_data["timestamp"].min()
        latest_ts = all_data["timestamp"].max()
        elapsed_overall = (latest_ts - start_ts_overall).total_seconds()
        expected_overall = elapsed_overall / SAMPLE_INTERVAL
        actual_overall = len(all_data)
        success_overall = actual_overall / expected_overall if expected_overall > 0 else 0

        # 5 min window success rate
        start_ts_recent = datetime.now(timezone.utc) - timedelta(minutes=5)
        df_recent = all_data[all_data["timestamp"] >= start_ts_recent]
        if not df_recent.empty:
            latest_recent_ts = df_recent["timestamp"].max()
            elapsed_recent = (latest_recent_ts - start_ts_recent).total_seconds()
            expected_recent = elapsed_recent / SAMPLE_INTERVAL
            actual_recent = len(df_recent)
            success_recent = actual_recent / expected_recent if expected_recent > 0 else 0
        else:
            elapsed_recent = 0
            expected_recent = 0
            actual_recent = 0
            success_recent = 0

        print(f"[Overall] Elapsed: {elapsed_overall:.1f}s, Expected: {expected_overall:.1f}, Actual: {actual_overall}, Success: {success_overall:.2%}")
        print(f"[5min]    Elapsed: {elapsed_recent:.1f}s, Expected: {expected_recent:.1f}, Actual: {actual_recent}, Success: {success_recent:.2%}")
        print(f"Latest packet UTC: {latest_ts}, Local: {latest_ts.astimezone(local_tz)}")

        update_plot(all_data, success_overall, success_recent)
    
    time.sleep(POLL_INTERVAL)




The test was conducted on the balcony of OlympiaDorf. It is worth noting that the device was not directly connected to a computer, but was powered by a portable power bank.

This setup required all data transmission to be handled via LoRaWAN and also demonstrated the feasibility of using a power bank for the device. The successful operation provides a valuable reference for future practical data collection work.

Real-time Monitoring and Comparing

Since we now have 2 set up, the comparison between 2 different spreading-factors or 2 different LoRaWAN services could be compared in real time monitoring.

Name

	

GroupNo

	

Thing

	

DevEUI

	

Sensor

	

ObservedProperty

	

LppChannelNr

	

FROST Datastream IDs




TUM-Group15

(testing with SF-12)

	

15

	

TUM-Group15-TTN-01 (thing_iot_id: 529)

	

TTN: 8765182202E81E1E

	

Seeed BME680

	

Temperature [°C]

	

1

	

1440(TTN)   1501(SWM)




TUM-Group15-SWM-01(thing_iot_id: 571)

	

SWM: 0009296F1A9F134F

	

Humidity [%H]

	

2

	

1499(TTN)   1554(SWM)



	
	

vhbw GPS

	

lat/lon/height

	

3

	

1576(SWM)






TUM-Group15

(testing with SF-7)

	

15

	

TUM-Group15-TTN-02 (thing_iot_id: 597)

	

TTN:8765182202E81E02

	

Grove DHT-11

	

Temperature [°C]

	

1

	

1601(TTN)   1599(SWM)




TUM-Group15-SWM-02(thing_iot_id: 596)

	

SWM:00876EA598282BF6

	

Humidity [%H]

	

2

	

1602(TTN)   1600(SWM)

By monitoring the device logging from url like gi3.gis.lrg.tum.de/log/all?dev_eui=eq.8765182202E81E02, the SNR and RSSI could be easily seen and successful-rate could also be calculated like the previous step.

The plot above compares the LoRaWAN performance of two nodes operating at different Spreading Factors (SF): TTN1 at SF12 and TTN2 at SF7. The data was collected in room 0126, located very close to a TTN gateway.

Despite SF12 being designed for long-range and poor signal conditions, the success rate of TTN2-SF07 is slightly higher (65.01% overall, 69.23% in the last 5 minutes) compared to TTN1-SF12 (60.73% overall, 68.85% in the last 5 minutes). This result is consistent with the indoor, short-distance test environment, where high data rate and low airtime (as provided by SF7) lead to reduced channel occupancy and fewer collisions.

Furthermore, TTN2-SF07 exhibits stronger RSSI (around -45 dBm) and higher SNR (around 9–11 dB) compared to TTN1-SF12, which maintains lower RSSI (around -55 dBm) and slightly lower SNR. This suggests that under close-range conditions, using a lower spreading factor like SF7 not only ensures higher transmission efficiency but also achieves better signal quality and reliability.

These observations highlight the importance of choosing the appropriate spreading factor based on deployment context, with SF7 being advantageous in short-range, low-interference indoor environments like this one.

All of the process above could be done base on the codes below:

import requests
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from datetime import datetime, timedelta, timezone
from backports.zoneinfo import ZoneInfo
import time

# Timezone as local time
local_tz = ZoneInfo("Europe/Berlin")

URL = "https://gi3.gis.lrg.tum.de/log/all"
POLL_INTERVAL = 30
SAMPLE_INTERVAL = 20
LAT_TOL = 0.0001
LON_TOL = 0.0001

# Input DevEUIs and set their names and colors
DEVICES = {
    "8765182202E81E1E": "TTN1-SF12",
    "8765182202E81E02": "TTN2-SF07"
}
DEVICE_COLORS = {
    "8765182202E81E1E": "skyblue",
    "8765182202E81E02": "orange"
}

REFERENCE_COORDS = {}
all_data_dict = {dev_eui: pd.DataFrame() for dev_eui in DEVICES.keys()}

plt.ion()
fig, ax = plt.subplots(2, 1, figsize=(10, 6))

def fetch_data():
    try:
        response = requests.get(URL, timeout=10)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Request Failed: {e}")
        return []

def filter_data(data):
    filtered_dict = {dev_eui: [] for dev_eui in DEVICES.keys()}
    today_local = datetime.now(local_tz).date()

    for item in data:
        dev_eui = item.get("dev_eui")
        if dev_eui not in DEVICES:
            continue

        ts_str = item.get("ts", "")
        try:
            ts_dt_utc = pd.to_datetime(ts_str, utc=True)
            ts_dt_local = ts_dt_utc.astimezone(local_tz)
        except Exception as e:
            print(f"Invalid timestamp: {ts_str}, error: {e}")
            continue

        if ts_dt_local.date() != today_local:
            continue

        lat = item.get("lat")
        lon = item.get("lon")
        if lat is None or lon is None:
            continue

        if dev_eui not in REFERENCE_COORDS:
            REFERENCE_COORDS[dev_eui] = (lat, lon)

        ref_lat, ref_lon = REFERENCE_COORDS[dev_eui]
        if abs(lat - ref_lat) > LAT_TOL or abs(lon - ref_lon) > LON_TOL:
            continue

        filtered_dict[dev_eui].append({
            "dev_eui": dev_eui,
            "timestamp": ts_dt_utc,
            "timestamp_local": ts_dt_local,
            "snr": item.get("snr"),
            "rssi": item.get("rssi"),
            "temperature": item.get("temperature_1"),
            "relative_humidity": item.get("relative_humidity_2")
        })

    return filtered_dict

def update_plot(all_data_dict, success_dict):
    ax[0].clear()
    ax[1].clear()

    for dev_eui in DEVICES.keys():
        df = all_data_dict[dev_eui]
        if df.empty:
            continue

        df_sorted = df.sort_values("timestamp_local")
        label = DEVICES[dev_eui]
        color = DEVICE_COLORS.get(dev_eui, "gray")

        ax[0].plot(df_sorted["timestamp_local"], df_sorted["snr"], marker='o', label=label, color=color)
        ax[1].plot(df_sorted["timestamp_local"], df_sorted["rssi"], marker='o', label=label, color=color)

    ax[0].set_title("SNR over time (Local time)")
    ax[0].set_ylabel("SNR (dB)")
    ax[0].legend()

    ax[1].set_title("RSSI over time (Local time)")
    ax[1].set_ylabel("RSSI (dBm)")
    ax[1].legend()

    time_format = mdates.DateFormatter('%H:%M:%S', tz=local_tz)
    ax[0].xaxis.set_major_formatter(time_format)
    ax[1].xaxis.set_major_formatter(time_format)

    summary = "\n".join([
        f"{DEVICES[dev]} Successful Rate Overall: {success_dict[dev]['overall']:.2%}, 5min: {success_dict[dev]['recent']:.2%}"
        for dev in DEVICES.keys()
    ])
    fig.suptitle(f"TTN LoRaWAN Connection\n{summary}", fontsize=14)

    plt.tight_layout()
    plt.draw()
    plt.pause(0.1)

while True:
    data = fetch_data()
    records_dict = filter_data(data)

    for dev_eui in DEVICES.keys():
        records = records_dict.get(dev_eui, [])
        if records:
            df_new = pd.DataFrame(records)
            all_data_dict[dev_eui] = pd.concat([all_data_dict[dev_eui], df_new]).drop_duplicates(subset=["timestamp"])

    success_dict = {}

    for dev_eui in DEVICES.keys():
        df = all_data_dict[dev_eui]
        if df.empty:
            continue

        df["timestamp"] = pd.to_datetime(df["timestamp"], utc=True)

        # Overall successful rate
        start_ts_overall = df["timestamp"].min()
        latest_ts = df["timestamp"].max()
        elapsed_overall = (latest_ts - start_ts_overall).total_seconds()
        expected_overall = elapsed_overall / SAMPLE_INTERVAL
        actual_overall = len(df)
        success_overall = actual_overall / expected_overall if expected_overall > 0 else 0

        # 5 minutes' successful rate
        start_ts_recent = datetime.now(timezone.utc) - timedelta(minutes=5)
        df_recent = df[df["timestamp"] >= start_ts_recent]
        if not df_recent.empty:
            latest_recent_ts = df_recent["timestamp"].max()
            elapsed_recent = (latest_recent_ts - start_ts_recent).total_seconds()
            expected_recent = elapsed_recent / SAMPLE_INTERVAL
            actual_recent = len(df_recent)
            success_recent = actual_recent / expected_recent if expected_recent > 0 else 0
        else:
            success_recent = 0

        print(f"[{DEVICES[dev_eui]}] Overall: {success_overall:.2%}, 5min: {success_recent:.2%}")
        print(f"Latest packet UTC: {latest_ts}, Local: {latest_ts.astimezone(local_tz)}")

        success_dict[dev_eui] = {"overall": success_overall, "recent": success_recent}

    update_plot(all_data_dict, success_dict)
    time.sleep(POLL_INTERVAL)





All relevant data could be saved to excel based on the following codes:

After that, the time limit could be set to filter out the required data during test period.

import requests
import pandas as pd
from datetime import datetime
from dateutil import parser, tz

start_time = datetime(2025, 7, 2, 10, 0, 0, tzinfo=tz.UTC)  # Time limit, 2 hours differences between UTC and Munich
end_time = datetime(2025, 7, 2, 11, 0, 0, tzinfo=tz.UTC)

API_URL = "https://gi3.gis.lrg.tum.de/log/all?dev_eui=eq.00876EA598282BF6"  # Use url based on DevEUI

response = requests.get(API_URL)
if response.status_code != 200:
    raise Exception(f"Failed to get: {response.status_code}")

data = response.json()

filtered = []
for entry in data:
    ts = parser.isoparse(entry["ts"])  
    if start_time <= ts <= end_time:
        filtered.append({
            "ts": ts.isoformat(),
            "dev_eui": entry.get("dev_eui"),
            "network": entry.get("network"),
            "snr": entry.get("snr"),
            "rssi": entry.get("rssi"),
            "spreading_factor": entry.get("spreading_factor"),
            "bandwidth": entry.get("bandwidth"),
            "gateway_eui": entry.get("gateway_eui"),
            "lat": entry.get("lat"),
            "lon": entry.get("lon"),
        })

df = pd.DataFrame(filtered)
df.sort_values(by="ts", inplace=True)


output_file = "lorawan_data_20250702_.xlsx"
df.to_excel(output_file, index=False)

print(f"In total {len(df)} data are saved into {output_file}")









Evaluation

All LoRaWAN measured data could be downloaded via github IoT_LoRaWAN_in_Munich_Comparison/LoRaWANData.zip at main · HuangChenhao/IoT_LoRaWAN_in_Munich_Comparison

Or by clone the file https://github.com/HuangChenhao/IoT_LoRaWAN_in_Munich_Comparison.git




Data filtering and coarse evaluation

To evaluate the connection quality at a specific location, four key indicators were considered:

SNR (Signal-to-Noise Ratio): Reflects the quality of the received signal.

RSSI (Received Signal Strength Indicator): Indicates the power of the received signal.

SR (Success Rate): The ratio of successfully received signal timestamps to the total expected packets in 30-second intervals.

Gateways: The average number of gateways that received the transmission.

In the preprocessing step, the raw LoRaWAN data was cleaned and structured. For each timestamp (ts), only the record with the highest SNR was retained, representing the best possible connection at that moment. This filtering ensures that the evaluated metrics reflect the upper bound of connection performance rather than average or poor reception conditions.

After filtering, the connection quality level at the measurement point was calculated by averaging these best-case values over the entire observation period. This provides a performance-oriented assessment based on how well the connection could potentially perform.

This approach provides a performance-oriented assessment by quantifying how well the connection can perform under ideal conditions, rather than how it typically performs.

The calculated indicators are defined as follows:

%% Data reading and filtering part
clear; clc; close all

data = readtable('lorawan_data_SWM1_test.xlsx');    % Reading part
data.ts = datetime(data.ts, 'InputFormat', 'yyyy-MM-dd''T''HH:mm:ss.SSSSSSXXX', 'TimeZone', 'UTC');

% 1. Seperate the data by its time serious
[G, ~] = findgroups(data.ts);

% 2. Only keep the max SNR and RSSI for each time-epoch
idxMaxSNR = splitapply(@(x) find(x == max(x), 1, 'first'), data.snr, G);
rowStart = splitapply(@(x) x(1), (1:height(data))', G);  % Index for each epoch
rowIdx = rowStart + idxMaxSNR - 1;
filtered_data = data(rowIdx, :);

max_rssi = splitapply(@(x) max(x), data.rssi, G);
filtered_data.rssi = max_rssi;

% 3. Counting the number of gateways
gateway_count = splitapply(@(x) numel(unique(x(~strcmp(string(x), "")))), data.gateway_eui, G);
filtered_data.gateway_count = gateway_count;

% 4. Only keep the required data
wantedVars = {'ts', 'network','spreading_factor', 'snr', 'rssi', 'gateway_count'};
filtered_data = filtered_data(:, ismember(filtered_data.Properties.VariableNames, wantedVars));

disp(head(filtered_data));


%% LoRaWAN Evaluation Part
dt=  max(filtered_data.ts) - min(filtered_data.ts) ;
num30s_intervals = ceil(seconds(dt) / 30);

SR = length(filtered_data.ts) / num30s_intervals    % Successful Rate
SNR = mean(filtered_data.snr)                       % Signal Noise Rate
RSSI = mean(filtered_data.rssi)                     % Received Signal Strength Indicator
Gateways = mean(filtered_data.gateway_count)        % Gateway Amount

figure
subplot(2,1,1)
plot(filtered_data.ts+ hours(2), filtered_data.snr),hold on
yline(SNR,'LineWidth',1.5,'DisplayName', sprintf('Mean SNR = %.2f', SNR));
legend('show');
xlabel('Local Time (UTC+2)');
ylabel('SNR (dB)');
title('SNR over Time with Mean Line');
grid on;

subplot(2,1,2)
plot(filtered_data.ts+ hours(2), filtered_data.rssi),hold on
yline(RSSI,'LineWidth',1.5,'DisplayName', sprintf('Mean RSSI = %.2f', RSSI));
legend('show');
xlabel('Local Time (UTC+2)');
ylabel('RSSI (dB)');
title('RSSI over Time with Mean Line');
grid on;





To characterize the signal quality at the measurement point, different statistical approaches were chosen for RSSI and SNR, based on the nature of their observed distributions.

RSSI (Received Signal Strength Indicator):
In contrast, the RSSI values exhibited a positively skewed, unimodal distribution, which is well-aligned with the characteristics of a Gamma distribution. Since Gamma models are commonly used to describe signal amplitude and energy variations in wireless communication, a Gamma distribution was fitted to the RSSI data. The resulting distribution effectively captures both the central tendency and the spread of signal strength under ideal reception conditions.

figure;
% Histogram of RSSI based on its own pdf
histogram(filtered_data.rssi, ...
    'BinWidth', 1, ...
    'Normalization', 'pdf', ...
    'FaceColor', [0.2 0.6 0.8], ...
    'DisplayName', 'RSSI Histogram');
hold on;

title('Histogram of RSSI Values with Gamma Fit');
xlabel('RSSI (dB)');
ylabel('Probability Density');
grid on;

% Align with Gamma-Distribution
rssi_data = filtered_data.rssi;
rssi_shift = abs(min(rssi_data)) + 1;
rssi_for_fit = rssi_data + rssi_shift;

pd = fitdist(rssi_for_fit, 'Gamma');
% disp(pd);

x_vals = linspace(min(rssi_for_fit), max(rssi_for_fit), 100);
y_vals = pdf(pd, x_vals);
x_vals_original = x_vals - rssi_shift;
plot(x_vals_original, y_vals, 'r-', 'LineWidth', 2, 'DisplayName', 'Fitted Gamma PDF');

if pd.a > 1
    rssi_mode = (pd.a - 1) * pd.b - rssi_shift
    xline(rssi_mode, 'k--', 'LineWidth', 1.5, 'DisplayName', sprintf('Mode = %.2f dB', rssi_mode));
end

legend('show');

SNR (Signal-to-Noise Ratio):
Although a Gamma distribution was initially used to model the SNR values due to their positive skew, the fitted curve does not align well with the empirical histogram, especially near the peak region. This indicates that the SNR data may not follow a standard parametric distribution.

In contrast, using the mean value as a representative metric for SNR provides a more intuitive and robust summary of the signal characteristics, especially when the underlying distribution is irregular or multimodal. Therefore, the final analysis uses the mean of indicators to represent signal quality at the measurement location.

figure;
histogram(filtered_data.snr, ...
    'BinWidth', 1, ...
    'Normalization', 'pdf', ...
    'FaceColor', [0.2 0.6 0.8], ...
    'DisplayName', 'SNR Histogram');
hold on;

title('Histogram of SNR Values with Mean');
xlabel('SNR (dB)');
ylabel('Probability Density');
grid on;
xline(mean(filtered_data.snr), 'k--', 'LineWidth', 1.5, 'DisplayName', sprintf('Mean = %.2f dB', mean(filtered_data.snr)));
grid on;
legend('show');


This combination of approaches ensures that each indicator is represented in a statistically meaningful and physically interpretable way.










Results
Discussion
Summary

References














