class Persona:
    edad=25
    nombre="Jorge"

persona1=Persona()
persona1.edad=33
persona1.direccion="san juan"
print(persona1)
print(persona1.edad)
print(persona1.direccion)


persona2=Persona()
persona2.edad=65
print(persona2)
print(persona2.edad)

persona3=persona1
print(persona3)
print(persona3.edad)