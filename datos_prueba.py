'''
#Los menues pueden tener una pinta similar a esta:
-------------------------------------------------------------
-		(1) BUSCAR GENTE			(3) EDITAR				-
-		(2) MENSAJES				(4) SALIR DEL SISTEMA	-
-------------------------------------------------------------
#o una mas sencilla
(1) BUSCAR GENTE    (2) MENSAJES	(4) SALIR DEL SISTEMA	(3) EDITAR
'''




'''
#MENU PRINCIPAL
	#CARGAR UN GRUPO DE PERSONAS PREDETERMINADO
	#va a llamar a una funcion, dicha funcion está en datos_prueba.py, es un diccionario que contiene los datos guardados
	
	#CARGAR UNA NUEVA PERSONA
	
	#(opcional) EDITAR INFORMACION DE UNA PERSONA
	
	#INGREAR AL SISTEMA:
		PEDIR NOMBRE DE USUARIO Y CONTRASEÑA:
			Si 	#NO INGRESÓ AL SISTEMA 
			#Contraseña o usuario incorrectas o no existen	 #volver a PEDIR NOMBRE DE USUARIO Y CONTRASEÑA
		
		
			#Sí INGRESÓ AL SISTEMA						
				OPCIONES PARA EL USUARIO					
					#BUSCAR GENTE
					#MENSAJES	#despues fijate la linea 58
					#EDITAR	(esto es opcional??)
						NOMBRE
						APELLIDO
						INTERESES
						CONTRASEÑA
						EDAD
						SEXO
						UBICACION
					
					#SALIR DEL SISTEMA
#BUSCAR GENTE
-Radio máximo de búsqueda (en kilómetros, puede ser un flotante).
-Sexos de interés (puede ser hombre, mujer o ambos) #supongo que el sexo "indefinido" va a aparecer en la busqueda no importa si se pone hombre o mujer
-Rango de edades (edad máxima y edad mínima a buscar).
	#CUANDO EL USUARIO BUSCA van a aparecer las personas que cumplan con:
	- Vivan dentro del área buscada por el usuario actual. (libreria geopy)
	- Su sexo coincida con los sexos buscados por el usuario actual
	
	#UNA VEZ FINALIZADA LA BUSQUEDA
	#Se va a mostrar por pantalla, los usuarios que conicidan con la busqueda (uno por uno).
	#Cada vez que se muestra un usuario:
		-porcentaje de coincidencia =  (100 * 2) / (numeroDegustosDeA + numeroDegustosDeB)
		-la opcion de #LIKE   #IGNORAR   #VOLVER AL MENU
		
			#Si la otra persona ya habia likeado al usuario actual, entonces se va a mostar la opcion de
				-DEJAR UN MENSAJE (el cual estara en la seccion de mensajes cuando la otra persona ingrese al sistema)
									#esto lo hacemos asi? o que directamente cuando la otra persona ni bien entre al sistema le aparezca el mensaje?		
				-CONTINUAR
				
			#Si ya no quedan usuarios, entonces directamente vuelve a OPCIONES PARA EL USUARIO
	
		
#CARGAR UNA NUEVA PERSONA
#se almacena en un diccionario que tiene como clave=pseudonimo y de valor=una lista que contenga:
# - Nombre
# - Apellido
# - Contraseña (requiere al menos una mayúscula, una minúscula, un dígito decimal, y un
# largo mínimo de 5 caracteres)
# - Sexo
#         #Indefinido
#         #Mujer
#         #Hombre
# - Edad (de 18 a 99)
# - Ubicación actual: Latitud y longitud en grados decimales (ejemplo: 41.40338, 2.17403)
# - Intereses (va a ser otra lista)
'''



#-------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------


# from math import radians, cos, sin, asin, sqrt #para la harvensine
from geopy.distance import vincenty	#installar geopy, ejecutar desde la consola   tambien vale "great_circle"
from datos_prueba import dicDatos
from datos_prueba import dicBusq

min = "qwertyuiopasdfghjklñzxcvbnm"
may="QWERTYUIOPASDFGHJKLÑZXCVBNM"
num="1234567890"
gb="_"


def menuPrincipal():
	OpcionesMenuPrincipal = input("""
	(1) CARGAR UN GRUPO DE PERSONAS PREDETERMINADO
	(2) CREAR CUENTA NUEVA
	(3) (opcional) EDITAR INFORMACION DE UNA PERSONA
	(4) INGRESAR AL SISTEMA
	Escriba el numero de opcion deseada: 
	""")
	if OpcionesMenuPrincipal=="1":
		print("hola")
	#cuando cargo el grupo de persona predeterminado este se va a actualizar con "usuariosDeEstructura"
	#llama a la funcion "datos_prueba.base_de_datos_de_prueba()",
	# print(datos_prueba.base_de_datos_de_prueba())
	elif OpcionesMenuPrincipal == '2':
		crearUsuario()
		filtrarBusquedas()
	elif OpcionesMenuPrincipal=='3':
		print("as")
		#llama a una funcion para que sirve para editar la info de una persona
	elif OpcionesMenuPrincipal=='4':
		ingresarSistema()
	else:
		print("Por favor, ingrese una de las opciones")
		menuPrincipal()	#vuelve al menu principal



