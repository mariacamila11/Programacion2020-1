pesosPacientesIniciales=[32,64,74,85,98,115,122,127,137,148]
pesoPaciente=[]
presion= (6*(pesoPaciente))

_opcion= int(input("""
    1.Mostar el peso
    2.Añadir mas pesos
    3.Mostrar Informacion 
    4.Salir
"""))
while (_opcion !=4 ):
    if (_opcion==1):
        if (len(pesosPacientesIniciales) == len(pesoPaciente)):
            print("Peso","Valor Presion")
            for i in range(len(pesosPacientesIniciales)):
                print(pesosPacientesIniciales[i],"--->",pesoPaciente[i])
    elif(_opcion==2):
            lista = []
            decision =input("ingrese s--> Para agregar mas Pesos n--> Para no agregar mas Pesos : ")
        while (decision == "s"):
            lista.append (input("Ingrese peso del paciente : "))
            decision = input ("ingrese s--> Para agregar mas Pesos n--> Para no agregar mas pesos :")
        return lista
    elif(_opcion==3):
        print("El Peso mayor {} es el {}".format(presion, max (presion)))
        print("la edad menor {} es el {}".format(presion, min(presion)))
        presion.sort()
        print("Presiones en orden creciente {}".format(presion))
        
    else:
        print("Ingrese un numero valido")
_opcion= int(input("""
    1.Mostar el peso
    2.Añadir mas pesos
    3.Mostrar Informacion 
    4.Salir
"""))