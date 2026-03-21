def rutina(diccs, meta):
    total = 0

    for dia in diccs:
        total += dia["calorias"]

    cumple = total >= meta

    return (total, cumple)


historial = [{"calorias": 500}, {"calorias": 700}]
resultado = rutina(historial, 1000)
print(f"Total calorías: {resultado[0]}, ¿Cumplió meta?: {resultado[1]}")