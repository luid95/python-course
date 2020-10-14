"""
Ejercicio 5
    Hacer una lista con el contenido de esta tabla:
    - ACCION       AVENTURA            DEPORTES
       GTA          ASSINS             FIFA 21
       COD          CRASH               PRO 21
       PUGB     PRINCE OF PERSIA       MOTO GP 21
    
    -Mostrar esta informacion ordenada
"""

table = [
    {
        "categoria": "ACCION",
        "juegos": ["GTA", "COD", "PUGB"]
    },
    {
        "categoria": "AVENTURA",
        "juegos": ["ASSINS", "CRASH", "PINCE OF PERSIA"]
    },
    {
        "categoria": "DEPORTES",
        "juegos": ["FIFA 21", "PRO 21", "MOTO GP 21"]
    },
]

for categoria in table:
    print(f"################ {categoria['categoria']} ####################")

    for juegos in categoria['juegos']:
        print(juegos)