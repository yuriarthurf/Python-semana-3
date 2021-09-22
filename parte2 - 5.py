def lista_sem_repetidos(list):
    nova_lista = []
    for i in list:
        if i not in nova_lista:
            nova_lista.append(i)
    return nova_lista


list = []
n = 0
while n != 'sair':
    list.append(n)
    n = input("Digite os elementos da lista. Digite 'sair' para sair: ")
list.pop(0)
print(lista_sem_repetidos(list))
