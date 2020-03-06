# numero = 0
# NUMERO_DESEADO = 12
# while(numero < NUMERO_DESEADO):
#     numero= numero+1
#     print(numero)
# print (numero)
import random 
PREGUNTA_NUMERO= " Ingrese un numero entero de 1 a 10: " 
MENSAJE_FALLO= " FAllASTE, INTENTATLO OTRA VEZ"
MENSAJE_ACIERTO= " ACERTASTE "
MENSAJE_MAYOR= "ESTAS CERCA, PERO EL NUMERO ES MAYOR"
MENSAJE_MENOR= "ESTAS CERCA, PERO EL NUMERO ES MENOR"
NUMERO_FAVORITO = random.randint(1,10)
_numeroIngresado= int(input(PREGUNTA_NUMERO))
while (_numeroIngresado != NUMERO_FAVORITO):
    print(MENSAJE_FALLO)
    if (_numeroIngresado > NUMERO_FAVORITO): print(MENSAJE_MAYOR)
    else: print(MENSAJE_MENOR)
    _numeroIngresado=int(input(PREGUNTA_NUMERO))
print(MENSAJE_ACIERTO)