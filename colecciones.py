#Clase dia miercoles 16/8 - Primera clase 2° cuatrimestre.
#listas en Python
#Se losconoce como VECTORES o FILAS 

#lista de nombres: Noelia, Nadia, Facundo, Ana, Bruno, Braian, Ernesto, Juany, Carlos, Gabriel
perricornios = ["Noelia", "Nadia", "Facundo", "Ana", "Bruno", "Braian", "Ernesto", "Juany", "Carlos", "Gabriel"]

#Para mostrar por índices
print(perricornios[0])
print(perricornios[1])
print(perricornios[2])
print(perricornios[3])
print(perricornios[4])
print(perricornios[5])
print(perricornios[6])
print(perricornios[7])
print(perricornios[8])
print(perricornios[9])
print('\n') #hago un salto de línea

#Para recorrer de atrás hacia adelante
print(perricornios[-1])
print(perricornios[-2])
print(perricornios[-3])
print(perricornios[-4])
print(perricornios[-5])
print(perricornios[-6])
print(perricornios[-7])
print(perricornios[-8])
print(perricornios[-9])
print('\n')
#Recuperar rango de la lista
print(perricornios[0:2]) #solo muestra el 0 y 1.
print(perricornios[:2]) #muestra los primeros 2 elementos.
print(perricornios[1: ]) #muestra desde el índice 1 hasta el final.
print('\n')

#Modificamos un valor
perricornios[1] = "Alberto" #reemplaza a Nadia
perricornios[2] = "Jonatan" #reemplaza a Facundo
print(perricornios) #muestra los nuevos valores de la lista.
print('\n')

for miembros in perricornios:
    print(miembros)
else:
    print("No hay mas nombres.")

#Preguntamos cuantos elementos tiene una lista:
print('\n')
print(len(perricornios))

#Agregamos un elemento
perricornios.append("Marcelo") #lo añade al final de la lista.
perricornios.append([1, 2, 3]) #añadimos listas dentro de listas
perricornios.append(True) # pueden contener calquier valor, ejemplo: booleanos
perricornios.append([4.5]) # o números reales
perricornios.append(7) # números enteros, etc
print(perricornios)

#Insertar elemento en un índice específico
perricornios.insert(1, "Ariel") #ingresar el índice y despues el elemento.
print(perricornios) #se desplazan los demás elementos de la lista una posición hacia la derecha.

perricornios.insert(3, "Debora") #añade a Debora en elindice 3
print(perricornios)

#Eliminamos un elemento de la lista.
perricornios.remove("Alberto") #pasamos el string con el valor) 
print(perricornios) #se elimina a Alberto de nuestra lista

#Eliminar el último elemento
perricornios.pop()
print(perricornios) #en este caso, se elimina a Marcelo

#Eliminar por índice específico
del perricornios[2] #borra al elemento de la posición 2
print(perricornios) #en este caso, borramos a Debora de la lista

#Eliminar, borrar o limpiar todos los elementos
perricornios.clear()
print(perricornios) #solo vemos la lista vacía, aparecen los []

#Eliminar la lista
del perricornios #del, viene de delete --> borrar
#print(perricornios) sale error, lista no definida.. fue borrada

#TUPLAS
#lo escribimos entre ()
print('\n')
#definimos una tupla asi:
cocina = ("cuchara", "cuchillo", "tenedor")
print(cocina) # vemos todos los elementos de la tupla

#Para ver el largo de la tupla
print(len(cocina)) # nos muestra que tiene 3 elementos

#Para acceder a un elemento usamos [], no ()
print(cocina[0]) #vemos el índice 0 de la tupla, en este caso 'cuchara'

#Mostrar de manera inversa
print(cocina[-1]) # muestra el último elemento de la tupla, "tenedor"
print(cocina[-2]) # muestra el anteúltimo, en este caso "cuchillo"

#Accedemos a un rango
print(cocina[0:1]) #muestra ('cuchara',) --> asi se ven las tuplas, lo reconozco por la coma
print(cocina[0:2]) #muestra ('cuchara', 'cuchillo')
#ejemplo
verduras = ('papa') #esto NO es una tupla, es tipo string
print(verduras)
verduras = ('papa', ) #ahora SI es una tupla.
print(verduras) #muestra ('papa',)

#Recorremos los elementos de la tupla
for cubiertos in cocina: #print usa los \n para los saltos de linea
    print(cubiertos, end=' ') #con end=' ' lo mostramos al lado, en la misma linea

#cocina[0] = "plato"
#print(cocina) #da ERROR --> las tuplas NO se pueden modificar/reasignar

#Modificar las tuplas
#NO son buena practica, pero cuando sea necesario
#Hacemos la conversión de tupla a lista
#y luego convertimos de lista a tupla

cocinaLista = list(cocina) #convertimos de tupla a lista
cocinaLista[0] = "plato" #hacemos la modificación
cocina = tuple(cocinaLista) #volvemos a convertir a tupla
print('\n', cocina) #con '\n' hacemos de nuevo el salto de línea y 'plato' reemplaza a 'cuchara'

del cocina #eliminamos la tupla
#print(cocina) #cocina ya no está definido
