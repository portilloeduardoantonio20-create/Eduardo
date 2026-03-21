def convertir_monedas(precios, tasas):
    resultado = []

    for precio in precios:
        conversiones = {}

        for moneda, tasa in tasas.items():
            conversiones[moneda] = precio * tasa

        resultado.append((precio, conversiones))

    return resultado


precios = [10, 20]
tasas = {"EUR": 0.9, "COP": 4000}
print(f"Conversiones: {convertir_monedas(precios, tasas)}")