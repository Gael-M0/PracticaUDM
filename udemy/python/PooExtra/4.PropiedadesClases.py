class Vehiculo:
    pass

print(Vehiculo.__name__)
print(Vehiculo.__bases__) #En caso de usar bases sin tener herencias muestra a clase object porq no hereda nada

class Vehiculo:
    pass

print(Vehiculo.__module__) #Devuelve el nombre del modulo donde esta la clase

class transporte:
    pass

class Vehiculo(transporte):
    pass

print(Vehiculo.__bases__) #Si en caso de q haya una herencia base devuelve una tupla detallando la herencia