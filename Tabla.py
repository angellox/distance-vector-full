from tabulate import tabulate

class Tabla:

    def __init__(self, id, datos): #n = nodo, w = peso
        self.id = id
        self.datos = datos

    def formarTabla(self):
        print(tabulate(self.datos, headers = ["ID","Peso"], tablefmt="github"))
    
    def getPeso(self):
        pesos = [dato[1] for dato in self.datos]
        return pesos

    def setPeso(self, element, nuevo_peso):
        
        self.datos[element][1] = nuevo_peso
        