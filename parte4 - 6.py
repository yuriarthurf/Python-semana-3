import csv
from matplotlib import pyplot as plt
import numpy as np

dataset = {
    'Actor': [],
    'Total Gross': [],
    'Number of Movies': [],
    'Average per Movie': [],
    '#1 Movie': [],
    'Gross': []}


with open('actors.csv', 'r') as f:
    arquivo_csv = csv.reader(f, delimiter=',', quotechar='"')
    for i, row in enumerate(arquivo_csv):
        if i == 0:
            continue
        dataset['Actor'].append(row[0])
        dataset['Total Gross'].append(float(row[1]))
        dataset['Number of Movies'].append(int(row[2]))
        dataset['Average per Movie'].append(float(row[3]))
        dataset['#1 Movie'].append(row[4])
        dataset['Gross'].append(float(row[5]))

for k in dataset.keys():
    dataset[k] = np.array(dataset[k])

criterio = 'Number of Movies'
criterio2 = 'Actor'
indice_top_5 = np.sort(dataset[criterio])[::-1][:5]
nomes = ['Robert DeNiro', 'Samuel L.Jackson', 'Liam Neeson', 'Morgan Freeman',
                      'Bruce Willis']
plt.title('Índice de atores X número de filmes')
plt.xlabel("Atores")
plt.ylabel("Número de filmes")


plt.xticks(range(5), ['Robert DeNiro', 'Samuel L.Jackson', 'Liam Neeson', 'Morgan Freeman',
                      'Bruce Willis'])

plt.figure(figsize=(20,20))
grafico = plt.bar(nomes, indice_top_5)


plt.show()
