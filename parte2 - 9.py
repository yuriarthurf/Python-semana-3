def recebe_elementos(*args, **kwargs):
    for i in args:
        print(i)
    for j in kwargs:
        print(j)