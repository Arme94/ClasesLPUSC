def invertir_lista_rec(lista):    
    if not lista:
        return []
    else:
        head, *tail = lista
        return invertir_lista_rec(tail) + [head]

def invertir_cadena_rec(cadena):
    if not cadena:
        return ""
    else:
        head, *tail = cadena
        return invertir_cadena_rec("".join(tail)) + head

def list_fibonacci_rec(n):
    if n == 0:
        return []
    elif n == 1:
        return [1]
    elif n == 2:
        return [1, 1]
    else:
        fibo = list_fibonacci_rec(n-1)
        return fibo + [fibo[-1] + fibo[-2]]
    

lista = [1,2,4,8,9,20,14]
lsita_invertida = invertir_lista_rec(lista)

cadena = "Hello World"
cadena_invertida = invertir_cadena_rec(cadena)

print("lista: ", lista)
print("lista invertida: ", lsita_invertida)

print("cadena: ", cadena)
print("cadena invertida: ", cadena_invertida)

fibo = list_fibonacci_rec(10)
print("fibo", fibo)
