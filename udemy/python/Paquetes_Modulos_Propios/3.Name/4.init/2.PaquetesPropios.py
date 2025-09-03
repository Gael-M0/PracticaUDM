from operaciones.sumar import sumar
from operaciones.multiplicar import multiplicar
from operaciones.mas_operaciones.restar import restar
from operaciones.mas_operaciones.dividir import dividir

resultado_suma = sumar(5, 3)
resultado_multiplicacion = multiplicar(5, 3)
resultado_resta = restar(5, 3)
resultado_division = dividir(20, 10)

print("Suma:", resultado_suma)
print("Multiplicación:", resultado_multiplicacion)
print("Resta:", resultado_resta)
print("División:", resultado_division)