#Funciones guia examen
 
 
 
autos = {
    'A001' : ['Toyota','Corolla',2010,5],
    'A002' : ['Ford', 'Ranger',2019,4],
    'A003' : ['Chevrolet', 'Spark',2022,4],
    'A004' : ['Suzuki', 'Aerio',2005,4],
    'A005' : ['Toyota','Yaris',2015,5],
    'A006' : ['Chevrolet', 'Impala',1950,1],
}
operaciones = {
    'A001' : ['01-01-2024','12-12-2025'],       #Significa que entró a la empresa en la fecha inicial y ya se ha hecho la venta
    'A002' : ['07-08-2024','Pendiente'],        #Significa que entró a la empresa en la fecha inicial y todavía no se vende
    'A003' : ['09-01-2025','Pendiente'],
    'A004' : ['24-03-2025','Pendiente'],
    'A005' : ['24-03-2024','24-07-2024'],
    'A006' : ['24-03-2024','24-09-2024'],
}
#print(operaciones['A002'][-1])
#Función para mostrar todos los autos:
def MostrarAutos(diccionario):
    if len(diccionario)<1:
        print("No hay productos para mostrar")
    else:    
        c=1
        for key, value in diccionario.items():
            print("-"*60)
            print(f"{key}.- {value}")
            print("-"*60)
            c+=1
#MostrarAutos(autos)

#Muestra solo autos vendidos
#como lo hice yo
def AutosVendidos(diccionario):
    for key , value in diccionario.items():
        if value[1] != 'Pendiente':
            print("-"*60)
            print(f"{key}.- {value}")
            print("-"*60)

#Como lo hizo el profe
def AutosVendidos(diccionario):
    for id , vehiculo in diccionario.items():
        if operaciones[id][1] != 'Pendiente':
            print("-"*60)
            print(f"{id}.- {vehiculo}")
            print("-"*60)
            
AutosVendidos(operaciones)            

#Examen es similar
# Habrán 2 listas
# Tendremos que descubrir la relación entre ambas.
# Listas ya vienen con datos

def  autos_vendidos_por_marca(marca):
    total=0
    for id , vehiculos in autos.items():  #Keys = id, value = vehiculos
        # print("-"*60)
        # print(f"{key}.- {value}")
        # print("-"*60)
        if vehiculos[0].lower()==marca.lower():
            if operaciones[id][-1] != 'Pendiente':             
                total+=1
    print(f"El total de autos vendidos de la marca {marca} es de {total}.")            
autos_vendidos_por_marca("Chevrolet")

print(operaciones["A003"][-1])
def actualizar_fecha_venta(id_auto, nueva_fecha):
    if id_auto in operaciones:
        operaciones[id_auto][-1]=nueva_fecha
        return True
    else:
        return False
    
# while True:    
#     id=input("Ingrese el id del auto: ")
#     fecha=input("Ingrese la fecha de venta: ")
    
#     if actualizar_fecha_venta(id, fecha):
#         print("Éxito, nueva fecha de venta actualizada")
#     else:
#         print("Datos erróneos")
#     next=input("¿Desea actualizar otro vehículo (s/n)?: ")
#     if next.lower=="n":
#         break


def AgregarVehiculo():
    print("")

def validar_ID():
    id=input("Ingrese el id del vehiculo a agregar: ")
    if " " in id and id== "":
        return False
    else:
        return True
    
def validar_nueva_marca():
    nueva_marca=input("Ingrese la marca del vehiculo a agregar: ").capitalize()
    if " " in nueva_marca and nueva_marca== "":
        return False
    else:
        return True

def validar_nuevo_modelo():
    # nuevo_modelo=input("Ingrese el modelo del vehiculo a agregar: ")
    # if nuevo_modelo==" " or nuevo_modelo.len<1:
    #     print("El modelo nuevo no puede estar vacío o ser menor a 1 caracter")
    #     nuevo_modelo=input("Ingrese el modelo del vehiculo a agregar: ")
    nuevo_modelo=input("Ingrese el modelo del vehiculo a agregar: ").capitalize()
    if " " in nuevo_modelo and nuevo_modelo== "":
        return False
    else:
        return True
        
