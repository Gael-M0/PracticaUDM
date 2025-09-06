def sumar(a, b):
    return a + b
def restar(a, b):
    return a - b

print(__name__)

if __name__ == "__main__":
    resultado_suma = sumar(5, 3)
    resultado_resta = restar(5, 3)
    print(f"Suma: {resultado_suma}")
    print(f"Resta: {resultado_resta}")
else:
    print("El módulo ha sido importado.")