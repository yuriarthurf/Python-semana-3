def le_idade(nome, idade):
    if idade < 0:
        return f'Idade incorreta! Você ainda não nasceu!'
    else:
        return f'{nome}, você completará 100 anos em {(100 - idade) + 2020}'


nome = input("Digite seu nome: ")
idade = int(input("Digite a sua idade para saber em que ano completará 100 anos: "))
print({le_idade(nome, idade)})
