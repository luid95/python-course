"""
Ejercicio 5
    Realizar un programa que muestre:
    - Todos los numeros entre 2 numeros que diga el usuario
"""

# Definir mi funcion que imprima la lista de numeros
def listar(minn, maxx):

    print(f"Los numeros dentro del intervalo [ {minn}-{maxx} ] son:")
    for numero in range(minn, (maxx+1)):
        print(f"{numero}")

# Solicitar los 2 numeros al usuario
print("### Lista de numeros entre un intervalo ###")

num1 = int(input("Proporcione el primer numero: "))
num2 = int(input("Proporcione el segundo numero: "))

# Verificar el menor de los 2 numeros
if num1 <= num2:
    listar(num1, num2)
else:
    listar(num2, num1)