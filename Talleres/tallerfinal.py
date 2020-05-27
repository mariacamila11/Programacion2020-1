import matplotlib.pyplot as plt
import pandas as p 
import sys

# Graficas
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

ppg =p.read_csv(file,encoding='UTF-8',header=0, delimiter=";").to_dict()
x= list(ppg["muestra"].values())
y = list(ppg["valor"].values())
plt.title(input("Ingrese el titulo de la grafica : "))
plt.xlabel(input("Ingrese el titulo de eje X : "))
plt.ylabel(input("Ingrese el titulo del eje Y : "))
plt.plot(x,y)
#plt.savefig(input("Ingrese el nombre de la grafica para guardar : "))
plt.show()

# # Calculo IMC 
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

# Graficos mercado
kilo_arroz= "No ingreso los kilos de arroz"
try:
    kilo_arroz= float(input(" Escribe los kilos de arroz: "))
except ValueError:
    print(" No dijitaste un valor valido")
print("Los kilos totales fueron",kilo_arroz)

kilo_lentejas= "No ingreso los kilos de lentejas"
try:
    kilo_lentejas= float(input(" Escribe los kilos de lentejas: "))
except ValueError:
    print(" No dijitaste un valor valido")
print("Los kilos totales fueron",kilo_lentejas)

kilo_frijoles= "No ingreso los kilos de frijol"
try:
    kilo_frijoles= float(input(" Escribe los kilos de frijol: "))
except ValueError:
    print(" No dijitaste un valor valido")
print("Los kilos totales fueron",kilo_frijoles)

kilo_papa= "No ingreso los kilos de arroz"
try:
    kilo_papa= float(input(" Escribe los kilos de papa: "))
except ValueError:
    print(" No dijitaste un valor valido")
print("Los kilos totales fueron",kilo_papa)

compras= { "Articulos": ["Arroz", "Lentejas", "Frijoles", "papa"]}
total= (kilo_arroz,kilo_frijoles,kilo_lentejas,kilo_papa)

print(compras["Articulos"])
print(total)

plt.bar(compras["Articulos"],total)
plt.title("Productos vs Kilos", fontsize=20)
plt.xlabel("Articulos")
plt.ylabel("kilos")
plt.savefig("Articulos_kilo.png")
plt.show()

#Parrafo
def reconocer_parraf(Parrafo):
    assert(Parrafo.endswith("."))
    return False
reconocer= True

while(reconocer):
    Parrafo= input(" Como te sientes al salir de compras, cuando termines de escribir termina en punto : ")
    try:
        reconocer=reconocer_parraf(Parrafo)
    except AssertionError:
        print("No terminaste con punto")

#Compras de la tienda
labels= "Leche", "Huevo", "Vino", "Arroz", "Queso", "Salchichas"
sizes=[12,8,4,26,30,20]
explode= (0,0,0,0,0.1,0)
plt.pie(sizes, explode=explode, labels=labels, shadow=False, startangle=0)
plt.title("% De productos" )
plt.savefig("Productos.png")
plt.show()

