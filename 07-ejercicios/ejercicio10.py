"""
Ejercicio 10
    - Solicitar las notas de 15 alumnos
    - Mostrar el numero de aprobados y suspendidos
"""

aprobado =0
suspendido=0
    
for x in range(1, 16):

    # Solicitar las notas de los 15 alumnos 
    num = int(input(f"Proporcione la nota del alumno {x}: "))
    
    # Comparar si el alumno esta aprobado o suspendido
    if num>5 and num<11:
        aprobado +=1
    elif num>0 and num<6:
        suspendido+=1

print(f"Hay {aprobado} alumnos aprobados y {suspendido} alumnos suspendidos")

print("FIN DE PROGRAMA")