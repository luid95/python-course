"""
Una varibles es un contenedor de informacion
que dentro guardara un dato, se pueden crear
muchas variables y que cada una tenga un dato distinto.

"""
# Crear variables y asignarles un valor
texto = "Master en Python"
texto2 = "con Luis Morales"
numero = 45
decimal = 6.7

# Mostrar valor de varables

print(texto)
print(texto2)
print(numero)
print(decimal)

print("--------------------------------------------")

#Sustituir el valor de algunas variables / reasignacion de valores

numero = 77
decimal = 8.7

print(numero)
print(decimal)

# Concatenacion

nombre ="Luis"
apellido="Morales"
email ="luisdavidmorales95@gmail.com"

print(nombre + " " + apellido + " con email: " + email)
print("O tambien mostrar la info de la siguiente manera")
print(f"{nombre} {apellido} con email: {email}")
print("Tambien se puede mostrar info de la siguiente manera")
print("Hola mi nombre es {} {} y mi email es {}".format(nombre, apellido, email) )
print(nombre, apellido, email)