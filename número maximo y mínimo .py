numeros = [12, 45, 3, 67, 23, 89, 1]

maximo = numeros[0]
minimo = numeros[0]

for numero in numeros:
    if numero > maximo:
        maximo = numero
    if numero < minimo:
        minimo = numero

print(f"Máximo: {maximo}")
print(f"Mínimo: {minimo}")