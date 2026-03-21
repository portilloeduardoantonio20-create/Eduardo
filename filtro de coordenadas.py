def hemisferio(lista):
    resultado = []

    for lat, lon in lista:
        if lat > 0:
            coord = {
                "latitud": lat,
                "longitud": lon
            }
            resultado.append(coord)

    return resultado


coords = [(10, -70), (-5, 30), (25, 60)]
print(hemisferio(coords))