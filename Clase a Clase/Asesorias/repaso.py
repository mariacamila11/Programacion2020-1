estudiantes= ["Camila", "Alejandro", "Santiago", "Daniel"]
edades= [20,20,19,25]
id= [234,244,456,123]

mensaje_pregunta= """
    1. Desea ingresar un nuevo estudiante edad, nombre, ID
    2. Mostrar lista estudiante segun el nombre
    3. Mostrar lista de nombres y edades
    4. Ingresar varios estudiantes hasta que desee parar
    5. Salir
"""
def estudiante_nuevo(lista_nombres, lista_edades, lista_id):
    nombre= input("Ingrese un nombre : ")
    lista_nombres.append(nombre)
    edades= int(input("Ingrese una edad : "))
    lista_edades.append(edades)
    id= int(input("Ingrese el id: "))
    lista_id.append(id)

def mostar_lista(estudiante):
    for elemento in estudiantes:
        print(elemento)

def mostrar_dos_listas(lista_nombres,lista_edades):
    size_lista_nombres= len(lista_nombres)
    size_lista_edades= len(lista_edades)
    if (size_lista_nombres == size_lista_edades ):
        for i in range(size_lista_nombres):
            print(lista_nombres[i], lista_edades[i])
    else:
        print("Las listas no son del mismo tamaño")

def agregar_mas(lista_nombres, lista_edades, lista_id):
    _opcion= "s"
    pregunta= """
        s --> Para agregar personas 
        n --> Para no agregar nadie mas
""" 
    while (_opcion != "n"):
        if (_opcion == "s"):
            estudiante_nuevo(lista_nombres,lista_edades,lista_id)
        else:
            print(" Entrada no valida")
        _opcion= input(pregunta)

def main():
    _eleccion_usuario=0 
    while (_eleccion_usuario != 5):
        _eleccion_usuario= int(input(mensaje_pregunta))
        if (_eleccion_usuario == 1):
            estudiante_nuevo(estudiantes,edades,id)
        elif (_eleccion_usuario ==2):
            mostar_lista(estudiantes)
        elif (_eleccion_usuario == 3):
            mostrar_dos_listas(estudiantes, edades)
        elif (_eleccion_usuario == 4):
            agregar_mas(estudiantes,edades,id)
        else:
            print("Ingrese un numero valido")

main()