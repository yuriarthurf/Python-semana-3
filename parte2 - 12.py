def reparte_lista(lista_1, n):
    return [lista_1[i:i+n] for i in range(0,len(lista_1), n)]


numeros = 0
lista_1 = []
while numeros != 'sair':
    lista_1.append(numeros)
    numeros = input("Digite os elementos da lista. Digite 'sair' para sair: ")
lista_1.pop(0)
lista_1 = list(map(int, lista_1))
print(reparte_lista(lista_1, 3))