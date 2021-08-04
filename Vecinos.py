from Nodo import *

class Vecinos(Nodo):

    def __init__(self, id, peso):
        Nodo.__init__(self, id)
        self.peso = peso

    def getVecino(self):
        return self.id

    def getPeso(self):
        return self.peso