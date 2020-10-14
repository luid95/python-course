nombre="Luis David"

# Funciones generales
print(nombre)

# Detectar el tipado
comprobar = isinstance(nombre, str)

if comprobar:
    print(f"La variable es un string")
else:
    print(f"La variable NO es un string :(")

if not isinstance(nombre, float):
    print("La variable no es un numero con decimales")

# Limpiar espacios
frase = "  mi contenido   "

print(frase)
print(frase.strip())

# Eliminar variables
year = 2020
print(year)

del year

# print(year)

# Comprobrar variables vacias
text = " ff   "

if len(text) <= 0:
    print("La variables esta vacia")
else:
    print("La variable tiene contenido: ", len(text))

# Encontrar caracteres

frase = "La vida es bella"

print(frase.find("vida"))

# Reemplazar variables en un string

nueva_frase = frase.replace("vida", "moto")
print(nueva_frase)

# Mayuscular y minusculas
print(nombre)
print(nombre.lower())
print(nombre.upper())