from facultad import Facultad
from carrera import Carrera
from Manejador_facultad import ManejadorF
from Manejador_carrera import ManejadorC

def opciones_menu():
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")
    print("5. Salir")
    
def opcionC(self, nombre):
    pass

def menu():
    opciones_menu()
    opcion1=int(input("Ingrese una opción (1-4): (0 para finalizar)"))
    
    
if __name__ == "__main__":
    gf=Manejador_facultad()
    gc=Manejador_carrera()
    gf.cargarFacultad()
    gc.cargarCarrera()
    gc.ordenar()
    menu()
    nombre = input("Ingrese el nombre de la carrera: ") #opcion c
    id=gc.buscarCarrera(nombre)
    if id != -1:
        nomF=gf.buscarFacultad(id)
        print(f"\nEl nombre de la facultad de la carrera ingresada es:{nomF}")
    else:
        print("\nNo se encontro.")
        
    gf.MostrarFacultad(gc) # opcion d
    facu=input("Ingrese el nombre de la facultad: ")
    aux=gf.BuscarFacu(facu)
    if aux != -1:
        gc.listarOrdenado(aux)
    else:
        print("\nNo se encontro")