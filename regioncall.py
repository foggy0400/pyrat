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
print(regionNames)
print(regionIds)