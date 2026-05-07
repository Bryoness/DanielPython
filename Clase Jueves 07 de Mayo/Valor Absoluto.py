#Valor Absoluto
import random, time
# num=random.randint(1,9)

# while abs(-3)!=num:
#     num=random.randint(1,9)
#     print(num)
#     time.sleep(1)
    
# n1=int(input("Ingrese el valor del límite inferior: "))
# n2=int(input("Ingrese el valor del límite superior: "))
# #Validar que el límite superior sea mayor al límite inferior
# while n1 >= n2:
#     print("El límite superior DEBE ser mayor al límite inferior")
#     n2=int(input("Ingrese el valor del límite superior: "))
# num=random.randint(n1,n2)
# print(num)


'''
Realizar las clasificaciones de peces
Generar una cantidad aleatoria de peces entre 10 y 20
Capturar peces y clasificarlos por su pesa
para saber cómo se venderán
800 grs o menos, a lata
801 ó más, a la planca (máx 3000)
El peso de los peces se genera aleatoriamente
Contar cuándo quedaron a la planca y
cuantos quedaron para envasar en lata
'''
# Cómo lo hice yo
# CantPeces=random.randint(10,20)
# PezLata=0
# PezPlancha=0
# print("Se ha capturado un total de: ", CantPeces, " peces")
# for CantPeces in range (CantPeces):
#     PesoPeces=random.randint(500, 3000)
#     print("Se ha capturado un pez de:", PesoPeces, "g")
#     time.sleep(1)
#     if PesoPeces <= 800:
#         print("Se ha capturado un pez para lata")
#         PezLata+=1
#         print("Hasta ahora hay: ", PezLata, " peces para enlatar")
#         time.sleep(1)
#     if PesoPeces>=801 and PesoPeces<=3000:
#         print("Se ha capturado un pez para plancha")
#         PezPlancha+=1
#         print("Hasta ahora hay: ", PezPlancha, " peces para plancha")    
#         time.sleep(1)

# print(f"La cantidad de peces para lata son {PezLata} y la cantidad de peces para plancha es {PezPlancha}")
# print("En total se capturaron ", PezLata+PezPlancha, " peces")


#Cómo lo hizo el profesor
# peces=random.randint(10,20)
# p_lata=0
# p_plancha=0
# print(f"Capturamos {peces} peces")
# time.sleep(2)
# for p in range (peces):
#     pez=random.randint(257,3000)
#     if pez<=800:
#         p_lata+=1
#     else:
#         p_plancha+=1

# print(f"La cantidad de peces para enlatar es {p_lata}")       
# print(f"La cantidad de peces para plancha es {p_plancha}")

'''
Fábrica de enlatados
Se necesita hacer el algoritmo de productos enlatados
Se debe consultar el peso del producto (en gramos y sólo valores positivos)
El porcentaje de sodio en él (sólo valores entre 1 y 100)
Y si se va a vender nacional o internacionalmente (solo valores entre 1 y 2)
Considerar los criterios en la siguiente tabla

Menos de 500grs, lata normal
501-1500 grs, lata mediana
1501 y más, lata grande
Si el sodio es menos de 5%, lata queda igual
Si es entre 5% y 8% lata especial
Si tiene 9$ o más, lata acorazada
A las latas internacionales se le debe pegar 
un sticker de validación sanitaria

Ej: 800, 7%, 2==> Lata mediana especial con sticker sanitario
'''

# Peso_Producto=int(input("Ingrese el peso del producto"))
# Cant_Sodio=int(input("Ingrese el porcentaje de sodio en el producto. Valores aceptables 1 - 100"))
# Nacional=True
# lata_normal=0
# lata_mediana=0
# lata_grande=0

# lata_Na_Normal=0
# lata_Na_especial=0
# lata_Na_acorazada=0
# def Class_Peso():
#     Peso_Producto=int(input("Ingrese el peso del producto"))
#     if Peso_Producto<=500:
#         lata_normal+=1
#     elif Peso_Producto<=1500:   
#         lata_mediana+=1
#     elif Peso_Producto>=1501:
#         lata_grande+=1    

# def Cant_Sodio():
#     Porcen_Sodio=int(input("Ingrese el porcentaje de sodio en el producto. Valores aceptables 1 - 100"))
#     while Porcen_Sodio>1 and Porcen_Sodio<100:
#         if Porcen_Sodio<=5:
#             lata_Na_Normal+=1
#         elif Porcen_Sodio>=5 and Porcen_Sodio<=8:   
#             lata_Na_especial+=1
#         elif Porcen_Sodio>8:
#             lata_Na_acorazada+=1    

# peso=int(input("Ingrese el peso del producto en gramos: "))
# while 0>peso: 
#     print("Solo ingrese valores positivos")
#     peso=int(input("Ingrese el peso del producto en gramos: "))

# sodio=int(input("Ingrese el porcentaje de sodio del producto: "))
# while 0<sodio and sodio<=100:
#     print("El porcentaje solo debe ser entre 1 y 100")
#     sodio=int(input("Ingrese el porcentaje de sodio del producto: "))


# mercado=int(input("Ingrese el mercado del producto. 1=Nacional 2=Internacional "))

peso=int(input("Ingrese el peso del producto: "))
while peso<1:
    print("Ingrese solo valores positivos")
    peso=int(input("Ingrese el peso del producto: "))
sodio=int(input("Ingrese el porcentaje de sodio del producto: "))
while sodio<1 or sodio>100:
    print("El porcentaje solo debe ser entre 1 y 100")
    sodio=int(input("Ingrese el porcentaje de sodio del producto: "))
mercado=int(input("Ingrese el mercado del producto 1.- Nacional , 2 Internacional:"))

while mercado<1 or mercado>2:
    mercado=int(input("Ingrese el mercado del producto 1.- Nacional , 2 Internacional:"))



if peso < 500:
    lata="Lata Normal"
elif 501< peso <1500:
    lata="Lata Mediana"
elif peso>1500:
    lata="Lata Grande"
else:
    print("Ingrese un peso válido mayor a 0")    


if sodio < 5:
    CantNa="Sodio Normal"
elif 5<= sodio <= 8:
    CantNa="Lata Especial"
elif sodio>8:
    CantNa="Lata Acorazada"
else:
    print("Ingrese un porcentaje válido")    


if mercado == 1:
    sticker="Sin sticker sanitario para mercado nacional"
elif mercado == 2 :
    sticker="Con sticker sanitario para mercado internacional"   
else:
    print("Ingrese una opción válida")                     

print(f"{lata} {CantNa} {sticker}")    