class FabricaTelefonos():
    marca = "Huawei"
    color = "Azul"
    MemoriaRam = 32
    Almacenamiento = 125

    def llamar(self , mensaje):
        return mensaje
    
    def Musica(self):
        print("Estas escuchando musica")

telefonoCelular = FabricaTelefonos()

telefonoCelular.marca
telefonoCelular.color
telefonoCelular.MemoriaRam
telefonoCelular.Almacenamiento

print(telefonoCelular.marca)
print(telefonoCelular.Almacenamiento)

print(telefonoCelular.llamar("Hola, q paso?"))
telefonoCelular.Musica()