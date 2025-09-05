def contar_palabras(texto):
    palabras = texto.split()
    return len(palabras)

def promedio(numeros):
    return sum(numeros) / len(numeros) if numeros else 0