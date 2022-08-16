#clase dia miercoles 16/8 - primera clase 2° cuatrimestre
#laboratorio 2, python

#lista = Noelia, Nadia, Facundo, Ana, Juani, Ernesto, Bruno, Gabriel, Carlos
perricornios = ["Noelia", "Nadia", "Facundo", "Ana", "Juani", "Ernesto", "Gabriel", "Carlos"]

#Para mostrar por indices
print(perricornios[0])
print(perricornios[1])
print(perricornios[2])
print(perricornios[3])
print(perricornios[4])
print(perricornios[5])
print(perricornios[6])
print(perricornios[7])

#Para recorrer de atras hacia adelante
print(perricornios[-1])
print(perricornios[-2])
print(perricornios[-3])
print(perricornios[-4])

#recuperar rango de la lista
print(perricornios[0:2]) #solo muestra el 0 y 1
print(perricornios[:2])
print(perricornios[1:])

#modificamos un valor
perricornios[1]= "Braian"
perricornios[0]= "Carlos"
print(perricornios)

for nombres in perricornios:
    print(nombres)
else:
    print("No hay mas nombres")

#preguntamos cuantos elementos tiene
print(len(perricornios))

#agregamos un elemento
perricornios.append("Marcelo")
print(perricornios)

#insertar en un índice específico
perricornios.insert(1, "Alberto") #ingresar el indice y despues el elemento
print(perricornios) #se desplazan los demas elementos una posición al ingresar uno nuevo

perricornios.insert(3,"Debora")
print(perricornios)

#eliminamos un elemento de la lista
perricornios.remove("Alberto") #pasamos el string con el valor
print(perricornios) #muestra la lista sin el elemento seleccionado

#eliminar el ultimo elemento
perricornios.pop()
print(perricornios) #elimina el ultimo elemento de la lista, en este caso "Marcelo"

#eliminar indice específico
del perricornios[2]
print(perricornios) #desaparece el elemento de la posición 2, en este caso "Debora"

#eliminar, borrar o limpiar todos los elementos
perricornios.clear()
print(perricornios) #la lista está vacía, vemos dos []

#eliminar la lista
del perricornios # del, viene de "delete"
print(perricornios) #tira error, lista no definida.. fue borrada 