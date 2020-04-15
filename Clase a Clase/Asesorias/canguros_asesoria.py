# Canguros:
#        atributos: edad, id
#        funciones: saltar(cantidad_de_saltos)
#        --> entradas: cantidad_de_saltos = cantidad de saltos del canguro
#        --> salidas :none
class Canguros ():
    def __init__(self,edad_ingresada,id_ingresado):
        self.edad = edad_ingresada
        self.id = id_ingresado
    def saltar(self,cantida_de_saltos):
        for i in range(cantida_de_saltos):
            print("hola a todos soy un canguro de identificacion {} y di mi salto numero {} y estoy en forma".format(self.id,i+1))

# Cuidadores:
#        atributos: nombre, id
#        funciones: alimentar_canguros(cantidad_de_canguros)
#                   --> entradas: cantidad_de_canguros = cantidad de canguros a alimentar
#                   --> salidas :none
#
class Cuidadores():
    def __init__(self,name, id_ingresado):
        self.nombre = name
        self.id = id_ingresado
    def alimentar_canguros (self,cantidad_canguros):
        for i in range(cantidad_canguros):
            print("""
                hola a todos soy un cuidador de nombre {} 
                y alimenté al canguro numero {} y estoy ocupado"""
            .format(self.nombre,i+1))

#Jefe(Cuidadores)
#        funciones: 
#               contratar(nombre, id)
#                   --> entradas: nombre = nombre del cuidador
#                   --> entradas: id = identificacion del cuidador
#                   --> salida:contratado 
#               dar_mensaje(mensaje)
#                   --> entradas: mensaje = mensaje a mostrar
#                   -->salidas: none

class Jefe(Cuidadores):
    def dar_mensaje(self,mensaje):
        print("hola todos mi nombre es {} y vengo dar el siguiente mensaje".format(self.nombre))
        print(mensaje)
    def contratar (self,id,nombre):
        cuidador = Cuidadores(nombre,id)
        return cuidador

canguro1 = Canguros(27,100)
canguro1.saltar(140)

cuidador1= Cuidadores("mafer",120)
cuidador1.alimentar_canguros(69)

jefe1= Jefe("Octavio",32)
jefe1.dar_mensaje("Espero que haya servido de algo esta asesoria")

cuidador2 = jefe1.contratar(23,"daniel") 
cuidador2.alimentar_canguros(34)