def validar_nuevo_año():
    # nuevo_año=int(input("Debe ser mayor a 1900. Ingrese el año del vehiculo a agregar: "))
    # if nuevo_año==" " or nuevo_año.len<1 or nuevo_año>1900:
    #     print("El año de ingreso no puede estar vacío, ser menor a 1 caracter o ser más antiguo a 1900")
    #     nuevo_año=int(input("Ingrese el año del vehiculo a agregar: "))
    try:
        nuevo_año=int(input("Ingrese el año del vehiculo a agregar: "))

    except ValueError as error:
        print("Error", error) 
    
    if nuevo_año > 1900:
        return True
    else:
        return False
    
def validar_nuevo_ranking():
    # nuevo_ranking=int(input("Ingrese el ranking del vehiculo a agregar: "))
    # if nuevo_ranking==" " or nuevo_ranking.len<1:
    #     print("El nuevo ranking no puede estar vacío o ser menor a 1 caracter")
    #     nuevo_ranking=int(input("Ingrese el ranking del vehiculo a agregar: "))
    try:
        nuevo_ranking=int(input("Ingrese el ranking del auto: "))
    except ValueError as error:
        print("Error", error) 

    if 1<= nuevo_ranking >= 5:
        return True
    else:
        return False
    
'''

COMO LO ESTABA HACIENDO, LENTO Y EXTENSO

nueva_fecha_ingreso=input("Ingrese la fecha de ingreso del vehiculo a agregar: ")
if nueva_fecha_ingreso==" " or nueva_fecha_ingreso.len<1:
    print("La nueva fecha de ingreso no puede estar vacía o ser menor a 1 caracter")
    nueva_fecha_ingreso=input("Ingrese la fecha de ingreso del vehiculo a agregar: ")

nueva_fecha_venta=input("Ingrese la fecha de venta del vehiculo a agregar: ")
if nueva_fecha_venta==" " or nueva_fecha_venta.len<1:
    print("La nueva fecha de venta no puede estar vacía o ser menor a 1 caracter")
    nueva_fecha_venta=input("Ingrese la fecha de venta del vehiculo a agregar: ")
    
autos.append({"id": nueva_id, "marca":nueva_marca, "modelo": nuevo_modelo, "año": nuevo_año, "ranking":nuevo_ranking})
operaciones.append({"id": nueva_id, "fecha ingreso": nueva_fecha_ingreso, "fecha venta": nueva_fecha_venta})

'''    
#Como lo indica el profesor

def validaString(h):
    if h != "" or h!=" ":
        return False
    else:
        return True
    
def valida_anio(a):
    if a<1900:
        return True
    else:
        return False
    
def valida_ranking(r):
    if 1>= r <=5:
        return False
    else:
        return True    
    

def creAuto():
    id=input("Ingresa el nuevo ID: ")
    if validaString(id):
        print("Dato inválido")
        return
    marca=input("Ingresa la marca: ")
    if validaString(marca):
        print("Dato inválido")
        return
    modelo=input("Ingresa el nuevo modelo: ")
    if validaString(modelo):
        print("Dato inválido")
        return
    anio=int(input("Ingresa el año: "))
    if valida_anio(anio):
        print("Dato inválido")
        return
    ranking=int(input("Ingresa el ranking: "))
    if valida_ranking(ranking):
        print("Dato inválido. Ranking debe ser un número entero entre 1 y 5")
        return
    fecha=input("Ingresa la fecha (dd-mm-yyyy): ")
    if validaString(fecha):
        print("Dato inválido")
        return
    autos[id]=[marca, modelo, anio, ranking]
    operaciones[id][fecha, 'Pendiente']

MostrarAutos(autos)
creAuto()    
MostrarAutos(autos)

def eliminar_auto(id_auto):
    if id_auto in autos:
        del autos[id_auto]
        del operaciones[id_auto]
        return True
    else:
        return False
    



# hacer un menú con todas las funciones que 
# hicimos en clase
# Debe tener manejo de errores, try - except    