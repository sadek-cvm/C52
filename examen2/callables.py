from typing import Callable

def my_func(arg):
    print('my_func', arg)

my_func(1)
    
my_lambda = lambda arg1, arg2: print('my_lambda', arg1, arg2)

my_lambda(1, 2)

class MyClasse:
    
    def __init__(self, init_value):
        self.current_value = init_value
        
    def obj_func(self):
        print(self.current_value)
        
    def obj_func_val(self, value):
        print(f'Yo {value}')
        
    @classmethod
    def class_func(cls):
        print(cls.__name__)
        
    @staticmethod
    def static_func():
        print('Y\'a rien')
        
    def __call__(self, value):
        self.current_value += 1
        print(f'{self.current_value:02}) trop émouvant : {value}')
        

my_obj = MyClasse(88)

my_obj.obj_func() # obj_func(my_obj)
MyClasse.class_func() # class_func(MyClass)
my_obj.class_func() # class_func(MyClasse)

MyClasse.static_func() # static_func()
my_obj.static_func() # static_func()

# - - - - - -

my_obj(32)

# - - - - - -


def cool(data, task : Callable): # objectif => task est callable
    for value in data:
        task(value)

values = [i**2 for i in range(10)]
def display(value):
    print(value)
def put_to_db(value):
    print(f'{value} => into db')
cool(values, display)
cool(values, put_to_db)
cool(values, lambda v: print(f'lambda -> {v}'))
cool(values, my_obj)
cool(values, my_obj.obj_func_val)