def ingresarSistema():
	pseu=str(input("Ingrese su nombre de usuario:"))
	if pseu in dicDatos.keys():
		contraseña=(input("Ingrese su contraseña:"))
		if contraseña == dicDatos[pseu]["contraseña"]:
			print("Bienvenide",dicDatos[pseu]["nombre"])
			menuSecundario()
		else:
			print("Contraseña incorrecta")
			ingresarSistema()
	else:
		print("Usuario inválido, volviendo al menu principal")
		ingresarSistema()
			
			
def menuSecundario():
	opcionesMenuSecundario = input("""
	(1) BUSCAR GENTE
	(2)	MENSAJES
	(3) EDITAR
	(4) SALIR DEL SISTEMA	
	""")
	if opcionesMenuSecundario=="1":
		filtrarBusquedas()
		
	elif opcionesMenuSecundario=="2":
		print("s")
		
	elif opcionesMenuSecundario=="3":
		print("aun no")
	
	elif opcionesMenuSecundario=="4":
		print("Adios")
		menuPrincipal()
	else:
		print("Por favor, ingrese una de las opciones")
		menuSecundario()
			
			
			
			
def filtrarBusquedas():
	pseu = str(input("Vuelva a ingresar su nombre de usuario:"))
	sexoInteres=str(input("Ingrese el/los sexo/s de interes (M, F o A):"))
	sexoInt = definirSexoInt(sexoInteres)
	
	edadMinima=int(input("Ingrese la edad mínima del rango de búsqueda:"))
	# validarEdad(edadMinima)
	edadMaxima=int(input("Ingrese la edad máxima del rango de búsqueda:"))
	# validarEdad(edadMaxima)
	
	crearRango(edadMinima,edadMaxima)
	
	radioDeBusq=int(input("Ingrese un radio de busqueda en km: "))
	# dicBusq[pseu]={sexoInt,[rangoEdad], radioDeBusq}	#me parece que el enunciado era viejo, y no hacia falta ponerlo en un diccionario aparte
	
	funcionBusqueda()	#dados sexoInt,[rangoEdad], radioDeBusq compara con lo que está en dic_Datos

	
def validarEdad(edad):
	if edad<18:
		print("Debe tener por lo menos 18 años para registrarse")
		menuPrincipal()
	if edad>99:
		print("Debe tener menos de 99 años para registrarse")
		menuPrincipal()
		
		
def definirSexoInt(sexoInteres):
	if sexoInteres==("M" or "m"):
		sexoInt = "M"
	elif sexoInteres==("F" or "f"):
		sexoInt = "F"
	else:
		sexoInt=["M","F"]
	return sexoInt
	
	
def crearUsuario():
	pseu = str(input("Ingrese nombre de usuario: "))
	validarPseudonimo(pseu)
	contraseña = str(input("Ingrese contraseña: "))
	validarContraseña(contraseña)
	nombre = str(input("Ingrese su/s nombre/s: "))
	apellido = str(input("Ingrese su/s apellido/s: "))
	sexo = str(input("Sexo (M, F o I):"))
	edad = int(input("Ingrese su edad: "))
	validarEdad(edad)
	intereses=str(input("Ingrese separados por espacios y guiones hobbies, intereses, etc. Ej.: 'green-day gatos viajar museos-de-arte"))
	interesesEnListado(intereses)
	dicDatos[pseu]=nombre,apellido,contraseña,sexo,edad,ubicacion,intereses
	filtrarBusquedas()


def validarPseudonimo(pseudonimo):  #devuelve True o False
	if any(letra.isupper() for letra in pseudonimo)==True:
		return False
	elif (any(i.isdigit() for i in pseudonimo)==True) or (any(i == "_" for i in pseudonimo))==True or any(i.isupper() for i in pseudonimo)==False:
		#si hay un numero o un digito en pseudonimo
		#EJEMPLO print (any (i == "_" for i in "pseudonimo"))  # devuelve True si hay algun guion bajo
		return True #("hay almenos un numero o un guion bajo")
	else:
		return False
# print(any(i.isdigit() for i in "hla1")) #la funcion any, verifica si en cada iteracion al menos hay algo verdadero, si es asi devueve tru



def validarContraseña(contraseña):  #devuelve True o False
#debe contener al menos una minúscula, una masyucula, un número y 5 caracteres")
	if ((any(i.isdigit() for i in contraseña)==True) or (any(i == "_" for i in contraseña))==True or any(i.islower() for i in contraseña)==True or any(i.isupper() for i in contraseña)==True)==True and len(contraseña)>5:
		return True
	else:
		return False
	#nose porque pero si pongo un signo "!" me sigue tirando true
		
# print(validarContraseña("hosdasg_9!"))
		
		
		
def interesesEnListado(intereses):
	interesesLista = intereses.split
def crearRango(edadMin,edadMax):
	for x in range(edadMin,edadMax+1):
		rangoEdad=[x]
		return rangoEdad

		
	
#usando Vicenty (necesita geopy)
def distanciaEntreDos(distancia1, distancia2):
#dadas dos distancias(variable que contiene una lista), devuelve la distancia en km
    return vincenty(distancia1, distancia2).km


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


def funcionBusqueda(sexoInteres, randoEdades, Ubicacion):
	return "not yet"


print(menuPrincipal())



