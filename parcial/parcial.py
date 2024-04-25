'''
Este examen evalúa los conceptos básicos de programación funcional en Python vistos en clase, a saber:

funciones de orden superior
funciones puras
funciones lambda
recursión sobre listas
evaluación perezosa y funciones generadoras
Procedimiento:

la criba de Eratóstenes es una técnica algorítmica clásica usada para encontrar los números primos en un determinado rango y fue planteado por el matemático griego Eratóstes en el siglo III a.C., y funciona de la siguiente manera:

se crea una lista de números enteros desde 2 hasta un límite N dado por el usuario
el algoritmo empieza con el 2, el primer número primo
se van "tachando" todos los múltiplos de este número, excepto él mismo (en este caso, los múltiplos de 2, excepto el 2)
se avanza al siguiente número en la lista que no ha sido "tachado", y se parte desde este número primo, desde el paso 2

- Se repite hasta que queden solo números entre 2 y N sin tachar, los números primos
Implemente una función generadora en Python que vaya devolviendo números primos de forma perezosa, usando el método de eratóstenes.
- El algoritmo puede  ser recursivo y debe usar evaluación perezosa en lo posible
- Puede usar funciones map, filter y las de orden superior que considere necesarias dentro de la función generadora.
- Puede usar la siguiente prueba de primalidad en Python
'''

def is_prime(n):
    return len(list(filter(lambda x: n % x == 0, range(2, n)))) == 0

def _criba_eratostenes(n, i, primos):
    if i == 2:
        return _criba_eratostenes(n, i+1, primos)
    elif i > n:
        return primos
    else:
        if is_prime(i):
            primos.append(i)
        return _criba_eratostenes(n, i+1, primos)

def criba_eratostenes(n):
    return _criba_eratostenes(n, 2, [2])

def criba_eratostenes_lazy(n):
    i = 2
    while i <= n:
        if is_prime(i):
            yield i
        i += 1

def criba_erostatenes_lazy_vlist(n):
    i = 2
    primos = []
    while i <= n:
        if is_prime(i):
            primos.append(i)
        i += 1
        yield primos


n = int(input("Select the number n: "))

# primos = criba_eratostenes(n)
# print(primos)

gen_primos = criba_eratostenes_lazy(n)
first_10 = [next(gen_primos) for _ in range(10)]
print(f"primeros 10: \n{first_10}")
next_10 = [next(gen_primos) for _ in range(10)]
print(f"siguientes 10: \n{next_10}")