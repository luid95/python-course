"""
# Condicional IF

SI se_se_cumple_esta_condicion:
    Ejecutar grupo de instrucciones
SI NO:
    Se ejecuta otro tipo de instrucciones

if condicion:
    instrucciones
else
    otras instrucciones

Operadores de comparacion

== igual
!= diferente
< menor que
> mayor que
<= menor o igual que
>= mayor o igual que

# Operadores logicos

and Y
or O
! NEGACION
not NO


"""

# Ejemplo 1
print("#################### EJEMPLO 1 ##################")
# color = input("Adivina cual es mi color favorito? ")
color = 'rojo'

if color == 'rojo':
    print("Enhorabuena!!")
    print(f"El color es {color}")
else:
    print("El color no es correcto")
    print("El color que tecleaste es ",color)
    print("Vuelve a intentarlo...")

# Ejemplo 2
print("#################### EJEMPLO 2 ##################")
year = 2020
# year = int(input("En que año estamos? "))

if year >= 2021:
    
    print(f"{year} Esta en el 2021 en adelante!!")
else:
    print(year, " Es un año anterior a 2021")

# Ejemplo 3
print("#################### EJEMPLO 3 ##################")
nombre = "Luis Morales"
ciudad = "Puebla"
continente = "America"
edad = 55
mayoria_de_edad = 18

if edad >= mayoria_de_edad:
    print(f"{nombre} es mayor de edad")

    if continente != "America":
        print(f"{nombre} NO es Americano")
    else:
        print(f"{nombre} es Americano y de {ciudad}")

else:
    print(f"{nombre} NO es mayor de edad")

# Ejemplo 4
print("#################### EJEMPLO 4 ##################")
# elif

dia = 1
# dia = int(input("Introduce el numero del dia de la semana"))

"""
if dia == 1:
    print("Es Lunes")
else:
    if dia == 2:
        print("Es Martes ")
    else:
        if dia == 3:
            print("Es Miercoles ")
        else:
            if dia == 4:
                print("Es Jueves ")
            else:
                if dia == 5:
                    print("Es Viernes ")
                else:
                    print("Ya es fin de semana")
"""
if dia == 1:
    print("Es Lunes")
elif dia == 2:
    print("Es Martes")
elif dia == 3:
    print("Es Miercoles")
elif dia == 4:
    print("Es Jueves")
elif dia == 5:
    print("Es Viernes")
else:
    print("Es fin de semana")

# Ejemplo 5
print("#################### EJEMPLO 5 ##################")

# Operadores logicos y multiples condicionales

edad_minima = 18
edad_maxima = 65
edad_oficial = 17
# edad_oficial = int(input("Tienes edad para trabajar? Introduce tu edad: "))

if edad_oficial >= 18 and edad_oficial <= 65:
    print("Esta en edad de trabajar!!")
else:
    print("No esta en edad de trabajar")

# Ejemplo 6
print("#################### EJEMPLO 6 ##################")


pais = "Rusia"

if pais == 'Mexico' or pais == 'España' or pais == 'Colombia':
    print(f"{pais} si es un pais de habla hispana")
else:
    print(f"{pais} no es un pais de habla hispana :(")

# Ejemplo 7
print("#################### EJEMPLO 7 ##################")


pais = "Mexico"

if not (pais == 'Mexico' or pais == 'España' or pais == 'Colombia'):
    print(f"{pais} NO es un pais de habla hispana :(")
    
else:
    print(f"{pais} SI es un pais de habla hispana")

# Ejemplo 8
print("#################### EJEMPLO 8 ##################")


pais = "Mexico"

if pais != 'Mexico' and pais != 'España' and pais != 'Colombia':
    print(f"{pais} NO es un pais de habla hispana :(")
    
else:
    print(f"{pais} SI es un pais de habla hispana")