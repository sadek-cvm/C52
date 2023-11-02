import numpy as np

from distance import Distance

class Circle():
    def __init__(self, image) -> None:
        self.rayon = Distance(image).get_dist_max()
    
    def get_circle_area(self):
        return np.pi * self.rayon**2
    