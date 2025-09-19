class Persona:
    especia = "Homo sapiens"

    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

persona1 = Persona("Juan", 30)

print(persona1.especia)
print(persona1.edad)

Persona.especia = "Humano moderno"
print(persona1.especia)