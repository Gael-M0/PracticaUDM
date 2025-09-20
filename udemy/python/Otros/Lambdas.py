def suma(a,b):
    return a + b
print(f"Resultado normal {suma(1,3)}")

sumar = lambda x , y : x + y 

print(f"resultado de lambda {sumar(4,3)}")

def exponenciar(num):
    return num**2

print(f"Resultado a la funcion normal a la exponenciar: {exponenciar(6)}")

exponenciacion = lambda num : num ** 2

print(f"Resultado a la funcion lambda a la exponenciar: {exponenciacion(9)}")