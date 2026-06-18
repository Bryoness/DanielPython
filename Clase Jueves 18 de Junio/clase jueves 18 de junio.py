## Crear un gestor de pacientes

pacientes=[
    {"nombre": " Aquiles Baeza", "prevision": "Fonasa", 
     "temperatura":34.6, "grave": False},
    {"nombre": " Kiko Baeza", "prevision": "Fonasa", 
     "temperatura":34.6, "grave": False},
    {"nombre": " Chavo Baeza", "prevision": "Fonasa", 
     "temperatura":34.6, "grave": False},          
]

print(pacientes)

'''crear al gestor de pacientes en un centro medico
Para poner el nombre se debe validar que no este vacio 
y ademas tenga mas de 8 caracteres
Para la prevision de salud solo exiten 3 posibles valores
Fonasa, Isapre, o Fodesa
Al ingresar un paciente, se debe poner la temperatura
Crear una funcion que valide si esta grave o no
Para que este grave debe tener mas de 39°
Cada atencion vale $25.000
Los despcuentos corresponden a 
FOnasa 54%
Isapre 27%
Fodesa 12,5%
'''


pacientes.append({"nombre": "Alan Brito", "prevision": "Isapre", 
     "temperatura":39.6, "grave": True})

#Agregar un paciente con los datos que ingresa el usuario

#Cómo lo hizo el profesor:

def validTemp(t):
    if t>39:
        return True
    else:
        return False

def mostrarPaciente():
    c=1
    for paciente in pacientes:
        print(f"{c}.- {paciente}")
        c+=1
        print(" ")

def agregarPaciente():    
    nombre=input("Ingrese el nombre del paciente nuevo: ")
    while nombre==" " or len(nombre)<9:
        print("Nombre no puede ser vacío ni tener menos de 8 caracteres")
        nombre=input("Ingrese el nombre del paciente nuevo: ")
    prevision=input("Ingrese la prevision del paciente nuevo: ")
    while prevision.lower() not in ("fonasa", "isapre", "fodesa"):
        print("La previsión solo puede ser fonasa, isapre o fodesa.")
        prevision=input("Ingrese la prevision del paciente nuevo: ")

    temperatura=float(input("Ingrese la temperatura del paciente nuevo: "))
    pacientes.append({"nombre": nombre, "prevision": prevision, 
        "temperatura":temperatura, "grave": validTemp(temperatura)})

def quitarPaciente():
    # poner nombrediccionario.remove({"nombre", "prevision", etc}) significa eliminar todo de un diccionario 
    # pero se deben escribir todas las entradas.
    # en cambio, en usar nombrediccionario.pop() se usa solo el numero de entrada
    mostrarPaciente()
    egreso=int(input("¿Que paciente egresa?: "))
    pacientes.pop(egreso-1)
    print("Paciente eliminado.")

def cobrarPaciente():
    mostrarPaciente()
    paciente=int(input("Ingrese el número del paciente que va a pagar: "))
    while -1<paciente< len(pacientes):
        print("Paciente no encontrado")
        mostrarPaciente()
        paciente=int(input("Ingrese el número del paciente que va a pagar: "))
    prevision=pacientes[paciente-1]["prevision"]
    valor=25000
    total=0
    print(f"Ha seleccionado al paciente {pacientes[paciente-1]["nombre"]}")
    print(f"La prevision es {pacientes[paciente-1]["prevision"]}")   
    print(f"La atencion tiene un valor de: ${valor}")
    print(f"Por su prevision se le hace un descuento de: ")
    match prevision.lower():
        case "fonasa":
            total = valor*0.54
            print(total)
        case "isapre":
            total = valor*0.27
            print(total)
        case "fodesa":
            total = valor*0.125
            print(total)            
    print(f"Total a pagar: ${valor-total}")        


#Como lo hizo el profesor
# def cobrarpaciente():
#   mostrarPaciente()
#   cobrar = int(input("A quien le va a cobrar?: "))
#   if pacientes[cobrar-1][prevision] == "fonasa":
#       total= 25000*0.46
#   elif pacientes[cobrar-1][prevision] == "isapre":
#       total= 25000*0.73
#   elif pacientes[cobrar-1][prevision] == "fodesa":
#       total= 25000*0.875
#   else:
#     print("Prevision inválida")
#   print(f"El total a pagar es: {total}")



