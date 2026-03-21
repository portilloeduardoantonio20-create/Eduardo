def ruta(lista_diccs):
    urgente = []
    normal = []

    for paquete in lista_diccs:
        if paquete["urgente"]:
            urgente.append((paquete["id"], paquete["distancia"]))
        else:
            normal.append((paquete["id"], paquete["distancia"]))

    urgente.sort(key=lambda x: x[1])
    normal.sort(key=lambda x: x[1])

    return {
        "prioritaria": urgente,
        "normal": normal
    }


paquetes = [
    {"id": 1, "distancia": 10, "urgente": True},
    {"id": 2, "distancia": 5, "urgente": False}
]

print(f"Rutas organizadas: {ruta(paquetes)}")