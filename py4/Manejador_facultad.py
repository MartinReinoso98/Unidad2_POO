import csv
from facultad import Facultad
import numpy as np
class ManejadorF:
    __cantidad: int
    __dimension: int
    __incremento = 5
    __dimension = 10
    __arreF: np.array
    
    def __init__(self, dimension = 10, incremento=5):
        self.__arreF = np.empty(dimension, dtype=Facultad)
        self.__cantidad = 0
        self.__dimension = dimension
    def agregarFacultad(self, unaFacultad):
        if self.__cantidad==self.__dimension:
            self.__dimension+=self.__incremento
            self.__arreF.resize(self.__dimension)
        self.__arreF[self.__cantidad]=unaFacultad
        self.__cantidad += 1
    
    def cargarFacultad(self):
        bandera = False
        with open("Facultades.csv") as archivoFacultades:
            reader = csv.read(archivoFacultades, delimiter=";")
        for Fac in archivoFacultades:
            if not bandera:
                bandera = True
            else:
                unaFacultad = (int(Fac[0]), Fac[1], Fac[2], Fac[3], Fac[4])
            self.__agregarFacultad(unaFacultad)
        archivoFacultades.close()
    
    def MostrarFacultad(self, gc):
        for i in range(self.__cantidad):
            print("En esta facultad hay: {}".format (gc.cantidad(self.__arreF[i].get_id())))
    
    def buscarFacultad(self, id):
        i=0
        encontrado = False
        while i< self.__cantidad and not encontrado:
            if int(self.__arreF[i].get_id()) == int(id):
                aux = self.__arreF[i].get_nombre()
                encontrado= True
            else:
                i +=1
        return aux
    
    def BuscarFacu(self, nombre):
        i = 0
        aux =-1
        encontrado = False
        while i < self.__cantidad and not encontrado:
            if self.__arreF[i].get_nombre() == nombre:
                aux = int(self.__arreF[i].get_id())
                encontrado = True
            else:
                i += 1
        return aux