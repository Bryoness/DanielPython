
# def suma(a, b):
#     print(a+b)

# suma(22, 363)

# notas1=[6.3,6.8, 3.7, 2.1]
# notas2=[6.3,1.8, 3.9, 2.1]

# def creaProm(n):
#    return round(sum(n)/len(n),1)


# print("El promedio del notas 1 es", creaProm(notas1))
# print("El promedio del notas 2 es", creaProm(notas2))

pinturas=[
    {"color": "verde", "capacidad": 1500, "formato": "tarro"}, #0
    {"color": "azul", "capacidad": 1500, "formato": "tarro"}, #1
    {"color": "blanco", "capacidad": 3500, "formato": "tinaja"}, #2
    {"color": "purpura", "capacidad": 500, "formato": "bolsa"}, #3
]
listaColores=[]
for i in pinturas:
    print(f"{i["color"]}")
    listaColores.append({i["color"]})
print(listaColores)

listaCapacidad=[]
for i in pinturas:
    print(f"{i["capacidad"]}")
    listaCapacidad.append({i["capacidad"]})
print(listaCapacidad)

print(min(listaCapacidad))

def mayorCap(lista):
    listaCapacidad=[]
    for p in lista:
        listaCapacidad.append(p["capacidad"])
        return max(listaCapacidad)    
print(mayorCap(pinturas))    