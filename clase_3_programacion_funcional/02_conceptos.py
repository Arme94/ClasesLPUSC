def concat(x,y):
    return x+" "+y

lista_palabras = ["muchos","años","despues","frente","al","peloton","de","fusilamiento","el","coronel","Aureliano","Buendia"]

texto = reduce(lambda x,y: " ".join([x,y]), lista_palabras)
print(texto)
