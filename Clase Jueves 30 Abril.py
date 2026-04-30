#For, match, if, while todo a la prueba.
#Lo único que no va en la prueba es funciones (def)
#Si va el uso de random que veremos ahora.
#Uso y ejemplo de random
#Para importar librerias para ser usadas se usa
import random
import time
#time.sleep(1) --> esperar 1 segundo
# #Va a generar un número entero aleatorio entre el límite inferior (que va primero)
# # y el límite superior, incluidos ambos números
# print(random.randint(1,10))
#No es recomendable ponerlo así, si no que DENTRO DE UNA VARIABLE
#La diferencia es que al usar una variable, se puede usar dentro de otros objetos
# num=random.randint(1,10)
# print(num)

# for i in range(num):
#     print("Hola Daniel")

# dado=random.randint(1,6)
# print("El dado salió", dado)


#Crear una tabla de multiplicar
#de 1 a 24, mostrar la tabla

# num=random.randint(1,24)
# for i in range (1,11):
#     print(f"{num}x{i}={num*i}")

#Al tirar 2 dados, y si sale par
#Se va a la cárcel, sino avanza

# dado1=random.randint(1,6)
# dado2=random.randint(1,6)
# print(f"Resultado del dado 1: {dado1}")
# print(f"Resultado del dado 2: {dado2}")
# if dado1 == dado2:
#     print("A la cárcel")
# else: 
#     print("Avanza")


#Se genera un golé aleatorio entre 10 y 70
#Si el golpe tiene más de 50 de fuerza es un golpe crítico
#Sino, no es muy efectivo

# strike=random.randint(10,70)
# if strike>50:
#     print("Es un golpe crítico. Daño: ", strike)
# else:
#     print("No es muy efectivo. Daño: ", strike)

#3 personas juegan golf
#cada persona tiene la posibilidad de golpear la pelota
#y la distancia varía entre 60 y 190
#mostrar al final el golpe más fuerte


#Mi código
# golpe=random.randint(60,190)
# jugador1=str(input("Ingrese el nombre del jugador 1: "))
# jugador2=str(input("Ingrese el nombre del jugador 2: "))
# jugador3=str(input("Ingrese el nombre del jugador 3: "))

# golpe1=random.randint(60,190)
# golpe2=random.randint(60,190)
# golpe3=random.randint(60,190)

# if golpe1 > golpe2 and golpe1 > golpe3:
#     print(f"{jugador1} ha sido quién más fuerte ha golpeado, con un valor de {golpe1}")
# elif golpe2 > golpe1 and golpe2 > golpe3:
#     print(f"{jugador2} ha sido quién más fuerte ha golpeado, con un valor de {golpe2}")
# else:
#     print(f"{jugador3} ha sido quién más fuerte ha golpeado, con un valor de {golpe3}")


# #Cómo lo hizo el profe
# j1=random.randint(60,190)
# j2=random.randint(60,190)
# j3=random.randint(60,190)
# print(f"El jugador 1 lanzó la pelota {j1} metros")
# print(f"El jugador 2 lanzó la pelota {j2} metros")
# print(f"El jugador 3 lanzó la pelota {j3} metros")

# if j1>j2 and j1>j3:
#     print(f"El jugador 1 ha sido quién más fuerte ha golpeado, con un valor de {j1} metros")
# elif j2>j1 and j2>j3:
#     print(f"El jugador 2 ha sido quién más fuerte ha golpeado, con un valor de {j2} metros")
# else:
#     print(f"El jugador 3 ha sido quién más fuerte ha golpeado, con un valor de {j3} metros")
        

#Killer Instinct
#Dos peleadores se piden al inicio de la pelea
#Cada peleador inicia con 100hp
#Se debe hacer una pelea por turnos
#y cada golpe varia entre 7 y 18
#Se termina el match cuando uno de los 2
#tiene su hp menor o igual a 0
#se debe mostrar el ganador al final
#Bonus: mostrar las barras de energía de cada peleador

#Consejos del profe, usar while y usar turnos
# turno=1
# if turno%2==0:
#     print("Turno del jugador 1")
# else:
#     print("Turno del jugador 2")    
#usar turno+=1

j1=str(input("Ingrese el nombre del jugador 1: "))
j2=str(input("Ingrese el nombre del jugador 2: "))
vida_j1=100
vida_j2=100
turno=1
BarraVida ="◘" 
while vida_j1>0 and vida_j2>0:
    golpe1=random.randint(7,18)
    golpe2=random.randint(7,18)
    if turno % 2 == 0:
      print(f"Es el turno {turno}")
      print(f"La vida de {j1} es {vida_j1}HP")
      print(f"{j1} ataca y hace {golpe1} de daño a {j2}")
      print(f"La vida de {j2} es de {vida_j2-golpe1}")
      print(f"Vida de {j1}: {vida_j1}")
      print(f"Vida de {j2}: {vida_j2}")
      print(BarraVida*vida_j1)
      print(f"Vida de {j2}: {vida_j2}")
      print(BarraVida*vida_j2)
      print("")
      vida_j2=vida_j2-golpe1
      turno+=1
      time.sleep(2)
    else:
      print(f"Es el turno {turno}")
      print(f"La vida de {j2} es {vida_j2}HP")
      print(f"{j2} ataca y hace {golpe2} de daño a {j1}")
      print(f"La vida de {j1} es de {vida_j1-golpe2}")
      print(f"Vida de {j1}: {vida_j1}")
      print(f"Vida de {j2}: {vida_j2}")
      print(BarraVida*vida_j1)
      print(f"Vida de {j2}: {vida_j2}")
      print(BarraVida*vida_j2)
      print("")
      vida_j1=vida_j1-golpe2
      turno+=1
      time.sleep(2)

if vida_j1 < 0:
   print(f"{j1} ha sido derrotado")
   print(f"La victoria es de {j2}")
   print(f"{j2} ha sobrevivido con {vida_j2} HP")
elif vida_j2 < 0:
    print(f"{j2} ha sido derrotado")
    print(f"La victoria es de {j1}")
    print(f"{j1} ha sobrevivido con {vida_j1} HP")
else:
   print("Ha sido un empate")

#Adivina el número

#Crea un número random 1 y 100