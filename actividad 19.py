
num1 = int(input("ingresa el primer numero: "))
num2 = int(input("ingresa el segundo numero: "))

valor1 = num1 % num2

if valor1 % 2 == 0:
    print(f"El numero: {valor1} es par")
        
else:
    print(f"El numero: {valor1} es impar")