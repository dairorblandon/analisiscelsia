import random

def generarDatos():
    datos =[]
    for i in range  (5000):
        dato={}
        id=random.randint(1,10000)
        referencia=random.choice(["ach01","ach02","ach03"])
        marca= random.choice(["sony","rico","kalley"])
        capacidad=random.randint(100, 200)
        ciudad=random.choice(["medellin,","bolombolo","yolombo","bello","caucacia"])
        responsable=random.choice(["jaime","carlos","rosa","luzma","jairo"])

        dato=[id,referencia,marca,capacidad,ciudad,responsable]

        datos.append(dato)

    return datos

print(generarDatos())    