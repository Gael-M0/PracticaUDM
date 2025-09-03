if __name__ == "__main__":
    print("Ejecucion directa")
else:
    print("Ejecucion importada")


# El __name__ es una variable usada para determinar de q forma se esta ejecutando un script
print(__name__) #Su funcionalidad es determinar si un script se esta ejecutando de forma directa o importado
# Si el script se ejecuta de forma directa, el valor de __name__ sera "__main__" osea q el modulo se esta ejecutando de forma directa
