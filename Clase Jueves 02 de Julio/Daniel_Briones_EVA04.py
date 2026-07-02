productos=[
    {"nombre": "pan" , "stock": "25", "precio":"1200.0", "estado": "DISPONIBLE"},
    {"nombre": "sal" , "stock": "0", "precio":"350.0", "estado": "SIN STOCK"}
    ]

#Datos que debe manejar el sistema
#"nombre" "stock" "precio" "disponible"
#Opción 1 - Agregar producto:
#Opción 2 - Buscar producto:
#Opción 3 - Eliminar producto:
#Opción 4 - Actualizar disponibilidad:
#Opción 5 - Mostrar productos:
#Opción 6 - Salir:

def verificarNumero():
    while True:
        try:
            num=int(input("Ingrese un número: "))
            if num<0:
                print("debe ingresar un número mayor o igual a 0")
            else:
                return num
        except Exception as e:
            print("Solo numeros enteros positivos")


def MostrarProductos():
    if len(productos)<1:
        print("No hay productos para mostrar")
    else:    
        c=1
        for nombre in productos:
            print(f"{c}.- {nombre}")
            c+=1

def AgregarProducto():
    nombre=input("Ingrese el nombre del producto a agregar: ")
    while nombre==" " or len(nombre)<1:
        print("El nombre del producto no puede estar vacío")
        nombre=input("Ingrese el nombre del producto a agregar: ")
    stock=int(input("Ingrese el stock del producto: "))
    while stock<0:
        print("Error al ingresar el stock")
        print("El stock debe ser un número entero mayor o igual que cero")
        stock=int(input("Ingrese el stock del producto: "))   
    precio=float(input("Ingrese el precio del producto. El precio debe ser un número decimal mayor que cero: "))
    while precio<0:
        print ("Error al ingresar el precio")
        precio=float(input("Ingrese el precio del producto. El precio debe ser un número decimal mayor que cero: "))
    productos.append({"nombre": nombre, "stock": stock, "precio": precio, "estado": False})
    print("Producto agregado")

def BuscarProducto():
    nombre=input("Ingrese el producto a buscar: ")
    for i in productos:
        if productos==nombre:
            print("Producto encontrado")
            print(productos[nombre])
            return 1
    print("Producto no encontrado")
    return -1

def EliminarProducto():
    MostrarProductos()
    eliminar=int(input("¿Qué entrada de producto desea eliminar?: "))
    productos.pop(eliminar-1)
    print("Entrada eliminada")

def ActualizarDisponibilidad():
    MostrarProductos()
    entrada=int(input("¿Qué entrada desea actualizar?: "))
    print("1.- Nombre")
    print("2.- Stock")
    print("3.- Precio")
    print("4.- Estado")
    dato=int(input("¿Qué valor desea actualizar?: "))
    nuevovalor=input
    if dato==1:
        nuevovalor=input("Ingrese el nombre actualizado: ")
        productos[entrada-1]["nombre"]=nuevovalor
    elif dato==2:
        nuevovalor=input("Ingrese el stock actualizado: ")
        productos[entrada-1]["stock"]=nuevovalor
    elif dato==3:
        nuevovalor=input("Ingrese el precio actualizado: ")
        productos[entrada-1]["precio"]=nuevovalor    
    elif dato==4:
        nuevovalor=input("Ingrese el estado actualizado: ")
        productos[entrada-1]["estado"]=nuevovalor
    else:
        print("Dato Inválido")

def MenuProductos():
    while True:
        try:
            print("========== MENÚ PRINCIPAL ==========")
            print("1. Agregar producto")
            print("2. Buscar producto")
            print("3. Eliminar producto")
            print("4. Actualizar disponibilidad")
            print("5. Mostrar productos")
            print("6. Salir")
            print("=====================================")
            op=int(input("¿Qué desea hacer?: "))
            match op:
                case 1:
                    AgregarProducto()
                case 2:
                    BuscarProducto()
                case 3:
                    EliminarProducto()                
                case 4:
                    ActualizarDisponibilidad()
                case 5:
                    MostrarProductos()
                case 6:
                    print("Gracias por usar el sistema. Vuelva Pronto")
                    break
                case _:
                    print("Opción Inválida")                                

        except Exception as error:
            print("Error ", error)    

MenuProductos()
