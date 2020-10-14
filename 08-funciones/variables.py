"""
Variable local:
    Se definen dentro de la funcion y no se pueden usar fuera de ella,
    solo estan disponibles dentro. A no ser que se realice un return.

Variables globlales
    Son las que se declaran fuera de la funcion y estan disponibles
    dentro y fuera de ellas.
"""

# Variable global
frase= "Ni los genios son tan genios, ni los mediocres tan mediocres"

print(frase)

def holaMundo():

    frase = "Hola mundo!!"
    print("Dentro de la funcion:")
    print(frase)

    year = 2021
    print(year)
    
    global website
    website = "luisdavidmorales95@gmail.com"

    print("Dentro: ", website)

    return "Dato devuelto " + str(year)

print(holaMundo())

print("Fuera: ", website)