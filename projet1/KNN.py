import numpy as np

class KNN:
    def __init__(self, matrix, k = 3):
        # contenu de matrix ex:
        # [
        #   [x1, x2, x3, ..., xn, t], 
        #   [x1, x2, x3, ..., xn, t],
        #   [x1, x2, x3, ..., xn, t]
        #   ...
        #   ...
        # ]
        
        self.k = k
        self.matrix = matrix


    @property
    def matrix(self):
        return self.__matrix
    
    @matrix.setter
    def matrix(self, value):
        if isinstance(matrix, np.ndarray):
            self.__matrix = value
        else:
            self.__matrix = np.array(value)
        
    @property
    def k(self):
        return self.__k
    
    @k.setter
    def k(self, value):
        if not isinstance(value, int):
            raise TypeError("pas un int")
        if value > self.__matrix.shape()[0]:
            raise ValueError(f"k doit etre entre 0 et {self.__matrix.shape()[0]}")
        self.__k = value

    def calculate_distances(self, element):
        matrix_without_tags = self.__matrix[:, :-1]
        differences = matrix_without_tags - element
        return np.linalg.norm(differences, axis=1)
        # axis = 1: faire le calcul pour chaqu'un des lignes
    
    def find_nearest_neighbors(self, element):
        distances = self.calculate_distances(element)
        sorted_indices = np.argsort(distances) # ex: [2, 4, 5, 3, 1] (indexes)
        nearest_indices = sorted_indices[:self.__k] # ex: [2, 4, 5] (indexes)
        nearest_neighbors = self.__matrix[nearest_indices] # ex: [[1, 2, 3, 0], [4, 5, 6, 0], [7, 8, 9, 1]] (coordonnées)
        return nearest_neighbors

# Example:
matrix = np.array([[1, 2, 3, 0], [4, 5, 6, 0], [7, 8, 9, 1]])
element = np.array([3, 4, 5])
k = 1



knn = KNN(matrix, k)

knn.k = "ahmed"
nearest_neighbors = knn.find_nearest_neighbors(element)
# print(nearest_neighbors)


# notes random: 
# pour le centroide
# (somme(des index des x des points pleins), somme(des index des y des points pleins)) / aire