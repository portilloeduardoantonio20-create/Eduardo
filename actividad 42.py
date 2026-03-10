contador = 0

while True:
    numero = int(input("Ingrese un número: "))

    if numero < 0:
        break
    else:
        contador += 1

print(f"Cantidad de numeros positivos ingresados son : {contador}")