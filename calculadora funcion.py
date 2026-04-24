def suma():
            print("El formato es número1 + número2")
            n1=int(input("ingrese el primer número para sumar: "))
            n2=int(input("ingrese el segundo número para sumar: "))
            print("El resultado de la suma es", n1+n2)

def resta():
            print("El formato es número1 - número2")
            n1=int(input("ingrese el primer número para restar: "))
            n2=int(input("ingrese el segundo número para restar: "))
            print("El resultado de la resta es", n1-n2)

def multi():
            print("El formato es número1 x número2")
            n1=int(input("ingrese el primer número para multiplicar: "))
            n2=int(input("ingrese el segundo número para multiplicar: "))
            print("El resultado de la multiplicación es", n1*n2)

def div():
            print("El formato es número1 / número2")
            n1=int(input("ingrese el primer número para dividir: "))
            n2=int(input("ingrese el segundo número para dividir: "))
            print("El resultado de la multiplicación es", n1/n2)

def calculadora():
    op=0                        
    while op !=5: 
        print("1.- Suma")
        print("2.- Resta")
        print("3.- Multiplicación")
        print("4.- División")
        print("5.- Salir")
        print("Selecciona una operación")
        op=int(input())
        match op:
            case 1:
                suma()
            case 2:
                resta()
            case 3:
                multi()
            case 4:
                div()
            case 5:
                print("Saliendo")    
            case _:
                print("Opción inválida")
calculadora()                