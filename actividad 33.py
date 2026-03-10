print ("coloca los 3 lados para determinar el triangulo")

a = float(input("Lado 1: "))
b = float(input("Lado 2: "))
c = float(input("Lado 3: "))

if a + b > c and a + c > b and b + c > a:

    if a == b == c:
        print("Triángulo equilátero")

    elif a == b or a == c or b == c:
        print("Triángulo isósceles")

    else:
        print("Triángulo escaleno")

else:
    print("No forma un triángulo válido")