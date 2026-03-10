contraseña = 1234
intentos = 3

for i in range(intentos):
    ingreso = input("Ingrese la contraseña: ")

    if ingreso == contraseña:
        print("Acceso concedido")
        break
    else:
        print("Contraseña incorrecta")

else:
    print("Se agotaron los intentos")