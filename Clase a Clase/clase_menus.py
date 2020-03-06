lista_nombres= ["santiago",
"juanes","marco","elena","mch betancur","mch mesa", "leslly","ysabella","Santiago hernan","mafe","david","susi","daniel","daniel h"]
lista_nombres[4]= "Maria Camila Betancur"
lista_nombres[5]="Maria Camila Mesa"
print(lista_nombres)
lista_nombres.pop(13)
print(lista_nombres)
lista_nombres.append("Daniel Herrera")
print(lista_nombres)
_decision= int(input("""
            ingrese:
            1.Para ver lista de nombres
            2.Para ver edades
            3.para ver notas
            4.Para salir
"""))
while ( _decision != 4):
    if (_decision ==1):
        print(lista_nombres)
    elif(_decision ==2):
        print("lista edades")
    elif(_decision ==3):
        print(" lista notas")
    else:
        print("ingrese un valor valido")
    _decision= int(input("""
            ingrese:
            1.Para ver lista de nombres
            2.Para ver edades
            3.para ver notas
            4.Para salir
    """))