from datos_prueba import dicDatos
from datos_prueba import diccionarioPrueba
from math import floor
# from math import radians, cos, sin, asin, sqrt  # para la harvensine
from geopy.distance import vincenty  # instalar geopy, ejecutar desde la consola   tambien funciona con "great_circle"

pseu = ""  # se la define globalmente, para despues usarla en las distintas funciones
listaUsers = []  # es una lista de usuarios global, la cual se actualiza con las claves de los diccionarios, cuando se carga el grupo de persona predeterminado


def menuPrincipal():
    global listaUsers
    OpcionesMenuPrincipal = input ("""
    (1) CARGAR UN GRUPO DE PERSONAS PREDETERMINADO
    (2) CREAR CUENTA NUEVA
    (3) INGRESAR AL SISTEMA
    Escriba el numero de opcion deseada: 
    """)

    if OpcionesMenuPrincipal == "1":
        dicDatos.update (diccionarioPrueba)
        # print ("\n" * 100) una manera de limpiar la pantalla
        listaUsers = list (dicDatos.keys ())
        menuPrincipal ()
    elif OpcionesMenuPrincipal == '2':
        crearUsuario ()
    # llama una func, la cual sirve para cargar datos, y esto aladirlos al diccionario principal, osea a usuariosDeEstructura
    elif OpcionesMenuPrincipal == '3':
        ingresarSistema ()
    else:
        print ("Por favor, ingrese una de las opciones")
        menuPrincipal ()  # vuelve al menu principal


def ingresarSistema():
    global pseu  # hace que se pueda modificar globalmente el valor de pseu, dentro de esta func
    pseu = str (input ("Ingrese su nombre de usuario:"))
    if pseu in dicDatos.keys ():
        contraseña = (input ("Ingrese su contraseña:"))
        if contraseña == dicDatos[pseu]["contraseña"]:
            print ("Bienvenido a Tinder ", dicDatos[pseu]["nombre"])
            menuSecundario ()
        else:
            print ("Contraseña incorrecta")
            menuPrincipal ()
    else:
        print ("Usuario inválido, volviendo al menu principal")
        menuPrincipal ()


def menuSecundario():
    opcionesMenuSecundario = input ("""
    (1) BUSCAR GENTE
    (2) MENSAJES
    (3) EDITAR
    (4) SALIR DEL SISTEMA   
    """)
    if opcionesMenuSecundario == "1":
        filtrarBusquedas ()
    elif opcionesMenuSecundario == "2":
        mostrarMensajes ()
        menuSecundario ()
    elif opcionesMenuSecundario == "3":
        print ("Funcion aun sin terminar")
        menuSecundario ()
    elif opcionesMenuSecundario == "4":
        print ("Adios, gracias por visitar Tinder")
        menuPrincipal ()
    else:
        print ("Por favor, ingrese una de las opciones")
        menuSecundario ()


def filtrarBusquedas():
    ubicacionUsuarioLogueado = dicDatos[pseu]["ubicacion"]

    sexoInteres = str (input ("Ingrese el/los sexo/s de interes (M, F o A):"))
    sexoInt = definirSexoInt (sexoInteres)

    edadMinima = int (input ("Ingrese la edad mínima del rango de búsqueda:"))
    edadMaxima = int (input ("Ingrese la edad máxima del rango de búsqueda:"))

    if (validarEdad (edadMaxima) == False) or (validarEdad (edadMinima) == False):
        print ("Por favor ingrese un rango de edad de entre 18 y 99 años.")
        filtrarBusquedas ()

    radioDeBusq = int (input ("Ingrese un radio de busqueda en km: "))
    funcionBusqueda (sexoInt, [edadMinima, edadMaxima], radioDeBusq)


