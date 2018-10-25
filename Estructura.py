from datos_prueba import dicDatos
from datos_prueba import dicBusq
# from math import radians, cos, sin, asin, sqrt  # para la harvensine
from geopy.distance import vincenty  # instalar geopy, ejecutar desde la consola   tambien vale "great_circle"

min = ["q", "w", "e", "r", "t", "y", "u", "i", "o", "p", "a", "s", "d", "f", "g", "h", "j", "k", "l", "ñ", "z", "x",
	   "c", "v", "b", "n", "m"]
may = ["Q", "W", "E", "R", "T", "Y", "U", "I", "O", "P", "A", "S", "D", "F", "G", "H", "J", "K", "L", "Ñ", "Z", "X",
	   "C", "V", "B", "N", "M"]
num = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
gb = "_"


def menuPrincipal():
	OpcionesMenuPrincipal = input ("""
	(1) CARGAR UN GRUPO DE PERSONAS PREDETERMINADO
	(2) CREAR CUENTA NUEVA
	(3) INGRESAR AL SISTEMA
	Escriba el numero de opcion deseada: 
	""")

	if OpcionesMenuPrincipal == "1":
		print ("hola")
	# cuando cargo el grupo de persona predeterminado este se va a actualizar con "usuariosDeEstructura"
	# llama a la funcion "datos_prueba.base_de_datos_de_prueba()",
	# print(datos_prueba.base_de_datos_de_prueba())	#va a imprimir el diccionario entero, para probar vió.
	elif OpcionesMenuPrincipal == '2':
		crearUsuario ()
	# llama una func, la cual sirve para cargar datos, y esto aladirlos al diccionario principal, osea a usuariosDeEstructura
	elif OpcionesMenuPrincipal == '3':
		ingresarSistema ()
	else:
		print ("Por favor, ingrese una de las opciones")
		menuPrincipal ()  # vuelve al menu principal


		
pseu = ""  # se la define globalmente, para despues usarla en las distintas funciones
def ingresarSistema():
	global pseu  # hace que se pueda modificar globalmente el valor de pseu, dentro de esta func
	pseu = str (input ("Ingrese su nombre de usuario:"))
	if pseu in dicDatos.keys ():
		contraseña = (input ("Ingrese su contraseña:"))
		if contraseña == dicDatos[pseu]["contraseña"]:
			print ("Bienvenide", dicDatos[pseu]["nombre"])
			menuSecundario ()
		else:
			print ("Contraseña incorrecta")
			menuSecundario ()
	else:
		print ("Usuario inválido, volviendo al menu principal")
		ingresarSistema ()


def menuSecundario():
	opcionesMenuSecundario = input ("""
	(1) BUSCAR GENTE
	(2)	MENSAJES
	(3) EDITAR
	(4) SALIR DEL SISTEMA	
	""")
	if opcionesMenuSecundario == "1":
		filtrarBusquedas ()
	elif opcionesMenuSecundario == "2":
		print ("s")
	# va a decir los mensajes que tiene, y luego borrarlos
	elif opcionesMenuSecundario == "3":
		print ("aun no")
	elif opcionesMenuSecundario == "4":
		print ("Adios")
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

	# rangoEdad = crearRango (edadMinima, edadMaxima)
	radioDeBusq = int (input ("Ingrese un radio de busqueda en km: "))
	# dicBusq[pseu]=[sexoInt,[rangoEdad]]
	funcionBusqueda (sexoInt, [edadMinima, edadMaxima], radioDeBusq)


def funcionBusqueda(sexoDeInteres, rangoEdades, radioBusqueda):
	listaUsers = list(dicDatos.keys ())
	listaUsers.remove (pseu)  # elimina de la lista de usuarios, el usuario logueado
	ubicacionUsuarioLogueado = dicDatos[pseu]["ubicacion"]
	interesesUsuarioLogueado = dicDatos[pseu]["intereses"]
	
	
	
	for numUser in range (len (listaUsers)):
		# va a repetirse las veces como numero de usuario haya
	
		# va a recorrer la lista de usuarios, las variables de aca abajo cambian en cada iteracion
		sexo = dicDatos[listaUsers[numUser]]["sexo"]
		ubicacion = dicDatos[listaUsers[numUser]]["ubicacion"]
		edad = dicDatos[listaUsers[numUser]]["edad"]
		intereses = dicDatos[listaUsers[numUser]]["intereses"]
	
		if ((sexo == sexoDeInteres[0]) or (sexo == "I")) and (rangoEdades[0] <= edad and rangoEdades[1] >= edad):
			# si coincide con el sexo que buscaba                # si entra en el rango de edades
			if distanciaEntreDos (ubicacionUsuarioLogueado, ubicacion) <= radioBusqueda:
				# si la distancia entre los dos es menor a la especificado por el usuario, osea radioBusqueda
	
				porcentajeCoin=calcularPorcentaje(interesesUsuarioLogueado,intereses)
				
				print (listaUsers[numUser]," y tu tienen {} de coincidencia".format(porcentajeCoin))
				eleccion=input ("""
				¿Que deseas hacer?
				Dar Like(L)
				Ignorar(I)
				Salir(S)
				""")
				
				
				
		if len (sexoDeInteres) == 2:
		# para el caso que busco H y M, osea si hay dos elementos en la lista
			print ("xD")
	
	return "finish"

