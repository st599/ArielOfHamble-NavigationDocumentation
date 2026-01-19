# Navigation Overview

This is an overview of the software and hardware used for Ariel of Hamble's Navigation.

> NOTE: Please be aware that some information is measured and some is derived from those measurements.  For example, Apparent Wind Speed (AWS) is measured and True Wind Speed (TWS) is calculated from AWS and Speed Through the Water (STW).  A problem with a measured value will cause knock-on issues with values derived from it.

## TackTicks

### Depth

### Speed

### Wind Speed and Direction

## EmTrak AIS

The EmTrak AIS is a multipurpose device.  It is the vessel's source of location data, it is an AIS class B+ transceiver, sending the boat's location to other vessels and, when in range, shore stations, it receives the locations of other vessels and it has an inbuilt switch connecting both the internal AIS and the VHF to the mast-head antenna.

To prevent the VHF being powered on and transmitting in to a switched off AIS unit, both the EmTrak and VHF are on the same power switch "VHF".  Please switch on "VHF", wait until it acquires a position and displays it on the VHF front panel and then switch on the "Navigation" switch.

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

## Open Plotter

### Safe Switch Off

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

### Dashboard

## Custom Software

Our custom software uses a number of tools that are built in to the Raspberry Pi's operating system.  The majority use a service called `cron` which runs a specific programme at a specific time.

### Engine Hours

The engine hours meter works by sampling the voltage output from the alternator.  If a voltage is present, the alternator and engine are running.  The total hours value is stored in a text file.  Every 3 mins the software checks for the presence of voltage and if present, increments the time stored in the file and sends to new value to the SignalK database.

### Offsite Notifier


#### Location

#### Sunset
