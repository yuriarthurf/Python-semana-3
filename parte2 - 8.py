
def funcao(j):
    return j + 1


list = []
n = 0
while n != 'sair':
    list.append(n)
    n = input("Digite os elementos da lista. Digite 'sair' para sair: ")
list.pop(0)


def my_map(list, f):
    for i in list:
        print(i)


print(my_map(list, funcao(10)))