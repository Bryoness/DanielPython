#Uso y explicación de listas:
#      -5     -4    -3   -2   -1
lista=[91,   -7,    44,   88,  4]
#       0      1     2     3   4
print(lista)
print(lista[3])

for i in lista:
    print(i)



pokemons=["Leafeon", "Ivysaur", "Metagross", "Psyduck", "Snorlax"]
print(pokemons[2])
print(len(pokemons[2]))

for p in pokemons:
    print(p.upper())


#Hacer una lista de 5 frutas, y que muestre cuántas frutas terminan con A

frutas=["Pepino", "Piña", "Pera", "Plátano", "Mango"]

for f in frutas:
    if f[-1].lower() == "a":
        print(f"La fruta {f} terminaa en A ")
    else:
        print(f"La fruta {f} NO termina en A ")