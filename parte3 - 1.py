import numpy as np

a = np.arange(1, 26).reshape(5, 5)
print(a)
soma = sum(np.diagonal(a))
print(f'A soma da diagonal é {soma}')
