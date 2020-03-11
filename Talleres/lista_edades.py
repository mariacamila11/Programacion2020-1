lista_nombres= ["santiago",
"juanes","marco","elena","mch betancur","mch mesa", "leslly","ysabella","Santiago hernan","mafe","david","susi","daniel","daniel h"]
lista_edades= [20,17,19,18,20,18,19,18,18,21,21,20,19,26]
lista_notas=[3.0, 4.5, 4.0, 3.4, 3,6, 4.0, 3.4, 3.3, 3.5, 3,7, 3.5,4.6, 4.1, 3,9]
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
        print(lista_edades)
    elif(_decision ==3):
        print(lista_notas)
    else:
        print("ingrese un valor valido")
    _decision= int(input("""
            ingrese:
            1.Para ver lista de nombres
            2.Para ver edades
            3.para ver notas
            4.Para salir
    """))