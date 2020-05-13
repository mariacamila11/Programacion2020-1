import matplotlib.pyplot as plt
import pandas as p

#Elementos vs Unidades 
inventario = p.read_csv("inventario.csv",encoding='UTF-8',header=0, delimiter=";").to_dict()
plt.title("Elementos VS Unidades", fontsize=20)
plt.bar(inventario["Elemento"].values(),inventario["Unidades"].values(),align="center")
plt.xlabel("Elementos")
plt.ylabel("Unidades")
plt.xticks(rotation=90)
figure = plt.gcf()
figure.set_size_inches(15,15)
plt.savefig("Elementos.png")
plt.close()

#Elementos viejos
inventario = p.read_csv("inventario.csv",encoding='UTF-8',header=0, delimiter=";").to_dict()
plt.title("Elementos VS Elementos viejos", fontsize=20)
plt.bar(inventario["Elemento"].values(),inventario["Viejo"].values(),align="center")
plt.xlabel("Elementos")
plt.ylabel("Elementos Viejos")
figure = plt.gcf()
figure.set_size_inches(15,15)
plt.savefig("Elementos_Viejos.png")
plt.close()

#Elementos nuevos
inventario = p.read_csv("inventario.csv",encoding='UTF-8',header=0, delimiter=";").to_dict()
plt.title("Elementos VS Elementos nuevos", fontsize=20)
plt.bar(inventario["Elemento"].values(),inventario["Nuevos"].values(),align="center")
plt.xlabel("Elementos")
plt.ylabel("Elementos Nuevos ")
plt.xticks(rotation=90)
figure = plt.gcf()
figure.set_size_inches(15,15)
plt.savefig("Elementos_Nuevos.png")
plt.close()

#Ppg
ppg =p.read_csv("ppg.csv",encoding='UTF-8',header=0, delimiter=";").to_dict()
x= list(ppg["muestra"].values())
y = list(ppg["valor"].values())
plt.title("PPG-(uV)-Paciente diagnosticado")
plt.xlabel("Tiempo(ms)")
plt.ylabel("Volataje(uV)")
plt.plot(x,y)
plt.savefig("PPG_Diagnostico.png")
plt.close()

#Pacientes UCI
labels = 'Recuperados en casa', 'Hospitalizado', 'UCI'
sizes = [85, 10, 5]
explode = (0, 0, 0.1) 
plt.pie(sizes, explode=explode, labels=labels, shadow=False, startangle=0)
plt.title("Casos Diagnosticados")
plt.savefig("Poblacion_Casos.png")