def tomarTemperatura():
    mostrarPaciente()
    paciente=int(input("¿A qué paciente le tomará la temperatura?: "))
    t=float(input("Ingrese la nueva temperatura: "))
    pacientes[paciente-1]["temperatura"]=t
    pacientes[paciente-1]["grave"]=validTemp(t)


while True:
    try:
        print("Menú principal")
        print("1.- Agregar Paciente")
        print("2.- Quitar Paciente")                
        print("3.- Tomar Temperatura")
        print("4.- Cobrar a Paciente")
        print("5.- Mostrar Pacientes")
        print("6.- Salir")        
        op=int(input("Seleccione una opción: "))
        match op:
            case 1:
                agregarPaciente()

            case 2:
                quitarPaciente()

            case 3:
                tomarTemperatura()

            case 4:
                cobrarPaciente()


            case 5:
                c=1
                for paciente in pacientes:
                    print(f"{c}.- {paciente}")
                    c+=1
                    print(" ")


            case 6:
                print("Saliendo del sistema")
                break
            case _:
                print("Opción Inválida")
    except Exception as e:
        print("Error: ", e)




# def agregarPaciente():
#     nombre=input("Ingrese nombre: ")
#     prevision=input("Ingrese prevision: ")
#     temp=float(input("Ingrese temp: "))
#     gravedad=bool(input("¿Es de gravedad el paciente? Responder si o no."))
#     if gravedad=="si":
#         gravedad=True
#     elif gravedad=="no":
#         gravedad=False
#     else:
#         print("Opción inválida. Sólo responder sí o no")    
#     pacientes.append({"nombre": nombre, "prevision": prevision, 
#                 "temperatura":temp, "grave": gravedad })
#     print("Paciente agregado al listado")


# def validarEstado(tempe):
#    if tempe>39:
#        return True 
#    else:
#        return False
# def mostrarPacientes():
#     if len(pacientes)==0:
#         print("No hay pacientes")
#     else:
#         c=1
#         for p in pacientes:
#             print(f"{c} .- {p}")
#             c+=1
# def agregarPaciente():
#     nombre=input("Ingrese nombre: ")
#     prevision=input("Ingrese prevision: ")
#     temp=float(input("Ingrese temp: "))
#     pacientes.append({"nombre": nombre, "prevision": prevision, 
#                 "temperatura":temp, "grave": validarEstado(temp)})
#     print("Paciente agregado al listado")
# def eliminarPaciente():
#     mostrarPacientes()
#     paci=int(input("Que paciente se vá?: "))
#     pacientes.pop(paci-1)
#     print("Paciente eliminado.")
# def tomarTemp():
#     mostrarPacientes()
#     paciente=int(input ("A que paciente le tomamos temperatura?: "))
#     tomarTemp=float(input("ingrese su temperatura: "))
#     pacientes[paciente-1]["temperatura"]=tomarTemp
#     pacientes[paciente-1]["grave"]=validarEstado(tomarTemp)
# def cobrarAtencion():
#     mostrarPacientes()
#     pa=int(input("¿que paciente va a pagar?: "))
#     if pacientes[pa-1]["prevision"].lower()=="fonasa":
#         pagar=25000*0.46
#     elif pacientes[pa-1]["prevision"].lower()=="isapre":
#         pagar=25000*0.73
#     elif pacientes[pa-1]["prevision"].lower()=="fodesa":
#         pagar=25000*0.875
#     else:
#         print("prevision incorrecta")
#     print("Su total a pagar es: ", pagar)
# while True:
#     try:
#         print("1.- Ingresar paciente")
#         print("2.- Quitar paciente")
#         print("3.- Tomar Temperatura")
#         print("4.- Cobra atencion")
#         print("5.- Mostrar Pacientes")
#         print("9.- Salir")
#         op=int(input("Ingrese una opcion: "))
#         match op:
#             case 1:
#                 agregarPaciente()
#             case 2:
#                 eliminarPaciente()
#             case 3:
#                 tomarTemp()
#             case 4:
#                 cobrarAtencion()
#             case 5:
#                 mostrarPacientes()
#             case 9:
#                 print("Saliendo")
#                 break
#             case _:
#                 print("Opción inválida")
#     except Exception as e:
#         print("Error:" , e)