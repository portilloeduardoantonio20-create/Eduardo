def recomendar_peliculas(tupla_vistas, lista_catalogo_diccs):
    recomendaciones = {}

    for peli in lista_catalogo_diccs:
        if peli["titulo"] not in tupla_vistas:
            genero = peli["genero"]

            if genero not in recomendaciones:
                recomendaciones[genero] = []

            recomendaciones[genero].append(peli["titulo"])

    return recomendaciones


vistas = ("Matrix",)
catalogo = [
    {"titulo": "Matrix", "genero": "Sci-Fi"},
    {"titulo": "Titanic", "genero": "Romance"},
    {"titulo": "Avengers", "genero": "Accion"}
]

print(f"Recomendaciones: {recomendar_peliculas(vistas, catalogo)}")