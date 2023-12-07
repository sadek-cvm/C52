import numpy as np

data = np.array([[ 0,  1,  2,  3],
                [ 4,  5,  6,  7],
                [ 8,  9, 10, 11]])

c, r = np.meshgrid(np.arange(data.shape[1]), np.arange(data.shape[0]))

print(c)
print(r)