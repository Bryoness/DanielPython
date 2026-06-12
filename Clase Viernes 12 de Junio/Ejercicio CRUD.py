#Crear un diccionario de lo que usted prefiera
#Debe tener la menos 3 propiedades

juegos={
    1:{"Nombre": "Age of Empires II: Definitive Edition", "Estreno": 2019, "Género Principal": "Estrategia en Tiempo Real", "Desarrollador": "World's Edge"},
    2:{"Nombre": "Hollow Knight: Silksong", "Estreno": 2025, "Género Principal": "Metroidvania", "Desarrollador": "Team Cherry"},
    3:{"Nombre": "Stellaris", "Estreno": 2016, "Género Principal": "Estrategia en Tiempo Real", "Desarrollador": "Paradox Studios"},
    4:{"Nombre": "Divinity: Original Sin II", "Estreno": 2017, "Género Principal": "Rol", "Desarrollador": "Larian Studios"},
    5:{"Nombre": "Mini Metro", "Estreno": 2015, "Género Principal": "Puzzle", "Desarrollador": "Dinosaur Polo Club"},
    6:{"Nombre": "Left 4 Dead 2", "Estreno": 2018, "Género Principal": "Disparos en Primera Persona", "Desarrollador": "Valve"},
}

def AgregarJuego():
    print("¿Cual es el nombre del juego?")
    nombre = input()
    print("¿Cuál es el año de estreno?")
    estreno = int(input())
    print("¿Cuál es el género principal?")
    generoprincipal=int(input())
    print("¿Cuál es el Desarrollador?")
    desarrollador=input()
    nuevoKey=list(juegos.keys())
    nuevoKey.sort()
    juegos[nuevoKey[-1]+1]= {"nombre": nombre, "Estreno": estreno}


def MostrarProducto():
    for key, nombre in juegos.items():
        print(f"{key}.- {nombre}")

def eliminarProducto():
    MostrarProducto()
    try:
        borrar=int(input("¿Cual juego borrará?: "))
        if borrar in juegos.keys():
            del juegos[borrar]
        else:
            print("Producto no existe")
    except Exception as error:
        print("Error: ", error)     

def actualizarProducto():
    MostrarProducto()
    try:
        num=int(input("¿Que juego desea actualizar?: "))
        if num in juegos.keys():
            print("¿Cual es el nombre del juego?")
            nombre = input()
            print("¿Cuál es el año de estreno?")
            estreno = int(input())
            print("¿Cuál es el género principal?")
            generoprincipal=int(input())
            print("¿Cuál es el Desarrollador?")
            desarrollador=input()
            nuevoKey=list(juegos.keys())
            nuevoKey.sort()
            juegos[nuevoKey[-1]+1]= {"nombre": nombre, "Estreno": estreno}            
        else:
            print("El producto no existe")
    except Exception as error:
        print("Error: ", error)        
