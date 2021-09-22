import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
import csv


with open('landmarks.csv', 'r') as f:
    landmarks = []
    arquivo_csv = csv.reader(f, delimiter=',', quotechar='"')
    for i in (arquivo_csv):
        landmarks.append(i)
    x = [[int(float(m)) for m in i] for i in landmarks]
    for j, k in x:
        plt.scatter(j, k, color='black')
    plt.show()