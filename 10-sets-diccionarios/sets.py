"""
SET
    Es un tipo de dato, para tener una coleccion de valores,
    pero no tiene indice ni orden
"""

personas ={
    "luis",
    "Marco",
    "Miguel"
}

print(type(personas))
print(personas)

# Agregar elemento
personas.add("Carlos")

print(personas)

# Eliminar elemento
personas.remove("Miguel")

print(personas)
