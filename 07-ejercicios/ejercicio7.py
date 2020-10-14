"""
Ejercicio 7
    Realizar un programa que muestre todos los numeros impares
    - Entre 2 numeros que decida el usuario
"""
# Definir mi funcion que imprima la lista de numeros
def impares(minn, maxx):

    print(f"Los numeros impares dentro del intervalo [ {minn}-{maxx} ] son:")
    for numero in range(minn, (maxx+1)):

        # Verificar que sea un numero impar
        if numero%2 != 0:

            print(f"{numero}")

# Solicitar los 2 numeros al usuario
print("### Lista de numeros impares entre un intervalo ###")

num1 = int(input("Proporcione el primer numero: "))
num2 = int(input("Proporcione el segundo numero: "))

if num1 <= num2:
    impares(num1, num2)
else:
    impares(num2, num1)