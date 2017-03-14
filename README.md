# Greenhouse-arduino-pi
A rundown of a low cost solution for arduino light/motor control and optional logging system via raspberry pi
- Can control lights and motors with a simple timer and relay board using the millis() function on arduino, goal is to expand to different stages of plant growth autmatically throughout the plant life cycle
- Can import sensor data into a file via raspberry pi, through a cron scheduled task and python script - file will have to be formatted for import into a usable format for analysis in the future, and commercial grade sensors can be added to improve aeroponic/hydroponic solution monitoring (EC, pH, water temp, etc)
- Bill of Materials in Current System
- Bucket Cloner
  - Black 5 Gallon Bucket
  - Submersible water pump
  - pvc piping, drill holes in them
  - nozzles to plug into pvc piping (optional but best for spread of water spray)
  - low cost LED light(coverage area is quite small, so once clones develop sufficient roots they can be transplanted to a larger system)
  - baskets for placement into lid, hole saw to drill holes
  - rockwool plugs
- Germinator
 - small plant tray with translucent lid
 - heating mat
- Large aeroponic/hydroponic system for later stages of growth (flowering and vegetation)
 - Large container for root system with pvc nozzles
 - higher flow rate pump for larger spray area
 - pvc with holes and novels
 - lower chamber for gravity feed refill to pump after spray
 - covered holes for baskets filled with growing media to prevent overspray/water loss
 - mylar sheeting
 - high powered LED (currently ~200$ as of 11/2016)
 
 - Added "Worm Shower" to eliminate the need for constant addition on nutrients to hydroponic solution.
 - essentially runs a pump from the hydroponic reservoir to the top of the worm bin, approx 1.5 Gal every 3 days,
 at which point it will wait for 20 minutes to go through the worm bins and 150 micron SS mesh filter, and gravity feed into a bucket, where another pump will go back into the hydroponic reservoir with worm tea. 
 03/17
 - edited crontab to schedule python script
 - flashed board with nanpy
 - wrote python script to control whole system sequentially, and generate log files each day, important to keep number of log files in folder equal to number of days
 - need to add tutorial for flashing with nanpy, setting up crontab, and creating log folder in standard location in target master computer
 - still need to add wiring diagrams
 - need to add analog sensor readings, and print them to logs for light sensor
 - need to add DHT11 readout for temperature and humidity
