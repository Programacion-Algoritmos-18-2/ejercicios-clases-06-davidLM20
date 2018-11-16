from mipaquete.modelo import *

#p = Persona_equipo("Luis") // ejemplo de error de instancia
f = Futbolista("Antonio") #se añade un nombre a futbolista
m = Medico("Ramon") # se añande un nombre a medico
p = Presidente_equipo("Francisco") # se añade un nombre al presidente del quipo
e = Entrenador("José")# se añade un nombre al enternador del quipo


# se crea una lista que contenga a los objetos 
lista =[f , m, p, e ]
# se itera la lista de objeto a objeto
for l in lista:
	l.entrenar()# se imprime lo que el mensaje de cada objeto