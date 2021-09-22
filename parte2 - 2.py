def apenas_impares():
    a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
    l = []
    for i in a:
        if i % 2 != 0:
            l.append(i)
    return l

print(apenas_impares())