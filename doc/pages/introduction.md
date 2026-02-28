# Introduction


This document contains details on how the Navigation System on Ariel of Hamble works, how various tasks can be undertaken and how issues can be reported or troubleshot.

As more feedback is gathered and as more tools are added to the system, we'll add more details and update the version numbers.  The most up-to-date version will be available on the website, but the software does also create a PDF version that will be available to download.  We'll also include dates of chart updates.

The web version of the document can be [found here](https://st599.github.io/ArielOfHamble-NavigationDocumentation/index.html).

The PDF version can be [downloaded here](https://github.com/st599/ArielOfHamble-NavigationDocumentation/tree/main/doc/pdf_build/simplepdf).


## Terms and Definitions

> Measured Data

Data that can be directly measured from the boat's systems.
For example, Apparent Wind Speed, Location

> Derived Data

Data that needs to be derived from multiple data sources.
Examples include True Wind Speed (from Apparent Wind Speed, Speed and Heading), Sunset Time (from Location, Date and a Database). 

> GNSS

Global Navigation Satellite System, examples include GPS and Galileo.

> Speed

How fast you're moving in any direction.

> Velocity

How fast you're moving in relation to a specific direction.  Travel relative to North at a Speed of 5kts, then you're velocity is 5kts.  Travel South - your speed is still 5kts but your velocity is -5kts.  Travel due East, your velocity is 0kts, even though your speed is 5kts.

> Open Standard 

A specification that is published by a standards developing organisation and is available under fair, reasonable and non-discriminatory (FRAND) terms - this does not mean free.  This allows a number of organisations to make equipment that can interact with each other.
Examples include NMEA 0183, Ethernet


> Proprietary

A data format designed and used by one company for their products, not usually available under FRAND terms.  Any interaction with such a format usually requires a degree of reverse engineering.
Examples include SeaTalk, Micronet


> Open Source

Usually used for software to mean that it is available under a licence such as the GNU General Public Licence, which allow you to use, build upon, distribute, sell etc. provided you allow others to do the same.
Examples include the OpenCPN Plotter and SignalK data format and software.