# pyrat
###**Open-source utility for analysing Eve Online PvE activity**

**A Gumby Replacement For One Section Of The MER**

I began writing this project after CCP announced they would not be showing economic details for particular regions in the monthly economic reports. It is (eventually) going to be able to figure out how much isk has been made from ratting over the past 24 hours in a system (through the assumption that on average, 1 rat kill = 500k isk).

**Ideas For Future Expansion**

Once the tool can take a region as an input and figure out the isk made in that region (so in about 3 years), I'd like to expand it in a few ways:
 * Write data to a CSV for use in graphs 'n' stuff
 * Only survey systems owned by specified alliance
 * Support for analysing multiple regions at once
 * Support for reading config file to auto-analyse regions at boot
 * GUI (aaaah!) for running software and creating .cfg files
 * Daemon for auto-running pyrat at a specified time every day (to create weekly/monthly data)
 
