def procesar_votacion(votos, vetados):
    conteo = {}

    for usuario, voto in votos:
        if usuario not in vetados:
            if voto not in conteo:
                conteo[voto] = 0
            conteo[voto] += 1

    return conteo


votos = [("u1", "A"), ("u2", "B"), ("u3", "A")]
vetados = ("u2",)
print(f"Resultado votación: {procesar_votacion(votos, vetados)}")