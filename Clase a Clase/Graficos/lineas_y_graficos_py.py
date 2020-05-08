import matplotlib.pyplot as plt
import pandas as p
year =[2000,2001,2002,2003,2004,2005,2006]
dolar_pesos_colombianos =[1950,1820,1620,1650,1930,2080,2020]
dolar_soles =[250,820,620,350,430,280,920]
dolar_mexico =[50,25,20,50,30,80,20]



plt.plot(year,dolar_pesos_colombianos,color="g")
plt.plot(year,dolar_soles)
plt.plot(year,dolar_mexico)
plt.xlabel("Año")
plt.ylabel("Valor del dolar en pesos colombianos")
plt.title("Evolución del dolar")
plt.legend(["Dolar en Pesos colombianos", "Dola en Soles", "Dolar en pesos mexicanos"])
plt.savefig("Grafico dolar.png")
plt.close()
ecg =p.read_csv("ecg.csv",encoding='UTF-8',header=0, delimiter=";").to_dict()
x= list(ecg["muestra"].values())
y = list(ecg["valor"].values())
plt.title("ECG-uV")
plt.xlabel("Tiempo(ms)")
plt.ylabel("Volataje(uV)")
plt.plot(x,y)
plt.savefig("mi_ecg.png")
plt.close()

# Pie chart, where the slices will be ordered and plotted counter-clockwise:
labels = 'Java', 'python', 'C#', 'JavaScript'
sizes = [15, 45, 30, 10]
explode = (0.1, 0, 0, 0)  # only "explode" the 2nd slice (i.e. 'Hogs')
plt.pie(sizes, explode=explode, labels=labels, shadow=False, startangle=0)
plt.title("Lenguajes más usados")
plt.savefig("Grafico_pie.png")
plt.show()