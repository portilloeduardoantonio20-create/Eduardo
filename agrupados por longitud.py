def agrupar(valor1):
    resultado = {}

    for palabra in valor1:
        longitud = len(palabra)

        if longitud not in resultado:
            resultado[longitud] = []

        resultado[longitud].append(palabra)

    return resultado


palabras = ("hola","mundo"  "sol", "eduardo", "luz")
print(agrupar(palabras))