import abc #se imprta las libreias de la clase abstracta 

class Persona_equipo(metaclass = abc.ABCMeta):# se crea la super clase // abstracta

 	#__metaclass__ = abc.ABCMeta
	def __init__(self, n):
		self.nombre = n

	#metodo para agregar un nombre
	def setNombre(self,n):
		self.nombre = n # atributo // este atributo sera utilizado para cada clase hija

	#metodo que retorna el nombre
	def getNombre(self):
		return self.nombre
	
	@abc.abstractmethod # decorador
	#se crea el metodo abstracto ya que al tener la clase abstracta se necesita necesariamente un metodo abstracto
	def entrenar(self):
		pass

#se crea la clase entrenador que hereda de Persona equipo el nombre
class Entrenador(Persona_equipo):
	#se crea el metodo que asigne los atributo de esta clase 
	def __init__(self,n):
		super(Entrenador, self).__init__(n)#se hereda los atributos de la superclase
		self.codigo_entrenador = ""#atributo caracteristico

	def entrenar(self):
		print("Yo %s,  entrenador, soy el director del entrenamiento." %(self.getNombre())) # se envia el mensaje para con el nombre del entrenador

#se crea la clase futbolista esta hereda de Persona equipo el atributo nombre
class Futbolista(Persona_equipo):
	#se crea el metodo que asigne los atributo de esta clase 
	def __init__(self,p):
		super(Futbolista,self).__init__(p)#se hereda los atributos de la superclase
		self.posicion_campo = ""#atributo caracteristico

	def entrenar(self):
		print("Yo %s, futbolista, hago practicas en el entrenamiento" %(self.getNombre())) # se envia el mensaje para con el nombre del jugador


#se crea la clase Medico esta hereda de Persona equipo el atributo nombre
class Medico(Persona_equipo):
		#se crea el metodo que asigne los atributo de esta clase 
		def __init__(self,t):
			super(Medico, self).__init__(t)#se hereda los atributos de la superclase
			self.titulo = ""#atributo caracteristico

		def entrenar(self):
			print("Yo %s, medico, atiendo a los jugadores en el entrenamiento." %(self.getNombre())) # se envia el mensaje para con el nombre del medico

#se crea la clase Presidente equipo esta hereda de Persona equipo el atributo nombre			
class Presidente_equipo(Persona_equipo):
	#se crea el metodo que asigne los atributo de esta clase 
	def __init__(self, e):
		super(Presidente_equipo, self).__init__(e)#se hereda los atributos de la superclase
		self.numero_propiedades = 0#atributo caracteristico

	def entrenar(self):
		print("Yo %s,  presidente, pongo el dinero para el entrenamiento." %(self.getNombre())) # se envia el mensaje para con el nombre del presidente 
		
		
						
		