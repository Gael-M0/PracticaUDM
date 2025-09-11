try:
    num1 = 10/10
except ZeroDivisionError:
    print("No se puede dividir entre cero")
else:
    print("El resultado es: ", num1)
finally:
    print("Ejecución del bloque finally")