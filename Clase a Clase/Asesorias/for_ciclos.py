#creando una lista de numeros del 0,1,2,3
range(4)
print (list(range(8)))
estudiantes = ["lesly","marco","daniel","Santiago","daniel","juanes"]
for i in estudiantes:
    print(i)
print("#"*60)
sizeList = len(estudiantes) #len es para encontrar el tamaño de la lista 
print(sizeList)
print("#"*60)
lista2 = list(range(sizeList))
print(len(lista2))
print("#"*60)
for i in range (sizeList):
    print (i)
    print(estudiantes[i])
    
