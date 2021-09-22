class Lampada:
    def __init__(self, var):
        self.var = var

    def liga(self):
        return True

    def desliga(self):
        return False

    def esta_ligada(self):
        if self.liga():
            return 'True'
        else:
            return 'False'


x = Lampada(False)
x.desliga()
x.liga()
x.desliga()
print(x.esta_ligada())
