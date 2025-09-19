class Animales():
    def __init__(self , edad):
        self.edad = 10


    def hablar(self):
        print("Yo soy un animal")

    def descripcion(self):
        print("yo soy un {}".format(self.animal))

class Perro(Animales):
    def __init__(self, edad):
        super().__init__(edad)
        self.animal = "Perro"

class Abeja(Animales):
    def __init__(self , animal , edad):
        super().__init__(edad)
        self.animal = animal


dog = Perro(5)
dog.hablar()

abeja = Abeja("Abeja", 10)
abeja.descripcion()
print(abeja.edad)
