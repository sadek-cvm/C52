import numpy as np

class KNN:
    def __init__(self, matrix, k = 3):
        self.matrix = matrix
        self.k = k 

    def calculate_distances(self, vector):
        # axis = 1: calculer la distance pour chaque un des lignes
        return np.linalg.norm(self.matrix - vector, axis=1)
        # equivalent à : 
        # for ligne in range(matrix.shape[0]):
        #     distance = []
        #     distance.append(np.linalg.norm(matrix[ligne] - vector))

    def find_nearest_neighbors(self, vector):
        distances = self.calculate_distances(self, vector)
        sorted_neighbors = np.sort(distances) # mettre à l'ordre croissant
        nearest_neighbors = sorted_neighbors[:self.k]
        return nearest_neighbors

# array1 = np.array([[1,2,3],[2,3,4],[3,4,5]])
# array2 = np.array([1,2,4])
# print(array1)
# print(array2)
# print(array1 - array2)
# distances = np.linalg.norm(array1 - array2, axis=1)
# print(distances)
# print(array1[1])
