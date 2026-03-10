print("combierte un 0 a 100 en A, B, C, D, F")

valor = float(input("ingresa un numero entre 0 y 100: "))

if 90<valor<100:
    print(f"El numero {valor} es equivalente a la letra A")
elif 80<valor<70:
    print(f"El numero {valor} es equivalente a la letra B")
elif 60<valor<50:
    print(f"El numero {valor} es equivalente a la letra C")
elif 40<valor<30:
    print(f"El numero {valor} es equivalente a la letra D")
elif 20<valor<0:
    print(f"El numero {valor} es equivalente a la letra F")
else:
    print(f"Este numero no se encuentra entre 0 y 100")