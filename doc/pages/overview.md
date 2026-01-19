# Navigation Overview

This is an overview of the software and hardware used for Ariel of Hamble's Navigation.

> NOTE: Please be aware that some information is measured and some is derived from those measurements.  For example, Apparent Wind Speed (AWS) is measured and True Wind Speed (TWS) is calculated from AWS and Speed Through the Water (STW).  A problem with a measured value will cause knock-on issues with values derived from it.

## TackTicks

### Depth

### Speed

### Wind Speed and Direction

## EmTrak AIS

The EmTrak AIS is a multipurpose device.  It is the vessel's source of location data, it is an AIS class B+ transceiver, sending the boat's location to other vessels and, when in range, shore stations, it decodes the locations of other vessels and it has an inbuilt switch that switches the internal AIS and the VHF to the mast-head antenna.

To prevent the VHF being powered on and transmitting in to a switched off AIS unit, both the EmTrak and VHF are on the same power switch "VHF"  Please switch on the VHF, wait until it acquires a position and displays it on the VHF front panel and then switch on the "Navigation" switch.

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

### OpenCPN

#### O-Charts

### Dashboard

## Custom Software

Our custom software uses a number of tools that are built in to the Raspberry Pi's operating system.  The majority use a service called `cron` which runs a specific programme at a specific time.

### Engine Hours

The engine hours meter works by sampling the voltage output from the alternator.  If a voltage is present, the alternator and engine are running.  The total hours value is stored in a text file.  Every 3 mins the software checks for the presence of voltage and if present, increments the time stored in the file and sends to new value to signalk.

### Offsite Notifier

#### Location

#### Sunset
