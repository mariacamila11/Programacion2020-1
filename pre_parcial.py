class Canguro():
    def __init__(self,peso,genero,cantidad,saltos):
        self.peso=  peso 
        self.saltos= saltos
        self.genero= genero 
        self.cantidad= cantidad

class Cuidador():
    def __init__(self,nombre):
        self.nombre= nombre
    def alimentar_canguro(self,gramos,cantidad):
        print("Le dare comida a los canguros")
        total= cantidad/gramos_cuido
        return total

class Jefe(Cuidador):
    def contrato_cuidador(self,nombre):
        print("Voy a contratar un cuidador")
        nuevo_cuidador= Cuidador(nombre)
        return nuevo_cuidador

canguro1= Canguro(70,"masculino",90,20)
canguro2= Canguro(60,"femenino",91,30)
canguro3= Canguro(50,"masculino",91,11)
canguro4= Canguro(90,"femenino",91,21)
canguro5= Canguro(100,"masculino",91,39)
canguro6= Canguro(60,"femenino",91,6)
canguro7= Canguro(60,"masculino",91,24)
canguro8= Canguro(60,"femenino",91,20)
canguro9= Canguro(60,"masculino",91,10)
canguro10= Canguro(60,"femenino",91,8)

saltoo= (canguro1.saltos+4)

print("El genero del primer canguro es", canguro1.genero)
print("El genero del primer canguro es", canguro2.genero)

cuidador1=  Cuidador("Camila")
gramos_cuido= 30000
porcion= cuidador1.alimentar_canguro(gramos_cuido,canguro1.cantidad)

print("Hola soy", cuidador1.nombre, "y le dividi la comida para", gramos_cuido, "Canguros")
print("La porcion para cada uno es", porcion)
print("El canguro dio", saltoo, "Saltos")

cuidador2= Jefe("Maria")
contrato= cuidador2.contrato_cuidador("Alejandro")
print(contrato)