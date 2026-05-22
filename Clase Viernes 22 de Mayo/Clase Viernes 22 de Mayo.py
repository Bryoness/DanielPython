'''
Registro de juegos
Preguntar cuantos juegos son.
Debe preguntar al usuario Nombre del juego;
-Al menos 5 caracteres
-No debe incluir espacios y todas mayúsculas
Preguntar precio
-Sólo números enteros positivos
-Si vale más de 20000 es Indie, pero menos de 40000
-Si vale 40000 o más, es de estudio
-Mostrar al final cuántos hay de cada categoría
Clasificación (debe preguntar la edad objetiva)
-E para todos (<12)
+12 para adolescentes (12 y 17)
M para personas de más de  18 (+18)
-MOSTRAR RESUMEN
EJ: Hay 4 indies, y 5 de estudio. Solo 3 son clasificación E
Uso de try-except obligatorio
'''
# Solicitar al usuario cantidad de juegos
# Cant_Juegos = int(input("Ingrese la cantidad de juegos (sólo números enteros): "))
# while Cant_Juegos<=0:
#     try:
#         print("La cantidad de juegos debe ser mayor a 0")
#         Cant_Juegos = int(input("Ingrese la cantidad de juegos (sólo números enteros): "))
#     except ValueError as error:
#         print("Error:", {error})    

# for i in range (Cant_Juegos):
#     try: 
#      print("Ingrese el nombre del juego. Al menos 5 caracteres. No contarán espacios")
#      NombreJuego=str(input("Por favor, ingrese el nombre del juego: "))
#      largo=len(NombreJuego.strip)
#      if 5<= largo:
#       print(f"El nombre {NombreJuego.upper} tiene el tamaño adecuado")
#      else:
#         print("Nombre de usuario inválido")
#     except ValueError as error:
#         print("Nombre demasiado corto.", (error))

# Indie=0
# Estudio=0
# precio=int(input("Ingrese el precio del juego (sólo números enteros): "))
# for i in range (Cant_Juegos):
#     try: 
#      print(f"Ingrese el valor del juego N° {i}. Precio mínimo 20.000")
#      precio=int(input(f"Por favor, ingrese el precio del juego N° {i}: "))
#      if 20000<=precio>=40000:
#       Indie+=1
#      elif precio>40000:
#       Estudio+=1  
#     except ValueError as error:
#         print("Error.", (error))

# Clasif_E=0
# Clasif_T=0
# Clasif_M=0
# for i in range (Cant_Juegos):
#     print(f"Clasificación ¿Para qué público es apto el juego N° {i}?")
#     print(f"1.- Clasificación E --> para Todos (menores de 12 años)")
#     print(f"2.- Clasificación T --> para Adolescentes (entre 12 y 17 años")
#     print(f"3.- Clasificación M --> para Adultos (mayores de 18 años")
#     print(f"Ingrese la clasificación del juego N° {i}.")
#     try:
#         edad=str(input(f"Por favor, ingrese la opción numérica de clasificación del juego N° {i}: "))
#         if edad==1:
#             Clasif_E+=1
#         elif edad==2:   
#             Clasif_T+=1
#         elif edad==3:
#             Clasif_M+=1
#         else:
#            error    
#     except ValueError as error:
#        print("Error. La opción debe ser 1, 2 o 3", error)    


# print("RESUMEN")
# print(f"Hay {Indie} juegos indie")
# print(f"Hay {Estudio} juegos de estudio")
# print(f"Hay {Clasif_E} juegos con clasificación E")
# print(f"Hay {Clasif_T} juegos con clasificación T")
# print(f"Hay {Clasif_M} juegos con clasificación M")



'''Cómo lo hizo el profesor'''
while True:
    try:
        juegos=int(input("Cuantos juegos se registrarán?"))
        break
    except ValueError as error:
        print("Número de juegos inválido. Error", error)


for i in range (juegos):
    titulo=input("Ingrese el nombre del juego. (Al menos 5 caracteres sin espacios): ").upper()
    #titulo=titulo.repacle(" ", "") --> Forma de reemplazar los espacios. Lo hace el sistema en lugar del usuario.
    while " " in titulo:
        print("No de incluir espacios")
        titulo=input("Ingrese el nombre del juego (Al menos 5 caracteres y sin espacios): ").upper

    while len(titulo)<5:
        print("El título es muy corto") 
        titulo=input("Ingrese el nombre del juego (Al menos 5 caracteres y sin espacios): ").upper

    while True:
        try:
            precio=int(input("Ingrese el precio del juego: "))
            if precio>20000 and precio<40000:
                print("El juego es indie")
                indie+=1
                break
            elif precio>=40000:
                print("El juego es de estudio")
                estudio+=1
                break
            else:
                print("El precio no puede ser menor a 20.000")
        except:
            print("Solo números enteros positivos")

while True:
    try:
        clasif=int(input("Ingrese la clasificación del juego (edad): ")) 
        break
    except:
        print("Solo numeros enteros positivos")

    if clasif <= 12:
        print("El juego es de todo publico")
