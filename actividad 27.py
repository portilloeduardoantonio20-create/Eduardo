print("Sistema de autorizacion")

puesto = input("\n1: administrador\n2: trabajador\n3: vendedor\nIngresa tu puesto: ").lower()

if puesto == "administrador" or puesto == "1":
    print("Puesto admitido, ingresa la clave para continuar")
    clave = int(input("Clave: "))
    
    if clave == 1234:
        print("Clave correcta, acceso aprobado")
    else:
        print("Clave incorrecta, acceso denegado")

elif puesto == "trabajador" or puesto == "2":
    print("Trabajador sin autorizacion")

elif puesto == "vendedor" or puesto == "3":
    print("Puesto no autorizado")

else:
    print("Colocar una opcion valida")