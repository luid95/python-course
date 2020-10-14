"""
Ejercicio 3
    - Escribir un script que nos muestra los cuadrados
      de los 60 primeros numeros naturales.
    - Una primera version con uso del bucle for
    - Una segunda version con uso del bucle while
"""

# Generar los numeros mediente un bucle for

print("Lista de los primeros 60 numeros naturales y sus cuadrados")
for numero in range(0, 61):

    # Realizar los cuadrados de cada numero
    cuadrado = numero * numero

    # Imprimir los numeros naturales y sus cuadrados
    print(f"{numero} - {cuadrado}")

print("\n Fin de la lista de numeros con bucle for")

# Generar los numeros mediente un bucle while
contador = 0

while contador <= 60:
    # Realizar los cuadrados de cada numero
    cuadrado = contador * contador

    # Imprimir los numeros naturales y sus cuadrados
    print(f"{contador} - {cuadrado}")
    contador += 1

print("\n Fin de la lista de numeros con bucle while")
print("\n Y de todos los cuadrados")