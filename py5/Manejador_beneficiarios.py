import csv
from Beneficiario import beneficiario

class ManejadorBene:
    __beneficiarios = list
    
    def __init__(self):
        self.__beneficiarios = []
     
    def cargarBeneficiarios(self):    
        archivoBene = open("beneficiarios.csv")
        reader = csv.reader(archivoBene, delimiter=";")
        bandera = True
        for Bene in reader:
            if not bandera:
                bandera = False
            else:
                unBeneficiario = beneficiario(Bene[0], int(Bene[1]), int(Bene[2]), int(Bene[3]), int(Bene[4]), Bene[5], Bene[6])
                self.__beneficiarios.append(unBeneficiario)
        archivoBene.close()
        
        
    def mostrarBeneficiarios(self, tipoBeca, unaBeca):
        acum = 0
        for beneficiario in range(len(self.__beneficiarios)):
            if beneficiario.getIdBeca() == tipoBeca:
                print("- {} {} {}".format(beneficiario.getNombre(), beneficiario.getApellido(), beneficiario.getDni()))
                acum += unaBeca.getImporte()
        print("El importe de la beca es: ", acum)
    

    def informarBeneficiarios(self, numDni):
        cont = 0
        for beneficiario in range(len(self.__beneficiarios)):
            if beneficiario.getDni() == numDni:
                cont += 1
        if cont > 1:
            print("El beneficiario {} {} tiene mas de una beca".format(beneficiario.getNombre(), beneficiario.getApellido()))
    
    def ordenamiento(self):
        self.__beneficiarios.sort()
        
    def listarBeneficiarios(self):
        for beneficiario in self.__beneficiarios:
            if beneficiario.getPromedio() > 8 and beneficiario.getIdBeca() == 0:
                print("- {} {} {}".format(beneficiario.getNombre(), beneficiario.getApellido(), beneficiario.getPromedio()))
"""def burbuja(self):
    n = len(self.__beneficiarios)
    for i in range(n-1):
        for j in range(n-1-i):
            if self.__beneficiarios[j].getSigla > self.__beneficiarios[j+1].getSigla:
                self.__beneficiarios[j], self.__beneficiarios[j+1] = self.__beneficiarios[j+1], self.__beneficiarios[j]"""
                
"""def burbuja(self):
    n = len(self.__beneficiarios)
    for i in range(n - 1):
        for j in range(n - 1 - i):
            if self.__beneficiarios[j].getSigla() > self.__beneficiarios[j + 1].getSigla():
                aux = self.__beneficiarios[j]
                self.__beneficiarios[j] = self.__beneficiarios[j + 1]
                self.__beneficiarios[j + 1] = aux"""

                
            
    
# a. Leer por teclado un tipo de Beca, e informar los beneficiarios de dicha beca y el importe total que debe disponer la Secretaría para el pago de dicha Beca. 
# b. Leer por teclado un dni, informar si el beneficiario tiene más de una beca, mostrando nombre y apellido. #
# c. Listar los beneficiarios, ordenados de mayor a menor por Facultad. Regla de negocio: para resolver este último punto, el analista le solicita que sobrecargue el operador “>”. #
# d. Listar nombre, apellido y promedio de los estudiantes, que poseyendo un promedio mayor que 8, no poseen beca de ayuda económica. #