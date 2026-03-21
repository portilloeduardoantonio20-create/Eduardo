def emparejar_jugadores(lista_diccs):
    parejas = []

    for i in range(len(lista_diccs)):
        for j in range(i + 1, len(lista_diccs)):
            j1 = lista_diccs[i]
            j2 = lista_diccs[j]

            if j1["region"] == j2["region"]:
                diferencia = abs(j1["nivel"] - j2["nivel"])

                if diferencia <= 5:
                    parejas.append((j1["id"], j2["id"]))

    return parejas


jugadores = [
    {"id": 1, "region": "NA", "nivel": 10},
    {"id": 2, "region": "NA", "nivel": 13},
    {"id": 3, "region": "EU", "nivel": 9}
]

print(f"Parejas encontradas: {emparejar_jugadores(jugadores)}")