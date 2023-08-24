


# Bonnes pratiques
# --------------------------------------------------------------------------------------------

# CALTAL - Code a little | Test a little
# DRY - Don't repeat yourself
# UMUTD - You must use the debugger (Do not print)

# Normes de codage
# --------------------------------------------------------------------------------------------

# PEP8

# Types fondamentaux
# --------------------------------------------------------------------------------------------

import copy


a = 10 # int
b = 3.14 # reel
c = True # bool
d = "C52" # chaine de caracteres
e = None # Nonetype
f = 1+2j # nombre complexe

print("a", type(a), a)
print("b", type(b), b)
print("c", type(c), c)
print("d", type(d), d)
print("e", type(e), e)
print("f", type(f), f)


value = -5
print(0 <= value < 10)
print('positif' if value >= 0 else 'negatif')


# Structures de donness

my_str = 'abc'
my_list = []
my_tuple = (1,2)
my_dict = {'a': 1, 'b': 2}
my_set = {1, 2}

# Slicing 
# --------------------------------------------------------------------------------------------

my_list = list(range(0,10))

print(my_list)
print(my_list[0])
print(my_list[-1])
print(my_list[-2])
print(my_list[0:3])
print(my_list[4:6])
print(my_list[:6])
print(my_list[4:])
print(my_list[-10:])
print(my_list[8:2:-1])
print(my_list[::-1])

# Parcours

my_list_1 = list(range(0,10))
my_list_2 = list(range(100,110))


for value1, value2 in zip(my_list_1, my_list_2):
    print(f"{'? :':<5} {value1=} - {value2=}")
print()


for i, value in enumerate(my_list_1):
    print(f"{i:<5} {value=}")
print()

values = []
for i in range(10):
    if i % 2 == 0:
        values.append(i**2)
        
print(values)

values2 = [i**2 for i in range(10) if i % 2 == 0] # comprehension list

print(value2)

text = 'hello world'

print([i for i in range(10) if i % 2])
print([i if i % 2 else '!' for i in range(10)])

# Reference et "garbage collector"

a = 5
b = 5

print(f'{a=} {b=} {hex(id(a))} {hex(id(b))} : same => {id(a) == id(b)}')

a = 10
b = 5

print(f'{a=} {b=} {hex(id(a))} {hex(id(b))} : same => {id(a) == id(b)}')

a = 5
print(f'{a=} {b=} {hex(id(a))} {hex(id(b))} : same => {id(a) == id(b)}')

a = 'allo'
print(hex(id(a)))
a = a + ' monde'
print(hex(id(a)))

a = [0,1,2]
b = a

print(f'{a=} {b=} {hex(id(a))} {hex(id(b))} : same => {id(a) == id(b)}')

a[0] = 10
print(f'{a=} {b=} {hex(id(a))} {hex(id(b))} : same => {id(a) == id(b)}')

b = copy.deepcopy(a)
b = copy(a)