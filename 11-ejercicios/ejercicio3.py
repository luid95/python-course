"""
Ejercicio 3
    Hacer un programa que compruebe si una variable esta vacia
    - si esta vacia, rellenarla con texto en minuscula y mostrarla en mayuscula
"""

# pedir texto a usuario
print("##### Comprobar si una variable esta vacia  #####")
texto = input("Teclee texto ( es opcional): ")

if len(texto.strip()) == 0:
    texto = "texto en minuscula, convertido en mayuscula."
    texto = texto.upper() # convertir en mayuscula
    print(texto)
else:
    print(texto)