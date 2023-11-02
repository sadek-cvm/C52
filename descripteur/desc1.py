import sys
import numpy as np

sys.path.append('descripteur/calculation')

from perimetre import Perimetre
from area import Area

class DescOne():
    def __init__(self, image) -> None:
        self.image = image
    
    def get_ratio(self):
        return ((4 * np.pi) * Area(self.image).getArea()) / (Perimetre(self.image).getPerimetre())**2