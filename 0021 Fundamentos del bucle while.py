# Abraham M.R. 23310382

bloques = int(input("Numero de bloques a acomodar: "))
h = 0
bloques_nec = 1

while bloques >= bloques_nec:
    bloques = bloques - bloques_nec
    h = h + 1
    bloques_nec = bloques_nec + 1

print("La altura de la piramide sera de:", h)