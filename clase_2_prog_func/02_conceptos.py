
def op1(a,b):
    return a+b

def op2(a,b):
    return a*b

def op3(a,b):
    return a**b

def op4(a,b):
    return a-b

operacion = input("Que operacion desea realizar? 1-Suma, 2-Resta, 3-Multiplicación 4-Potencia: ")

val1 = int(input("Ingrese el primer valor: "))
val2 = int(input("Ingrese el segundo valor: "))

if operacion == "1":
    f = op1
elif operacion == "2":
    f = op4
elif operacion == "3":
    f = op2
elif operacion == "4":
    f = op3
else:
    print("Funcion no definida")

print(f"El resultado es: {f(val1,val2)}")