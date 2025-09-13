from functools import reduce

lista = [1,2,3,4,5,6,7,8,9,10]

#Usando map
cuadrados = list(map(lambda x: x**2, lista))
print("Cuadrados de la lista:", cuadrados)

#Usando filter
pares = list(filter(lambda x: x % 2 == 0, lista))
print("Números pares:", pares)

#La suma de [1..10]
suma_lista = reduce(lambda x, y: x + y, lista)
print("Suma de la lista [1..10] =", suma_lista)

#El producto de [1..5]
producto_lista = reduce(lambda x, y: x * y, [1,2,3,4,5])
print("Producto de la lista [1..5] =", producto_lista)