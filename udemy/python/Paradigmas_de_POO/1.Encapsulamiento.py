class A():
    def __init__(self):
        self.contador = 0

    def incrementar(self):
        self.contador +=1

    def cuenta(self):
        return self.contador

class B():
    def __init__(self):
        self._contador = 0

    def incrementar(self):
        self._contador +=1

    def cuenta(self):
        return self._contador
    
print("Primer objeto creado: ")
objeto1 = A()
print(objeto1.cuenta())
objeto1.incrementar()
print(objeto1.cuenta())
print(objeto1.contador)
objeto1.contador = 10
print(objeto1.contador)

print("Segundo objeto creado: ")
objeto2 = B()
print(objeto2.cuenta())
objeto2.incrementar()
print(objeto2.cuenta())
print(objeto2._contador)
'''
objeto2.__contador = 10
print(objeto2.__contador)
'''