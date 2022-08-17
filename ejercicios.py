#ejercicio 1
#iterar un rango de 0 a 10 e imprimir los números que son divisibles entre 3
#ejemplo de ejecución: 0, 3, 6, 9
print('Rango de 0 a 10 con números divisibles por 3')
for i in range(11):
    if(i%3 == 0):
        print(i)

#ejercicio 2
#crear un rango con números de 2 a 6 e imprimirlos
#ejemplo de ejecución: 2,3,4,5,6
print('Rango con valores de inicio en 2 y fin en 6')
rango = range(2,7)
for i in rango:
    print(i)

#ejercicio 3
#crear un rango de 3 a 10 con incremento de 2 en 2 (y no de 1 en 1)
#ejemplo de ejecución: 3,5,7 y 9
print("Rango con valor de inicio en 3 y fin en 10 con iterador de 2 en 2") 
for i in range(3,11,2):
    print(i)