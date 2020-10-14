"""
MODULOS:
    Son funcionalidades ya hechas para reutilizar.
    Podemos consseguir modulos que ya se vienen en el lenguaje,
    modulos en internet, y tambien podemos usar nuestros modulos.
"""
# Importar modulo propio
# import mimodulo
## o importar una funcion del modulo
## from mimodulo import holamundo
### o importar todas las funciones del modulo para llamarlo por nombre
from mimodulo import *

# print(mimodulo.holamundo("Luis David"))
# print(mimodulo.calculadora(3,5,True))
## print(holamundo("Luis"))

print(holamundo("Luis"))
print(calculadora(10, 5, True))

# MODULO DE FECHA POR DEFECTO
import datetime

print(datetime.date.today())
fecha_completa = datetime.datetime.now()

print(fecha_completa)
print(fecha_completa.year)
print(fecha_completa.month)
print(fecha_completa.day)


fecha_personaliada = fecha_completa.strftime("%d/%m/%Y, %H:%M:%S")

print(f"Fecha personalizada {fecha_personaliada}")

print(datetime.datetime.now().timestamp())

# MODULO MATEMATICAS
import math

# Operaciones basicas
print(f"Raiz cuadrada de 10: {math.sqrt(10)}")

print(f"Numero PI: {math.pi}")
print(f"Redondear: {math.ceil(6.5678)}")
print(f"Redondear floor: {math.floor(6.5678)}")

# Modulo Random
import random

print(f"Numero aleatorio entre 15 y 65: {random.randint(15, 65)}")