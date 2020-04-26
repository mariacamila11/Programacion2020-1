import pandas as p 
# Primera entrada nombre de archivo 
# Segunda entrada encoding(siempre sera UTF-8)
# Tercera entrada entrada es el header(como el encabezado, el titulo)
# El delimitador es el caracter que separa ms datos en este caso el ;
# .to_dict transforma mis datos en un diccionario 

diccionario =p.read_csv("balance.csv",encoding='UTF-8',header = 0, delimiter= ';').to_dict()
print(diccionario)
print(diccionario.keys())
print(diccionario["Ciudad"])


mayor_nombre= max(diccionario["Ciudad"].values(), key=len)
menor_nombre= min(diccionario["Ciudad"].values(), key=len)

print("\n\n La Ciudad con el nombre mas largo es {} y la ciudad con el nombre mas corto es {}".format(mayor_nombre, menor_nombre))

mayor_ganancia= max(diccionario["Ganancias"].values())
mayor_perdidas= max(diccionario["Perdidas"].values())

print("\n\n La mayor ganancia fue {}".format(mayor_ganancia))
print("\n\n La mayor Perdida fue {}".format(mayor_perdidas))