texto = input("Introduce una cadena de texto: ")
texto = texto.lower()
texto = texto.replace(" ", "")
contados = []

for c in texto:
    if c not in contados:
        contador = 0
        for x in texto:
            if x == c:
                contador += 1
        print(f"{c}: {contador} veces")
        contados.append(c)