numero = int(input("Ingrese un número positivo: "))

if numero < 0:
    print("El número no puede ser negativo")
else:
    factorial = 1

    for i in range(1, numero + 1):
        factorial *= i

    print(f"El factorial es: {factorial}")