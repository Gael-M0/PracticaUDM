def exterior(x):
    def interior(y):
        return x - y
    return interior

def creadorDividisor(n):
    def dividir(x):
        return n/x
    return dividir

division = creadorDividisor(10)#Parametro n
print(division(2))#se llama dentro de dividir para darle el valor a x