######################################################################
# pyrat - An Eve Online PvE analyser
# Copyright (C) 2017 Instigo Pares [SUAD]
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.
#
# If you need to, contact me on reddit @ /u/instigo
######################################################################

import csv


# Function to generate list of systems in specified region from csv file
def pull_systems(region):
    systems = []
    regid = region[0]
    with open('../resources/mapSolarSystems.csv', newline='') as csvfile:
        syslist = csv.reader(csvfile, delimiter=',', quotechar='|')
        for row in syslist:
            if regid == row[0]:
                systems.append(row[1])
    return systems
