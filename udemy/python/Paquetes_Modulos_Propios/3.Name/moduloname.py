def saludar():
    return "Hola desde el móduloname"

print(__name__)

if __name__ == "__main__":
    print(saludar())
else:
    print("El módulo ha sido importado")