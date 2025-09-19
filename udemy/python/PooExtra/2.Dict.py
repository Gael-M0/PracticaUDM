'''
class Animal:
    def __init__(self, especie, nombre):
        self.especie = especie
        self.nombre = nombre

animal1 = Animal("Felino","Lion")
animal2 = Animal("Canino","Firulais")

print(animal1.__dict__)
print(animal2.__dict__)
'''

class Animal:
    reino = "Animalia"

    def __init__(self, especie, nombre):
        self.especie = especie
        self.nombre = nombre

print(Animal.__dict__)