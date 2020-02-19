#Mesajes 
PREGUNTA_NOMBRE= "ingrese su nombre \n "
MENSAJE_BIENVENIDO= "Bienvenido"
PREGUNTA_EDAD= "Tu edad es"
PREGUNTA_ESTATURA= "Tu estatura es"


_nombrePersona = input(PREGUNTA_NOMBRE)
print (MENSAJE_BIENVENIDO, _nombrePersona,)
_edadPersona =int(input("ingrese su edad \n "))
print (PREGUNTA_EDAD, _edadPersona)
print (type(_edadPersona))
_estaturaPersona =float(input("ingrese su estatura \n "))
print (PREGUNTA_ESTATURA, _estaturaPersona)
print (type(_estaturaPersona))