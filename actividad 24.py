print("Ingresa tu gasto total para ver si llegas al descuento")
valor1 = float(input("Gasto total: "))

if valor1 >= 100:
    descuento = valor1 * 0.15
    final = valor1 - descuento
    print(f"Felicidades se te a aplicado el descuento tu monto final es: {final}")

elif valor1 >= 0:
    print("No as alcanzado el monto necesario para aplicar el descuento")

else:
    print("El monto no puede ser negativo")