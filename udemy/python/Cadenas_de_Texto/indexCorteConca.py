cadena = "Python"

primercaracter = cadena[0]
print(primercaracter)

print(cadena[3])
print(f"valor -1 de la cadena Python: {cadena[-1]}")

cadena1 = "Python" #Corte de cadenas

print(cadena1[0 : 2])#Inicia desde 0 y termina desde el 2(este no sera tomado en cuenta osea solo 1 y 2)
print(cadena1[1 : 4])
print(cadena1[2 :])# imprime desde el 2 hasta el final
print(cadena1[ : 4])#Imprime desde el 0 hasta el numero dicho

cadena2 = "Hola"
cadena3 = "Mundo"

print(f"Esta es la cadena concatedana: {cadena2 + cadena3}")