import matplotlib.pyplot as plt
import pandas as p
#Agua
barrios = p.read_csv("barrios.csv",encoding='UTF-8',header=0, delimiter=";").to_dict()
plt.title("Barrios VS Agua", fontsize=20)
plt.bar(barrios["Barrio"].values(),barrios["Agua"].values(),align="center")
plt.xlabel("Barrios")
plt.ylabel("Agua")
plt.xticks(rotation=90)
figure = plt.gcf()
figure.set_size_inches(12,18)
plt.savefig("Agua.png")
plt.close()

#Gas
plt.title("Barrios VS Gas", fontsize=20)
plt.bar(barrios["Barrio"].values(),barrios["Gas"].values(),align="center")
plt.xlabel("Barrios")
plt.ylabel("Gas")
plt.xticks(rotation=90)
figure = plt.gcf()
figure.set_size_inches(12,18)
plt.savefig("Gas.png")
plt.close()

#Ecg paciente diagnostiado 
ecg =p.read_csv("ecg.csv",encoding='UTF-8',header=0, delimiter=";").to_dict()
x= list(ecg["muestra"].values())
y = list(ecg["valor"].values())
plt.title("ECG-(uV)-Paciente diagnosticado")
plt.xlabel("Tiempo(ms)")
plt.ylabel("Volataje(uV)")
plt.plot(x,y)
plt.savefig("ECG_Diagnostico.png")
plt.close()

#Grafico de pie 
labels = 'Bogota', 'Medellin', 'Leticia', 'Villavivencio'
sizes = [80, 7, 5, 8]
explode = (0, 0, 0.1,0)  # only "explode" the 2nd slice (i.e. 'Hogs')
plt.pie(sizes, explode=explode, labels=labels, shadow=False, startangle=0)
plt.title("Poblaciones analizadas")
plt.savefig("Pie_poblacion.png")
