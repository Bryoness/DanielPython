# # ejemplo de manipulacion de datos en una lista
# listado=[3, 6.5, 4, 5,["Link", "Zelda"], {"pkm":"weeddle"}]
# #        0   1   2  3        4                  5

# print(listado[5]["pkm"])# muestra weeddle, por que es el valor del key "pkm"

# for e in listado:
#     print(e)

# listado.append({"dia": "lunes", "temp": 25.7, "humedad":29})
# print("-"*50)
# input()
# for e in listado:
#     print(e)

# # ejemplo de return

# def suma():
#     return 5+7

# print(suma()*4)

# def calculaIVA(neto):
#     return neto*1.19

# print("El valor a pagar sera:" , calculaIVA(2000))


def verificarNumero():
    while True:
        try:
            num=int(input("Ingrese un numero: "))
            if num<0:
                print("debe ingresar un numero mayor o igual a 0")
            else:
                return num
        except Exception as e:
            print("Solo numero enteros positivos")


pinturas=[
    {"color": "verde", "capacidad": 1500, "formato": "tarro"}, #0
    {"color": "azul", "capacidad": 1500, "formato": "tarro"}, #1
    {"color": "blanco", "capacidad": 3500, "formato": "tinaja"}, #2
    {"color": "purpura", "capacidad": 500, "formato": "bolsa"}, #3
]

pinturas2=[
    {"color": "rojo", "capacidad": 1500, "formato": "tarro"}, #0
    {"color": "naranja", "capacidad": 1500, "formato": "tarro"}, #1
    {"color": "negro", "capacidad": 3500, "formato": "tinaja"}, #2
    {"color": "celeste", "capacidad": 500, "formato": "bolsa"}, #3
]

def mostrarPinturas():
    if len(pinturas)<1:
        print("no hay pinturas para mostrar")
    else:
        c=1
        for p in pinturas:
            print(f"{c}.- {p}")
            c+=1
def quitarPintura():
    mostrarPinturas()
    ele=int(input("Que pintura va a eliminar?: "))
    pinturas.pop(ele-1)
def agregarPintura():
    color=input("Que color será?: ")
    capacidad=int(input("Que capacidad será?: "))
    formato=input("Que formato será?: ")
    pinturas.append({"color": color, "capacidad":capacidad, "formato": formato})
def actualizarPintura():
    mostrarPinturas()
    ele=int(input("Que pintura va a actulizar?: "))
    print("1.- Color")
    print("2.- Capacidad")
    print("3.- Formato")
    dato=int(input("Que dato de la pintura va a actulizar?: "))
    nuevoValor=input
    if dato==1:
        nuevoValor=input("Ingrese el nuevo color")
        pinturas[ele-1]["color"]=nuevoValor
    elif dato==2:
        nuevoValor=int(input("Ingrese la nueva capaciadad"))
        pinturas[ele-1]["capacidad"]=nuevoValor
    elif dato==3:
        nuevoValor=input("Ingrese el nuevo formato")
        pinturas[ele-1]["formato"]=nuevoValor
    else:
        print("Dato invalido")
def mayorCap(lista):
    listaCapacidad=[]
    for p in lista:
        listaCapacidad.append(p["capacidad"])
    return max(listaCapacidad)
def menuPinturas():    
    while True:
        try:
            print("-"*60)
            print("1.- Agregar Pintura")
            print("2.- Quitar Pintura")
            print("3.- Actualizar Pintura")
            print("4.- Mostrar Pinturas")
            print("5.- Mostrar mayor capacidad")
            print("9.- Salir")
            op=int(input("Seleccione una opcion: "))
            match op:
                case 1:
                    agregarPintura()
                case 2:
                    quitarPintura()
                case 3:
                    actualizarPintura()
                case 4:
                    mostrarPinturas()  
                case 5:
                    print(f"El recipiente con mayor capacidad tine : {mayorCap(pinturas)}")           
                case 9:
                    print("Saliendo...")
                    break
                case _:
                    print("Opcion invalida")
        except Exception as e:
            print("error: ", e)
    
#menuPinturas()


#Cree una función para buscar un color específico
#Pase la lista como argumento, y el color como segundo argumento
#Retorne "Disponible"
#Si el color existe. "No existe" en caso contrario.

# def Disponibilidad(lista, color):
#     for i in lista:
#         if color == i["color"]:
#             return "Disponible"
#     return "No disponible"
# c = input("¿Qué color busca?: ")
# print(Disponibilidad(pinturas, c))
# print(Disponibilidad(pinturas2, c))

# def BuscarColor(lista, color):
#     for paint in lista:
#         if color.lower()==paint["color"]:
#             return "Disponible"
#     return "No existe"    
# busca=input("Ingrese el color a buscar: ")
# print(BuscarColor(pinturas, busca))


''' EJERCICIO 2 '''
def mostrarPinturas():
    if len(pinturas)<1:
        print("no hay pinturas para mostrar")
    else:
        c=1
        for p in pinturas:
            print(f"{c}.- {p}")
            c+=1
#En lugar de pasar la lista pinturas, poner la lista como argumento

def PinturasDisponibles(lista):
    if len(lista)<1:
        print("No hay elementos para mostrar")
    else:    
        contador=1
        for pintura in lista:
            print(f"{contador}.- {pintura}")
            contador+=1
print(PinturasDisponibles(pinturas))
print(PinturasDisponibles(pinturas2))        

nombres=["Batman", "Robin", "Dos Caras", "Joker"]

apellidos=["Jara", "Kast", "Pinochet", "Allende"]

def mostrarLista(lista):
    if len(lista)<1:
        print("No hay elementos para mostrar")
    else:
        c = 1
        for p in lista:
            print(f"{c}.- {p}")
            c+=1
mostrarLista(nombres)


nums = [20, 3, 7, 11, 67, 64, -8]
#                lista/valor a buscar
def buscaNumeros(lista, nums):
    for n in lista:
        if n==nums:
            return "Número encontrado"
    return "No se encontró el número", nums

# NumeroBuscar=int(input("Ingrese el número a buscar: "))
# print(buscaNumeros(nums, NumeroBuscar))

''' EJERCICIO 4 '''

def quitarPintura():
    mostrarPinturas()
    ele=int(input("Que pintura va a eliminar?: "))
    pinturas.pop(ele-1)

#Ahora el usuario debe escribir el color y borrarlo    

def quitarPintura2(lista, quitar):
    for j in lista:
        if quitar == j["color"]:
            lista.remove(j)
            print("Color Eliminado")

quitarPintura2(pinturas, (eliminar).lower)
print(pinturas)