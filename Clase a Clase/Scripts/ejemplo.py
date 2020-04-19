import funciones_lectura_archivos as helper
##Leimos el archivo
lineas= helper.leer_archivo("Libro.txt")
#Lo mostramos linea por linea
helper.mostrar_lineas(lineas)

Texto = ["Hola este es mi primer archivo creado en python\n","Espero que funcione bien!! \n"
"más contenido"]
helper.escritura_archivo("Intento1.txt",Texto)
helper.agregar_lineas_archivo("noticia.txt","\n16 de Abril")


#Actividad : Crear archivo nuevo llamado noticia.txt y allí vamos agregar una noticia favorita
#Mostrar en pantalla el archivo

#Luego crear un archivo que se llame opinion.txt que contenga su punto de vista referente a la noticia
#Agregar una linea a la noticia original que sea la fecha en la que se publicó y el medio