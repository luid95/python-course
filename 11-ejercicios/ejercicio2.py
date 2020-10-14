"""
Ejercicio 2
    Hacer un programa que agregue valores a una lista mientras su longitud
    sea menor a 120; y luego mostrar la lista:
    - (PLUS) Usar while y for
"""

coleccion = []
coleccion2 = []

cont = 1
x = 1

for cont in range(0, 120):

    coleccion.append(cont)

print(coleccion)


while x <= 120:

    coleccion2.append(x)
    x += 1

print(coleccion2)
    
