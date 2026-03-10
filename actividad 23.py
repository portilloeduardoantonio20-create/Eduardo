
print("Ingrese los numeros a comparar")
num1 = float(input("Ingrese el primer numero: "))
num2 = float(input("Ingrese el segundo numero: "))

if num1 < num2:
    print(f"{num1} es menor que {num2}")
elif num1 == num2:
    print(f"{num1} es igual a {num2}")
else:
    print(f"{num1} es mayor que {num2}")