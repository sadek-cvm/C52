import numpy as np
from centroid import Centroid
# from circle import Circle

class Perimetre:
    def __init__(self, shape) -> None:
        self.current = shape[1:-1, 1:-1]
        self.left = shape[1:-1, 0:-2]
        self.right = shape[1:-1, 2:]

        self.top = shape[:-2, 1:-1]
        self.topLeft = shape[0:-2, 0:-2]
        self.topRight = shape[0:-2, 2:]

        self.bottom = shape[2:, 1:-1]
        self.bottomLeft = shape[2:, :-2]
        self.bottomRight = shape[2:, 2:]
        
        totalCount = self.__countNeighbor() * self.current

        pattern = np.array([0,1,1,1,1,1,1,1,0])
        self.perimetre = pattern[totalCount]

    def __countNeighbor(self):
        return self.left + self.right + self.top + self.topLeft + self.topRight + self.bottomLeft + self.bottom + self.bottomRight

    def getPerimetre(self): 
        return np.sum(self.perimetre)
    
    def getShapePerimetre(self):
        return self.perimetre
    
if __name__ == "__main__":
    image = np.array([
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 1, 1, 1, 0, 0],
        [0, 1, 1, 1, 1, 1, 0],
        [0, 1, 1, 1, 1, 1, 0],
        [0, 1, 1, 1, 1, 1, 0],
        [0, 0, 1, 1, 1, 0, 0],
        [0, 0, 0, 0, 0, 0, 0]
    ])

    
    p = Perimetre(image).getShapePerimetre()
    print(p)
    
    c = Centroid().getCentroid(p)
    print(c)
    
    coord = np.argwhere(p)
    print(coord)
    
    dist = np.linalg.norm(coord - c, axis=1)
    print(dist)
    print(dist.max())