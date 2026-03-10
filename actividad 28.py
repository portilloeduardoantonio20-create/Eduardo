print("calculador de peso ideal IMC ")

peso = float(input("Ingresa tu peso en kg: "))
estatura = float(input("Ingresa tu estatura: "))

imc = peso / (estatura ** 2)

print(f"Tu IMC es: {imc:.2f}")

if imc < 18.5:
    print("tu peso es bajo")
elif imc < 25:
    print("tu peso es normal")
elif imc < 30:
    print("tienes sobre peso")
else:
    print("estas muy sobrepasado de peso")