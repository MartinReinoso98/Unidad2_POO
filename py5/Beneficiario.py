class beneficiario:
    __dni = int
    __nombre = str
    __apellido = str
    __carrera = str
    __sigla = int
    __anio = int
    __promedio = float
    __idbeca = int
    
    def __init__(self, Dni, Nombre, Apellido, Carrera, Sigla, Anio, Promedio, idBeca):
        self.__dni = Dni
        self.__nombre = Nombre
        self.__apellido = Apellido
        self.__carrera = Carrera
        self.__sigla = Sigla
        self.__anio = Anio
        self.__promedio = Promedio
        self.__idbeca = idBeca
        
    def getDni(self):
        return self.__dni
    
    def getNombre(self):
        return self.__nombre
    
    def getApellido(self):
        return self.__apellido
    
    def getCarrera(self):
        return self.__carrera
    
    def getSigla(self):
        return self.__sigla
    
    def getAnio(self):
        return self.__anio
    
    def getPromedio(self):
        return self.__promedio
    
    def getIdBeca(self):
        return self.__idbeca
    
    def __gt__(self, otro):
        return self.__sigla > otro.getSigla()