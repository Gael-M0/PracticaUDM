class Persona: # Las variables son los datos dentro de la clase como en este caso nombre y edad

    def __init__(self, nombre, edad):
        self.nombre = nombre   # Variable de instancia
        self.edad = edad       # Variable de instancia

#Los objetos son datos hechos por medio de la clase y los datos dentro de ella
p1 = Persona("Ana", 20)   # Objeto 1
p2 = Persona("Luis", 25)  # Objeto 2

print(p1.nombre)  # Ana
print(p2.nombre)  # Luis
