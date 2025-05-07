class Carrera:
    __codigo: int
    __nombre: str
    __titulo: int
    __duracion: str
    __nivel: str
    __codigoF: int
    
    def __init__(self,codi,nombre,titulo,duracion,niv,codigo):
        self.__codigo=codi
        self.__nombre=nombre
        self.__titulo=titulo
        self.__duracion=duracion
        self.__nivel=niv
        self.__codigoF=codigo
        

    def getCodigo(self):
        return self.__codigo

    def getNombre(self):
        return self.__nombre

    def getTitulo(self):
        return self.__titulo

    def getDuracion(self):
        return self.__duracion

    def getNivel(self):
        return self.__nivel
    
    def getidFacultad(self):
        return self.__codigoF
    
    def __lt__(self, otro):
        return self.__nombre < otro.getNombre()
