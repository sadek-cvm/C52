import sys
import numpy as np

sys.path.append('descripteur/calculation')

from distance import Distance

class DescThree():
    def __init__(self) -> None:
        pass

    def get_ratio(self, image):
        return  Distance(image).get_dist_min() / Distance(image).get_dist_max()