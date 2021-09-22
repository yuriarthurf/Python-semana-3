def pega_numeros(dict):
    valores = speed.values()
    valores_list = list(valores)
    res = []
    [res.append(x) for x in valores_list if x not in res]
    return res


speed = {'jan':47, 'feb':52, 'march':47, 'April':44,
         'May':52, 'June':53, 'july':54, 'Aug':44, 'Sept':54}
print(pega_numeros(speed))