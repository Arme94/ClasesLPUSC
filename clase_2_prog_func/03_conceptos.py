
operacion = input("Que operacion desea realizar? 1-Suma, 2-Resta, 3-Multiplicación 4-Potencia: ")

val1 = int(input("Ingrese el primer valor: "))
val2 = int(input("Ingrese el segundo valor: "))

if operacion == "1":
    f = lambda a,b: a+b
elif operacion == "2":
    f = lambda a,b: a-b
elif operacion == "3":
    f = lambda a,b: a*b
elif operacion == "4":
    f = lambda a,b: a**b
else:
    print("Funcion no definida")

print(f"El resultado es: {f(val1,val2)}")