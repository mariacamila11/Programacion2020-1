#------------MENSAJES----------#
import random
DADO1= int
DADO2= int 
suma= int
#------------CODIGO-----------
while (suma != 12 ):
    DADO1= random.randint(1,6)
    DADO2= random.randint(1,6)
    suma= DADO1 + DADO2
    print(DADO1)
    print(DADO2)
    print(suma)