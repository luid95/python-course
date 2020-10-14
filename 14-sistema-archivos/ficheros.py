from io import open
import pathlib

# Abrir archivo
ruta = str(pathlib.Path().absolute()) + "/fichero_texto.txt"
# print(ruta)
archivo = open(ruta, "a+")

# Escribir dentro de un archivo
archivo.write("***** Soy un texto metido desde python *****\n")

# Cerrar un archivo
archivo.close()

# Abrir archivo
ruta = str(pathlib.Path().absolute()) + "/fichero_texto.txt"
archivo_lectura = open(ruta, "r")

# Leer contenido
# contenido = archivo_lectura.read()

# print(contenido)

# Leer contenido y guardar en lista
lista = archivo_lectura.readlines()
archivo_lectura.close()

for frase in lista:
    
    print("- " + frase.upper())