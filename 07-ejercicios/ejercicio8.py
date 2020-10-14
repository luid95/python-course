"""
Ejercicio 8
    - Solicitar una catidad al usuario
    - Solicitar al usuario el porcentaje a obtener de la cantidad solicitada
    - Mostrar el resultado de ese porcentaje
"""

# Solicitar los 2 numeros al usuario
print("### OBTENER PORCENTAJE DE UNA CANTIDAD ###")

cantidad = int(input("Proporcione una cantidad: "))
porcentaje = int(input(f"Que porcentaje quieres obtener del {cantidad}?: "))

# Calcular el porcentaje de la cantidad
resultado = (porcentaje*cantidad)/100

# Mostrar el resultado
print(f"El {porcentaje}% de {cantidad} es: {resultado}")