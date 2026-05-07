# titulo="Clima actual" #tipo string
# temp=18.6 #float
# diaDelMes=16 #int
# mes=4 #int
# llueve=True

# print(f"{titulo}")
# print(f"Fecha de hoy: {diaDelMes}-{mes}")
# print(f"Tempreatura actual {temp} grados")

# if llueve :
#     print("Saco el paraguas")
# else:
#     print("No saco el paraguas")

# num=10

# 7>num --->False
# "blue"=="blue"--->True

# num=int(input("Ingrese un numero: "))

# for i in range(num):

#     print(f"{i+1} Hola Camello")

# nombre=input("Ingrese su nombre: ")
# vocales=0
# cons=0
# for i in nombre:
#     print(i)
#     # vocales=vocales+1
#     if i in "aeiou":
#         vocales+=1
#     elif i==" ":
#         print()
#     else:
#         cons+=1
# print(f"La cant de vocales es {vocales}")
# print(f"La cant de consonantes es {cons}")
# 

# print("Hola Daniel"*3)
# n="daniel"
# print(n[-5])


# name1="Catalina Pinochet"
# name2=" Vicente "
# print(name2.strip())
# print(name1.upper())
# print(name1.lower())
# print(name1.replace("Pinochet", "Frei"))
# print(name1.find("Pinochet"))

'''Pedir a la clave al usuario y verificar
que sea SHAZAM independiente de su case
(sin importar si son mayúsculas o minúsculas)'''

'''Crear un nombre de usuario y verificar que 
su largo esté entre 4 y 10 caracteres'''

'''Crear un pin y que éste tenga exactamente
4 dígitos'''


# #Ejercicio 1
# clave="SHAZAM"
# Palabra2=input("Ingrese su clave secreta: ")

# if Palabra2.upper() == clave:
#     print("Bienvenido al sistema")
# else:
#     print("Contraseña incorrecta")


# #Ejercicio 2
# NombreUsuario=input("Por favor, ingrese su nombre de usuario: ")
# largo=len(NombreUsuario)

# # if largo<= 10 and largo>= 4:
# #     print("Su nombre de usuario tiene el tamaño adecuado")
# # else:
# #     print("Nombre de usuario inválido")

# if 4<= len(NombreUsuario)<=10:
#     print("Nombre dentro del rango")
# else:
#     print("Nombre fuera de rango")


#Ejercicio 3
pin=int(input("Ingrese su número secreto: "))
# digitos=len(pin)

# if digitos == 4:
#     print("Número secreto adecuado")
# else:
#     print("Clave Inválida")


if len(str(pin))==4:
    print("Pin creado")
else:
    print("Pin inválido")    

if 1000<=pin<=9999:
    print("Clave válida")
else:
    print("Clave creada")    