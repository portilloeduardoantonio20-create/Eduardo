lista1 = [1, 2, 3, 4]
lista2 = [3, 4, 5, 6]

interseccion = []

for elemento in lista1:
    if elemento in lista2 and elemento not in interseccion:
        interseccion.append(elemento)

print(f"Intersección: {interseccion}")