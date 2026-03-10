print("LOSP")
print("As viajado en una avioneta que se termina accidentando  y terminas en sentro de lo que parece ser una especie de isla ")

opcion = input("Piensas que debes buscar la manera de llegar a la avioneta asi que te pones a ver la zona y observas dos caminos un camino por la derecha y otro por la izquirda que camino decides tomar \n derecha o izquierda \n: ").lower()

if opcion == "derecha":
    print(f"El camino de la {opcion} se ve despejado pero a medida que avansas sientes la tierra mas floja en cada pisada y escuchas ruidos adelante")
    
    opcion1 = input("Que decides hacer avansar o devolverte ")
    if opcion1 == "avansar":
        print(f"Terminas tropesando y callendo por un acantilado y perdiendote")
        print("FIN")
    elif opcion1 == "devolverte":
        print("No logras encontrar la manera de llegar y terminas perdido en la isla")
        print("FIN")
    else:
        print("opcion no valida")
        
elif opcion == "izquierda":
    print(f"El camino de la {opcion} te muestra un camino que parece llevarte a la playa donde se encuentra la avioneta pero antes de llegar encuentras un cofre perteneciente a la cabima de la avioneta que decides hacer")
    opcion2 = input("revisar el cofre \n ir directo a la avioneta \n:")
    
    if opcion2 == "revisar el cofre":
        print(f"Resulta encontrarse la caja negra dentro activas la obicasion ")
        print("As sido rescapado")
    elif opcion2 == "ir directo a la avioneta":
        print("La avioneta se encuentra dañada empiesas a buscar la manera de arreglarla y terminas probocando un axidente  ")
        print("FIN")
    else:
        print("opcion no valida")
else:
    print("opcion no valida")