"""
Ejercicio 4
    Hacer un programa que tenga 4 variables, una lista , un string, 
    un entero y un booleano; y que imprima un mensaje.
    - Segun el tipo de dato de cada variable, usar variable
"""
def traducirTipo(tipo):
    res = None
    if tipo == list:
        res = "LISTA"
    elif tipo == str:
        res = "STRING"
    elif tipo == int:
        res = "INT"
    elif tipo == bool:
        res = "BOOLEAN"
    return res

def comprobarTipado(dato, tipo):
    # Detectar el tipado
    comprobar = isinstance(dato, tipo)

    res = " "

    if comprobar:
        res = f"Este dato es del tipo {traducirTipo(tipo)} "
    else:
        res = "El tipo de dato no es correcto :("
    
    return res

milista = ["mi", "lista", "es", "esta",123]
mistring= "Mi string"
mientero=123
mibool=True

print(comprobarTipado(milista, list))

print(comprobarTipado(mistring, str))

print(comprobarTipado(mientero, int))

print(comprobarTipado(mibool, bool))
