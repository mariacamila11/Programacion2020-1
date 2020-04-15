####Import#####

#########variables########
estudiantes = ["David", "santiago", "juanes", "lesly"]
estudiantes_edades = [20,19,17,19]
estudiantes_identificaciones = [20,19,17,19]
########mensajes#########
mensaje_pregunta= """    
    1- sea ingresar un nuevo estudiante edad,nombre, ID
    2- mostrar lista de estudiantes segun el nombre
    3- mostrar lista de nombres y edades
    4- ingresar varios estudiantes hasta que desee parar edad,nombre,id
    5-salir
"""
#########Definiciones##########
def agregar_estudiante(lista_nombres, lista_edades,lista_id):
    nombre= input("ingrese nombre del estudiante nuevo : ")
    lista_nombres.append(nombre)
    edad = int(input("ingrese la edad del estudiante nuevo : "))
    lista_edades.append(edad)
    identificacion = int (input ("ingrese el nuevo id : "))
    lista_id.append(identificacion)

def mostrar_lista(lista):
    for elemento in lista:
        print(elemento)

def mostrar_dos_listas(lista1,lista2):
    size_lista1 = len(lista1)
    size_lista2 = len(lista2)
    if (size_lista1==size_lista2):
        for i in range(size_lista1):
            print(lista1[i],lista2[i])
    else:
        print("las listas son de diferente tamaño no se muestran juntas")

def agregar_varios(lista_nombres, lista_edades, lista_id):
    _decision = "s"
    pregunta = """
        s-> Argegar más estudiantes
        n->para salir
    """
    while (_decision != "n"):
        if (_decision =="s"):
            agregar_estudiante(lista_nombres,lista_edades,lista_id)
        else:
            print("entrada no válida")
        _decision = input(pregunta)

def main():
    _eleccion_usuario =0
    while (_eleccion_usuario!=5):
        _eleccion_usuario = int(input(mensaje_pregunta))
        if (_eleccion_usuario==1):
            agregar_estudiante(estudiantes,estudiantes_edades,estudiantes_identificaciones)
        elif (_eleccion_usuario ==2):
            mostrar_lista(estudiantes)
        elif (_eleccion_usuario == 3):
            mostrar_dos_listas(estudiantes, estudiantes_edades)
        elif (_eleccion_usuario == 4):
            agregar_varios(estudiantes,estudiantes_edades,estudiantes_identificaciones)
        elif(_eleccion_usuario == 5):
            print("Gracias por usar el programa")
        else:
            print("ingrese un número válido")


######Entrada al código

main()