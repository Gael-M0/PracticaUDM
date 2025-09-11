#Resultado = 10 / 0
#print(Resultado)
# Error: ZeroDivisionError: division by zero
# Excepcion que ocurre cuando se intenta dividir un número por cero.

try:
    Resultado = 10 / 0
    print(Resultado)
except ZeroDivisionError:
    print("Error: No se puede dividir entre cero.")

try: 
    Numero = int(input("Ingrese un número: "))
except ValueError:
    print("Error: Debe ingresar un número válido y entero.")