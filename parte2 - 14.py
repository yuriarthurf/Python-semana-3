import random
random_list = random.sample(range(500), 50)


def valor_minimo(list):
    sorted(random_list)
    return random_list[0]


def valor_maximo(list):
    sorted(random_list)
    return random_list[-1]


def valor_medio(list):
    return sum(random_list)//len(random_list)

def calcula_mediana(list):
    sorted(random_list)
    return (random_list[24]+random_list[25])//2



