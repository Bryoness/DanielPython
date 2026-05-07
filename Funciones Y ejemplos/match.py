#Explicacion y uso de match

op=0
total=0
while op !=4: 
    print("1.- PC Ryzen $800.000")
    print("2.- LG TV 55 Pulgadas #450.000")
    print("3.- Parlante JBL Pure Sound $90.000")
    print("4.- Salir")
    print("Selecciona una opción")
    op=int(input())
    match op:
        case 1:
            print("Tiene que pagar", 800000*1.19)
            total+=800000*1.19
        case 2:
            print("Tiene que pagar", 450000*1.19)
            total+=450000*1.19 
        case 3:
            print("Tiene que pagar", 90000*1.19)
            total+=90000*1.19
        case 4:
            print("Saliendo")
            print("El total a pagar es", {round(total)})
        case _:
            print("Opción inválida")