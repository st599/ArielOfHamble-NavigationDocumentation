# Starting the Navigation System

The navigation system needs to be turned on in a particular order.

1. As described in the overview, the boat's GNSS source is the EmTrak AIS unit.  As this is connected to the VHF to share the antenna, it is powered by the VHF switch.  Switch on the VHF first.

2. Wait for the Location and Time to appear on the VHF screen.

3. Power on the Navigation switch.  The Raspberry Pi will boot and the  OpenCPN chartplotter software will load.  The satellite position indicator on OpenCPN should show 3-4 bars.

4. The navigation instruments need to be switched on near the navigation cupboard.  Switching on one will send a signal to the other units and they will switch on too.  Once a connection to the RayNet network occurs, information will start to be displayed.  The units can now be moved outside.