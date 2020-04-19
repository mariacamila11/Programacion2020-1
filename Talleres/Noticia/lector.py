archivo = open ("noticia.txt",'r')
lineas_archivo = archivo.read().splitlines()
print(lineas_archivo[0])
