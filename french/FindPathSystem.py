"""
MIT License

Copyright (c) 2025 KyleCie

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

class PathSystem:
    def __init__(self) -> None:
        self.Etage1Gauche: list = [115, 117, 119, 121, 123, 125, 127, 129, 131, 133, 135, 137]
        self.Etage1Droite: list = [114, 116, 118, 120, 122, 124, 126, 128, 130, 132, 134, 136]

        self.Etage2Gauche: list = [239, 241, 243, 245, 247, 249, 251, 253, 256, 257, 259, 261, 263]
        self.Etage2Droite: list = [238, 242, 244, 246, 248, 250, 252, 254, 255, 258]

        self.Etage3Gauche: list = [365, 367, 369, 371, 373, 375, 377, 379, 381, 383, 385, 387, 389]
        self.Etage3Droite: list = [360, 362, 364, 366, 368, 370, 372, 374, 376, 378]

        self.Allfloors: list = []
        self.Allfloors.extend(self.Etage1Droite)
        self.Allfloors.extend(self.Etage1Gauche)
        self.Allfloors.extend(self.Etage2Droite)
        self.Allfloors.extend(self.Etage2Gauche)
        self.Allfloors.extend(self.Etage3Droite)
        self.Allfloors.extend(self.Etage3Gauche)

    def TraductDirectionButSameFloor(self, path: list = ['str', 'str', 'str']) -> list[str]:
        """
        Fait les phrases pour l'utilisateur avec la liste de findDirectionButSameFloor.

        path: list[str, str] <- ce qu'a return findDirectionButSameFloor

        return: list[str, str] <- mais different que l'entree
        """

        return [f"Quand tu sors de la salle va à {path[0]},", f"La salle sera à ta {path[1]}."]


    def findDirectionButSameFloor(self, start: int = 115, end: int = 135) -> list[str]:
        """
        Trouve la direction comme findDirection mais si le startpath et le endpath est sur le meme etage.

        start:  numero de salle <- startpath

        end:    numero de salle <- endpath

        return: list['str', 'str']
        """
        floor = int(str(start)[0])

        if floor == 1:
            if start in self.Etage1Droite and end in self.Etage1Droite:
                posStart = self.Etage1Droite.index(start)
                posEnd = self.Etage1Droite.index(end)
                return [f"{"gauche" if posStart > posEnd else "droite"}", f"{"gauche" if posStart > posEnd else "droite"}"]
            
            if start in self.Etage1Gauche and end in self.Etage1Gauche:
                posStart = self.Etage1Gauche.index(start)
                posEnd = self.Etage1Gauche.index(end)
                return [f"{"droite" if posStart > posEnd else "gauche"}", f"{"droite" if posStart > posEnd else "gauche"}"]
            
            if start in self.Etage1Gauche and end in self.Etage1Droite:
                posStart = self.Etage1Gauche.index(start)
                posEnd = self.Etage1Droite.index(end)
                return [f"{"droite" if posStart > posEnd else "gauche"}", f"{"gauche" if posStart > posEnd else "droite"}"]

            if start in self.Etage1Droite and end in self.Etage1Gauche:
                posStart = self.Etage1Droite.index(start)
                posEnd = self.Etage1Gauche.index(end)
                return [f"{"gauche" if posStart > posEnd else "droite"}", f"{"droite" if posStart > posEnd else "gauche"}"]

        if floor == 2:
            if start in self.Etage2Droite and end in self.Etage2Droite:
                posStart = self.Etage2Droite.index(start)
                posEnd = self.Etage2Droite.index(end)
                return [f"{"gauche" if posStart > posEnd else "droite"}", f"{"gauche" if posStart > posEnd else "droite"}"]
            
            if start in self.Etage2Gauche and end in self.Etage2Gauche:
                posStart = self.Etage2Gauche.index(start)
                posEnd = self.Etage2Gauche.index(end)
                return [f"{"droite" if posStart > posEnd else "gauche"}", f"{"droite" if posStart > posEnd else "gauche"}"]
            
            if start in self.Etage2Gauche and end in self.Etage2Droite:
                posStart = self.Etage2Gauche.index(start)
                posEnd = self.Etage2Droite.index(end) *1.3
                return [f"{"droite" if posStart > posEnd else "gauche"}", f"{"gauche" if posStart > posEnd else "droite"}"]

            if start in self.Etage2Droite and end in self.Etage2Gauche:
                posStart = self.Etage2Droite.index(start) *1.3
                posEnd = self.Etage2Gauche.index(end)
                return [f"{"gauche" if posStart > posEnd else "droite"}", f"{"droite" if posStart > posEnd else "gauche"}"]
            
        if floor == 3:
            if start in self.Etage3Droite and end in self.Etage3Droite:
                posStart = self.Etage3Droite.index(start)
                posEnd = self.Etage3Droite.index(end)
                return [f"{"gauche" if posStart > posEnd else "droite"}", f"{"gauche" if posStart > posEnd else "droite"}"]
            
            if start in self.Etage3Gauche and end in self.Etage3Gauche:
                posStart = self.Etage3Gauche.index(start)
                posEnd = self.Etage3Gauche.index(end)
                return [f"{"droite" if posStart > posEnd else "gauche"}", f"{"droite" if posStart > posEnd else "gauche"}"]
            
            if start in self.Etage3Gauche and end in self.Etage3Droite:
                posStart = self.Etage3Gauche.index(start)
                posEnd = self.Etage3Droite.index(end) *1.3
                return [f"{"droite" if posStart > posEnd else "gauche"}", f"{"gauche" if posStart > posEnd else "droite"}"]

            if start in self.Etage3Droite and end in self.Etage3Gauche:
                posStart = self.Etage3Droite.index(start) *1.3
                posEnd = self.Etage3Gauche.index(end)
                return [f"{"gauche" if posStart > posEnd else "droite"}", f"{"droite" if posStart > posEnd else "gauche"}"]
        return ["unknown"]


    def TraductDirection(self,stairspath: str = 'A', path: list = ['str', 'str', 'str'], start: int = 0) -> list[str]:
        """
        Fait les phrases pour l'utilisateur avec la liste de findDirection.

        stairspath: "A" ou "B" ou "C" ou "D" (selon findStairs)

        path: list[str, str, str] <- ce qu'a return findDirection

        start: 0 ou sartpath_de_findpath

        return: list[str, str, str] <- mais different que l'entree
        """

        go: str = "monté"

        if start != 0:
            path[0] -= int(str(start)[0])

        if path[0] < 0:
            go = "descendu"
            path[0] = int(str(path[0])[1])

        return [f"Va à l'escalier {stairspath}",f"Après avoir {go} {path[0]} {"étage" if path[0] == 1 else "étages"},", f"Va à {path[1]},", f"La salle sera à ta {path[2]}."]


    def findDirection(self, end: int, stairs: str) -> list[int | str]:
        """
        Trouve la direction (droite ou gauche) à aller après avoir monter les escaliers + de quelle côté sera la salle.

        end:    la salle = int

        stairs: "A" ou "B" ou "C" ou "D" (selon findStairs)

        return: [cb_etage_de_difference, ou_aller_apres_avoir_monte, dans_quelle_cote_sera_la_salle]
        """

        floor: int = int(str(end)[0])
        direction: str = ""
        OuAller: str = ""

        if stairs == "A":
            if floor == 1:
                direction = "droite" if end in self.Etage1Droite else "gauche"
            elif floor == 2:
                direction = "droite" if end in self.Etage2Droite else "gauche"
            elif floor == 3:
                direction = "droite" if end in self.Etage3Droite else "gauche"
            return [floor, "gauche", direction]
        
        if stairs == "B":
            if floor == 1:
                OuAller = "gauche" if end in [117, 118, 119] else "droite"
                if OuAller == "droite":
                    direction = "droite" if end in self.Etage1Droite else "gauche"
                else:
                    direction = "gauche" if end in self.Etage1Droite else "droite"
            elif floor == 2:
                OuAller = "gauche" if end in [241, 242, 243] else "droite"
                if OuAller == "droite":
                    direction = "droite" if end in self.Etage2Droite else "gauche"
                else:
                    direction = "gauche" if end in self.Etage2Droite else "droite"
            elif floor == 3:
                OuAller = "gauche" if end in [362, 367] else "droite"
                if OuAller == "droite":
                    direction = "droite" if end in self.Etage3Droite else "gauche"
                else:
                    direction = "gauche" if end in self.Etage3Droite else "droite"
            return [floor, OuAller, direction]

        if stairs == "C":
            if floor == 1:
                OuAller = "droite" if end in [132, 135, 133] else "gauche"
                if OuAller == "droite":
                    direction = "droite" if end in self.Etage1Droite else "gauche"
                else:
                    direction = "gauche" if end in self.Etage1Droite else "droite"
            elif floor == 2:
                OuAller = "droite" if end in [255, 259, 261] else "gauche"
                if OuAller == "droite":
                    direction = "droite" if end in self.Etage2Droite else "gauche"
                else:
                    direction = "gauche" if end in self.Etage2Droite else "droite"
            elif floor == 3:
                OuAller = "droite" if end in [376, 387] else "gauche"
                if OuAller == "droite":
                    direction = "droite" if end in self.Etage3Droite else "gauche"
                else:
                    direction = "gauche" if end in self.Etage3Droite else "droite"
            return [floor, OuAller, direction]
        
        if stairs == "D":
            if floor == 1:
                direction = "gauche" if end in self.Etage1Droite else "droite"
            elif floor == 2:
                direction = "gauche" if end in self.Etage2Droite else "droite"
            elif floor == 3:
                direction = "gauche" if end in self.Etage3Droite else "droite"
            return [floor, "droite", direction]
        
        return ["unknown"]


    def findStairs(self, end: int) -> str:
        """
        Trouve les escaliers parfait pour le chemin

        end:    salle = int

        return: "A" ou "B" ou "C" ou "D"
        """

        if end in [114, 115, 116, 238, 239, 360, 365]:
            return "A"
        
        if end in [i for i in range(117, 126, 1)] or end in [241, 242, 243, 244, 245, 246, 247, 248, 249, 251] or end in [362, 364, 366, 367, 368, 369, 371, 373, 375, 377]:
            return "B"

        if end in [i for i in range(126, 134, 1)] or end in [250, 252, 253, 254, 255, 256, 257, 259, 261] or end in [370, 372, 374, 376, 379, 381, 382, 383, 385, 387]:
            return "C"

        if end in [134, 135, 136, 137, 258, 263, 378, 389]:
            return "D"

        return "unknown"


    def findpath(self,startpath: int = 0, endpath: int = 115, otherstair: str = "Z") -> dict:
        """

        startpath:  0 <- depuis l'extérieur OU numero de salle <- d'où tu viens

        endpath:    numero de salle <- où aller

        otherstair: "A" ou "B" ou "C" ou "D" <- dans le cas si l'utilisateur a pris un autre escalier (la merde ;-} )

        return: dict = {
                    "phrase": ["sent1", "sent2", "sent3"],
                        
                    "escalier": "A" ou "B" ou "C" ou "D"
                }
        """

        dict_to_return: dict = {}

        if otherstair != "Z":
            Direction = self.findDirection(end=endpath, stairs=otherstair)
            DirectionPath = self.TraductDirection(stairspath=otherstair, path=Direction, start=startpath)

            dict_to_return = {"phrase": DirectionPath, "escalier": otherstair}

        elif startpath == 0:
            StairsPath = self.findStairs(end=endpath)
            Direction = self.findDirection(end=endpath, stairs=StairsPath)
            DirectionPath = self.TraductDirection(stairspath=StairsPath, path=Direction, start=startpath)

            dict_to_return = {"phrase": DirectionPath, "escalier": StairsPath}
        
        else:
            if int(str(startpath)[0]) == int(str(endpath)[0]):
            
                Direction = self.findDirectionButSameFloor(start=startpath, end=endpath)
                DirectionPath = self.TraductDirectionButSameFloor(path=Direction)

                dict_to_return = {"phrase": DirectionPath, "escalier": None}

            else:
                StairsPath = self.findStairs(end=startpath)
                Direction = self.findDirection(end=endpath, stairs=StairsPath)
                DirectionPath = self.TraductDirection(stairspath=StairsPath, path=Direction, start=startpath)

                dict_to_return = {"phrase": DirectionPath, "escalier": StairsPath}
        
        return dict_to_return