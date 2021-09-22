import numpy as np

a = np.random.uniform(size=(8, 8))
ultima_coluna = (a[:, 0]+10)
print(ultima_coluna)