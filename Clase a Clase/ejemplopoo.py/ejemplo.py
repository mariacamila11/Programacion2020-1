class Humano():
    def __init__(self,nombre):
        self.raza="ser humano"
        self.nombre= nombre 

ser_humano= Humano("camila")
ser_humano2=Humano("santiago")
print (ser_humano.raza)
print(ser_humano.nombre)
print(ser_humano2.raza)
print(ser_humano2.nombre)