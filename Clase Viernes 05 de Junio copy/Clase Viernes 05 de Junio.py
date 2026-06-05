# # # #CRUD --> Create, Reade, Update, Delete

# # #Suma()
# # #Sin argumento y con retorno

# # def sumaret():
# #     n1=int(input("ingrese el primer número para sumar: "))
# #     n2=int(input("ingrese el segundo número para sumar: "))
# #     return n1+n2

# # res=sumaret()
# # print("El resultado es, ", res)


# # #Con argumento y sin retorno
# # def saludoME(name):
# #     print("Hola,", name)

# # saludoME("Ganon")

# # def MitadPrecio(precio):
# #     print("El precio es:", precio/2)
# # p=int(input("Ingrese el precio: "))
# # MitadPrecio(p)    

# # pre=sumaret()
# # MitadPrecio(pre)

# #Con argumento y con retorno

# # def sumaRetArg(n1,n2):
# #     return n1+n2
# # a=int(input("ingrese el primer número para sumar: "))
# # b=int(input("ingrese el segundo número para sumar: "))
# # print("El resultado de la suma es", sumaRetArg(a,b))


# #Crear una calculadora para las 4 operaciones
# #básicas y usando funciones. Éstas deben tener
# #Argument y return.

# def SumaReturn(n1,n2):
#     return n1+n2


# def RestaReturn(n1,n2):
#     return n1-n2


# def MultiReturn(a,b):
#     return num1*num2


# def DivReturn(n1,n2):
#     return n1/n2






# #Cómo lo hizo el profesor
# while True:
#     try:
#         print("1.- Suma")
#         print("2.- Resta")
#         print("3.- Multiplicación")
#         print("4.- División")
#         print("5.- Salir")
#         op=int(input("Ingrese una opción: "))
#         match op:
#             case 1:
#                 num1=int(input("Ingrese un número: "))
#                 num2=int(input("Ingrese otro número: "))
#                 Resultado=SumaReturn(num1,num2)
#             case 2:
#                 num1=int(input("Ingrese un número: "))
#                 num2=int(input("Ingrese otro número: "))
#                 Resultado=RestaReturn(num1,num2)
#             case 3:
#                 num1=int(input("Ingrese un número: "))
#                 num2=int(input("Ingrese otro número: "))
#                 Resultado=MultiReturn(num1,num2)
#             case 4:
#                 num1=int(input("Ingrese un número: "))
#                 num2=int(input("Ingrese otro número: "))
#                 while num2==0:
#                     num2=int(input("Ingrese otro número distinto de 0: "))
#                 Resultado=DivReturn(num1,num2)
#             case 5:
#                 print("Saliendo")
#             case _:
#                 print("Escoja una opción válida")                              
#         print("El resultado es ", Resultado)
#     except Exception as e:
#             print("Error: ", e)  



'''



COPIAR AQUÍ CÓDIGO DEL PROFESOR




'''






# nombres=["Akiles", "Florencio", "Alan", "Zoila"]

# apellidos=["Baeza", "Flores", "Brito", "Cerda"]

# for n in range(len(nombres)):
#     print(nombres[n], apellidos[n])

# no=input("Agregue un nombre: ") 
# ap=input("Agregue un apellido: ") 
# nombres.append(no)
# apellidos.inser(1,ap)

# for n in range(len(nombres)):

# juguetes=["yo-yo", "tetris"]
# def agregar():
#     print("Lista de juguetes actuales")
#     print(juguetes)
#     añadir=input("Agregue un juguete: ")
#     juguetes.append(añadir)
#     print(juguetes)

# def mostrar():
#     contador=1
#     for j in juguetes:
#         print(contador, ".-", j)
#         contador+=1
#         print("-"*20)

# def actualizar():
#     mostrar()
#     print("¿Qué juguete desea actualizar?: ")
#     actualizar=int(input())
#     nuevo_juguete=input("Ingrese nuevo juguete: ")
#     juguetes[actualizar-1]=nuevo_juguete    

# def eliminar():
#     mostrar()
#     eliminar=int(input("¿Qué juguete desea eliminar?: "))
#     juguetes.pop(eliminar-1)
#     print("Juguete eliminado")

# def menujuguetes():
#     while True:
#         try:
#             print("-"*20)
#             print("1.- Agregar Juguete")
#             print("2.- Eliminar Juguete")
#             print("3.- Actualizar Juguete")
#             print("4.- Mostrar Juguete")
#             print("5.- Salir")
#             op=int(input("Ingrese una opción: "))
#             match op:
#                 case 1:
#                     print("Lista de juguetes actuales")
#                     print(juguetes)
#                     añadir=input("Agregue un juguete: ")
#                     juguetes.append(añadir)
#                     print(juguetes)

#                 case 2:
#                     mostrar()
#                     eliminar=int(input("¿Qué juguete desea eliminar?: "))
#                     juguetes.pop(eliminar-1)
#                     print("Juguete eliminado")
#                 case 3:
#                     actualizar()
#                 case 4:
#                     mostrar()    
#                 case 5:
#                     print("Saliendo")
#                     break
#                 case _:
#                     print("Opción Inválida")        
#         except Exception as error:
#             print("Error", error)    

# menujuguetes()
# print(juguetes)
# añadir=input("Agregue un juguete: ")
# juguetes.append(añadir)
# print(juguetes)


'''
Objetivo del programa: Un programa funcional que, dada una lista de números ingresada por el usuario, 
identifica y muestra los números pares e impares de manera clara y organizada.
Reglas de negocio:
1.	Solicitar al usuario que ingrese una lista de números enteros separados por espacios.
2.	Implementar una función llamada validar_lista_numeros que verifique que todos los elementos
    ingresados sean números enteros. Si se ingresa algún valor no válido, solicitar nuevamente la lista.
3.	La función validar_lista_numeros debe utilizar un bucle y maneja excepciones para asegurar 
    que todos los elementos ingresados sean números enteros.
4.	Utilizar el operador de módulo % (MOD) para determinar si un número es par o impar en la lista de números a ingresar. 
    Considerar que un número es par cuando el mod es igual a 0, en caso contrario, es impar
5.	Crear dos listas separadas: una para los números pares y otra para los impares.
6.	Mostrar al usuario las listas resultantes, indicando los números pares, e indicando los números impares

'''

#Actividad 3.3.3

numeros=(input("Ingrese números enteros separados por espacios: "))

ListaNumeros=numeros.split()
ListaNumerosInt=[]
pares=[]
impares=[]

for n in ListaNumeros:
    ListaNumerosInt.append(int(n))

for hh in ListaNumerosInt:
    if hh%2==0:
        pares.append(hh)
    else:
        impares.append(hh)

print(f"Los números pares son {pares}")
print(f"Los números impares son {impares}")                