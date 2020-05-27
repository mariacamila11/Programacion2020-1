import matplotlib.pyplot as plt
import pandas as p 
import sys

#Archivos
def reconocer_archivo (file):
    assert(file)
    return False
reconocer= True

while (reconocer):
    file= input(" Digite el nombre del archivo que quieras ejecutar : ")
    try:
        reconocer= open(file)
        reconocer= False
    except FileNotFoundError:
        print("El nombre del archivo no es valido")

eeg =p.read_csv(file,encoding='UTF-8',header=0, delimiter=";").to_dict()
x= list(eeg["muestra"].values())
y = list(eeg["valor"].values())
plt.title(input("Ingrese el titulo de la grafica : "))
plt.xlabel(input("Ingrese el titulo de eje X : "))
plt.ylabel(input("Ingrese el titulo del eje Y : "))
plt.plot(x,y)
#plt.savefig(input("Ingrese el nombre de la grafica para guardar : "))
plt.show()

#IMC
nombre = "\nNo ingresaste el nombre"
try:
    nombre = (input('Ingrese su nombre : '))
except ValueError:
    print ("ingresaste mal el nombre")
print ("Hola", nombre,"procederemos a calcular tu IMC")

edad = "No ingresaste edad"
try:
    edad = int (input('Ingrese su edad : '))
except ValueError:
    print ("ingresaste mal la edad")
print ("Tu edad es", edad)

estatura = "No ingresaste tu estatura"
try:
    estatura = float (input('Ingrese su estatura : '))
except ValueError:
    print ("ingresaste mal la estatura")
print ("Tu estatura es", estatura)

peso = "No ingresaste tu peso"
try:
    peso = float (input('Ingrese su peso : '))
except ValueError:
    print ("ingresaste mal el peso")
print ("Tu peso es", peso)

IMC = ((peso/estatura**2))
print ("Como resultado tu IMC ES : ",IMC)

# Casa
labels= "Sala", "Alcoba", "Baño", "Cocina", "Balcon"
sizes=[5,75,5,5,10]
explode= (0,0.1,0,0,0)
plt.pie(sizes, explode=explode, labels=labels, shadow=False, startangle=0)
plt.title("% De lugares" )
plt.savefig("Lugares.png")
plt.show()

#Graficos 

Pico_ecg= 9

Pico_eeg= 10

pico_ppg= 9

picos= { "Picos": ["ECG", "EEG", "PPG"]}
total= (Pico_ecg,Pico_eeg,pico_ppg)

print(picos["Picos"])
print(total)

plt.bar(picos["Picos"],total)
plt.title("Picos vs Analisis", fontsize=20)
plt.xlabel("Picos")
plt.ylabel("Analisis")
plt.savefig("Picos.png")
plt.show()

#Texto
Texto = ["El aprendizaje supervisado es crear una función capaz de predecir el valor correspondiente a cualquier objeto de entrada válida por ejemplo una maquina necesita a alguien pendiente de los procesos" 
"El aprendizaje no supervisado (inteligencia artificial) es un método de Aprendizaje Automático donde un modelo se ajusta a las observaciones. " ]

print(Texto)
