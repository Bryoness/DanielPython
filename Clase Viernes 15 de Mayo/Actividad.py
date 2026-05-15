'''
Deberás construir un programa que esta diseñado para ayudar en la venta de pasajes. 
Inicia preguntándote cuántos pasajes deseas vender. 
Luego, utiliza un proceso organizado (llamado bucle for) para pedirte el precio de cada pasaje por separado. 
Si ingresas un valor que no es un número, te indica que necesitas proporcionar un valor numérico válido. 
Al final, muestra el monto total que se ha obtenido por la venta de todos los pasajes
•	Solicita al usuario la cantidad de pasajes a vender.
•	Se utiliza un bucle for para iterar sobre la cantidad de pasajes.
•	Dentro del bucle, se solicita al usuario el precio de cada pasaje y se acumula en la variable totalIngresos.
•	Si el usuario ingresa un valor no numérico para el precio del pasaje, el programa muestra un mensaje y sale del bucle usando break.
•	Finalmente, se imprime el total de ingresos por la venta de pasajes
'''
# while True:
#     try:
#         Num_Pasajes=int(input("Por favor, ingrese la cantidad de pasajes que desea adquirir: "))
#         break
#     except Exception as error:
#         print(f"La cantidad de pasajes debe ser un número entero. Error: ", error)

# totalIngresos=0
# for i in range(Num_Pasajes):
#     print(f"Pasaje número: {i+1}")
#     while True:
#         try:
#             Precio_Pasajes=int(input("Ingrese el precio del pasaje individual: "))
#             totalIngresos+=Precio_Pasajes
#             break 
#         except ValueError as error:
#             print(f"El valor de los pasajes debe ser un número entero. Error: ", error)

# print(f"El total a pagar por los {Num_Pasajes} pasajes es {totalIngresos}")    


'''
Realiza construcción de un programa que deba realizar lo siguiente:
Comienza con la inicialización de variables y solicita al usuario la cantidad de bultos. Luego,
utiliza un bucle FOR para procesar cada bulto, solicitando el peso al usuario y manejando
posibles errores (agregar excepciones). Dependiendo del peso ingresado, acumula valores y
contadores correspondientes para bultos livianos y normales. Finalmente, imprime el total a
pagar por bultos livianos y normales, así como la cantidad de bultos en cada categoría
'''
while True:
    try:
        Cant_Bultos=int(input("Por favor, ingrese la cantidad de bultos: "))
        break
    except Exception as error:
        print(f"La cantidad de bultos debe ser un número entero. Error: ", error)

bulto_liviano=0
bulto_normal=0
# valor_livano=1000
# valor_normal=2000
for i in range(Cant_Bultos):
    print(f"Bulto número: {i+1}")
    while True:
        try:
            Peso_Bulto=float(input(f"Ingrese el peso (en kg) del bulto. Bulto número {i+1}: "))
            if Peso_Bulto <= 5:
                bulto_liviano+=1
                # valor_livano=valor_livano*bulto_liviano
            else:
                bulto_normal+=1   
                #valor_normal=valor_normal*bulto_normal     
            break 
        except ValueError as error:
            print(f"Solo valores decimales. Error: ", error)

print(f"El valor por bultos livianos es: {bulto_liviano*1000}")
print(f"El valor por bultos normales es: {bulto_normal*2000}")
print(f"El total por todos los bultos es: {(bulto_liviano*1000)+(bulto_normal*2000)}")


#Pedir la cantidad de notas al usuario
#Luego pedir cada nota individualmente
#Calcular el promedio de todas las notas
#mostrar si aprueba o no

while True:
    try:
        notas=int(input("Ingrese la cantidad de notas: "))
        break
    except ValueError as error:
        print("La cantidad de notas debe ser un número entero. Error: ", error)


suma=0

for i in range(notas):
    while True:
        try:
            n=float(input(f"Nota número {i+1}. Ingrese el valor: "))
            suma=suma+n
            break
        except:
            print("El valor de notas debe ser un número decimal. Error: ", error)
    
prom=suma/notas
print("El promedio es: ", round(prom,1))

if prom>=4:
    print("Alumno aprobado")
else:
    print("Alumno reprobado")    