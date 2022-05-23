from pila import Pila
pila1=Pila()

class personajes_de_marvel():
    nombre, cant_peliculas= None, None
nombres=["Clint Barton", "Groot", "Rocket Raccoon", "Falcon", "Viuda Negra", "Deadpool"]
cantidad_peliculas=[6, 2, 4, 8, 2, 5]

for i in range (len(nombres)):
    dato=personajes_de_marvel()
    dato.nombre=nombres[i]
    dato.cant_peliculas=cantidad_peliculas[i]
    print(dato.nombre, dato.cant_peliculas)
    pila1.apilar(dato)
cont1=0
vec=[]
while (not pila1.pila_vacia()):
    dato=pila1.desapilar()
    cont1 += 1
    if dato.nombre == "Rocket Raccoon":
        aux1=cont1
    elif dato.nombre=="Groot":
        aux2=cont1
    if dato.cant_peliculas >5:
        print(dato.nombre, " participo en mas de 5 peliculas.")
        print("participo en: ", dato.cant_peliculas, " peliculas.")
    if dato.nombre=="Viuda Negra":
        print("La Viuda Negra participo en ", dato.cant_peliculas, " peliculas.")
    if dato.nombre[0]=="C" or dato.nombre[0]=="D" or dato.nombre[0]=="G":
        vec.append(dato.nombre)

print("Rocket Raccoon se encuentra en la pocicion ", aux1)
print("Groot se encuentra en la pocicion ", aux2) 
print(vec)   
