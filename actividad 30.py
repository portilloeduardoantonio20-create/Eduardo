num1 = float(input("ingresa el primer numero: "))
num2 = float(input("ingresa el segundo numero: "))
num3 = float(input("ingresa el tercer numero: "))

if num1>num2:
    if num1>num3:
        print(f"El numero mayor es: {num1}")
elif num2 >num1:
    if num2>num3:
        print(f"El numero mayor es: {num2}")
    else:
        print(f"El numero mayor es: {num3}")