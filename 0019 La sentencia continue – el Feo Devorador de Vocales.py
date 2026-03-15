# Abraham M.R. 23310382

palabra = input("Ingresa una palabra cualquiera: ")
palabra = palabra.upper()

for letra in palabra:
    if letra == "A" or letra == "E" or letra == "I" or letra == "O" or letra == "U":
        continue
    print(letra)