print("Para determinar el costo de tu paquete necesitamos saber su peso y el rango de envío del paquete")

peso = float(input("Ingresa el peso del paquete en kilogramos: "))

distancia = input("Necesitamos saber el rango de envío del paquete: nacional o internacional: ").lower()

if distancia == "nacional":
    print(f"Debido a que tu rango es {distancia} y el peso es de {peso} kg el costo por el envío es de {peso * 3}$")
elif distancia == "internacional":
    print(f"Debido a que tu rango es {distancia} y el peso es de {peso} kg el costo por el envío es de {peso * 6}$")
else:
    print("Por favor ingresa una opción válida: nacional o internacional")