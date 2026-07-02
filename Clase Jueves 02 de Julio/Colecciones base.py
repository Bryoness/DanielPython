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
    for keys , value in autos.items():  #Keys = id, value = vehiculos
        # print("-"*60)
        # print(f"{key}.- {value}")
        # print("-"*60)
        if value[0].lower()==marca.lower():
            if operaciones[keys][-1] != 'Pendiente':             
                total+=1
    print(f"El total de autos vendidos de la marca {marca} es de {total}.")            
autos_vendidos_por_marca("Chevrolet")