with open('archivo.txt','w') as archivo:
    archivo.write("Linea1")
    archivo.write("\nLinea2")
    archivo.write("\nLinea3")

with open('archivo.txt', 'r') as archivo:
    linea = archivo.readlines()
    print(linea)
