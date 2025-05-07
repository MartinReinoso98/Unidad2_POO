import csv
from carrera import Carrera
import numpy as np
class ManejadorC:
    __cantidad: int
    __dimension: int
    __incremento = 5
    __arreC: np.array
    
    def __init__(self, dimension = 10, incremento = 5):
        self.__arreC = np.empty(dimension, dtype=Carrera)
        self.__cantidad = 0
        self.__dimension = dimension
    def agregarCarrera(self, unaCarrera):
        if self.__cantidad==self.__dimension:
            self.__dimension+=self.__incremento
            self.__arreC.resize(self.__dimension)
        self.__arreC[self.__cantidad]=unaCarrera
        self.__cantidad += 1
    
    def cargarCarrera(self):
        bandera = False
        with open("Carreras.csv") as archivoCarreras:
            reader = csv.read(archivoCarreras, delimiter=";")
        for Carr in archivoCarreras:
            if not bandera:
                bandera = True
            else:
                unaCarrera = Carrera(int(Carr[0]), Carr[1], Carr[2], Carr[3], Carr[4], int(Carr[5]))
                self.__agregarCarrera(unaCarrera)
        archivoCarreras.close()
        
    def buscarCarrera(self, nombre):
        i=0
        aux = -1
        encontrado = False
        while i< self.__cantidad and not encontrado:
            if self.__ArreC[i].getNombre() == nombre:
                aux = int(self.__ArreC[i].getidFacultad())
                encontrado= True
            else:
                i +=1
        return aux
    
    def cantidad(self, id):
        cant=0
        for i in range(self.__cantidad):
            if (self.__arreC[i].getidFacultad() == id):
                cant+=1
        return cant
    
    def listarOrdenado(self, aux):
        for i in range(self.__cantidad):
            if self.__arreC[i].getidFacultad() == aux:
                print("Nombre: {}, \nDuracion: {}".format(self.__arreC[i].getNombre(), self.__arreC[i].getDuracion()))
    
    def ordenar(self):
        self.__arreC.sort()
        