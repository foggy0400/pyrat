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

# Delete these later when pyrat.py is done
import regioncall
import listsystems
# not these lol
from ratelimit import rate_limited
import urllib.request

systems = listsystems.pull_systems(regioncall.query_region())
print(systems)
