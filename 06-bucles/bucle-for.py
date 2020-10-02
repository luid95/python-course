"""
# FOR
for variable in elemento_iterable (lista, rango, etc)
    bloque de instrucciones

"""

contador = 0
res = 0

for contador in range(0, 10):
    print("Voy por el ", contador)

    res += contador

print(f"El resultado es: {res}")
print(type(res))

# Ejemplo con tablas de multiplicar
print("####################### EJEMPLO ####################")

numero_usuario = int(input("De que numero quieres la tabla?: "))

if numero_usuario < 1:
    numero_usuario = 1

print(f"### Tabla de multiplicar del numero {numero_usuario} ###")

for numero_tabla in range(1, 11):

    if numero_usuario == 45:
        print("No se puede hacer uso de numeros prohibidos!!!")
        break
    
    print(f"{numero_usuario} x {numero_tabla} = {numero_usuario*numero_tabla}")
else:
    print("Tabla finalizada")