import numpy as np

from perimetre import Perimetre
from centroid import Centroid

class Distance():
    def __init__(self, image) -> None:
        p = Perimetre(image).getShapePerimetre()
        self.distance = np.linalg.norm(np.argwhere(p) - Centroid().getCentroid(p), axis = 1)
        
    def get_dist_max(self):
        return self.distance.max()
    
    def get_dist_min(self):
        return self.distance.min()
    
    