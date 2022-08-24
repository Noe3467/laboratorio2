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
#print(diccionario) #vemos el'NOT DEFINED