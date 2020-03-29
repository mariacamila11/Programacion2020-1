def bienvenida(): print("Bienvenido al código")
def mostrar_dos_listas(enfermos,estados):
    if (len(enfermos) == len(estados)):
        print("Enfermo","Estado")
        for i in range(len(enfermos)):
            print(enfermos[i],"---",estados[i])
    else:
        print("no se puede mostrar uno a uno")

def llenarListadoc():
    listadoc = []
    decicion = input ("ingrese s--> Para agregar los doctores n --> Para no agregar mas : ")
    while (decicion == "s"):
        listadoc.append(input("ingrese un Doctor a la lista: "))
        decicion = input ("ingres s--> Para agregar mas doctores n --> Para no agregar mas : ")
    return listadoc

def llenarListaenfermer():
    listaenfermer=[]
    decicion = input ("ingrese s--> Para agregar los enfermeros n --> Para no agregar mas : ")
    while (decicion == "s"):
        listaenfermer.append(input("ingrese un enfermero a la lista: "))
        decicion = input ("ingres s--> Para agregar mas enfermeros n --> Para no agregar mas : ")
    return listaenfermer

def llenarListaenfe():
    listaenfe=[]
    decicion = input ("ingrese s--> Para agregar los enfermos n --> Para no agregar mas : ")
    while (decicion == "s"):
        listaenfe.append(input("ingrese un enfermo a la lista: "))
        decicion = input ("ingres s--> Para agregar mas enfermos n --> Para no agregar mas : ")
    return listaenfe

def llenarListaesta():
    listaesta=[]
    decicion = input ("ingrese s--> Para agregar los estados n --> Para no agregar mas : ")
    while (decicion == "s"):
        listaesta.append(input("ingrese el estado a la lista: "))
        decicion = input ("ingres s--> Para agregar mas estados n --> Para no agregar mas : ")
    return listaesta

doctores = llenarListadoc ()
enfermeros= llenarListaenfermer ()
enfermos= llenarListaenfe ()
estados = llenarListaesta ()
mostrar_dos_listas(enfermos, estados)
print("Estos son los doctores" "-->" ,doctores)
print("Estos son los enfermeros" "-->", enfermeros)
