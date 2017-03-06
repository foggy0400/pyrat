# Importing csv library and declaring containers for region info
import csv

regionIds = []
regionNames = []
regions = []
returnreg = []

# Function to load the region IDs and names into an array
def load_regions():
    with open('../resources/mapRegions.csv', newline='') as csvfile:
        idlist = csv.reader(csvfile, delimiter=',', quotechar='|')
        for row in idlist:
            ids = row[0]
            regionIds.append(ids)
            names = row[1]
            regionNames.append(names)
        regions.append(regionIds)
        regions.append(regionNames)
        return regions


# Function to query the user for the region they wish to analyse
def query_region():
    regionlist = load_regions()
    ids = regionlist[0]
    names = regionlist[1]

    count = 1
    while count < (len(ids) - 1):
        print(repr(count) + ': ' + repr(names[count]))
        count += 1

    regionselect = int(input('Select region: '))
    useregion = ids[regionselect]
    useregionname = names[regionselect]
    print("You selected " + repr(useregionname) + ", region ID " + repr(useregion))

    returnreg.append(useregion)
    returnreg.append(useregionname)
    return returnreg
