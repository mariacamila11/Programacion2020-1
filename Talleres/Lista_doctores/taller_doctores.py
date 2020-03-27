doctores=[ "Camila," "Alejandro," "Sebastian"]
enfermeros=["Ana," "Luis," "Carlos"]
enfermos= ["Carolina," "Manuela" ] 
estados=["Grave," "Moderado," "Estable"]

def mostrar_dos_listas(lista_1,lista_2):
    if (len(lista_1) == len(lista_2)):
        print("Enfermo","Estado")
        for i in range(len(lista_1)):
            print(lista_1[i],lista_2[i])

    else:
        print("no se puede mostrar uno a uno")

def bienvenida(): print("Bienvenido al código")

def llenarLista():
    lista = []
    decicion = input ("ingrese s--> Para agregar los nombres n --> Para no agregar mas : ")
    while (decicion == "s"):
        lista.append(input("ingrese un Doctor de la lista: "))
        decicion = input ("ingres s--> Para agregar mas elementos n --> Para no agregar mas : ")
        lista.append(input("ingrese un enfermero de la lista: "))
        decicion = input ("ingres s--> Para agregar mas elementos n --> Para no agregar mas : ")
        lista.append(input("ingrese un Enfermo de la lista: "))
        decicion = input ("ingres s--> Para agregar mas elementos n --> Para no agregar mas : ")
    return lista

print ("Ingrese la lista de nombres")
doctores = llenarLista ()
enfermeros= llenarLista
enfermos= llenarLista
print ("Ingrese el estado de los enfermos")
estados = llenarLista ()
mostrar_dos_listas(enfermos, estados)