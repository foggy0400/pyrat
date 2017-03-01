import csv
regionIds = []
regionNames = []
def loadregions():
    with open('mapRegions.csv', newline='') as csvfile:
        regionsvar = csv.reader(csvfile, delimiter=',', quotechar='|')
        for row in regionsvar:
            ids = row[0]
            names = row[1]

            regionIds.append(ids)
            regionNames.append(names)
loadregions()

count = 1
while (count < (len(regionIds)-1)):
    print(repr(count) + ': ' + repr(regionNames[count]))
    count = count + 1

regionSelect = int(input('Select region: '))


useRegion = regionIds[regionSelect]
useRegionName = regionNames[regionSelect]

print("You selected " + repr(useRegionName) + ", region ID " + repr(useRegion))

