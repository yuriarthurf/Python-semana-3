from matplotlib import pyplot as plt
import numpy as np


def sigmoid(x):
    return 1 / (1 + np.exp(-x))


x = np.arange(-5, 5)
plt.plot(x)
plt.show()
