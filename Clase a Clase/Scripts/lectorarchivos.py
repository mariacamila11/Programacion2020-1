#Guarda en memoria el archivo para su posterior uso
archivo = open ("Libro.txt",'r')
# print(archivo)
lineas_archivo = archivo.read().splitlines()
print(lineas_archivo[0])
print("sentido" in lineas_archivo[0])