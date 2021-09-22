def abre_arquivo():
    arquivo = open('arquivo_texto.txt')
    linhas = arquivo.readlines()
    return linhas
print(abre_arquivo())