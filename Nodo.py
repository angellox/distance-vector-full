
class Nodo:

    def __init__(self, id):
        self.id = id
        self.vecinos = []
        self.distancia = float('inf')
        
    def getNodo(self):
        return self.id

    def getVecinos(self):
        return self.vecinos

    def setVecinos(self, vec):
        self.vecinos.append(vec)

    def setDistancia(self, d):
        self.distancia = d
