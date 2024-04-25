#CodeForces 236A 
#numero de caracteres distintos de una cadena
#si es par, contraseña inseguara
#si es impar, contraseña segura

def num_caracteres_distintos_rec(cadena):
    if not cadena:
        return 0
    else:
        head, *tail = cadena
        if head in tail:
            return num_caracteres_distintos_rec(tail)
        else:
            return 1 + num_caracteres_distintos_rec(tail)

cadena = input("Ingrese la cadena a comprobar: \n")

num_dist = num_caracteres_distintos_rec(cadena)

if (num_dist % 2) == 0:
    print("Contraseña insegura")
else:
    print("Contraseña segura")
 