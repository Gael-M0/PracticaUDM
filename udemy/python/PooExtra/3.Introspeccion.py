class vehiculo:
    ruedas = 4
    def __init__(self,marca,modelo):
        self.marca = marca
        self.modelo = modelo
    
    def arrancar(self):
        return "El vehiculo ha arrancado"

auto = vehiculo("Toyota","corolla")

print("Inspeccion del objeto")
print(hasattr(auto,'marca'))
print(hasattr(auto,'arrancar'))
print(hasattr(auto,'acelerar'))

print("Inspeccion de la clase")
print(hasattr(vehiculo,'ruedas'))
print(hasattr(vehiculo,'color'))
print(hasattr(vehiculo,'arrancar'))
