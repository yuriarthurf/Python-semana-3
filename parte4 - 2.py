from matplotlib import pyplot as plt
import numpy as np


def sigmoid(x): return 1 / (1 + np.exp(-x))
def relu(x): return np.maximum(0, x)


x = np.arange(-5, 5)

sigmoid, = plt.plot(sigmoid(x), label='Sigmoid(x)')
relu, = plt.plot(relu(x), label='Relu(x)')
plt.legend(handles=[sigmoid, relu])

plt.show()