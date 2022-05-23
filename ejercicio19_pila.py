from pila import Pila 

pila1=Pila()

class Pelicula():
    titulo, estudio_cinematografico, anio = None, None, None

titulos = ["la leyenda de Tarzan", "Bumblebee", "Hercules", "Rapido y furioso", "Capitan America: The Winter soldier", "Creed II", "Capitan America:Civil War"]
estudios_cinematograficos = ["Warner Bros", "Paramount","Paramount", "Universal", "Marvel", "Warner Bros", "Marvel"]
anio_estreno = ['2016', '2018', '2014', "2013", "2014", "2018", "2016"]

for i in range(len(titulos)):
    dato = Pelicula()
    dato.titulo = titulos[i]
    dato.estudio_cinematografico = estudios_cinematograficos[i]
    dato.anio = anio_estreno[i]
    print(dato.titulo, dato.estudio_cinematografico, dato.anio)
    pila1.apilar(dato)

aux=0
while (not pila1.pila_vacia()):
    dato=pila1.desapilar()
    if dato.anio=="2014":
        print (dato.titulo, " fue estrenada en el año 2014")
    if dato.anio=="2018":
        aux +=1
    if dato.estudio_cinematografico=="Marvel" and dato.anio=="2016":
        print(dato.titulo, "pelicula de Marvel estrenada en el 2016")
print("Cantidad de peliculas estrenadas en el 2018: ", aux)


