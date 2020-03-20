class Persona():
    def __init__(self,nombre,talla,sexualidad,peso,edad):
        self.raza = "Ser humano"
        self.name = nombre
        self.size = talla 
        self.gender = sexualidad
        self.weight = peso 
        self.age = edad
        print ("Hola a todos soy un", self.raza,"Mi nombre es",self.name)

    def mostrar_atributos(self):
        print("Mi nombre es ",self.name)
        print("Mi estatura es", self.size)
        print("Mi genero es",self.gender)
        print("Mi peso es",self.weight)
        print("Mi edad es",self.age)

    def caminar(self,cantidad_pasos):
        for i in range (cantidad_pasos):
                print("He caminado",i+1,"pasos")

ser_humano_1 = Persona("Camila",1.55,"Femenino",54,20)
ser_humano_2 = Persona("Daniel",1.67,"Masculino",77,26)

ser_humano_1.mostrar_atributos()
ser_humano_2.mostrar_atributos()

ser_humano_1.caminar(100)