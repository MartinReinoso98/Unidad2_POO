import csv
from Beca import beca

class ManejadorBecas:
    __becas = []
    
    def __init__(self):
        archivoBeca = open("becas.csv")
        reader = csv.reader(archivoBeca, delimiter=";")
        bandera = False
        for Beca in reader:
            if not bandera:
                bandera = False
            else:
                unaBeca = beca(beca[0],int(beca[1]), beca[2])
                self.__becas.append(unaBeca)
                
        archivoBeca.close()