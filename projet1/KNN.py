import numpy as np

class KNN:
    
    __instance = None
    
    # Singleton
    def __new__(cls):
        if cls.__instance is None:
            # appeller la methode __new__ de la super class de KNN (Object) pour recevoir une instace
            cls.__instance = super(KNN, cls).__new__(cls)
            cls.__instance.__initialized = False

        return cls.__instance

    def __init__(self):
        # pour ne pas reinitialiser le constructor si on a déja creaté une instance
        if not self.__initialized:
            self.__dataset = None
            self.__k = None
            self.__initialized = True

    def __validate_dataset(self, value):
        if value is None: # si c'est encore None
            raise TypeError("Veuillez fournir un dataset")
        elif not isinstance(value, np.ndarray):
            raise TypeError("Dataset doit être de type ndarray")
        elif value.ndim != 2:
            raise ValueError("Dataset doit être une liste à 2 dimensions")
        elif value.dtype != np.float64:
            raise ValueError("Dataset doit contenir des valeurs de type float")
        elif value.shape[1] < 2: # minimun une coordonnée et le tag
            raise ValueError("Dataset doit contenir une liste d'au moins deux elements (une coordonnée et le tag)")
        
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
        elif value.ndim != 1:
            raise ValueError("Sample doit être une liste à 1 dimension")
        elif value.dtype != np.float64:
            raise ValueError("Sample doit contenir des valeurs de type float")
        elif value.shape[0] != (self.__dataset[:, :-1]).shape[1]:
            raise ValueError("Les dimensions de sample et des coordonnées de dataset (sans compter les tags) doivent être égalaux")

    @property
    def dataset(self):
        return self.__dataset
    
    @dataset.setter
    def dataset(self, value):
        self.__validate_dataset(value)
        self.__dataset = value
        self.__k = 1 # reinisializer le k
        
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
        distances = np.linalg.norm(differences, axis=1)
        return distances
        # axis = 1: faire le calcul pour chaqu'un des lignes
    
    def __find_nearest_neighbors(self, sample):
        distances = self.__calculate_distances(sample)
        sorted_indices = np.argsort(distances) # ex: [2, 4, 5, 3, 1] (indices)
        nearest_indices = sorted_indices[:self.__k] # ex: [2, 4, 5] (indices)
        nearest_neighbors = self.__dataset[nearest_indices] # ex: [[1.0 , 2.5, 3.1, 0.0], [4.2, 5.6, 6.7, 0.0], [7.1, 8.7, 9.2, 1.0]] (coordonnées + tag)
        return nearest_neighbors
    
    def find_sample_tag(self, sample) -> int:
        self.__validate_dataset(self.__dataset)
        self.__validate_sample(sample)
        nearest_neighbors = self.__find_nearest_neighbors(sample)
        nearest_tags = nearest_neighbors[:, -1]
        nearest_tags = nearest_tags.astype(int) # on transform les tags in int (au lieu de float)
        tags_frequency = np.bincount(nearest_tags)
        sample_tag = np.argmax(tags_frequency) 
        # quand la méthode commence avec le mot "arg" cela veut dire qu'on prend la position de valeur et non pas la valeur
        return sample_tag
    
    def get_minimum_k(self): return 1
    def get_maximum_k(self): return self.__dataset.shape[0]

if __name__ == "__main__":

    #############################
    # Contenu de dataset:
    # [
    #   [x1, x2, x3, ..., xn, t],
    #   [x1, x2, x3, ..., xn, t],
    #   [x1, x2, x3, ..., xn, t],
    #   ...
    #   ...
    # ]
    #############################
    # Contenu de sample:
    # [x1, x2, x3, ..., xn]
    #############################

    def exemple():
        
        # une liste qui contient tous nos tags.
        tags = ["Cercle", "Carré", "Rectangle"]
        
        # une matrice de type ndarray contenant les coordonnées de chaque data point
        # suivi par l'index coorespondant à son tag (valeurs doit être de type float)
        dataset1 = np.array([[2, 1, 2, 0],
                            [4, 5, 6, 1],
                            [7, 3, 7, 2],
                            [5, 6, 6, 1],
                            [6, 2, 8, 2],
                            [1, 2, 2, 0],
                            [4, 5, 5, 1],
                            [7, 3, 8, 2],
                            [2, 1, 1, 0],
                            [3, 1, 2, 0]]
                        ).astype(float)
        
        # une liste de type ndarray contenant les coordonnées du sample (valeurs doit être de type float)
        sample = np.array([8, 4, 7]).astype(float)

        knn = KNN()
        knn.dataset = dataset1
        knn.k = 2
        tag_index = knn.find_sample_tag(sample) # retourne un int
        tag = tags[tag_index]
        print(tag) # rectangle

        # si jamais on change le dataset le k est reinitialiser a 1
        dataset2 = np.array([[2, 1, 2, 0],
                            [4, 5, 6, 1],
                            [7, 3, 7, 2],
                            [5, 6, 6, 1],
                            [6, 2, 8, 2]]
                        ).astype(float)

        knn.dataset = dataset2
        print(knn.k) # 1

    exemple()
    