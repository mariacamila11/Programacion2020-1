PREGUNTA1= "Que edad tienes : "
MENSAJE= "No puedes entrar porque eres menor de edad"
MENSAJEDESCU="Tienes un descuento del 30%"
MENSAJESESENTA= "Tienes un descuento igual a tu edad "
MENSAJEVALIDO= "Ingrese un valor valido"
MENSAJECOSAS="Desea Mercar? s -> si   n-> no : "
MENSAJENUMERO="Digita el numero que quieras eliminar : "
_preguntaEdad=" " 
lista_productos= ["Huevo--"
"--Pan--"
"--Arroz--"
"--Leche--"
"--Frutas--"
"--Galletas--" 
"--Papas--"]
#--------------------------------------------------------------
_opcion= int(input("""
    1.Digita tu edad 
    2.Ingresa la lista de productos
    3.Mostrar la lista elemento a elemento 
    4.Eliminar un elemento de la lista
    5.salir
"""))
while (_opcion !=5 ):
    if (_opcion == 1):
        _preguntaEdad= int(input(PREGUNTA1))
        if ((_preguntaEdad >= 0 ) and (_preguntaEdad <= 17 )): 
            print(MENSAJE)
        elif (( _preguntaEdad >= 30) and (_preguntaEdad <= 59)):
            print(MENSAJEDESCU)
        elif ( _preguntaEdad == 30):
            print(MENSAJEDESCU)
        else:
            print(MENSAJESESENTA)
   
    elif (_opcion ==2):
        productos=[]
        _lista_cosas= input(MENSAJECOSAS)
        while (_lista_cosas == "s"):
            productos.append (input("Ingrese : "))
            _lista_cosas= input(MENSAJECOSAS)
            print(productos)
    elif(_opcion ==3):                                                                                                                                                                                                                                              
        print(lista_productos)
        print(productos)
    elif (_opcion ==4):
        print(productos)
        _numero= int(input(MENSAJENUMERO))
        productos.pop(_numero)
        print(productos)
    else:
        print(MENSAJEVALIDO)
    _opcion= int(input("""
        1.Digita tu edad 
        2.Ingresa la lista de productos
        3.Mostrar la lista elemento a elemento 
        4.Eliminar un elemento de la lista
        5.salir
    """))

