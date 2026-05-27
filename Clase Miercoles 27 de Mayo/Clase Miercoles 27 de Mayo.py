# op=0

# while op!=3:
#     try:
#         print("selecciona una opción")
#         print("1.-Chocolate")
#         print("2.-Mocca")
#         print("3.-Salir")
#         op=int(input())
            
#     except ValueError as e:
#         print("solo numeros enteros")
#         print("error: ", e)
# else:
#     print("Bien hecho")


'''
Hacer un menú donde los camiones sean clasificados:
1 - 3 toneladas = Camión chico
4 - 8 toneladas = camión mediano
+9 toneladas = camión grande
Solo mostrar números enteros positivos

La marca del camión debe tener no más de 8 caracteres
Pero no menos de 3
'''
def menuCamiones():
    camion_chico=0
    camion_mediano=0
    camion_grande=0
    op=0
    capacidad=0
    while op!=6:
        try:
            print("Seleccione una opcion")
            print("1.- Ingresar un camión")
            print("2.- Mostrar Totales")
            print("3.- Mostrar cantidad de camiones")
            print("4.- Mostrar capacidad total")
            print("5.- Ingrese una marca de camión")
            print("6.- Salir")
            op=int(input())
            match op:
                case 1:
                    while True:
                        try:
                            camion=int(input("Ingrese la capacidad de carga, en toneladas: "))
                            if camion>0:
                                capacidad+=camion
                                if 1<=camion<=3:
                                    camion_chico+=1
                                elif 4<=camion<=8:
                                    camion_mediano+=1
                                elif 9<=camion:
                                    camion_grande+=1         
                                else: 
                                    print("El valor debe ser positivo")
                                break
                        except ValueError as error:
                            print("Solo números enteros.")
                            print("Error", error)      
                case 2:
                    print("1.- Cantidad de camiones Pequeños: ", camion_chico)
                    print("2.- Cantidad de camiones  Medianos: ", camion_mediano)
                    print("3.- Cantidad de camiones Grandes: ", camion_grande)
                case 3:
                    print("Cantidad de camiones en total: ", capacidad, " toneladas")
                case 4:
                    print("La capacidad de carga total (suma de todos los camiones ingresados) es de: ", camion)
                case 5:
                    print("Debe tener entre 3 y 8 Caracteres")
                    while True:
                        try:
                            marca=str(input("Ingrese la marca de los camiones: "))
                            if 3<= len(marca) <=8:
                                print(f"La marca {marca} fue ingresada correctamente")
                            else:
                                print(f"La marca no cumple los parámetros")    
                            break
                        except ValueError as error:
                            print("Error", error)    
                case 6:        
                    print("Saliendo del sistema")
                case _:                
                    print("Ingrese una opción válida")
        except ValueError as error:
            print("Seleccione una opción valida en números")
            print("Error", error)



# Una galería de arte tiene 100 espacios para cuadros
# Preguntar cuantas personas vinieron a ver cuadros
# Al salir de la galería, preguntar a cada persona, cuantos cuadros vió
# Por cada persona, clasificar los cuadros vistos y no vistos
#
#
galeria=100
vistos=0
NoVistos=0
while True:
    try:
        visitantes=int(input("¿Cuántas personas asistieron?. Sólo números enteros. "))
        break
    except ValueError as error:
        print("Error ", error)

for i in range(visitantes):
    while True:
        try:
            cantidad=int(input("¿Cuántos cuadros vió?: "))
            vistos+=cantidad
            NoVistos+=galeria-cantidad
            break
        except ValueError as error:
            print("Error ", error)    

print(f"En total de cuadros vistos fue {vistos}")
print(f"El total de cuadros NO vistos fue {NoVistos}")            