nombre = str(input("ingrese su nombre: "))
año_de_nacimiento = float(input("ingrese año de nacimiento: "))
año_actual = float(input("ingrese año actual: "))

edad = año_actual - año_de_nacimiento

mayor = edad > 18

print(f"La edad de {nombre} es: {mayor} ")