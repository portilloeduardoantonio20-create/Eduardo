numeros = [1, 2, 2, 3, 4, 4, 5]

sin_duplicados = []

for numero in numeros:
    if numero not in sin_duplicados:
        sin_duplicados.append(numero)

print(f"Lista sin duplicados: {sin_duplicados}")