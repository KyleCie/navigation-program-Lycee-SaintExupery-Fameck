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
        self.Floor1left: list = [115, 117, 119, 121, 123, 125, 127, 129, 131, 133, 135, 137]
        self.Floor1right: list = [114, 116, 118, 120, 122, 124, 126, 128, 130, 132, 134, 136]

        self.Floor2left: list = [239, 241, 243, 245, 247, 249, 251, 253, 256, 257, 259, 261, 263]
        self.Floor2right: list = [238, 242, 244, 246, 248, 250, 252, 254, 255, 258]

        self.Floor3left: list = [365, 367, 369, 371, 373, 375, 377, 379, 381, 383, 385, 387, 389]
        self.Floor3right: list = [360, 362, 364, 366, 368, 370, 372, 374, 376, 378]

        self.Allfloors: list = []
        self.Allfloors.extend(self.Floor1right)
        self.Allfloors.extend(self.Floor1left)
        self.Allfloors.extend(self.Floor2right)
        self.Allfloors.extend(self.Floor2left)
        self.Allfloors.extend(self.Floor3right)
        self.Allfloors.extend(self.Floor3left)

    def TraductDirectionButSameFloor(self, path: list = ['str', 'str', 'str']) -> list[str]:
        """
        Makes the sentences for the user with the list of findDirectionButSameFloor.

        path: list[str, str] <- what return findDirectionButSameFloor has

        return: list[str, str] <- but different than the input
        """

        return [f"When you leave the room go towards the {path[0]},", f"The room will be at your {path[1]}."]


    def findDirectionButSameFloor(self, start: int = 115, end: int = 135) -> list[str]:
        """
        Finds the direction like findDirection but if the startpath and endpath are on the same floor.

        start:  room number <- startpath

        end:    room number <- endpath

        return: list['str', 'str']
        """
        floor = int(str(start)[0])

        if floor == 1:
            if start in self.Floor1right and end in self.Floor1right:
                posStart = self.Floor1right.index(start)
                posEnd = self.Floor1right.index(end)
                return [f"{"left" if posStart > posEnd else "right"}", f"{"left" if posStart > posEnd else "right"}"]
            
            if start in self.Floor1left and end in self.Floor1left:
                posStart = self.Floor1left.index(start)
                posEnd = self.Floor1left.index(end)
                return [f"{"right" if posStart > posEnd else "left"}", f"{"right" if posStart > posEnd else "left"}"]
            
            if start in self.Floor1left and end in self.Floor1right:
                posStart = self.Floor1left.index(start)
                posEnd = self.Floor1right.index(end)
                return [f"{"right" if posStart > posEnd else "left"}", f"{"left" if posStart > posEnd else "right"}"]

            if start in self.Floor1right and end in self.Floor1left:
                posStart = self.Floor1right.index(start)
                posEnd = self.Floor1left.index(end)
                return [f"{"left" if posStart > posEnd else "right"}", f"{"right" if posStart > posEnd else "left"}"]

        if floor == 2:
            if start in self.Floor2right and end in self.Floor2right:
                posStart = self.Floor2right.index(start)
                posEnd = self.Floor2right.index(end)
                return [f"{"left" if posStart > posEnd else "right"}", f"{"left" if posStart > posEnd else "right"}"]
            
            if start in self.Floor2left and end in self.Floor2left:
                posStart = self.Floor2left.index(start)
                posEnd = self.Floor2left.index(end)
                return [f"{"right" if posStart > posEnd else "left"}", f"{"right" if posStart > posEnd else "left"}"]
            
            if start in self.Floor2left and end in self.Floor2right:
                posStart = self.Floor2left.index(start)
                posEnd = self.Floor2right.index(end) *1.3
                return [f"{"right" if posStart > posEnd else "left"}", f"{"left" if posStart > posEnd else "right"}"]

            if start in self.Floor2right and end in self.Floor2left:
                posStart = self.Floor2right.index(start) *1.3
                posEnd = self.Floor2left.index(end)
                return [f"{"left" if posStart > posEnd else "right"}", f"{"right" if posStart > posEnd else "left"}"]
            
        if floor == 3:
            if start in self.Floor3right and end in self.Floor3right:
                posStart = self.Floor3right.index(start)
                posEnd = self.Floor3right.index(end)
                return [f"{"left" if posStart > posEnd else "right"}", f"{"left" if posStart > posEnd else "right"}"]
            
            if start in self.Floor3left and end in self.Floor3left:
                posStart = self.Floor3left.index(start)
                posEnd = self.Floor3left.index(end)
                return [f"{"right" if posStart > posEnd else "left"}", f"{"right" if posStart > posEnd else "left"}"]
            
            if start in self.Floor3left and end in self.Floor3right:
                posStart = self.Floor3left.index(start)
                posEnd = self.Floor3right.index(end) *1.3
                return [f"{"right" if posStart > posEnd else "left"}", f"{"left" if posStart > posEnd else "right"}"]

            if start in self.Floor3right and end in self.Floor3left:
                posStart = self.Floor3right.index(start) *1.3
                posEnd = self.Floor3left.index(end)
                return [f"{"left" if posStart > posEnd else "right"}", f"{"right" if posStart > posEnd else "left"}"]
        return ["unknown"]


    def TraductDirection(self,stairspath: str = 'A', path: list = ['str', 'str', 'str'], start: int = 0) -> list[str]:
        """
        Makes the sentences for the user with the findDirection list.

        stairspath:"A" or "B" or "C" or "D" (according to findStairs)

        path: list[str, str, str] <- what return findDirection has

        start: 0 or startpath_de_findpath

        return: list[str, str, str] <- but different than the input
        """

        go: str = "going up"

        if start != 0:
            path[0] -= int(str(start)[0])

        if path[0] < 0:
            go = "go down"
            path[0] = int(str(path[0])[1])

        return [f"Go to the stairs {stairspath}",f"After having {go} {path[0]} {"floor" if path[0] == 1 else "floors"},", f"Go to the {path[1]},", f"The room will be at your {path[2]}."]


    def findDirection(self, end: int, stairs: str) -> list[int | str]:
        """
        Find the direction (right or left) to go after going up the stairs + which side the room will be on.

        end:    the room = int

        stairs: "A" or "B" or "C" or "D" (according to findStairs)

        return: [hm_difference_on_floors, where_to_go_after_getting_up, in_which_side_will_the_room_be]
        """

        floor: int = int(str(end)[0])
        direction: str = ""
        OuAller: str = ""

        if stairs == "A":
            if floor == 1:
                direction = "right" if end in self.Floor1right else "left"
            elif floor == 2:
                direction = "right" if end in self.Floor2right else "left"
            elif floor == 3:
                direction = "right" if end in self.Floor3right else "left"
            return [floor, "left", direction]
        
        if stairs == "B":
            if floor == 1:
                OuAller = "left" if end in [117, 118, 119] else "right"
                if OuAller == "right":
                    direction = "right" if end in self.Floor1right else "left"
                else:
                    direction = "left" if end in self.Floor1right else "right"
            elif floor == 2:
                OuAller = "left" if end in [241, 242, 243] else "right"
                if OuAller == "right":
                    direction = "right" if end in self.Floor2right else "left"
                else:
                    direction = "left" if end in self.Floor2right else "right"
            elif floor == 3:
                OuAller = "left" if end in [362, 367] else "right"
                if OuAller == "right":
                    direction = "right" if end in self.Floor3right else "left"
                else:
                    direction = "left" if end in self.Floor3right else "right"
            return [floor, OuAller, direction]

        if stairs == "C":
            if floor == 1:
                OuAller = "right" if end in [132, 135, 133] else "left"
                if OuAller == "right":
                    direction = "right" if end in self.Floor1right else "left"
                else:
                    direction = "left" if end in self.Floor1right else "right"
            elif floor == 2:
                OuAller = "right" if end in [255, 259, 261] else "left"
                if OuAller == "right":
                    direction = "right" if end in self.Floor2right else "left"
                else:
                    direction = "left" if end in self.Floor2right else "right"
            elif floor == 3:
                OuAller = "right" if end in [376, 387] else "left"
                if OuAller == "right":
                    direction = "right" if end in self.Floor3right else "left"
                else:
                    direction = "left" if end in self.Floor3right else "right"
            return [floor, OuAller, direction]
        
        if stairs == "D":
            if floor == 1:
                direction = "left" if end in self.Floor1right else "right"
            elif floor == 2:
                direction = "left" if end in self.Floor2right else "right"
            elif floor == 3:
                direction = "left" if end in self.Floor3right else "right"
            return [floor, "right", direction]
        
        return ["unknown"]


    def findStairs(self, end: int) -> str:
        """
        Find the perfect stairs for the path

        end:    room = int

        return: "A" or "B" or "C" or "D"
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

        startpath:  0 <- from outside OR room number <- where you come from

        endpath:    room number <- where to go

        otherstair: "A" or "B" or "C" or "D" <- in case the user took another stair

        return: dict = {
                    "sentence": ["sent1", "sent2", "sent3"],
                        
                    "stair": "A" or "B" or "C" or "D"
                }
        """

        dict_to_return: dict = {}

        if otherstair != "Z":
            Direction = self.findDirection(end=endpath, stairs=otherstair)
            DirectionPath = self.TraductDirection(stairspath=otherstair, path=Direction, start=startpath)

            dict_to_return = {"sentence": DirectionPath, "stair": otherstair}

        elif startpath == 0:
            StairsPath = self.findStairs(end=endpath)
            Direction = self.findDirection(end=endpath, stairs=StairsPath)
            DirectionPath = self.TraductDirection(stairspath=StairsPath, path=Direction, start=startpath)

            dict_to_return = {"sentence": DirectionPath, "stair": StairsPath}
        
        else:
            if int(str(startpath)[0]) == int(str(endpath)[0]):
            
                Direction = self.findDirectionButSameFloor(start=startpath, end=endpath)
                DirectionPath = self.TraductDirectionButSameFloor(path=Direction)

                dict_to_return = {"sentence": DirectionPath, "stair": None}

            else:
                StairsPath = self.findStairs(end=startpath)
                Direction = self.findDirection(end=endpath, stairs=StairsPath)
                DirectionPath = self.TraductDirection(stairspath=StairsPath, path=Direction, start=startpath)

                dict_to_return = {"sentence": DirectionPath, "stair": StairsPath}
        
        return dict_to_return