'''
def mostrarUsuarios(pseu):
for usuario in dicDatos.keys():
	if (dicDatos[usuario][3] in dicBusq[pseu][0]) and (dicDatos[usuario][4] in dicBusq[pseu][1]):
		print(dicDatos.keys())
'''

def calcularPorcentaje(interes1,interes2):	#funcion que dadas dos listas, devuelve el porcentaje de coincidencia entre ambas
    return
	# calcularPorcentaje(["1s","2","3","4s","5","5"],["1d","2","3","4"])


def definirSexoInt(sexoInteres):
	if sexoInteres == ("M" or "m"):
		return ["M"]
	elif sexoInteres == ("F" or "f"):
		return ["F"]
	else:
		return ["M", "F"]


def crearUsuario():
	pseu = str (input ("Ingrese nombre de usuario: "))
	if pseu in list(dicDatos.keys ()):
		print("Usuario ya existente, intente con uno diferente")
		crearUsuario()
	validarPseudonimo (pseu)
	
	contraseña = str (input ("Ingrese contraseña: "))
	if validarContraseña (contraseña)==True:
		nombre = str (input ("Ingrese su/s nombre/s: "))
		apellido = str (input ("Ingrese su/s apellido/s: "))
		sexo = (str (input ("Sexo (M, F o I):"))).upper ()
		if sexo != "M" and sexo != "F" and sexo != "I":
			print ("vuelva a ingresar los datos")
			crearUsuario()
			
		edad = int (input ("Ingrese su edad: "))
		validarEdad (edad)
		
		longitud = int(input("ingrese latitud: "))
		latitud = int(input("ingrese longitud: "))

		intereses = str (input ("Ingrese separados por espacios y guiones hobbies, intereses, etc. Ej.: 'green-day gatos viajar museos-de-arte: "))
		intereses=deTextoALista(intereses)
		
		dicLocal = {
		pseu: {
		"nombre":nombre,
		"apellido":apellido,
		"contraseña":contraseña,
		"sexo": sexo,
		"edad": edad,
		"ubicacion": [longitud,latitud],
		"intereses": intereses,
		"mensajes":{}
		}}
		
		dicDatos.update(dicLocal)	#mete el diccionario dicLocal, dentro de dicDatos
		
		print("Felicidades, ya es usuario de Tinder")
		print(dicDatos[pseu])
		menuPrincipal()
	else:
		print("vuelva a ingresar los datos")
		crearUsuario()


def validarPseudonimo(pseudonimo):  # devuelve True o False
	if any (letra.isupper () for letra in pseudonimo) == True:
		return False
	elif (any (i.isdigit () for i in pseudonimo) == True) or (any (i == "_" for i in pseudonimo)) == True or any (
			i.isupper () for i in pseudonimo) == False:
		# si hay un numero o un digito en pseudonimo
		# EJEMPLO print (any (i == "_" for i in "pseudonimo"))  # devuelve True si hay algun guion bajo
		return True  # ("hay almenos un numero o un guion bajo")
	else:
		return False


def validarContraseña(contraseña):  # devuelve True o False
	# debe contener al menos una minúscula, una masyucula, un número y 5 caracteres")
	if ((any (i.isdigit () for i in contraseña) == True) or (any (i == "_" for i in contraseña)) == True or any (
			i.islower () for i in contraseña) == True or any (
		i.isupper () for i in contraseña) == True) == True and len (
		contraseña) > 5:
		return True
	else:
		return False


# nose porque pero si pongo un signo "!" me sigue tirando true
# print(validarContraseña("hosdasg_9!"))
def validarEdad(edad):
	if edad < 18:
		print ("Debe tener por lo menos 18 años para registrarse")
		menuPrincipal ()
	if edad > 99:
		print ("Debe tener menos de 99 años para registrarse")
		menuPrincipal ()


def deTextoALista(texto):
	return texto.split(" ")


def crearRango(edadMin, edadMax):
	for x in range (edadMin, edadMax + 1):
		rangoEdad = [x]
		return rangoEdad


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
