import platform as pt

# Platform es un modulo que nos da informacion del sistema operativo
info = pt.platform()
print(f"Informacion del sistema operativo: {info}")

# Modulo Machine: Nos da informacion sobre la arquitectura de la maquina
print(f"Arquitectura de la maquina: {pt.machine()}")

# Modulo Processor: Nos da informacion sobre el procesador
print(f"Informacion del procesador: {pt.processor()}")

# Modulo System: Nos da el nombre del sistema operativo
print(f"Nombre del sistema operativo: {pt.system()}")

# Modulo Version: Nos da la version del sistema operativo
print(f"Version del sistema operativo: {pt.version()}")

# Modulo python_Implementation: Nos da la implementacion de Python
print(f"Implementacion de Python: {pt.python_implementation()}")

# Modulo python_version_tuple: Nos da la version de Python como una tupla
print(f"Version de Python (tupla): {pt.python_version_tuple()}")