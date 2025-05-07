class beca:
    __idBeca = int
    __tipo = str
    __importe = float
    
    def __init__(self, idB, tipoB, imp):
        self.__idBeca = idB
        self.__tipo = tipoB
        self.__importe = imp
    
    def getIdBeca(self):
        return self.__idBeca
    
    def getTipo(self):
        return self.__tipo
    
    def getImporte(self):
        return self.__importe