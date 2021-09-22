def le_palindromo(palavra):
    if palavra.lower()[::-1] == palavra.lower():
        return 'É palíndromo'
    else:
        return 'Não é palíndromo'

palavra = input("Digite uma palavra para saber se é um palíndromo: ")
print(le_palindromo(palavra))