dicDatos = {
    "juan": {
        "nombre": "Juan",
        "apellido": "Rodriguez",
        "contraseña": "juancito",  # contraseña
        "sexo": "H",
        "edad": 24,
        "ubicacion": [41.40338, 2.123],
        "intereses": ["tenis", "nadar", "pokemon", "anime", "escribir", "pintar", "taekwondo"],
        "likes": {},
        "mensajes": {"lasd": 2},
    },
    "LaJuancita": {
        "nombre": "Juana",
        "apellido": "Perez",
        "contraseña": "redsun9887",
        "sexo": "M",
        "edad": 21,
        "ubicacion": [42.34567, 23.123],
        "intereses": ["star-wars", "nueva-york", "fotografia", "francia", "asado", "bicicleta", "taekwondo",
                      "buenos-aires"],
    },
    "usuario1": {
        "nombre": "usuario1",
        "apellido": "usuario1",
        "contraseña": "usuario1",
        "sexo": "I",
        "edad": 32,
        "ubicacion": [2.34567, 23.123],
        "intereses": ["star-wars", "asado", "bicicleta", "taekwondo", "buenos-aires"],
    },
    "usuario2": {
        "nombre": "usuario2",
        "apellido": "usuario2",
        "contraseña": "usuario2",
        "sexo": "H",
        "edad": 55,
        "ubicacion": [2.34567, 3.123],
        "intereses": ["star-wars", "nueva-york", "fotografia", "francia", "asado", "bicicleta", "taekwondo",
                      "buenos-aires"],
    },
    "usuario3": {
        "nombre": "usuario3",
        "apellido": "usuario3",
        "contraseña": "usuario3",
        "sexo": "M",
        "edad": 75,
        "ubicacion": [2.4567, 3.123],
        "intereses": ["star-wars", "buenos-aires"],
    },

}


'''
#para hacer referencia
usuarios=list(dicDatos.keys())[0]	#ahi me refiero a juan

sexo=dicDatos[usuarios]["sexo"]
ubicacion=dicDatos[usuarios]["ubicacion"]
edad=dicDatos[usuarios]["edad"]
intereses=dicDatos[usuarios]["intereses"]
print(edad)	#edad de juan
'''

