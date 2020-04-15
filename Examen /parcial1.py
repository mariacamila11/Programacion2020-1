class Estudiantes():
    def __init__(self,nombre,edad,genero,colegio):
        self.nombre= nombre
        self.edad= edad
        self.genero= genero 
        self.colegio= colegio
    def asistencia_clase(self,num_clases):
        for i in range(num_clases):
            print("Soy el estudiante {} y asisti a la clase # {} ".format(self.nombre,i+1))

class Profesor():
    def __init__(self,nombre,edad,nivel_educativo):
        self.nombre= nombre
        self.edad= edad
        self.nivel= nivel_educativo
    def dictar_clases(self,clases_dia):
        for i in range(clases_dia):
            print("Soy el profesor {} y hoy dare mi clase # {}".format(self.nombre,i+1))

class Director(Profesor):
    def dar_noticia(self,mensaje):
        print("Hola soy la directora {} y contratare unos profesores".format(self.nombre))
        print(mensaje)
    def contrato(self,nombre):
        profesor_nuevo= Profesor("Ana",35,7)
        return(profesor_nuevo)

estudiante1= Estudiantes("Camila",20,"femenino","Santa maria del rosario")
estudiante2= Estudiantes("Maria",21,"femenino","La salle")
estudiante3= Estudiantes("Alejandro",20,"masculino","La colina")
estudiante4= Estudiantes("Tomas",28,"masculino","San jose de las vegas")
estudiante5=Estudiantes("Luis",19,"Masculino","Cerini")

estudiante1.asistencia_clase(5)
estudiante2.asistencia_clase(1)
estudiante3.asistencia_clase(2)
estudiante4.asistencia_clase(4)
estudiante5.asistencia_clase(3)

profesor1=Profesor("Javier",30,5)
profesor2=Profesor("Cristina",47,6)

profesor1.dictar_clases(2)
profesor2.dictar_clases(5)

director1= Director("Ana",35,7)
director1.dar_noticia("Nuevos Profesores: ")

profesor3=director1.contrato("Sara")
profesor4=director1.contrato("Daniel")

profesor3.dictar_clases(1)
profesor4.dictar_clases(4)

mensaje_pregunta= """    
    1- Mostrar atributos de los estudiantes
    2- Mostrar atributos de los Profesores
    3- Mostrar atributos del director
    4-Salir
"""
def main():
    _eleccion_usuario =0
    while (_eleccion_usuario!=4):
        _eleccion_usuario = int(input(mensaje_pregunta))
        if (_eleccion_usuario==1):
            print(estudiante1.nombre, estudiante1.edad, estudiante1.genero, estudiante1.colegio)
            print(estudiante2.nombre, estudiante2.edad, estudiante2.genero, estudiante1.colegio)
            print(estudiante3.nombre, estudiante3.edad, estudiante3.genero, estudiante1.colegio)
            print(estudiante4.nombre, estudiante4.edad, estudiante4.genero, estudiante1.colegio)
            print(estudiante5.nombre, estudiante5.edad, estudiante5.genero, estudiante1.colegio)
        elif (_eleccion_usuario ==2):
            print(profesor1.nombre, profesor1.edad, profesor1.nivel)
            print(profesor2.nombre, profesor2.edad, profesor2.nivel)
            print(profesor3.nombre, profesor3.edad, profesor3.nivel)
            print(profesor4.nombre, profesor4.edad, profesor4.nivel)
        elif (_eleccion_usuario == 3):
            print(director1.nombre)
        elif(_eleccion_usuario == 4):
            print("Gracias por usar el programa")
        else:
            print("ingrese un número válido")

main()