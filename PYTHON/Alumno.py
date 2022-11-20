# Creamos la clase "Alumno":
class Alumno:
    def __init__(self, nombre, nota):
        self.nombre = nombre
        self.nota = nota
    def __str__(self):
        return f"La nota de {self.nombre} es {self.nota}"

alumno1 = Alumno("Pedro", 7)
print(alumno1) # La nota de Pedro es 7
alumno1.nota = 10
print(alumno1) # La nota de Pedro es 10