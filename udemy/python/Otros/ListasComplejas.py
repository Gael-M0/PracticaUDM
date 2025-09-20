#[expresion(matematica, logica o propia) for iterador in iterable]

cuadrados = [1,2,3,4,5,6]
print(cuadrados)
#        Expresion|for|iterador|in|iterable
cuadrado = [x ** 2 for x in range(10)]
print(cuadrado)
#                             funcion extra para filtrar
pares = [x for x in range(20) if x % 2 == 0]
print(pares)