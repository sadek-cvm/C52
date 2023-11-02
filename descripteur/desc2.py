import sys
import numpy as np

sys.path.append('descripteur/calculation')

from circle import Circle
from centroid import Centroid
from area import Area

class DescTwo():
    def __init__(self) -> None:
        pass

    def get_ratio(self, image):
        return  Area(image).getArea() / Circle(image).get_circle_area()
