#seleccionar 3 programas que ya hemos hecho
#convertirlos en función
#ponerlos en un menú
#y llamarlos por su nombre

def cuentavocales():
    print("Cuenta la cantidad de vocales")
    nombre=input("Ingrese una palabra: ")
    vocals=0
    conso=0
    for i in nombre:
        print(i)
        if i in "aeiouAEIOU" :
            vocals+=1
        elif i ==" ":
            print("")
        else:
            conso+=1
    print("La cantidad de vocales es", vocals)
    print("La cantidad de consonantes es", conso)

def nombreusuario():
    NombreUsuario=input("Por favor, ingrese su nombre de usuario: ")
    largo=len(NombreUsuario)

    # if largo<= 10 and largo>= 4:
    #     print("Su nombre de usuario tiene el tamaño adecuado")
    # else:
    #     print("Nombre de usuario inválido")

    if 4<= len(NombreUsuario)<=10:
        print("Nombre dentro del rango")
    else:
        print("Nombre fuera de rango")

def menucalculadora():
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

def variosprogramas():
    op=0             
    while op !=4: 
            print("1.- Cuenta Vocales")
            print("2.- Nombre de Usuario")
            print("3.- Calculadora")
            print("4.- Salir")    
            op=int(input())
            match op:
                case 1:
                    cuentavocales()
                case 2:
                    nombreusuario()
                case 3:
                    menucalculadora()
                case 4:
                    print("Saliendo")    
                case _:
                    print("Opción inválida")
variosprogramas()