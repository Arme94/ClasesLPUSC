
val1 = int(input("Ingrese el primer valor: "))
val2 = int(input("Ingrese el segundo valor: "))

operaciones = [lambda a,b: a+b, lambda a,b: a-b, lambda a,b: a*b, lambda a,b: a**b]
list(map(lambda x: print(f"El resultado es: {x(val1,val2)}"), operaciones))
