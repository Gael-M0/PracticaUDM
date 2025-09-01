import math as mt
# Math es un modulo de funciones matematicas

#Modulo Ceil : Redondea un numero hasta la cifra entera mas arriba

var = mt.ceil(5.1)
print(f"Redondeo hacia arriba: {var}")

#Modulo Floor : Redondea un numero hasta la cifra entera mas abajo
var1 = mt.floor(5.9)
print(f"Redondeo hacia abajo: {var1}")

# Modulo Trunc : Elimina-omitir la parte decimal de un numero
var2 = mt.trunc(25.95963)
print(f"Eliminando parte decimal: {var2}")

# Modulo Factorial: Calcula el factorial de un numero
var3 = mt.factorial(5)# 5! = 5*4*3*2*1 = 120
print(f"El factorial de 5 es: {var3}")

# Modulo Hypot: Calcula la hipotenusa de un triángulo
var4 = mt.hypot(3, 4) # 3^2 + 4^2 = 25 => sqrt(25) = 5
print(f"La hipotenusa de un  triángulo con catetos 3 y 4 es: {var4}")

# Modulo SQRT: Calcula la raiz cuadrada de un numero
var5 = mt.sqrt(25)
print(f"La raiz cuadrada de 25 es: {var5}")