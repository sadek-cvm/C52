# C52 - Automne 2023 - Projet 0
# Ahmed Sadek et Erick Delgado Garcia

# height = 8  
# width = 10  


# def matrix_generator(height, width):
#     tab = []
#     for _ in range(height):
#         line = []
#         for _ in range(width):
#             line.append(random.randint(0,1))
#         tab.append(line) 
#     return tab

# matrix = matrix_generator(height, width)

# while 1 not in engine.matrix:  # mainloop
#     for r in engine.matrix:
#         for c in r:
#             print(c,end = " ")
#         print()

#     time.sleep(1)
    
import random
import time
    
class GOLEngine:
    
    def __init__(self, width=15, height=12, probability=0.25):
        # constants
        self.MIN_WIDTH = 3
        self.MAX_WIDTH = 10000
        self.MIN_HEIGHT = 3
        self.MAX_HEIGHT = 10000
        
        # variables
        self.width = width
        self.height = height
        self.probability = probability
        self.matrix = []
        
        for _ in range(self.__height):
            row = []
            for _ in range(self.__height):
                r = random.random()
                if r < self.__probability:
                    cell = 1
                else:
                    cell = 0
                row.append(cell)
            self.matrix.append(row)
        
    @property
    def width(self):
        return self.__width
    
    @property
    def height(self):
        return self.__height
    
    @property
    def probability(self):
        return self.__probability
    
    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("Pas un Int")
        elif value < self.MIN_WIDTH:
            raise ValueError(f"Minimum un width de {self.MIN_WIDTH}")
        elif value > self.MAX_WIDTH: 
            raise ValueError(f"Maximum un width de {self.MAX_WIDTH}")
        self.__width = value
    
    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("Pas un Int")
        elif value < self.MIN_WIDTH:
            raise ValueError(f"Minimum un height de {self.MIN_HEIGHT}")
        elif value > self.MAX_WIDTH: 
            raise ValueError(f"Maximum un height de {self.MAX_HEIGHT}")
        self.__height = value
    
    @probability.setter
    def probability(self, value):
        if not isinstance(value, float):
            if value == 0 or value == 1:
                pass
            else:
                raise TypeError("Pas un Float")
        if value < 0:
            raise ValueError("Minimum un probability de 0")
        elif value > 1: 
            raise ValueError("Maximum un probability de 1")
        self.__probability = value
        
    def resize(self, width, height):
        self.width = width
        self.height = height
        # modifier view et matrice
        
    def print(self):
        for r in self.matrix:
            for c in r:
                print(c,end = " ")
            print()
        
        
engine = GOLEngine()
engine.print()
pass