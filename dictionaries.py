#Diccionarios en Python, está compuesto por dos elementos:

#'Sagitario': 11 -> una llave y un valor
#dict --> (key and value)

diccionario = {
    'IDE' : 'Integrated Development Environment', #ponemos , siempre
    'POO' : 'Programación Orientada a Objetos',
    'SABD' : 'Sistema de Administración de Base de Datos' # acá no hace falta la coma 
}

print(diccionario)

#Verificar la cantidad de elementos de un diccionario 
print(len(diccionario))

#en el diccionario no hay indices

#Para acceder a lun diccionario con la llave (key)
print(diccionario['IDE']) #con la llave accedemos al valor

#Otra forma de recuperar un elemento
print(diccionario.get('POO'))
print(diccionario.get('SABD'))

#Modificamos el elemento
diccionario['IDE'] = 'Entorno de Desarrollo Integrado'
print(diccionario)

#Recorremos los elementos
for termino in diccionario: #recorremos mostrando solo las llaves
    print(termino)


#for termino, valor in diccionario: --> tenemos ERROR, no se muestra así
        #print(termino, valor)


#Necesitamos una función para recorrer un diccionario
#La función Ítems
for termino, valor in diccionario.items():
    print(termino,valor)

#Otras maneras de acceder a un diccionario con funciones
#Función keys
for termino in diccionario.keys():
    print(termino) #devuelve solo las llaves

#Función values
#devuelve solo los valores
for valor in diccionario.values():
    print(valor)

#Comprobar si un elemento existe
print('IDE' in diccionario) # --> Devuelve 'True'
print('IDE' not in diccionario) # --> Develve 'False' porque si está

#Agregar un elemento
diccionario['PK'] = 'Primary Key'
print(diccionario)

#No acepta elementos repetidos, si agrego 'PK' de nuevo,la reescribe
diccionario['PK'] = 'Llave Primaria'
print(diccionario)

#Eliminar un elemento
diccionario.pop('SABD') #eliminamos a SDBD
print(diccionario) #muestra eldiccionario sin elelemento borrado

#Vaciar un diccionario
diccionario.clear()
print(diccionario) #vemos solo las {}

#Eliminar diccionario
del diccionario #el diccionario se borró
#print(diccionario) #vemos el'NOT DEFINED'

#Concatenamos Listas
lista1 = [1, 2, 3]
lista2 = [4, 5, 6, 7]
lista3 = lista1 + lista2 #Se fusionan en una sola
print(lista3)

lista3.extend([7, 8, 9]) #agregamos varios elementos a una lista
print(lista3) #acepta valores repetidos, el 7
print(lista3.index(5)) # el elemento 5, está en la posición 4
print(lista3.index(7)) # el elemento 7 está en la posición 6
#print(lista3.index(0)) # devuelve error, porque el elemento 0 no está en la lista3

#Cuántos valores repetidos hay en una lista?
print(lista3.count(7)) # muestra cuantas veces se repite el valor 7,en este caso es 2

#Para poner al revés una lista
print(lista3.reverse())
print(lista3) # la muestra al revés

#Para que una lista de multiplique repitiendo sus elementos
lista = [1, 2, 3] * 2
print(lista)

lista3 = lista3 * 2
print(lista3)

#Métodos de ordenamiento
#La función SORT los ordena en ascendente por default
lista3.sort()
lista.sort()
print(lista)
print(lista3)

#Para ordenarlos de forma DESCENDENTE
lista3.sort(reverse = True)
print(lista3) #vemos ordenado de atrás hacia adelante

#Repaso de tuplas
tupla = (7, 'siete', [8, 9, 10], 'lista de números', 10.97, True) #puede tener diferentes tipos de datos.
print(tupla)

print(7 in tupla) #buscamos un elemento en la tupla, devuelve True si lo tiene
print(7 not in tupla) #devuelve False, porqe si lo tiene