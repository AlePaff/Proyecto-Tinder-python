#Los menues pueden tener una pinta similar a esta:
-------------------------------------------------------------
-		(1) BUSCAR GENTE			(3) EDITAR				-
-		(2) MENSAJES				(4) SALIR DEL SISTEMA	-
-------------------------------------------------------------

#o una mas sencilla
(1) BUSCAR GENTE    (2) MENSAJES	(4) SALIR DEL SISTEMA	(3) EDITAR






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



















