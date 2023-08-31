class Human:
    def __init__(self, name):
        self.__name = name
        self.__age = 0
    
    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self,value):
        if not isinstance(value, str):
            raise TypeError("pas un string")
        if len(value) < 2:
            raise ValueError("au moins 3 charactere")
        self.__name = value
    
    @property
    def age(self):
        return self.__age
    
    def tic(self):
        self.age += 1
        
u = Human(123)
u.name = 'Gustave'
pass