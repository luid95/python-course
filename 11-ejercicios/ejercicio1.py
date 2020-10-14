"""
Ejercicio 1
    Hacer un programa que tenga una lista de 8 numeros 
    y haga lo siguiente:
    - Recorrer la lista y mostrarla
    - hacer una funcion que recorra listas de numeros y devuelva un string
    - Ordenarla y mostrarla
    - Mostrar su longitud
    - Buscar algun elemento (que el usuario pida por el teclado)
"""

def mostrar(numeros):

    res = ""

    for elemento in numeros:
        res += "Elemento: " + str(elemento)
        res += "\n"
    
    return res

# Crear una lista
listaa = [10, 3, 200, 99, 1, 9, 4]

# mostrar lista
print("##### Recorrer y mostrar la lista #####")
for numero in listaa:
    print(numero)

# Funcion
print("##### Funcion #####")
print(mostrar(listaa))


# Ordenar y mostrar
print("##### Ordenar y mostrar #####")
listaa.sort()
print(listaa)

# Mostrar longitud
print("##### Mostrar longitud #####")
tam = len(listaa)
print(tam)

# Buscar algun elemento
print("##### Buscar elemento en lista #####")
num = int(input("Proporcione numero a buscar: "))

if num in listaa:
    print(f"El numero {num} se encuentra en la lista ")
else:
    print(f"El numero {num} no se encuentra en la lista!! :(")