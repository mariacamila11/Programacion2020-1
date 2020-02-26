#------------MENSAJES----------#
SALUDO_PERSONA= "Bienvenido, vamos a calcular su IMC"
PREGUNTA_NOMBRE= " Ingresa tu nombre: "
MENSAJE_ESTATURA= " Ingresa tu estaura (M): "
MENSAJE_PESO= " Ingresa tu peso (KG): "
MENSAJE_DELGADEZMUYSEV= " Tienes delgadez MUY severa"
MENSAJE_DELGADEZSEVERA= " Tienes delgadez severa "
MENSAJE_DELGADEZ= " Tienes delgadez "
MENSAJE_SALUDABLE= " Felicitaciones tienes un peso saludable"
MENSAJE_SOBREPESO= "Tienes sobrepeso "
MENSAJE_OBESIDADSEVERA= "Tienes obesidad severa"
MENSAJE_OBESIDADMORBIDA= "Tienes obesidad morbida"
MENSAJE_TOCAYO= "Somos tocayos"
MENSAJE_DESP= " Hasta pronto"
#------------VARIABLES--------
NOMBRE_MIO = "camila"
calculo_IMC= 0.0
#------------ENTRADAS---------
_nombreUsuario = " "
_pesoUsuario= 1
_estaturaUsuario= 1.0
#------------CODIGO-----------
print (SALUDO_PERSONA)
_nombreUsuario= input (PREGUNTA_NOMBRE)
if  (NOMBRE_MIO == _nombreUsuario) :
   print (MENSAJE_TOCAYO)
_pesoUsuario= int(input(MENSAJE_PESO))
_estaturaUsuario= float(input(MENSAJE_ESTATURA))
calculo_IMC= ((_pesoUsuario)/ ((_estaturaUsuario)**2))
if ((calculo_IMC > 0 ) and (calculo_IMC < 15)): 
    print (MENSAJE_DELGADEZMUYSEV)
elif ((calculo_IMC >=15 ) and (calculo_IMC < 15.9)) :
    print (MENSAJE_DELGADEZSEVERA)
elif ((calculo_IMC >= 15.9) and (calculo_IMC < 18.4)) :
    print (MENSAJE_DELGADEZ)
elif ((calculo_IMC >= 18.4) and (calculo_IMC < 24.9)) :
    print (MENSAJE_SALUDABLE)
elif ((calculo_IMC >=24.9 ) and (calculo_IMC < 29.9)) :
   print (MENSAJE_SOBREPESO)
elif ((calculo_IMC >=29.9) and (calculo_IMC < 34.5)) :
    print (MENSAJE_OBESIDADSEVERA)
else:
  print (MENSAJE_OBESIDADMORBIDA)
print (MENSAJE_DESP)