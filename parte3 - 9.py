import csv
import operator
from collections import Counter
import numpy as np


def maior_n_de_filmes():
    resultados = []
    with open('actors.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for linha2 in sorted(csv_reader, key=operator.itemgetter(2), reverse=True):
            resultados.append(linha2)
    ator = ([resultados[1][0]] + [resultados[1][2]])

    return ator



def media_de_filmes():
    with open('actors.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        conta_linha = 0
        lista_soma = []
        soma_lista = 0
        for linha in sorted(csv_reader, key=lambda Number_of_Movies: Number_of_Movies[1:51]):
            if conta_linha < 50:
                lista_soma.append((linha[2]))
                conta_linha += 1
        lista_soma = map(int, lista_soma)
        for i in lista_soma:
            soma_lista += i
    print(np.mean(soma_lista)//49)
    exit()


def maior_media_por_filme():
    with open('actors.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        conta_linha = 0
        for linha in sorted(csv_reader, key=operator.itemgetter(3), reverse=True):
            if conta_linha == 0:
                print(f'{(linha[0]), (linha[3])}')
                conta_linha += 1
            else:
                if conta_linha >= 1:
                    conta_linha += 1
                    if conta_linha == 38:
                        print(f'\t{linha[0], linha[3]}')
                        exit()


def filme_mais_frequente():
    with open('actors.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        conta_linha = 0
        nomes = []
        for linha in sorted(csv_reader, key=operator.itemgetter(4), reverse=False):
            if conta_linha == 0:
                conta_linha += 1
            else:
                if conta_linha >= 1:
                    nomes.append(linha[4])
                    conta_linha += 1
        x = (Counter(nomes))
        return x.most_common(1)


#print(maior_n_de_filmes())
#print(media_de_filmes())
#print(maior_media_por_filme())
#print(filme_mais_frequente())


