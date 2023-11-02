import numpy as np
from area import Area

class Centroid():
    def __init__(self) -> None:
        pass        
    
    def getCentroid(self, image):
        c, r = np.meshgrid(np.arange(image.shape[0]), np.arange(image.shape[1])) 
        
        print(np.sum(image))
        
        print(r * image)
        print(c * image)
        
        print(np.sum(r * image))
        print(np.sum(c * image))
        
        
        
        return (np.sum(r * image), np.sum(c * image)) / Area(image).getArea()
    
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
    
    print(Centroid().getCentroid(image))
    
    