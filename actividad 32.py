

print("Este es un sistema que te recomienda una pelica segun tu edad y tu presupusto")

edad = int(input("Ingresa tu edad: "))
presupuesto = float(input("Ingresa tu presupuesto para la pelicula: "))

if 5 < edad < 13 and 8 < presupuesto < 12:
    print(f"Ya que tu edad es de {edad} años y tu presupuesto es de {presupuesto}$ te recomindo las siguientes peliculas")
    valor1 = input("1: El rey leon \n2:El libro de la selva \n3:Pinocho \ncual deseas ver:")

    if valor1 == "El rey leon" or valor1 == "1":
        print("Espero disfrutes de la pelicula")

    elif valor1 == "El libro de la selva" or valor1 == "2":
        print("Espero disfrutes de la pelicula")

    elif valor1 == "Pinocho" or valor1 == "3":
        print("Espero disfrutes de la pelicula")

    else:
        print("elije una de las propuesta que son las de tu presupuesto")

elif 14 < edad < 17 and 13 < presupuesto < 18:
    print(f"Ya que tu edad es de {edad} años y tu presupuesto es de {presupuesto}$ te recomiendo las siguientes peliculas ")
    valor2 = input("1:Son como niños \n2:Dragon ball Z \n3:Naruto shippuden")

    if valor2 == "Son como niños" or valor2 == "1":
        print("Espero disfrutes de la pelicula")

    elif valor2 == "Dragon ball Z" or valor2 == "2":
        print("Espero disfrutes de la pelicula")

    elif valor2 == "Naruto shippuden" or valor2 == "3":
        print("Espero disfrutes de la pelicula")

    else:
        print("elije una de las peliculas propuesta que son las de tu presupuesto")

elif 18 < edad < 90 and 20 < presupuesto < 22:
    print(f"Ya que tu edad es de {edad} años y tu presupuesto es de {presupuesto}$ te recomiendo las siguintes peliculas")
    print(f"Ya que tu edad es de {edad} años y tu presupuesto es de presupuesto es de {presupuesto}$ te recomiendo la siguientes peliculas")
    valor3 = input("1:50 sombras de black \n2:El conjuro \n3:Scary Movey")

    if valor3 == "50 sombras de black" or valor3 == "1":
        print("Espero disfrutes de la pelicula")

    elif valor3 == "El conjuro" or valor3 == "2":
        print("Espero disfrutes de la pelicula")

    elif valor3 == "Scary Movey" or valor3 == "3":
        print("Espero disfrutes de la pelicula")

    else:
        print("elije una de las peliculas propuestas ")

else:
    print("no hay recomendaciones disponibles")