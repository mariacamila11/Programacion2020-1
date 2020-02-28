#------------MENSAJES----------#
MENSAJE_TEMPERATURA= "Ingrese la temperatura : "
MENSAJE_PROCEDENCIA= "Ingrese la procedencia : "
MENSAJE_SALUDABLE= " El estado es saludable "
MENSAJE_HIPOTERMIA= " El estado es hipotermia "
MENSAJE_ALERTA= "El estado es de alerta"
MENSAJE_PELIGRO= "El estado es de PELIGRO"
MENSAJE_5GRU= "Esta dentro de los destinos de observacion "
#------------VARIABLES--------
procedencia_italia= "italia"
procedencia_iran= "iran"
procedencia_china= "china"
#------------ENTRADAS---------
_procedencia_per= " "
_procedencia_ira= " "
_procedencia_chi= " "
_temperatura_persona= 1.0
_procedencia_per= ""
#------------CODIGO-----------
_temperatura_persona= float(input(MENSAJE_TEMPERATURA))
_procedencia_per= input(MENSAJE_PROCEDENCIA)
if (procedencia_italia == _procedencia_per or procedencia_iran==_procedencia_per or procedencia_china ==_procedencia_per) :
    print (MENSAJE_5GRU)
elif ((_temperatura_persona >=36) and (_temperatura_persona <= 38.4)):
    print (MENSAJE_SALUDABLE)
elif ((_temperatura_persona <36)) :
    print (MENSAJE_HIPOTERMIA)
elif (_temperatura_persona >= 38.5) and (_temperatura_persona <=40 ) :
    print(MENSAJE_ALERTA)
else:
    print (MENSAJE_PELIGRO)



