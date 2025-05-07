from Manejador_becas import ManejadorBecas
from Manejador_beneficiarios import ManejadorBene

def menu():
    opc=input('''Ingrese la opcion deseada: 
              a) Informar cantidad de beneficiarios por beca y importe
              b) Informar si un beneficiario tiene mas de una beca
              c) Listar los beneficiarios de mayor a menor
              d) Informar los promedios mayores a 8 y que no tienen beca
              e) Salir: ''')
    while opc != 'e':
        if opc == 'a':
            tipoBeca = input("Ingrese el tipo de beca: ")
            unBeneficiario.mostrarBeneficiarios(tipoBeca, unaBeca)
        elif opc == 'b':
            numDni = input("Ingrese el DNI del beneficiario: ")
            unBeneficiario.informarBeneficiarios(numDni)
        elif opc == 'c':
            unBeneficiario.ordenamiento()
        elif opc == 'd':
            unBeneficiario.listarBeneficiarios()
            
if __name__ == "__main__":
    unBeneficiario = ManejadorBene()
    unaBeca = ManejadorBecas()
menu()