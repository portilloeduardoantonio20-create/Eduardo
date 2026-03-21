def validar_esquema(payload_dicc, esquema_dicc):
    errores = []

    for clave, tipo in esquema_dicc.items():
        if clave not in payload_dicc:
            errores.append(f"Falta {clave}")
        else:
            if not isinstance(payload_dicc[clave], tipo):
                errores.append(f"Tipo incorrecto en {clave}")

    valido = len(errores) == 0
    return (valido, errores)


payload = {"nombre": "Juan", "edad": 25}
esquema = {"nombre": str, "edad": int}

print(f"Validación: {validar_esquema(payload, esquema)}")