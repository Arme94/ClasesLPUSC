
operacion = input("Que operacion desea realizar? 1-Suma, 2-Resta, 3-Multiplicación 4-Potencia: ")

val1 = int(input("Ingrese el primer valor: "))
val2 = int(input("Ingrese el segundo valor: "))

operaciones = [lambda a,b: a+b, lambda a,b: a-b, lambda a,b: a*b, lambda a,b: a**b]

if operacion != "1" and operacion != "2" and operacion != "3" and operacion != "4":
    print("Funcion no definida")
else:
    operaciones = list(map(lambda x: x(val1,val2), operaciones))
    print(f"El resultado es: {operaciones[int(operacion)-1]}")
