'''
def frecuencia_caracteres(cadena):
    cadena = cadena.replace(" ", "").lower()
    diccionario = {}
    for caracter in cadena:
        if caracter in diccionario:
            diccionario[caracter] += 1
        else:
            diccionario[caracter] = 1
    return diccionario

# Ejemplo de uso
texto = "Hola Mundo"
print(frecuencia_caracteres(texto))
'''
'''
Ejercicio 3
Crea una jerarquía de clases para representar empleados en una empresa. Debe haber una clase base 
Empleado y dos subclases Gerente y Desarrollador. La clase base debe tener atributos comunes como 
nombre y salario, y un método para calcular el salario anual. Las subclases deben agregar atributos 
específicos y sobrescribir el método de cálculo de salario si es necesario.
'''
class Empleado:
    def __init__(self, nombre, salario):
        self.nombre = nombre
        self.salario = salario

    def calcular_salario_anual(self):
        return self.salario * 12

class Gerente(Empleado):
    def __init__(self, nombre, salario, bono):
        super().__init__(nombre, salario)
        self.bono = bono

    def calcular_salario_anual(self):
        return (self.salario * 12) + self.bono

class Desarrollador(Empleado):
    def __init__(self, nombre, salario,proyectos):
        super().__init__(nombre,salario)
        self.proyectos = proyectos

    def Bono_proyecto(self, proyecto):
        return (self.salario * proyecto)