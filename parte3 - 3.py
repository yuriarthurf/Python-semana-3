import numpy as np

array = np.random.normal(0, 3, size=(5, 5))
array = np.sort(array)[::-1]
novo_array = np.sort(array, axis=0)
novo_array[4,4] = 0
print(novo_array)