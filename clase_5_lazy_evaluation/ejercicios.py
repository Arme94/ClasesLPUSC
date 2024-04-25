'''
    1 - e^x = 1 + x / 1! + x^2 / 2! + x^3 / 3! + ... + x^n / n!
'''

from math import factorial
from decimal import Decimal

def euler(n, x):
    result = 1
    for i in range(1,n):
        result += x**i/factorial(i)
    return result

def euler_lazy(n, x):
    result = 1
    for i in range(1,n):
        result += Decimal(x**i)/Decimal(factorial(i))
        yield result

x = int(input("Ingrese el valor de x: "))
n = int(input("Ingrese el número de términos: "))

gen_euler = euler_lazy(n, x)
euler_lazy_first_10 = [next(gen_euler) for _ in range(40)]
print(euler_lazy_first_10[-1])
euler_lazy_next_10 = [next(gen_euler) for _ in range(10)]
print(euler_lazy_next_10[-1])
euler_lazy_next_10 = [next(gen_euler) for _ in range(10)]
print(euler_lazy_next_10[-1])
euler_lazy_next_10 = [next(gen_euler) for _ in range(10)]
print(euler_lazy_next_10[-1])

#print(euler_lazy_next_10)
# euler = euler(n, x)

# print(f"El valor de e^{x} es {euler}")