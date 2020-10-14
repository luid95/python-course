cantantes =["2pac", "Drake", "Bad Bunny", "Julio Iglesias"]
numeros =[1, 2, 5, 8, 3, 4]

# Ordenar
print(numeros)
numeros.sort()
print(numeros)

# Agregar elementos
cantantes.append("Natos y waor")
cantantes.insert(1, "David Bisbal")
print(cantantes)

# Eliminar elementos
cantantes.pop(1)
cantantes.remove("Bad Bunny")
print(cantantes)

# Invertir orden
numeros.reverse()

print(numeros)

# Buscar dentro de una lista
print('Drake' in cantantes)

# Contar el numero de elementos de cantantes
print(len(cantantes))

# Cuantas veces aparece un elemento
print(numeros.count(8))
numeros.append(8)
print(numeros.count(8))

# Conseguir indice
print(cantantes.index('Drake'))

# Unir listas
cantantes.extend(numeros)
print(cantantes)