def le_par_ou_impar(numero):
    if numero % 2 == 0:
        return f'O número {numero} é par'
    else:
        return f'O número {numero} é ímpar'


numero_digitado = int(input("Digite um número para saber se é par ou ímpar: "))
print({le_par_ou_impar(numero_digitado)})
