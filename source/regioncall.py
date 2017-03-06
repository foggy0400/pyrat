#Importing csv library and declaring containers for region info
import csv
regionIds = []
regionNames = []

#Defining function to load the region IDs into an array
def loadRegionIds():
    with open('../resources/mapRegions.csv', newline='') as csvfile:
        idlist = csv.reader(csvfile, delimiter=',', quotechar='|')
        for row in idlist:
            ids = row[0]
            regionIds.append(ids)
        return regionIds

#Defining function to load the region names into an array
def loadRegionNames():
    with open('../resources/mapRegions.csv', newline='') as csvfile:
        namelist = csv.reader(csvfile, delimiter=',', quotechar='|')
        for row in namelist:
            names = row[1]
            regionNames.append(names)
        return regionNames

#Defining function to query the user for the region they wish to analyse
def queryRegion(ids, names):
    count = 1
    while (count < (len(ids)-1)):
        print(repr(count) + ': ' + repr(names[count]))
        count = count + 1
    regionSelect = int(input('Select region: '))
    useRegion = ids[regionSelect]
    useRegionName = names[regionSelect]
    print("You selected " + repr(useRegionName) + ", region ID " + repr(useRegion))
