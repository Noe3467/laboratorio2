#Clase dia miercoles 23/8 - Segunda clase 2° cuatrimestre.
#SET,--> SON LOS CONJUNTOS <--

#Seguimos con colecciones en Python:
#SET: No tiene un órden y no se pueden almacenar elementos duplicados o repetidos.
#Si bien NO SE PUEDEN MODIFICAR, se pueden agregar o quitar elementos.
#No mantiene ningun índice,el órden es ALEATORIO.

#En las colecciones para repasar:
#LISTAS: Mantienen un órden.. son MUTABLES, es decir que se pueden modificar.
#TUPLAS: También mantienen un órden pero no se pueden modificar, son INMUTABLES


#Tipo set, usamos las llaves {}
planetas = {'Marte', 'Jupiter', 'Venus'}
print(planetas)

#algunas funciones parecidas a tuplas y listas
print(len(planetas)) #_muestra el largo (length), la cantidad de elementos del conjunto

#Para saber si un elemento existe en un conjunto --> DEVUELVE UN BOOLEANO
print('Marte' in planetas) #devuelve True, porque lo contiene
print('Saturno' in planetas) #devuelve False, porque no lo contiene
print('Jupiter' not in planetas) #devuelve False porque si está

#Agregar un elemento
planetas.add('Tierra') #_con la función add, añadimos un planeta
planetas.add('Tierra') #NO se peden agregar elementos dplicados/repetidos
print(planetas) #_solo imprime una vez al elemento 'Tierra'

#Eliminar un elemento
#usando REMOVE, nos dá un ERROR si el elemento NO existe en el set o lo escribimos mal.
planetas.remove('Jupiter') #--> arroja ERROR si elemento NO EXISTE <--
print(planetas)

planetas.discard('Venus')
print(planetas)

#usando DISCARD, no nos tira error si el planeta NO existe o está mal escrito.
planetas.discard('tierra') #_si ese elemennto no existe, no tira error.
print(planetas)

#Limpiar set
planetas.clear()
print(planetas) # Nos muestra n set vacío

#Eliminar set
del planetas
#print(planetas) #_aparece 'planetas is NOT DEFINED' porque se borró