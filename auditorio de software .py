def revisar_suscripciones(anidado, actual):
    vencidos = []

    for email, datos in anidado.items():
        if datos["mes_vencimiento"] < actual:
            vencidos.append((email, datos["plan"]))

    return vencidos


usuarios = {
    "a@mail.com": {"plan": "pro", "mes_vencimiento": 2},
    "b@mail.com": {"plan": "basic", "mes_vencimiento": 6}
}
print(f"Usuarios vencidos: {revisar_suscripciones(usuarios, 5)}")