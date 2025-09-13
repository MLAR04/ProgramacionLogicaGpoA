""" Juan Antonio Roman Castro Práctica 3 
    Manipulación de listas              """
from functools import reduce

def lista():
    desarreglada = [1,2,3,4,5,6,7,8,9,10]
    print(f"Dada la lista {desarreglada}")
    boeponja = list(map(lambda i: i*i, desarreglada))
    print(f"Lista elevada al cuadrado: {boeponja}")
    nopar = list(filter(lambda i: i%2 != 0, desarreglada))
    print(f"Lista excluyendo los pares: {nopar}")
    sumita = reduce(lambda x, y: x+y, desarreglada)
    print(f"Suma del contenido de la lista: {sumita}")
    productito = reduce(lambda x, y: x*y, desarreglada[:5])
    print(f"Producto hasta el 5.º elemento de la lista: {productito}")
    
        
if __name__ == "__main__":
    lista()