"""
Ejercicio 2
    Escribir un script que nos muestra por pantalla
    todos los numeros pares del 1- 120
"""

# Generar los numeros mediente un bucle for

print("Lista de numeros pares de la lista 1-120")
for numero in range(1, 121):
    # Verificar si el numero es par
    par = numero%2

    # Imprimir los numeros pares
    if par == 0:
        print(f"{numero} es par")

print("\n Fin de la lista de numeros pares")