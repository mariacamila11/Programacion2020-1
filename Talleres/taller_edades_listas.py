listaEdades= [1,2,4,8,16,32,64]
print("Bienvenido")

listaEdades =[1,2,3,8,16,32,64]

def mostrar_lista(listaEdades):
    if ( len ( listaEdades)):
        for i in range (len(listaEdades)):
            print (listaEdades[i])

def llenar_lista ():
    lista = []
    decision =input("ingrese s--> Para agregar mas edades n--> Para no agregar mas edades : ")
    while (decision == "s"):
        lista.append (input("Ingrese la edad del paciente : "))
        decision = input ("ingrese s--> Para agregar mas gente n--> Para no agregar mas personas :")
    return lista

edades = llenar_lista() 
mostrar_lista(edades)

promedio = (((1+2+4+8+16+32+64)/7))
print ("Valor del promedio: ")
print (promedio)

listaEdades = [1,2,4,8,16,32,64]
listaAgregar = [edades]
listaAgregar.extend(listaEdades)
print(listaAgregar)

print("la edad mayor en la lista de nueva {} es el {}".format(edades, max (edades)))
print("la edad mayor en la lista inicial {} es el {}".format(listaEdades, max(listaEdades)))

print("la edad menor en la lista de nuevos {} es el {}".format(edades, min(edades)))
print("la edad menor en la lista inicial {} es el {}".format(listaEdades, min (listaEdades)))

edades.sort()
print("lista nuevos crecientemente {}".format(edades))
listaEdades.sort()
print ("lista iniciales crecientemente {}".format(listaEdades))

print(listaEdades)
listaEdades.insert (4,87)
print("Se inserto el numero 87 en la posicion 4")
print (listaEdades)