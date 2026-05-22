'''
El programa debe tener un menú de opciones de donde se pueda realizar el pago del cupo de la tarjeta de crédito, 
como también simular nuevas compras, y estas una vez sumadas se resten al cupo disponible. 
Las opciones disponibles deben estar construidas de la siguiente forma:
1.	Pago de Tarjeta de Crédito:
a.	El usuario comienza con una deuda de $100.000
b.	El usuario puede ingresar un monto para realizar un pago en la tarjeta de crédito.
c.	Se debe verificar que el monto ingresado sea mayor o igual a cero.
d.	Se debe verificar que el monto a pagar no sea mayor a la deuda actual.
e.	Al pagar el sistema debe descontar de la deuda total
f.	Si las verificaciones son exitosas, se realiza el pago y se actualiza el saldo de la tarjeta.

2.	Simulación de Compras:
a.	El usuario puede simular realizar un número ilimitado de compras.
b.	Para cada compra, se solicita al usuario ingresar el monto de la compra. El programa suma los montos de cada compra. 
c.	Se verifica que el monto de la compra sea mayor o igual a cero.
d.	Se realiza la compra y se actualiza el saldo de la tarjeta para cada iteración del bucle for.

3.	Salir:
a.	Al seleccionar esta opción, el programa debe cerrarse o finalizar.

A considerar:
1.	Manejo de Errores:
a.	Se utilizan bloques try y except para manejar posibles errores al ingresar datos, validar valores no numéricos 
y errores inesperados. 


'''
deuda=100000
op=0
while True:
    try:
        while op !=3: 
            print(f"Tiene una deuda de ${deuda}")
            print("1.- Pago tarjeta de crédito")
            print("2.- Simulación de compras")
            print("3.- Salir")
            print("Selecciona una opción: ")
            op=int(input())
            match op:
                case 1:
                    print("Ha seleccionado: Pago tarjeta de crédito")
                    print(f"Tiene una deuda de ${deuda}")
                    while True:
                        try:
                            A_Pagar=int(input("Ingrese el monto que desea pagar de su deuda total: "))
                            if A_Pagar<=deuda:
                                print(f"Ha pagado ${A_Pagar}")                                
                                print(f"Su deuda actual es ${deuda-A_Pagar}")
                                deuda-=A_Pagar

                                break
                            elif A_Pagar <= 0:
                                print(f"Debe ingresar un valor mayor a 0 y menor que su deuda actual. Deuda actual ${deuda}")
                                break
                            elif deuda<=A_Pagar:
                                print(f"No puede pagar un monto superior a su deuda actual. Deuda actual {deuda}")
                                break
                        except ValueError as error:
                                print(f"Solo números enteros positivos", error)
                case 2:
                    totalsimulacion=0
                    print("Ha seleccionado: Simulación de compras")
                    try: 
                        simulacion=int(input("Ingrese la cantidad de compras que desea simular: "))
                    except ValueError as error:
                         print("Debe ser un valor numérico.", error)
                         break
                         
                    if simulacion<=0:
                         print("La cantidad de simulaciones debe ser mayor a 0")
                    for i in range (simulacion):
                        while True:         
                            try:       
                                valor_simulacion=int(input(f"Ingrese el precio del producto N°{i+1}: "))
                                totalsimulacion+=valor_simulacion

                                break
                            except ValueError as error:
                                print("Solo números enteros")
                            
                            if valor_simulacion<=0:
                                print("Solo valores superiores a $0")
                                valor_simulacion=int(input(f"Ingrese el precio del producto N°{i+1}: "))
                        print(f"El total de su simulación es ${totalsimulacion}")
                    realizarsimulacion=int(input(f"¿Desea realizar éstas compras? 1=Sí 2=No: "))
                    try:
                            if realizarsimulacion == 1:
                                deuda+=totalsimulacion
                                print(f"Su deuda ahora es de {deuda}")
                                break
                    except ValueError as error:
                            print("Debe seleccionar una opción válida")        

                case 3:
                    print("Saliendo")

                case _:
                    print("Opción inválida")
    except ValueError as error:
        print("Debe seleccionar una opción numérica.", error)