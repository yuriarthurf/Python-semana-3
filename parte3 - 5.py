import numpy as np

a = np.arange(9, dtype=np.float32).reshape(3, 3)
a.dtype = np.int32
print(a.dtype)