def funcionBusqueda(sexoDeInteres, rangoEdades, radioBusqueda):
    global listaUsers
    if pseu in listaUsers:  # si el usuario esta en la lista
        listaUsers.remove (pseu)  # elimina de la lista de usuarios, el usuario logueado
    ubicacionUsuarioLogueado = dicDatos[pseu]["ubicacion"]
    interesesUsuarioLogueado = dicDatos[pseu]["intereses"]

    # recorre la longitud de LA COPIA de la lista de usuarios, para evitar el problema de out of range
    for numUser in range (len (listaUsers[:])):
        # va a repetirse las veces como numero de usuario haya y va a recorrer la lista de usuarios
        # las variables de aca abajo cambian en cada iteracion

        sexo = dicDatos[listaUsers[numUser]][
            "sexo"]  # en dicDatos, listaUsers[numUser] es un string, osea un pseudonimo en este caso
        ubicacion = dicDatos[listaUsers[numUser]]["ubicacion"]
        edad = dicDatos[listaUsers[numUser]]["edad"]
        intereses = dicDatos[listaUsers[numUser]]["intereses"]


        # si la longitud de la lista es 1 (es decir, que solamente eligiò F o M) o el sexo del usuario buscado es Indeterminado
        if ((len (sexoDeInteres) == 1) or (sexo == "I")) and (rangoEdades[0] <= edad and rangoEdades[1] >= edad):
            if (distanciaEntreDos (ubicacionUsuarioLogueado, ubicacion)) <= radioBusqueda:  #no esta puesto en el if de arriba para que no esté con tantas condiciones juntas
                # si entra en el rango de edades # si la distancia entre los dos es menor a la especificado por el usuario, osea radioBusqueda

                porcentajeCoin = calcularPorcentaje (interesesUsuarioLogueado, intereses)
                print (listaUsers[numUser], " y tu tienen {} % de coincidencia".format (porcentajeCoin))
                eleccionUsuario = input ("""
                ¿Que deseas hacer?
                Dar Like(L)
                Salir(S) 
                Ignorar(Cualquier Tecla)
                """)
                opcionesBusqueda (eleccionUsuario, numUser)

        # para el caso que busco H y M, osea si hay dos elementos en la lista
        if ((len (sexoDeInteres) == 2) or (sexo == "I")) and (rangoEdades[0] <= edad and rangoEdades[1] >= edad):
            if (distanciaEntreDos (ubicacionUsuarioLogueado, ubicacion)) <= radioBusqueda:
                # si entra en el rango de edades # si la distancia entre los dos es menor a la especificado por el usuario, osea radioBusqueda

                porcentajeCoin = calcularPorcentaje (interesesUsuarioLogueado, intereses)
                print (listaUsers[numUser], " y tu tienen {} % de coincidencia".format (porcentajeCoin))
                eleccionUsuario = input ("""
                ¿Que deseas hacer?
                Dar Like(L)
                Salir(S) 
                Ignorar(Cualquier Tecla)
                """)
                opcionesBusqueda (eleccionUsuario, numUser)


        else:
            print ("La busqueda ha finalizado.")
            menuSecundario ()
    return


# dados el numero de usuario y la eleccion...
def opcionesBusqueda(laEleccion, numeroDeUser):
    global listaUsers  # hace posible la modificacion de esta lista, dentro de esta funcion
    if laEleccion == "L" or laEleccion == "l":
        if pseu in dicDatos[listaUsers[numeroDeUser]]["likes"]:  # si el usuario actual esta en la lista de likes de la persona
            eleccion = input ("Quieres dejarle un mensaje a {} ?  (S/N)").format (listaUsers[numeroDeUser])
            if eleccion == "S":
                mensaje = str (input ("Deja un mensaje a ", listaUsers[numeroDeUser], ": "))
                dicDatos[numeroDeUser]["mensajes"][pseu] = [mensaje]
                listaUsers.remove (listaUsers[numeroDeUser])  # de la lista elimina al usuario actual de la busqueda
                return
            else:  # si su eleccion fue N
                listaUsers.remove (listaUsers[numeroDeUser])
                return
        else:  # si no està en la lista de likes
            print (listaUsers)
            listaUsers.remove (listaUsers[numeroDeUser])
            return "Le diste like"


    elif laEleccion == "S" or laEleccion == "s":  # si puso salir, vuelve al menu de inicio
        menuSecundario ()

    else:  # si el usuario apreta cualquier tecla, osea si lo ignora
        listaUsers.remove (listaUsers[numeroDeUser])
        return


def calcularPorcentaje(interes1, interes2):  # funcion que dadas dos listas, devuelve el porcentaje de coincidencia entre ambas
    acum = 0
    for ciclo in interes1:
        if ciclo in interes2:
            acum += 1
    return floor (((100 * acum) / (len (interes1) + len (interes2))))


def mostrarMensajes():
    if dicDatos[pseu]["mensajes"]:
        print ("tienes un mensaje de: ", dicDatos[pseu]["mensajes"])
    else:
        print ("No tiene ningún mensaje.")


def definirSexoInt(sexoInteres):
    if sexoInteres == "M" or sexoInteres == "m":
        sexoInt = ["M"]
    elif sexoInteres == "F" or sexoInteres == "f":
        sexoInt = ["F"]
    elif sexoInteres == "A" or sexoInteres == "a":
        sexoInt = ["M", "F"]
    else:
        print ("Por favor ingrese una de las opciones: sexo masculino ('M'), sexo femenino ('F') o ambos ('A')")
        sexoInteres = input ("Ingrese el sexo de interes: ")
        definirSexoInt (sexoInteres)
        sexoInt = ""
    return sexoInt


