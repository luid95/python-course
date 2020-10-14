"""
DICCIONARIO
    Es un tipo de dato que almacena un conjunto de datos.
    En formato clave > valor.
    Es parecido a un array asociativo o un objeto json.
"""

persona ={
    "nombre": "Luis",
    "apellido": "Morales",
    "email": "example@gmail.com"
}

print(type(persona))
print(persona)
print(persona['apellido'])

# LISTA CON DICCIONARIOS
contactos = [
    {
        'nombre': 'Antonio',
        'email': 'antonio@gmail.com'
    },
    {
        'nombre': 'Luis',
        'email': 'luis@gmail.com'
    },
    {
        'nombre': 'Salvador',
        'email': 'salvador@gmail.com'
    },
]

print(contactos)
print(contactos[0]['nombre'])
contactos[0]['nombre'] = 'Antony'

print(contactos[0]['nombre'])

print('\n --------------------------------------------')

for contacto in contactos:
    print(f"Nombre del contacto {contacto['nombre'] }")
    print(f"Email del contacto {contacto['email'] }")
    print('\n ###########################################')