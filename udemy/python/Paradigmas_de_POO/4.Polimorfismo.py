class Animales():
    def __init__(self, mensaje):
        self.mensaje = mensaje

    def hablar(self):
        print(self.mensaje)

class Perro(Animales):
    def hablar(self):
        print("Yo hago woof")

class Pez(Animales):
    def hablar(self):
        print("Yo no hablo")

perroO = Perro("woof")
perroO.hablar()

animal0 = Animales("miau")
animal0.hablar()

pez0 = Pez("NADA")
pez0.hablar()
