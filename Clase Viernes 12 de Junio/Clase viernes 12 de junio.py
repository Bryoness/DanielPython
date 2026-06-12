# # uso y eplicacion de diccionarios

# alumno={
#     "nombre":"Shinji Ikari",
#     "edad": 14,
#     "carrera":"piloto"
# }

# print(alumno)
# print(alumno["carrera"])

# for key ,value in alumno.items():
#     print(f"{key}= {value} ")
# print("---Cambios de datos---")
# # for dato ,valor in alumno.items():
# #     print(dato, valor )
# alumno["email"]="shinji@nerv.com"
# alumno["carrera"]="escritor"
# del alumno["edad"]
# for key ,value in alumno.items():
#     print(f"{key}= {value} ")

# productos={
#     1:{"nombre": "Control Inalambrico",
#        "categoria": "Electronica",
#        "precio": 45000},
#     2:{"nombre": "Pilas Recargables",
#        "categoria": "Insumos",
#        "precio": 5000},
#     3:{"nombre": "Pasta Termica",
#        "categoria": "Computacion",
#        "precio": 7000},
# }

# print(productos[1]["nombre"])

# '''
# Crear un diccionario de trabajadores 
# '''

# ##CRUD DE VEGETALES

# vegetales={
#    1:"Maracuyá",2:"Pera",3:"Cebolla",7:"Papa"
# }

# print(list(vegetales.keys()))[-1]


# def agregarVegetales():
#    print("-"*20)
#    agregar=input("Ingrese un vegetal: ")
#    nuevoKey=list(vegetales.keys())[-1]
#    vegetales[nuevoKey+1]=agregar
# def mostrarVegetales():
#    print("-"*40)
#    for num, nombre in vegetales.items():
#          print(f"{num}.- {nombre} ")
# def eliminarVegetal():
#    mostrarVegetales()
#    borrar=int(input("Cual vegetal borrará?: "))
#    del vegetales[borrar]
# def actualizarVegetal():
#    mostrarVegetales()
#    act=int(input("Cual vegetal actualizará?: "))
#    vegetales[act]=input("Ingrese nuevo nombre: ")

# def vegetalesMenu():
#    while True:
#       try:
#          print("-"*20)
#          print("1.- Agregar Vegetal")
#          print("2.- Eliminar Vegetal")
#          print("3.- Actualizar Vegetal")
#          print("4.- Mostrar Vegetal")
#          print("5.- Salir")
#          op=int(input("Seleccione una opcion: "))
#          match op:
#                case 1:
#                   agregarVegetales()
#                case 2:
#                   eliminarVegetal()
#                case 3:
#                   actualizarVegetal()
#                case 4:
#                   mostrarVegetales()
#                case 5:
#                   print("Salir")
#                   break
#                case _:
#                     print("Opcion invalida")  
#       except Exception as e:
#          print("Error:",e)

# vegetalesMenu()

##Diccionario con diccionarios
productosDicc={
   1:{"nombre": "Maracuyá", "precio": 3000},
   2:{"nombre": "Pera", "precio": 1500},
   3:{"nombre": "Cebolla", "precio": 1200}
}

productosDicc[4]={"nombre": "Piña", "precio": 3500}

# print(productosDicc.keys())
# print(list(productosDicc.keys())[-1]+1)
# print(productosDicc.values())
# print(productosDicc.items())

# total=0
# for p in productosDicc.values():
#     total=total+p["precio"]
# print(f"El total es {total}")

'''
En un diccionario hay pares de datos. Hay tipos de datos, como strings, boolean, o diccionarios. 
Cada par dentro de un diccionario tiene 2 componentes, los Keys que indican la posición dentro del diccionario (ej 1, 2, 3, etc)
Y los values, que pueden ser strings, true or false, etc.
El conjunto de key + value se le conoce como item.

'''

def agregarProducto():
   print("Cual es el nombre del producto?")
   nombre = input()
   print("cual es el precio?")
   precio = int(input())
   nuevoKey=list(productosDicc.keys())
   nuevoKey.sort()
   productosDicc[nuevoKey[-1]+1]= {"nombre": nombre, "precio": precio}

'''
Para poder agregar un producto, se necesita un índice nuevo. En un diccionario, los índices no se ajustan al eliminar o añadir.
En las listas sí se ajustan.
En diccionarios, es conveniente buscar el último número disponible y añadirle 1 para crear un nuevo disponible.

'''
def MostrarProducto():
    for key, producto in productosDicc.items():
        print(f"{key}.- {producto}")

def eliminarProducto():
    MostrarProducto()
    try:
        borrar=int(input("Cual Producto borrará?: "))
        if borrar in productosDicc.keys():
            del productosDicc[borrar]
        else:
            print("Producto no existe")
    except Exception as error:
        print("Error: ", error)     
def actualizarProducto():
    MostrarProducto()
    try:
        num=int(input("Que producto desea actualizar?: "))
        if num in productosDicc.keys():
            nombre=input("Cual es el nombre nuevo?: ")
            precio=int(input("Cual es el precio nuevo?: "))
            productosDicc[num]={"nombre": nombre, "precio": precio}
        else:
            print("El producto no existe")
    except Exception as error:
        print("Error: ", error)        
# print(productosDicc[2]["precio"])  # precio de la pera
# print(productosDicc[3]["nombre"])  # nombre de la cebolla



# # for num, veg in productosDicc.items():
# #     print(f"{num}.- {veg}")

# ##Lista con diccionarios
# productosList=[
#    {"nombre": "Maracuyá", "precio": 3000}, #0
#    {"nombre": "Pera", "precio": 1500},     #1  
#    {"nombre": "Cebolla", "precio": 1200}   #2
# ]

# print(productosList[2]["precio"]) #precio de la cebolla
# print(productosList[0]["nombre"]) #nombre de la naracuya

carrito=[]
pagar=0
def comprar():
    while True:
        MostrarProducto()
        try:
            compra = int(input("Ingrese el producto a comprar. Presione 0 para salir"))
            if compra==0:
                break  
            if compra in productosDicc.keys():
                carrito.append(productosDicc[compra])
                print(f"Producto agregado al carrito")
        except Exception as error:
            print("Error: ", error)

def boleta():
    total=0
    MostrarProducto()
    print("-"*30, "0", "-"*30)
    for prod in carrito:
        print(f"{prod["nombre"]}__${prod["precio"]}")
        total+=prod["precio"]
    print("-"*30, "0", "-"*30)
    print(f"El total neto es {total} y el IVA es {total*0.19}")
    print(f"El total a pagar es {total*1.19}")
    print(f"Gracias por venir al Minimarket")       

def vegetalesMenuDiccionario():
   while True:
      try:
         print("-"*20)
         print("1.- Agregar Vegetal")
         print("2.- Eliminar Vegetal")
         print("3.- Actualizar Vegetal")
         print("4.- Mostrar Vegetal")
         print("5.- Comprar")
         print("6.- Crear Boleta y Salir")
         op=int(input("Seleccione una opcion: "))
         match op:
               case 1:
                  agregarProducto()
               case 2:
                  eliminarProducto()
               case 3:
                  actualizarProducto()
               case 4:
                  MostrarProducto()
               case 5:
                  comprar()
               case 6:
                  boleta()
                  break
               case _:
                    print("Opcion invalida")  
      except Exception as e:
         print("Error:",e)
vegetalesMenuDiccionario()

# #Cambiar la funcion actualizar para que solo 
# # actualice una solo key 
# # Ademas, crear un CRUD pero con la lista 
# # de diccionarios.
