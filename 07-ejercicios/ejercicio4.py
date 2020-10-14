"""
Ejercicio 4
    - Pedir 2 numeros al usuario
    - Realizar las 4 operaciones basicas de una calculadora
    - Mostrarlo por pantalla
"""

# Solicitar los 2 numeros al usuario
print("### CALCULADORA ###")
num1 = int(input("Proporcione el primer numero: "))
num2 = int(input("Proporcione el segundo numero: "))

# Realizar los 4 operaciones basicas

# Suma
suma = num1 + num2

# Resta
resta = num1 - num2

# Multiplicacion
mult = num1 * num2

# Division
div = num1/num2

# Salida
print(f"Numero : {num1}, y numero 2: {num2}")
print(f"Suma : {suma}")
print(f"Resta : {resta}")
print(f"Multiplicacion : {mult}")
print(f"Division : {div}")

