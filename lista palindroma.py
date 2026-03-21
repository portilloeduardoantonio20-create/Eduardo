lista = [1, 2, 3, 2, 1, ]

palindromo = True

for i in range(len(lista) // 2):
    if lista[i] != lista[-(i + 1)]:
        palindromo = False
        break

print(f"Es palíndromo? : {palindromo}")