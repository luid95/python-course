"""
LISTAS [arrays]
    Son colecciones o conjuntos de datos/valores, bajo un unico nombre.
    Para acceder a esos valores usar el indice numerico.
"""

# Definir lista con []
peliculas = ["Batman", "Spiderman", "Star Wars"]

# Definir lista con function list()
cantantes = list(('2pac', 'Orake', 'JLO'))

years = list(range(2020, 2050))
variada = ['Luis', 23, 543, True, 'Texto']

"""
print(peliculas)
print(cantantes)
print(years)
print(variada)
"""

# Indices  

# Lista de peliculas
print(peliculas[1])
print(peliculas[-2])
print(peliculas[1:])

# Lista de cantantes
print(cantantes[0:2])

# Alteracion de lista por indice
peliculas[1]= "Superman"
peliculas[2]= "El hobbit"
print(peliculas[1:])

# AGREGAR ELEMENTOS A LA LISTA
cantantes.append("Kase O")
cantantes.append("Natos y waor")

print(cantantes)

# RECORRER LISTA
print("\n********* LISTADO DE PELICULAS *********")

nueva_pelicula =""
while nueva_pelicula != "parar":
    nueva_pelicula = input("Introduce la nueva pelicula: ")

    if nueva_pelicula != "parar":
        peliculas.append(nueva_pelicula)


for pelicula in peliculas:
    print(f"{ peliculas.index(pelicula)+1 }- {pelicula}")

# LISTAS MULTIDIMENSIONALES
print("\n********* LISTADO DE CONTACTOS *********")

contactos = [
    [
        'Antonio',
        'antonio@antonio.com'
    ],
    [
        'Luis',
        'luis@luis.com'
    ],
    [
        'Jose',
        'jose@jose.com'
    ],
    
]

print(contactos)

# Obtener el email de Luis
print(contactos[1][1])

# Recorrer todos los contactos
for contacto in contactos:
    for elemento in contacto:
        if contacto.index(elemento) == 0:
            print("Nombre: "+elemento)
        else:
            print("Email: "+elemento)
    print("\n")