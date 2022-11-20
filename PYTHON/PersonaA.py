class Persona():
# Método constructor
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
    def identificarse(self): # Método normal
        print(f"Hola. Soy {self.nombre}y tengo {self.edad} años.")


# Instanciamos
persona1 = Persona("Juan", 42)
persona1.identificarse()
persona1.edad = 43 # Modificamos la edad
persona1.identificarse()