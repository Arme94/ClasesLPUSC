# ejercicio 1:
from math import factorial
from functools import reduce

def map_func(x,n):
    return x**n/factorial(n)

num_x = int(input("Ingrese el valor de x: "))
num_terminos = int(input("Ingrese el número de términos: "))

list_aux = list(range(0,num_terminos+1))
list_num = list(map(lambda x: map_func(num_x,x), list_aux))

suma = reduce(lambda x,y: x+y, list_num)
print(f"el valor de e^{num_x} es {suma}")