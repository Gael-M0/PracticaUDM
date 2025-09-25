with open('archivo.txt','a') as archivo:
    archivo.write("Hola Mundo")

with open('archivo.txt','r') as archivo:
    contenido = archivo.read()
    print(contenido)