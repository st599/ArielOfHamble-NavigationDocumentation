# Navigation Overview

This is an overview of the software and hardware used for Ariel of Hamble's Navigation.

> NOTE: Please be aware that some information is measured and some is derived from those measurements.  For example, Apparent Wind Speed (AWS) is measured and True Wind Speed (TWS) is calculated from AWS and Speed Through the Water (STW).  A problem with a measured value will cause knock-on issues with values derived from it.

## TackTicks

### Depth

### Speed

### Wind Speed and Direction

## EmTrak AIS

### GPS Information

### AIS Targets

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
