#Pyplot es conjunto de instrucciones desarrollar graficos de diferente indolo
import matplotlib.pyplot as plt
import pandas as p 
personas = {
    "Nombres" : ["Pepito","Zacarias", "Julio", "Popeye", "Maria"],
    "Pesos" : [72,45,87,124,56]
}

print (personas["Nombres"])
print (personas["Pesos"])

plt.bar(personas["Nombres"],personas["Pesos"], color ="b", alpha=0.5)
plt.title("Pesos de pacientes")
plt.xlabel("Nombres")
plt.ylabel("Pesos (kg)")
plt.savefig("Pesos_pacientes.png")
plt.close()
#plt.show()

plt.barh(personas["Nombres"],personas["Pesos"], color ="b", alpha=0.5,align="center")
plt.title("Pesos de pacientes")
plt.xlabel("Nombres")
plt.ylabel("Pesos (kg)")
figure = plt.gcf()
figure.set_size_inches(9,9)
plt.savefig("Pesos_pacientes_horizontal.png")
plt.close()
#plt.show()

barrios = p.read_csv("barrios.csv",encoding='UTF-8',header=0, delimiter=";").to_dict()
print(barrios)
plt.title("Barrios habitantes", fontsize=20)
plt.bar(barrios["Barrio"].values(),barrios["Habitantes"].values(),align="center")
plt.xlabel("Barrios")
plt.ylabel("Habitantes")
plt.xticks(rotation=90)
figure = plt.gcf()
figure.set_size_inches(12,18)
plt.savefig("Barrios.png")
plt.close()
#plt.show()