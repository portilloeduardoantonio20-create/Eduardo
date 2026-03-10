
a = int(input("Ingrese el primer número: "))
b = int(input("Ingrese el segundo número: "))
c = int(input("Ingrese el tercer número: "))

if a > b and a > c:
    print(f"El numero mayor es el numero: {a}")
elif b > a and b > c:
    print(f"El numero mayor es el numero: {b}")
else:
    print(f"El numero mayor es el numero: {c}")