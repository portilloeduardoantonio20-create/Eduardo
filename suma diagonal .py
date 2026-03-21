matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

suma = 0

for i in range(len(matriz)):
    suma += matriz[i][i]

print(f"Suma total: {suma}")