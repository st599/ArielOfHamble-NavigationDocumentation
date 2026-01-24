# Navigation Overview

![Ariel Navigating the Kiel Canal](../assets/images/aoh.jpg)

This is an overview of the software and hardware used for Ariel of Hamble's Navigation.  The term navigation network is used to describe the network that is used to pass data between nodes around the boat, but in reality it is a number of networks.  Further data will be provided in a deep-dive section at a future date.

> NOTE: Please be aware that some information is measured and some is derived from those measurements.  For example, Apparent Wind Speed (AWS) is measured and True Wind Speed (TWS) is calculated from AWS and Speed Through the Water (STW).  A problem with a measured value will cause knock-on issues with values derived from it.

## TackTicks

The TackTick instruments are used to generate depth, speed through the water, water temperature, apparent wind speed and direction.  The TackTick units use a proprietary radio network called [Raymarine Micronet](https://open-boat-projects.org/en/micronet/) to pass information between the units installed in the navigation cupboard, the wind sensor and the display units.

### Display Units

Ariel has 3 display units:
* 1 wind display which can show either apparent wind direction and speed or true wind direction and speed.
* 2 double number displays which can be configured to show information such as depth, speed through the water, COG and SOG, time, location.

> NOTE - please be very careful with the TackTick display units.  They are extraordinarily expensive to replace - over £2000 per set.

### Depth

The depth sounder uses ultrasonic waves to measure the depth beneath the transducer.  The offset between the transducer and the bottom of the keel is applied in the Raspberry Pi.  The depth sounder also provides the sea water temperature to the network.  It connects to the unit in the navigation cupboard using a proprietary wired direct connection.

### Speed

The speed transducer uses a paddle wheel to measure the speed of the boat throught the water.  It connects to the unit in the navigation cupboard using a proprietary wired direct connection.

### Wind Speed and Direction

![Micronet](../assets/images/Micronet-768x464.png)

The Wind Speed and Direction unit at the top of the mast is solar powered.  It transmits the information to the unit in the Navigation locker using a proprietary format called .  

## EmTrak AIS

The EmTrak AIS is a multipurpose device.  It is the vessel's source of location data, it is an AIS class B+ transceiver, sending the boat's location to other vessels and, when in range, shore stations, it receives the locations of other vessels and it has an inbuilt switch connecting both the internal AIS and the VHF to the mast-head antenna.

To prevent the VHF being powered on and transmitting in to a switched off AIS unit, both the EmTrak and VHF are on the same power switch "VHF".  

### GPS Information

The EmTrak sends the following GNSS information to the Navigation system:
* Location
* COG and SOG
* Rate of Turn
* Time
* Number of Satellites
* Precision

> NOTE: The EmTrak unit uses the US GPS, EU Galileo, Russian Glonass and Chinese Beidou locations satellites.

### AIS Targets

The EmTrak also sends:
* Class A Vessel Location
* Class B Vessel Location
* Class A Vessel Type, Cargo, Destinations etc.
* Search and Rescue Aircraft
* Aids to Navigation ("Virtual Buoys")
* Safety Messages (MOB devices, SARTs etc.)

## Standard Horizon VHF

## Open Plotter



### RaspberryPi



### SignalK

SignalK is software designed to import data from a variety of sources around the boat and stores it in a central database which can be accessed by other software.  On Ariel, the SignalK servier takes data from a range of inputs such as the NMEA 0143 bus used by the TackTicks and EmTrak, from the barometer and thermometer in the navigation locker and software modules running on the Raspberry Pi and imports them in to the database.  SignalK also stores a range of static data in this database which can be used in calculations, e.g. vessel draught.

SignalK stores data addresses and values, for example:

`/vessels/<mmsi>/environment/windSpeedTrue 4.23`

`/vessels/<mmsi>/navigation/position 51.23453,-0.12248,2.34`

This database is available to other software to read from - the plotter software, OpenCPN, receives all of its locations details, AIS vessels to overlay, DSC alerts directly from the SignalK database.  SignalK also has a number of output plugins so the data is converted back to NMEA 0143 so derived values can be displayed on the TackTicks, to a data stream that can be used by Navionics or similar on member's phones and tablets and in some cases to files so that trends can be observed (e.g. we're actively monitoring battery state to see if we can understand better what is causing mysterious battery drainage).

Further details on SignalK can be found at [SignalK Website](https://signalk.org/)

### OpenCPN

#### O-Charts

![O Charts UK Overview](../assets/images/ocharts-uk.jpg)

[O-charts](https://www.o-charts.org/) use the latest information from a number of European hydrographic offices to create chart packages specifically designed for OpenCPN.  Each purchase is licensed to a USB key that is plugged in to the Raspberry Pi. 

> NOTE: without the USB key, the charts will not be displayed.

Each year we purchase the entire UK chart set plus any required for the summer cruise, e.g. Atlantic France.  If you are planning on sailing anywhere that could require new charts, please contact the Commodore.  Charts can be installed remotely.  Charts receive updates every four weeks - again updates can be run remotely.

#### MOB and Safety Notifications

### Dashboard

## Custom Software

Our custom software uses a number of tools that are built in to the Raspberry Pi's operating system.  The majority use a service called `cron` which runs a specific programme at a specific time.

### Engine Hours

The engine hours meter works by sampling the voltage output from the alternator.  If a voltage is present, the alternator and engine are running.  The total hours value is stored in a text file.  Every 3 mins the software checks for the presence of voltage and if present, increments the time stored in the file and sends to new value to the SignalK database.

### Offsite Notifier

The offsite notifier uses a service called ([ntfy.sh](https://ntfy.sh/)) - sending short notifications from the Raspberry Pi which can be read by the Boatswain's team and committee.  To ensure that Skippers and Mates are aware that a notification is running, a short jingle is played.  For information on the NTFY channel that you need to subscribe to, please contact the commodore.

#### Location

The location notification checks if the boat is approaching a fixed location and sends a ntfy.sh notification.  This is mainly used on the approach to Elephant Boatyard to know when the boatswain's team can visit the yard to do work. 

#### Sunset

The sunset notification lets us know that the navigation system is running at sunset, so we know that a night sail is taking place.

## Future Projects

### Better Data Dashboard

### Shutdown Information

We are planning to use the offsite notifier to send a set of data when the navigation system is shutdown.  This would be used for information important to planning maintenance and spotting early indications of issues.  In the initial rollout we're hoping to send engine hours, battery status and cabin humidity with a hope to add further information such as fridge minimum temperature, engine maximum temperature, bilge water level etc.

### Better Engine Information

### Better Battery Information
