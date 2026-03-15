# Abraham M.R. 23310382

palabra = input("Ingresa una palabra cualquiera: ")
palabra = palabra.upper()
palabra_vocalnt = ""
for letra in palabra:
    if letra == "A" or letra == "E" or letra == "I" or letra == "O" or letra == "U":
        continue
    else:
        palabra_vocalnt = palabra_vocalnt + letra
print(palabra_vocalnt)