"""
Ejercicio 9
    - Solicitar al usuario ingresar numeros indefinidadmente
    - Hasta que el usuario ingrese el numero 111
"""

# Solicitar numeros al usuario
print("### MOSTRAR LISTA DE NUMEROS HASTA MI BANDERA ###")

tope = 111
num = 0

while tope != num:
    num = int(input("Proporcione un numero: "))
    
    # Comparar si el numero es diferente al tope
    if num != tope:
        print(num)


print("FIN LISTA")