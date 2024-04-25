'''
Una lista de registros
[
    {
        "nombre":"sebastian",
        "notas":[5.0,3.5,4,7],
        "edad": 24
    },
    {
        "nombre":"Valentina",
        "notas":[3.0,3.8,4.3],
        "edad": 25
    }
]
utilizando map, filters y reduce

- calcular promedio de cada estudiante con el map
- filtrar estudiantes con edad > N
- promedio general con reduce
'''

from functools import reduce
from random import uniform

def get_data_set():
    return [
        {
            "nombre":"sebastian",
            "notas":get_notas(),
            "edad": 24
        },
        {
            "nombre":"Valentina",
            "notas":get_notas(),
            "edad": 25
        },
        {
            "nombre":"Juan",
            "notas":get_notas(),
            "edad": 26
        },
        {
            "nombre":"Maria",
            "notas":get_notas(),
            "edad": 27
        },
        {
            "nombre":"Carlos",
            "notas":get_notas(),
            "edad": 28
        },
        {
            "nombre":"Andres",
            "notas":get_notas(),
            "edad": 29
        },
        {
            "nombre":"Luis",
            "notas":get_notas(),
            "edad": 30
        },
        {
            "nombre":"Sofia",
            "notas":get_notas(),
            "edad": 31
        },
        {
            "nombre":"Valeria",
            "notas":get_notas(),
            "edad": 32
        },
        {
            "nombre":"Catalina",
            "notas":get_notas(),
            "edad": 33
        }
    ]

def get_notas():
    return [round(uniform(1.0,5.0),1) for _ in range(3)]

def promedio_notas(registro):
    promedio = round(reduce(lambda x,y: x+y, registro["notas"])/len(registro["notas"]),1)
    return {"nombre":registro["nombre"],"promedio":promedio}

def filtro_edad(registro,edad):
    return registro["edad"]>edad

def promedio_general(acumulado,registro):
    return round(acumulado+registro["promedio"],1)

def print_promedios(promedios):
    print("Nombre\t\tPromedio")
    print("------\t\t--------")
    list(map(lambda x: print(f"{x['nombre']}{calculate_tabs(x,'nombre')}{x['promedio']}"), promedios))

def calculate_tabs(x, prop):
    if len(x[prop])>7:
        return "\t"
    else:
        return "\t\t"

def print_filter(filtro):
    print("Nombre\t\tEdad\t\tNotas")
    print("------\t\t--------\t\t------")
    list(map(lambda x: print(f"{x['nombre']}{calculate_tabs(x,'nombre')}{x['edad']}\t\t{x['notas']}"), filtro))

### Main
exit = False
while not exit:
    print("1. Promedio de cada estudiante")
    print("2. Filtrar estudiantes con edad > N")
    print("3. Promedio general")
    print("4. Salir")
    opcion = input("Seleccione una opción: ")

    lista_registros = get_data_set()
    if opcion == "1":
        print("---------------------------------")
        print("Promedio de cada estudiante")
        print("---------------------------------")
        promedios = list(map(lambda x: promedio_notas(x), lista_registros))
        print_promedios(promedios)
        print("---------------------------------")
    elif opcion == "2":
        print("---------------------------------")
        print("Filtrar estudiantes con edad > N")
        print("---------------------------------")
        edad = int(input("Ingrese la edad: "))
        filtro = list(filter(lambda x: filtro_edad(x,edad), lista_registros))
        print(f"Estudiantes con edad mayor a {edad}:")
        print_filter(filtro)
        print("---------------------------------")
    elif opcion == "3":
        print("---------------------------------")
        promedios = list(map(lambda x: promedio_notas(x), get_data_set()))
        prom_general = round(reduce(lambda x,y: x+y, list(map(lambda x: x["promedio"], promedios)))/len(promedios),1)
        print(f"Promedio general de todos los estudiantes es: {prom_general}")
        print("---------------------------------")
    elif opcion == "4":
        print("---------------------------------")
        print("Gracias por usar el programa")
        print("Saliendo...")
        print("---------------------------------")
        exit = True
    else:
        print("Opción no válida")