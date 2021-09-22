import numpy as np

a = np.arange(2, 52, 2).reshape(5, 5)
print(a)


#soma das linhas
soma_linhas = np.sum(a, axis=0)
print(soma_linhas)

#soma das colunas
soma_colunas = np.sum(a, axis=1)
print(soma_colunas)

#media da linha 5
media_linha_5 = np.mean(a, axis=0)
print(media_linha_5[4])


#media da coluna 5
media_coluna_5 = np.mean(a, axis=1)
print(media_coluna_5[4])