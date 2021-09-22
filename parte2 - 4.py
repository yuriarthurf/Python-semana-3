primeirosNomes = ['Joao', 'Douglas', 'Lucas', 'José']
sobreNomes = ['Soares', 'Souza', 'Silveira', 'Pedreira']
idades = [19, 28, 25, 31]
for i, j, k in zip(primeirosNomes, sobreNomes, idades):
    print(f'{i} {j}, está com {k} anos')