def crearUsuario():
    pseu = str (input ("Ingrese nombre de usuario: "))
    if pseu not in list (dicDatos.keys ()): #se fija que no haya un usuario con el mismo nombre
        validarPseudonimo (pseu)

        contraseña = str (input ("Ingrese contraseña: "))
        validarContraseña (contraseña)

        nombre = str (input ("Ingrese su/s nombre/s: "))
        apellido = str (input ("Ingrese su/s apellido/s: "))
        sexo = (str (input ("Sexo (M, F o I):"))).upper ()
        if sexo != "M" and sexo != "F" and sexo != "I":
            print ("vuelva a ingresar los datos")
            crearUsuario ()
        edad = int (input ("Ingrese su edad: "))

        if validarEdad (edad) == False:
            print ("Debe tener entre 18 y 99 años para registrarse en el sistema.")
            menuPrincipal ()
        longitud = int (input ("ingrese latitud: "))
        latitud = int (input ("ingrese longitud: "))
        intereses = str (input (
            "Ingrese separados por espacios y guiones hobbies, intereses, etc. Ej.: 'green-day gatos viajar museos-de-arte: "))
        intereses = intereses.split(" ")

        dicLocal = {
            pseu: {
                "nombre": nombre,
                "apellido": apellido,
                "contraseña": contraseña,
                "sexo": sexo,
                "edad": edad,
                "ubicacion": [longitud, latitud],
                "intereses": intereses,
                "mensajes": {}
            }}
        dicDatos.update (dicLocal)  # mete el diccionario dicLocal, dentro de dicDatos
        print ("Felicidades, ya es usuario de Tinder")
        menuPrincipal ()
    else:
        print ("Usuario ya existente, intente con uno diferente")
        crearUsuario ()


def validarContraseña(contraseña):
    # debe contener al menos una minúscula, una masyucula, un número y 5 caracteres")
    # la funcion any, se fija si dada una iteracion AL MENOS encuentra un elemeneto que sea verdadero
    # EJEMPLO print (any (i == "_" for i in "pseudonimo"))  # devuelve True si hay algun guion bajo
    # EJEMPLO islower(), verifica si un caracter es minuscula


    if (any (i in "!#$%&/()=?¡¿[]+-{}" for i in contraseña)):   #si hay alguno de esos caracteres, entonces pide ingresar de nuevo
        print ("Contraseña invalida, por favor ingrese una contraseña que contenga por lo menos una minúscula, un número, una mayúscula y 5 caracteres")
        contraseña = str (input ("Ingrese una contraseña: "))
        validarContraseña (contraseña)

    elif (len (contraseña) > 5) and any (i.isdigit () for i in contraseña) and (any (i.isupper () for i in contraseña) and any (i.islower () for i in contraseña)):
        return

    else:
        print ("Contraseña invalida, por favor ingrese una contraseña que contenga por lo menos una minúscula, un número, una mayúscula y 5 caracteres")
        contraseña = str (input ("Ingrese una contraseña: "))
        validarContraseña (contraseña)
    # si pongo un signo "!" me sigue tirando true
    #porque verifica que al menos haya una mayusucla y una minuscula, si eso es cierto, entonces no importa el resto

#print (validarContraseña ("hosdaD5s!"))

def validarPseudonimo(pseudonimo):
    if any(i.isupper () for i in pseudonimo):
        print ("Usuario invalido, por favor ingrese un usuario que contenga únicamente minúsculas, números o guión bajo.")
        pseu = str (input ("Ingrese un nombre de usuario: "))
        validarPseudonimo (pseu)

    elif (any (i in "!#$%&/()=?¡¿[]+-{}" for i in pseudonimo)):
        print ("Usuario invalido, por favor ingrese un usuario que contenga únicamente minúsculas, números o guión bajo.")
        pseu = str (input ("Ingrese un nombre de usuario: "))
        validarPseudonimo (pseu)

    elif (any (i.isdigit () for i in pseudonimo)) or (any (i == "_" for i in pseudonimo)) or any (letra.islower () for letra in pseudonimo):
        #si entró a este elif, es porque no hay mayusculas, ni simbolos especiales
        return True  # ("hay almenos un numero o un guion bajo o una minuscula")

    else:
        print ("Usuario invalido, por favor ingrese un usuario que contenga únicamente minúsculas, números o guión bajo.")
        pseu = str (input ("Ingrese un nombre de usuario: "))
        validarPseudonimo (pseu)


def validarEdad(edad):
    if edad <= 18 or edad > 99:
        return False
    else:
        return True




# usando Vicenty (necesita geopy)
def distanciaEntreDos(distancia1, distancia2):
    # dadas dos distancias(variable que contiene una lista), devuelve la distancia en km
    return vincenty (distancia1, distancia2).km


'''
#usando Harvensine https://stackoverflow.com/questions/4913349/haversine-formula-in-python-bearing-and-distance-between-two-gps-points
def haversine(lon1, lat1, lon2, lat2):
    """
    Calculate the great circle distance between two points 
    on the earth (specified in decimal degrees)
    """
    # convert decimal degrees to radians 
    lon1, lat1, lon2, lat2 = map(radians, [lon1, lat1, lon2, lat2])
    # haversine formula 
    dlon = lon2 - lon1 
    dlat = lat2 - lat1 
    a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
    c = 2 * asin(sqrt(a)) 
    r = 6371 # Radius of earth in kilometers. Use 3956 for miles
    return c * r
# print(haversine(2.12,31.11,32.1,21))
'''

print (menuPrincipal ())
