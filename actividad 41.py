limite = int(input("Ingrese el valor límite: "))

suma = 0
numero = 1
contador = 0

while suma < limite:
    suma += numero
    numero += 1
    contador += 1

print(f"La suma total es: {suma}")
print(f"Se necesitaron {contador} numero")