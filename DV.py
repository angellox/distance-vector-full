from Vecinos import *
from Nodo import *
from Tabla import *
from tabulate import tabulate

class DV:

    tablas_originales = []
    tablas_respaldos = []
    tablas_modificables = []

    def __init__(self, archivo):
        self.archivo = archivo
        self.grafo = []

    def crearNodos(self):
        file = self.archivo + '.txt'
        file_open = open(file)
        lines = file_open.readlines()

        for line in lines:
            id_nodo = int(line.split(":")[0])
            vecs = line.split(":")[1].split("-")
            vertex = Nodo(id_nodo)

            for element in vecs:
                # Recopilar el id del vecino
                id_vecino = int(element.split(",")[0].rstrip())
                # Recopilar el peso del vecino
                peso_vecino = int(element.split(",")[1].rstrip())

                # Creando nodo vecino con sus valores
                objeto_vecino = Vecinos(id_vecino, peso_vecino)
                vertex.setVecinos(objeto_vecino)
            
            self.grafo.append(vertex)
        
        return self.grafo

    def crearTablas(self):

        for v in self.grafo:

            data_original = []
            data_respaldo = []
            data_modificable = []

            for vertice in self.grafo:

                vertice.setDistancia(float("inf"))
                v.setDistancia(0)

                for vecinos in v.vecinos:
                    if vertice.id == vecinos.id:
                        vertice.setDistancia(vecinos.getPeso())

                pair = [vertice.id, vertice.distancia]

                data_original.append(pair)
                data_respaldo.append(pair[:])
                data_modificable.append(pair[:])

            t_original = Tabla(v.id, data_original)
            t_respaldo = Tabla(v.id, data_respaldo)
            t_modificable = Tabla(v.id, data_modificable)

            self.tablas_originales.append(t_original)
            self.tablas_respaldos.append(t_respaldo)
            self.tablas_modificables.append(t_modificable)

    def distanceVector(self, nodo, tiempo):

        for i in range(1, tiempo + 1):
            print('------------------- Calculando tiempo: ', i , ' --------------------')
            for vtx in self.grafo:
                pesos_vertice = self.tablas_respaldos[vtx.id-1].getPeso() #Lista de pesos del vtx

                for vec in vtx.vecinos:
                    lista_pesos = self.tablas_respaldos[vec.id-1].getPeso()
                    peso_alvecino = pesos_vertice[vec.id-1] # Distancia del vtx al vec
                    pesos_vertice_mod = self.tablas_modificables[vtx.id-1].getPeso()

                    for elementos in self.tablas_respaldos:
                        temp_distancia = lista_pesos[elementos.id-1] + peso_alvecino

                        if pesos_vertice_mod[elementos.id-1] > temp_distancia:
                            self.tablas_modificables[vtx.id-1].setPeso(elementos.id-1, temp_distancia)
                
            
            self.tablas_respaldos = self.tablas_modificables
                #tabla_original[vtx.id-1].formarTabla()            

        print('\n')
        print("Tabla del nodo: ", nodo, "en el tiempo: ", tiempo)
        print("----------------------------------------\n")
        
        self.tablas_respaldos[nodo - 1].formarTabla()