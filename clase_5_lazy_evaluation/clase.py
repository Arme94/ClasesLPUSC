'''
    lazy evaluation (Programacion perezosa) / funciones generadoras

'''

# funcion impaciente para generar una lista  de n multiplos de m:
def mult(n, m):
    #mults = [ i * m for i in range(n)]
    mults = [ n for n in range(n+1) if n%m == 0]
    return mults

def mult_lazy (n, m):
    num = 0
    # while n > 0:
    #     if num % m == 0:
    #         yield num
    #         n -= 1
    #     num += 1
    while True:
        if num % m == 0:
            yield num
        num += 1

m = int(input("Ingrese m: "))
n = int(input("Ingrese el numero de terminos: "))

mults = mult(n, m)
gen_mults = mult_lazy(n, m)

first_100 = [next(gen_mults) for _ in range(100)]
print(f"primeros 100: \n{first_100}")
next_100 = [next(gen_mults) for _ in range(100)]
print(f"siguientes 100: \n{next_100}")

print(mults)
