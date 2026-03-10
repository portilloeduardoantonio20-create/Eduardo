print("ingresa tu edad para determinar si eres niño, adolecente, adulto o anciano")
edad = int(input("ingresa tu edad: "))

if 0<edad<11:
    print("Eres un niño")
elif 12<edad<19:
    print("Eres un adolesente")
elif 20<edad<59:
    print("Eres un adulto")
elif 60<edad<100:
    print("Eres un adulto mayor")
elif edad<0:
    print("Aun no as nacido")
else:
    print("ingresa una edad valida ")