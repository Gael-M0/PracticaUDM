#open(nombre_archivo,modo)


with open('archivo.txt','w') as archivo: #con w es un modo de open en caso de que no se habra lo crea
    archivo.write("He crado un archivo nuevo")

with open('archivo.txt','r') as archivo: # con r es un metodo open q se usa para abrir en modo lectura
          contenido = archivo.read()
          print(contenido)

with open('archivo.txt','a') as archivo:
       archivo.write("\nNueva linea agregada")

# con t es el modo texto y con b es el modo binario
# con a es el modo append que sirve para agregar contenido al final del archivo
# con x es el modo crear que sirve para crear un archivo pero si ya existe marca error
# con + es el modo actualizar que sirve para leer y escribir en el archivo

