import numpy as np

# Exemple du contenu de dataset:
# [
#   [x1, x2, x3, ..., xn, t], 
#   [x1, x2, x3, ..., xn, t],
#   [x1, x2, x3, ..., xn, t],
#   ...
#   ...
# ]

class KNN:
    def __init__(self, k=1):
        self.__dataset = None
        self.__k = k

    def __validate_dataset(self, value):
        if value is None:
            raise ValueError("Veuillez fournir un dataset")
        elif not isinstance(value, np.ndarray):
            raise TypeError("Dataset doit être de type ndarray")
        elif value.shape[1] < 2: # minimun une coordonnée et le tag
            raise ValueError("Dataset doit avoir au moins deux elements (une coordonnée et le tag)")
        
    def __validate_k(self, value):
        self.__validate_dataset(self.__dataset)
        if not isinstance(value, int):
            raise TypeError("K doit être de type int")
        # shape[0] == y, shape[1] == x
        elif value <= 0 or value > self.__dataset.shape[0]:
            raise ValueError(f"K doit être entre 1 et {self.__dataset.shape[0]}")
        
    def __validate_sample(self, value):
        if not isinstance(value, np.ndarray):
            raise TypeError("Sample doit être de type ndarray")
        elif value.shape[0] != (self.__dataset[:, :-1]).shape[1]:
            raise ValueError("Les coordonnées de sample doivent être de la même dimension que les coordonnées du dataset (sans compter les tags)")

    @property
    def dataset(self):
        return self.__dataset
    
    @dataset.setter
    def dataset(self, value):
        self.__validate_dataset(value)
        self.__dataset = value
        self.k = 1 # reinisializer le k
        
    @property
    def k(self):
        return self.__k
    
    @k.setter
    def k(self, value):
        self.__validate_k(value)
        self.__k = value

    def __calculate_distances(self, sample):
        coordinates = self.__dataset[:, :-1] # on enlève les tags
        differences = coordinates - sample
        return np.linalg.norm(differences, axis=1)
        # axis = 1: faire le calcul pour chaqu'un des lignes
    
    def __find_nearest_neighbors(self, sample):
        distances = self.__calculate_distances(sample)
        sorted_indices = np.argsort(distances) # ex: [2, 4, 5, 3, 1] (indices)
        nearest_indices = sorted_indices[:self.__k] # ex: [2, 4, 5] (indices)
        nearest_neighbors = self.__dataset[nearest_indices] # ex: [[1, 2, 3, 0], [4, 5, 6, 0], [7, 8, 9, 1]] (coordonnées)
        return nearest_neighbors
    
    def find_sample_tag(self, sample):
        self.__validate_dataset(self.__dataset)
        self.__validate_sample(sample)
        nearest_neighbors = self.__find_nearest_neighbors(sample)
        nearest_tags = nearest_neighbors[:, -1]
        tags_frequency = np.bincount(nearest_tags)
        sample_tag = np.argmax(tags_frequency) # quand il y a un arg avant le nom de la methode cela veut dire que l'information est représenté par l'indice
        return sample_tag

def main():
    dataset1 = np.array([[2, 1, 2, 1],  #cercle
                        [4, 5, 6, 2],   #carre
                        [7, 3, 7, 3],   #triangle
                        [5, 6, 6, 2],   #carre
                        [6, 2, 8, 3],   #triangle
                        [1, 2, 2, 1],   #cercle
                        [4, 5, 5, 2],   #carre
                        [7, 3, 8, 3],   #triangle
                        [2, 1, 1, 1],   #cercle
                        [7, 1, 5, 4]])  #rectangle
    
    dataset2 = np.array([[2, 1, 2, 1],   #cercle
                        [4, 5, 6, 2],   #carre
                        [7, 3, 7, 3],   #triangle
                        [5, 6, 6, 2],   #carre
                        [6, 2, 8, 3]])
    
    sample = np.array([7, 1, 6])

    knn = KNN()
    # knn.dataset = dataset1
    knn.k = 6
    sample_tag = knn.find_sample_tag(sample)
    print(sample_tag)

    knn.dataset = dataset2
    sample_tag = knn.find_sample_tag(sample)
    print(sample_tag)

if __name__ == "__main__":
    main()

# truc a faire:
# verifier que notre sample est de une dimension
# verifier que notre dataset est de deux dimensions
# une function qui donne le k maximal
