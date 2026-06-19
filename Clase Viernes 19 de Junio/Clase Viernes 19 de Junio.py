# notas=[4.6, 7.0, 3.4, 6.6, 3.9]

# #Crear una funcion para poder pasarla la lista
# #como parámetro y mostrar el promedio
# #mostrar si aprueba o reprueba

# def sumarnotas(lst):
#     sumanotas=0
#     cantidadnotas=0
#     for nota in lst:
#         sumanotas+=nota
#         cantidadnotas+=1
#     print(f"El promedio de sus notas es: {sumanotas/cantidadnotas}")

# sumarnotas(notas)        

# #Como lo hizo el profesor
# def calculaProm(n):
#     return round(sum(n)/len(n), 1)
# print("El promedio es ", calculaProm(notas))


# print(max(notas))
# print(min(notas))

peliculas=[
    {"titulo": "Inception", "director": "Christopher Nolan",
     "genero": "Ciencia Ficcion", "estreno": 2010 },
    {"titulo": "Jurassic Park", "director": "Steven Spielberg",
     "genero": "Ciencia Ficcion", "estreno": 1993 },
    {"titulo": "Se7en", "director": "David Fincher",
     "genero": "Thriller", "estreno": 1997 },

]




#crear un gestor de peliculas
#El titulo debe tener más de 2 carácteres
#El año debe ser mayor a 1960 y debe ser menor al año actual
#El director debe tener nombre y apellido
#Mostrar el siguiente menú
#
'''
1.- ingresar Película
2.- quitar Película
3.- Actualizar Película
4.- Mostar Película
5.- Mostrar solo los titulos
6.- Ordenar de mas reciente a mas antigua
7.- Salir
'''
def MostrarPeliculas():
    c=1
    for pelicula in peliculas:
        print(f"{c}.- {pelicula}")
        c+=1
        print(" ")

def IngresarPelicula():
    titulo=input("Ingrese el título de la película a ingresar: ")
    while titulo==" " or len(titulo)<2:
        print("Título no puede ser vacío ni tener menos de 2 caracteres")
        titulo=input("Ingrese el título de la película a ingresar: ")
    director=input("Ingrese el director de la pelicula a ingresar: ")
    genero=input("Ingrese el género de la película a ingresar: ")
    estreno=int(input("Ingrese el año de estreno de la película a ingresar: "))
    peliculas.append({"Título": titulo, "Director": director, 
        "Género":genero, "Estreno": estreno})
    print("")

def QuitarPelicula():
    MostrarPeliculas()
    eliminar=int(input("¿Que entrada de película desea eliminar?: "))
    peliculas.pop(eliminar-1)
    print("Entrada eliminada.")
    print("")

def ActualizarPelicula():
    MostrarPeliculas()
    entrada=int(input("¿A qué película se le actualizarán los datos? Indique la entrada: "))
    titulo=input("Ingrese el título de la pelicula a actualizar: ")
    director=input("Ingrese el director de la pelicula a actualizar: ")
    genero=input("Ingrese el género de la película a actualizar: ")
    estreno=int(input("Ingrese el año de estreno de la película a ingresar: "))
    peliculas[entrada-1]={"titulo": titulo, "director": director, "genero": genero, "estreno": estreno}
    print("")

def TitulosPeliculas():
    for pelicula in peliculas:
        print(pelicula["titulo"])
        print("")

def MenuPeliculas():
    while True:
        try:
            print("Menú Principal")
            print("1.- Ingresar Película")
            print("2.- Quitar Película")
            print("3.- Actualizar Película")
            print("4.- Mostar Película")
            print("5.- Mostrar solo los titulos")
            print("6.- Ordenar de mas reciente a mas antigua")
            print("7.- Salir")
            op=int(input("Ingrese el número de la opción: "))
            match op:
                case 1:
                    IngresarPelicula()
                case 2:
                    QuitarPelicula()
                case 3:
                    ActualizarPelicula()
                case 4:
                    MostrarPeliculas()
                case 5:
                    TitulosPeliculas()
                case 6:
                    print("")
                case 7:
                    print("Saliendo del sistema")
                    break
                case _:
                    print("Opción Inválida")
        except Exception as error:
            print("Error: ", error)

MenuPeliculas()            