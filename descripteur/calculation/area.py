import numpy as np

class Area():
    def __init__(self, img) -> None:
        self.area = np.sum(img)

    def getArea(self):
        return self.area