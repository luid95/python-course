"""
FUNCIONES
    Es un conjunto de instrucciones agrupadas bajo
    un nombre concreto que pueden reutilizarse invocando a
    la funcion tantas veces como sea necesario.
"""

# Ejemplo 1
print("##### EJEMPLO 1 #####")

def muestraNombre():
    print("Luis")
    print("David")
    print("Marcos")
    print("Carlos")
    print("Hector")
    print("\n")

# Invocar a la funcion
muestraNombre()
muestraNombre()

# Ejemplo 2
print("##### EJEMPLO 2 #####")

def mostrarNombre(nombre, edad):
    print(f"Tu nombre es: {nombre}")

    if edad >= 18:
        print("Y eres mayor de edad")
    else:
        print("Pero no eres mayor de edad :(")

nombre = input("Introduce tu nombre: ")
edad = int(input("Cual es tu edad?: "))
mostrarNombre(nombre, edad)

# Ejemplo 3
print("##### EJEMPLO 3 #####")

def tabla(numero):
    print(f"Tabla de multiplicar del numero {numero}")

    for contador in range( 11):
        operacion = numero*contador
        print(f"{numero} x {contador} = {operacion}")
    
    print("\n")

tabla(3)
tabla(7)
tabla(12)

# Ejemplo 3.1
print("##### EJEMPLO 3.1 #####")

for numero_tabla in range(1, 11):
    tabla(numero_tabla)

# Ejemplo 4
print("##### EJEMPLO 4 #####")

# Parametros opcionales

def getEmpleado(nombre, dni = None):
    print("\n")
    print("Empleado")
    print(f"Nombre: {nombre}")

    if dni != None:
        print(f"DNI: {dni}")

getEmpleado("Luis")
getEmpleado("Juan", 12345)

# Ejemplo 5: return o devolver datos

print("##### EJEMPLO 5 #####")

def saludame(nombre):
    saludo = f"Hola, saludos {nombre}"

    return saludo

print(saludame("Luis"))

# Ejemplo 6

print("##### EJEMPLO 6 #####")

def calculadora(num1, num2, basicas=False):

    suma = num1+num2
    resta = num1-num2
    multi = num1*num2
    div = num1/num2

    cadena = ""
    if basicas != False:

        cadena += "Suma: " + str(suma)
        cadena += "\n"
        cadena += "Resta:" + str(resta)
    else:
        cadena += "Multiplicacion: " + str(multi)
        cadena += "\n"
        cadena += "Division: " + str(div)

    return cadena

print("\n")
print(calculadora(5,5,True))
print("\n")
print(calculadora(10,5))

# Ejemplo 7: Funciones dentro de otras funciones

print("##### EJEMPLO 7 #####")

def getNombre(nombre):
    texto = f"El nombre es: {nombre}"
    return texto

def getApellidos(apellidos):
    texto = f"Los apellidos son: {apellidos}"
    return texto

def devuleveTodo(nombre, apellidos):

    texto = getNombre(nombre) + "\n" + getApellidos(apellidos)

    return texto

print(devuleveTodo("Luis", "Morales"))

# Ejemplo 8: Funciones Lamda (funciones anonimas)

print("##### EJEMPLO 8 #####")

dime_year = lambda year:f"El año es {year * 50}"

print(dime_year(2020))