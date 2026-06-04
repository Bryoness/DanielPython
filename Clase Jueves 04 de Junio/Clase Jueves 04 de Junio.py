# # #CRUD --> Create, Reade, Update, Delete

# #Suma()
# #Sin argumento y con retorno

# def sumaret():
#     n1=int(input("ingrese el primer número para sumar: "))
#     n2=int(input("ingrese el segundo número para sumar: "))
#     return n1+n2

# res=sumaret()
# print("El resultado es, ", res)


# #Con argumento y sin retorno
# def saludoME(name):
#     print("Hola,", name)

# saludoME("Ganon")

# def MitadPrecio(precio):
#     print("El precio es:", precio/2)
# p=int(input("Ingrese el precio: "))
# MitadPrecio(p)    

# pre=sumaret()
# MitadPrecio(pre)

#Con argumento y con retorno

# def sumaRetArg(n1,n2):
#     return n1+n2
# a=int(input("ingrese el primer número para sumar: "))
# b=int(input("ingrese el segundo número para sumar: "))
# print("El resultado de la suma es", sumaRetArg(a,b))


#Crear una calculadora para las 4 operaciones
#básicas y usando funciones. Éstas deben tener
#Argument y return.

def SumaReturn(n1,n2):
    return n1+n2


def RestaReturn(n1,n2):
    return n1-n2


def MultiReturn(a,b):
    return num1*num2


def DivReturn(n1,n2):
    return n1/n2






#Cómo lo hizo el profesor
while True:
    try:
        print("1.- Suma")
        print("2.- Resta")
        print("3.- Multiplicación")
        print("4.- División")
        print("5.- Salir")
        op=int(input("Ingrese una opción: "))
        match op:
            case 1:
                num1=int(input("Ingrese un número: "))
                num2=int(input("Ingrese otro número: "))
                Resultado=SumaReturn(num1,num2)
            case 2:
                num1=int(input("Ingrese un número: "))
                num2=int(input("Ingrese otro número: "))
                Resultado=RestaReturn(num1,num2)
            case 3:
                num1=int(input("Ingrese un número: "))
                num2=int(input("Ingrese otro número: "))
                Resultado=MultiReturn(num1,num2)
            case 4:
                num1=int(input("Ingrese un número: "))
                num2=int(input("Ingrese otro número: "))
                while num2==0:
                    num2=int(input("Ingrese otro número distinto de 0: "))
                Resultado=DivReturn(num1,num2)
            case 5:
                print("Saliendo")
            case _:
                print("Escoja una opción válida")                              
        print("El resultado es ", Resultado)
    except Exception as e:
            print("Error: ", e)  