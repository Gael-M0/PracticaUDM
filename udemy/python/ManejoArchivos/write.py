with open ('archivo.txt', 'w') as archivo:
    archivo.write("Escribiendo contenido en el archivo con Write")
    archivo.write("\nEste es un segundo mensaje en otra linea")

with open('archivo.txt', 'a') as archivo:
    archivo.write("\nEscribiendo contenido en el archivo con Write")

