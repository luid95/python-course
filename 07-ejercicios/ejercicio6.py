"""
Ejercicio 6
    Mostrar todas las tablas de multiplicar del 1 al 10
    - Mostrando el titulo y luego las multiplicaciones del 1 al 10
"""

print("### TABLAS DE MULTIPLICAR ###")

# Generar mediante 2 ciclos for
for x in range(1, 11):
    # Titulo de cada comienzo de tabla
    print(f"\n Tabla del {x}")

    for y in range(1, 11):
        print(f"{x} x {y} = {x*y}")

print("\n FIN LISTA TABLAS")