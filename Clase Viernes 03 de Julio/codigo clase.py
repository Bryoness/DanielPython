#Funciones guia examen
 
 
 
autos = {
    'A001' : ['Toyota','Corolla',2010,5],
    'A002' : ['Ford', 'Ranger',2019,4],
    'A003' : ['Chevrolet', 'Spark',2022,4],
    'A004' : ['Suzuki', 'Aerio',2005,4],
    'A005' : ['Toyota','Yaris',2015,5],
    'A006' : ['Chevrolet', 'Impala',1950,1],
    'A007' : ['Chevrolet', 'Impala',1959,2],
}
operaciones = {
    'A001' : ['01-01-2024','12-12-2025'],
    'A002' : ['07-08-2024','Pendiente'],
    'A003' : ['09-01-2025','Pendiente'],
    'A004' : ['24-03-2025','Pendiente'],
    'A005' : ['24-03-2024','24-07-2024'],
    'A006' : ['24-03-2024','24-09-2024'],
    'A007' : ['24-03-2024','01-09-2026'],
}
# print(operaciones["A002"][-1])
# funcion para mostrar todos los autos 

def muestrAutos(d):
    for id, vehiculo in d.items():
        print(f"{ id }: {vehiculo}")
    print("-"*50)
# muestrAutos(autos)

# muestra solo autos vendidos

def muestrAutosVendidos(d):
    for id, vehiculo in d.items():
        if operaciones[id][-1]!="Pendiente":
            print(f"{ id }: {vehiculo}")
    print("-"*50)
# muestrAutosVendidos(autos)

def autos_vendidos_por_marca(marca):
    total=0
    for id, vehiculo in autos.items():
        # print(f"{ id }: {vehiculo}")
        if vehiculo[0].lower()==marca.lower():
            if operaciones[id][-1]!="Pendiente":
                total+=1
    print(f" El total de vehiculos vendidos de la marca {marca} es de {total}")

# autos_vendidos_por_marca("Chevrolet")

# print ('A013' in operaciones)
# print(operaciones['A003'][-1])
def actualizar_fecha_venta(id_auto, nueva_fecha):
    if id_auto in operaciones:
        operaciones[id_auto][-1]=nueva_fecha
        return True
    else:
        return False

# while True:
#     id=input("Ingrese el id del auto: ")
#     fecha=input("Ingrese la fecha de venta: ")

#     if actualizar_fecha_venta(id,fecha):    
#         print("Exito, nueva fecha de venta actualizada")
#     else:
#         print("Metió mal las manos")
#     next=input("Desea actualizar otro vehículo (s/n)?")
#     if next.lower()=="n":
#         break

def validaString(h):
    if h=="" or h==" ":
        return True
    else:
        return False 
def validaAnio(a):
    if a <1900:
        return True
    else:
        return False
def validaRanking(a):
    if a>=1 and a<=5:
        return False
    else:
        return True
    
print(validaRanking(5))

# print(validaString(" "))


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
    if validaAnio(anio):
        print("El año debe ser superior a 1900")
        return
    ranking=int(input("Ingresa el ranking: "))
    if validaRanking(ranking):
        print("El ranking debe estar entre 1 y 5")
        return
    fecha=input("Ingrese la fecha ( dd-mm-yyyy): ")
    if validaString(fecha):
        print("Dato inválido")
        return
    autos[id]=[marca, modelo,anio,ranking]
    operaciones[id]=[fecha,'Pendiente']

# muestrAutos(autos)
# creAuto()
# muestrAutos(autos)

def  eliminar_auto(id_auto):
    if id_auto in autos:
        del autos[id_auto]
        del operaciones[id_auto]
        return True
    else:
        return False
    

# hacer un menu con todas las funciones que 
# hicimos en clase
# debe tener manejo de errores Try- except

   