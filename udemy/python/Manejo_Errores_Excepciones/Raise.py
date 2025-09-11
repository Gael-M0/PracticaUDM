class NumeroNegativoError(Exception):
    def __init__(self, mensaje):
        self.mensaje = mensaje
        super().__init__(self.mensaje)

num = int(input("Ingrese un número: "))
if num < 0:
    raise NumeroNegativoError("El número no puede ser negativo")

print("El número es:", num)