#------MENSAJES------#
PREGUNTA_NOMBRE= "ingrese su nombre : "
PREGUNTA_EDAD= "ingrese su edad : "
MENSAJE_BIENENIDO="Binvenido"
MENSAJE_DESPEDIDA="Chao"
MENSAJE_TOCAYO= "Hola somos tocayos"
MENSAJE_JOVEN= " Eres joven"
MENSAJE_ADULTO= " Eres adulto"
MENSAJE_ADULTO_MAYOR= "Eres adulto mayor"
#------VARIABLES---------------
NOMBRE_PERSONAL= "camila"
#------ENTRADAS----------------
_nombrePersona = " "
_edadUsuario= 0 
#------CODIGO------------------
print (MENSAJE_BIENENIDO)
_nombrePersona= input(PREGUNTA_NOMBRE)
if (NOMBRE_PERSONAL == _nombrePersona) :
    print(MENSAJE_TOCAYO)
_edadUsuario= int(input(PREGUNTA_EDAD))
if((_edadUsuario >= 0) and (_edadUsuario <= 25)) : 
    print(MENSAJE_JOVEN)
elif ((_edadUsuario >=26) and (_edadUsuario <= 65)) :
    print(MENSAJE_ADULTO)
else:
    print (MENSAJE_ADULTO_MAYOR)
print (MENSAJE_DESPEDIDA) 
