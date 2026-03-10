
valor1 = float(input("Ingrese el primer valor: "))
valor2 = float(input("Ingrese el segundo numero: "))

funcion = input("Ingresa la operación (suma, resta, multiplicacion, division): ")

if funcion == "suma":
    print(f"El resultado es: {valor1 + valor2}")
elif funcion == "resta":
    print(f"El resultado es: {valor1 - valor2}")
elif funcion == "multiplicacion":
    print(f"El resultado es: {valor1 * valor2}")
elif funcion == "division":
    if valor2 != 0:
        print(f"El resultado es: {valor1 / valor2}")
    else:
        print("No se puede dividir entre cero al menos no que yo sepa")
else:
    print("opcion no valida ingresa una funcion que si sea valida")