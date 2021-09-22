def le_numeros_separados_por_virgula(digitos):
    return sum(int(x) for x in digitos if x.isdigit())


digitos = input("Digite uma sequência de números separados por vírgula: ")
print(le_numeros_separados_por_virgula(digitos))
