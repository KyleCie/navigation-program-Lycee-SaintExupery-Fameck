
# IMPORTER LE FICHIER
from FindPathSystem import PathSystem

# L'INIIALISER
Path = PathSystem()

# AVOIR LES PHRASES POUR LA NAVIGATION
path_infos = Path.findpath(startpath=0, endpath=115,otherstair="Z")

from pprint import pprint
# PRINT LES INFORMATIONS
pprint(path_infos)

# AVOIR LES SALLES
print(Path.Etage1Gauche)

# AVOIR LE MEILLEUR ESCALIER POUR LA SALLE
stair = Path.findStairs(end=255)
print(stair)

# AVOIR LES DIRECTIONS POUR TROUVER LA SALLE (ETAGE DIFF, OU ALLER, OU SERA LA SALLE)
direction = Path.findDirection(end=255, stairs=stair)
print(direction)

# COMME findDirection MAIS POUR LE MEME ETAGE (SANS ETAGE DIFF)
direction = Path.findDirectionButSameFloor(start=250, end=255)
print(direction)