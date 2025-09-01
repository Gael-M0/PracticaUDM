import random as rd
# Random es un modulo para generar numeros aleatorios

# Modulo Random: Genera un numero aleatorio
var = rd.random()
print(f"Numero aleatorio entre 0 y 1: {var}")

# Modulo choice: Elige un elemento aleatorio de una lista
var1 = rd.choice(['manzana', 'banana', 'naranja'])
print(f"Fruta aleatoria: {var1}")

# Modulo sample: Elige una muestra aleatoria de una lista
varlista = [1, 2, 3, 4, 5, 6, 7, 8, 9]
var2 = rd.sample(varlista, 3)
print(f"Muestra aleatoria de 3 numeros: {var2}")
