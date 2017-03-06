import csv
regionIds = regionNames = []

def loadRegionIds():
    with open('mapRegions.csv', newline='') as csvfile:
        idlist = csv.reader(csvfile, delimiter=',', quotechar='|')
        for row in idlist:
            ids = row[0]
            regionIds.append(ids)
            return regionIds

def loadRegionNames():
    with open('mapRegions.csv', newline='') as csvfile:
        namelist = csv.reader(csvfile, delimiter=',', quotechar='|')
        for row in namelist:
            names = row[1]
            regionNames.append(names)
            return regionNames

def queryRegion(ids, names):
    count = 1
    while (count < (len(ids)-1)):
        print(repr(count) + ': ' + repr(names[count]))
        count = count + 1
    regionSelect = int(input('Select region: '))
    useRegion = ids[regionSelect]
    useRegionName = names[regionSelect]
    print("You selected " + repr(useRegionName) + ", region ID " + repr(useRegion))

idcontainer = loadRegionIds()
namecontainer = loadRegionNames()
queryRegion(idcontainer, namecontainer)

