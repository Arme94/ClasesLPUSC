#estados_conserv = Malo, Bueno, excelente
from functools import reduce

records = [
        { 
            "nombre":"panamamericano",
            "area": 200,
            "especies_a": [
                {
                    "nombe": "iguuana",
                    "ejemplares": 200
                },
                {
                    "nombe": "garzas",
                    "ejemplares": 500
                }
            ],
            "estado_conserv": "Bueno"
        },
        { 
            "nombre":"lago de la babilla",
            "area": 200,
            "especies_a": [
                {
                    "nombe": "babilla",
                    "ejemplares": 8
                },
                {
                    "nombe": "garzas",
                    "ejemplares": 100
                }
            ],
            "estado_conserv": "Bueno"
        }
    ]

'''
Calcuular usando map, reduce, filter:
area total de los humedales
filtrar humedales con un total de ejemplares animales > 150
promedio de numero de ejemplares de los humedales
'''

def area_total_hum(records_humedales):
    area_total = reduce(lambda x,y: x["area"] + y["area"], records_humedales)
    return area_total

def total_ejemplares(humedal):
    especies = humedal["especies_a"]
    total_ejem = reduce(lambda x,y: x["ejemplares"]+y["ejemplares"], especies)
    return total_ejem

def prom_num_ejem_hum(records):
    prom = reduce(lambda x,y: total_ejemplares(x) + total_ejemplares(y), records)/len(records)
    return prom

print("Area total: ", area_total_hum(records), "\n")

list_filter = list(filter(lambda x: total_ejemplares(x) > 150, records))
print("Humedales con total ejemplares animales > 150: \n", list_filter, "\n")

print("Promedio numero de ejemplares: \n", prom_num_ejem_hum(records))


