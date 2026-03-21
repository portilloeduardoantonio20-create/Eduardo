numeros = [1, 2, 3, 4, 5]

invertida = []

for i in range(len(numeros) - 1, -1, -1):
    invertida.append(numeros[i])

print(f"Lista invertida:  {invertida}")