#Votatoon
toon1=input("Ingrese el Toon 1: ")
toon2=input("Ingrese el Toon 2: ")

v1=0
v2=0
votantes=int(input("¿Cuántos votantes son? "))

while votantes>0:
    #Pedir votos
    voto=int(input(f"¿Por quién votará? 1.-{toon1} 2.- {toon2} "))
    if voto==1:
        v1+=1
    elif voto==2:
        v2+=1
    else:
        print("Voto nulo")
    votantes-=1

if v1>v2:
    print(f"Ganó {toon1} con {v1} votos")
elif v2>v1:
    print(f"Ganó {toon2} con {v2} votos")
else:
    print(f"Ha sido un empate")  