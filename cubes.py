class Cubes:
    def __init__(self):
        self.WGO = [0, 2, 0, 0, 135]
        self.WBO = [0, 2, 2, 0, 145]
        self.WBR = [2, 2, 2, 0, 146]
        self.WGR = [2, 2, 0, 0, 136]
        self.WG = [1, 2, 0, 0, 13]
        self.WO = [0, 2, 1, 0, 15]
        self.WB = [1, 2, 2, 0, 14]
        self.WR = [2, 2, 1, 0, 16]
        self.YGO = [0, 0, 0, 0, 235]
        self.YBO = [0, 0, 2, 0, 245]
        self.YBR = [2, 0, 2, 0, 246]
        self.YGR = [2, 0, 0, 0, 236]
        self.YG = [1, 0, 0, 0, 23]
        self.YO = [0, 0, 1, 0, 25]
        self.YB = [1, 0, 2, 0, 24]
        self.YR = [2, 0, 1, 0, 26]
        self.GO = [0, 1, 0, 1, 35]
        self.BO = [0, 1, 2, 1, 45]
        self.BR = [2, 1, 2, 1, 46]
        self.GR = [2, 1, 0, 1, 36]

cubesList = []
for i in vars(Cubes()):
    test = f"Cubes().{i}"
    cubesList.append(eval(test))


