#Ejemplo y uso de try except
# while True:   
#     try:
#         num=int(input("Ingrese un número: "))
#         break    
#     except:
#         print("Sólo números enteros: ")

#Éste será el nuevo estándar. Cada vez que se pida al usuario un dato
#los errores deberán ser manejados de ésta forma.

# while True:
#     try:
#         num=int(input("Ingrese un npumero: "))
#         break
#     except ValueError as er:
#         print("Solo números enteros")
#         print(er)


# '''Sacar promedio'''

# print("Ingrese 3 notas.")
# total=0

# for i in range (3):
#     while True: 
#         try: 
#             n=float(input(f"Ingrese la nota {i+1}: "))
#             break
#         except:
#             print("Sólo deben ser números para promediar.")
# total+=n            
# prom=total/3
# print(f"El promedio es {prom}")


#Cómo lo hice yo, y funciona
op=0
total=0
while op!=4:
    print("1.- PC $500.000")
    print("2.- LGTV 55 pulgadas $450.000")
    print("3.- Microondas Mademsa $100.000")
    print("4.- Salir")
    print("Seleccione una opcion")
    #op=int(input())
    while True:
        try: 
            op=int(input("Selecciona una opción"))
            break
        except:
            print("La opción debe ser en formato número")
    match op:
        case 1:
            print("El total a pagar es ",500000*1.19 )
            total+=500000*1.19
        case 2:
            print("El total a pagar es ",450000*1.19 )
            total+=450000*1.19
        case 3:
            print("El total a pagar es ",100000*1.19 )
            total+=100000*1.19
        case 4:
            print("Saliendo")
            print("El total a pagar es", total)
        case _:
            print("Opción inválida")

#Cómo lo hizo el profesor:
op=0
total=0
while op!=4:
    try:
        print("1.- PC $500.000")
        print("2.- LGTV 55 pulgadas $450.000")
        print("3.- Microondas Mademsa $100.000")
        print("4.- Salir")
        print("Seleccione una opcion")

        op=int(input())
        match op:
            case 1:
                print("El total a pagar es ",500000*1.19 )
                total+=500000*1.19
            case 2:
                print("El total a pagar es ",450000*1.19 )
                total+=450000*1.19
            case 3:
                print("El total a pagar es ",100000*1.19 )
                total+=100000*1.19
            case 4:
                print("Saliendo")
                print("El total a pagar es", total)
            case _:
                print("Opción inválida")
    except ValueError as e:
        print("Solo numeros enteros. Error: ", e)