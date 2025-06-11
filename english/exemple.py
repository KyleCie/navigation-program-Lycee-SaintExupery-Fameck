
# IMPORT THE FILE
from FindPathSystem import PathSystem

# INITIALIZE IT
Path = PathSystem()

# GET THE SENTENCES FOR YOUR NAVIGATION
path_infos = Path.findpath(startpath=0, endpath=115,otherstair="Z")

from pprint import pprint
# PRINT THE INFORMATIONS
pprint(path_infos)

# GET THE ROOMS
print(Path.Floor1left)

# GET THE BEST STAIRS FOR THE ROOM
stair = Path.findStairs(end=255)
print(stair)

# GET THE DIRECTION TO FIND THE ROOM (FLOORS DIFF, WHERE TO GO, WHERE THE ROOM WILL BE)
direction = Path.findDirection(end=255, stairs=stair)
print(direction)

# SAME AS findDirection BUT FOR THE SAME FLOOR (WITHOUT FLOORS DIFF)
direction = Path.findDirectionButSameFloor(start=250, end=255)
print(direction)