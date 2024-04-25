''' Notas de clase
1) funciones son ciudadanos de 1er orden
    -> funciones de orden superior
        - pueden recibir funciones como argumentos
        - pueden retornar funciones
    -> fnciones puras (inmuutabilidad) -> evitar efectos colaterales
        - variables globales, atribuutos de clase (no se deben usar)
        - Inmutabilidad gracias a transparencia referencial
        
Fuunciones orden superior: ejercicios con map y filter
'''

# Ejemplo de funciones de orden superior

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
    print(f"El resultado es: {op1(val1,val2)}")
elif operacion == "2":
    print(f"El resultado es: {op4(val1,val2)}")
elif operacion == "3":
    print(f"El resultado es: {op2(val1,val2)}")
elif operacion == "4":
    print(f"El resultado es: {op3(val1,val2)}")
else:
    print("Funcion no definida")