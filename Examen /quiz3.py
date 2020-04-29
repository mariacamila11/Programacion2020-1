import pandas as p

diccionario =p.read_csv("barrios.csv",encoding='UTF-8',header = 0, delimiter= ';').to_dict()
print(diccionario)
print(diccionario.keys())
print(diccionario["Barrio"])

# Nombre mas largo y mas corto
mayor_barrio= max(diccionario["Barrio"].values(), key=len)
menor_barrio= min(diccionario["Barrio"].values(), key=len)

print("\n\n El barrio con el nombre mas largo es {} y con el nombre mas corto es {}".format(mayor_barrio, menor_barrio))
# Mayor y menor consumo de agua
mayor_consumo_Agua= max(diccionario["Agua"].values())
menor_consumo_Agua= min(diccionario["Agua"].values())

print("\n\n El mayor consumo de agua fue {}".format(mayor_consumo_Agua))
print("\n\n El consumo minimo de agua fue {}".format(menor_consumo_Agua))
# Mayor y menor consumo de energia
mayor_consumo_Energia= max(diccionario["Energía"].values())
menor_consumo_Energia= min(diccionario["Energía"].values())

print("\n\n El mayor consumo de energia fue {}".format(mayor_consumo_Energia))
print("\n\n El consumo minimo de energia fue {}".format(menor_consumo_Energia))
# Mayor y menor consumo de gas
mayor_consumo_Gas= max(diccionario["Gas"].values())
menor_consumo_Gas= min(diccionario["Gas"].values())

print("\n\n El mayor consumo de gas fue {}".format(mayor_consumo_Gas))
print("\n\n El consumo minimo de gas fue {}".format(menor_consumo_Gas))
# Mayor y menor consumo de Internet 
mayor_consumo_Internet= max(diccionario["Internet"].values())
menor_consumo_Internet= min(diccionario["Internet"].values())

print("\n\n El mayor consumo de internet fue {}".format(mayor_consumo_Internet))
print("\n\n El consumo minimo de internet fue {}".format(menor_consumo_Internet))
# Cantidad maxima y minima de habitantes
mayor_Habitantes= max(diccionario["Habitantes"].values())
menor_consumo_Internet= min(diccionario["Habitantes"].values())

print("\n\n La cantidad maxima de habitantes es {}".format(mayor_consumo_Internet))
print("\n\n La cantidad minima de habitantes es {}".format(menor_consumo_Internet))
