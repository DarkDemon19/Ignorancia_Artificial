# Abraham M.R. 23310382

numerito = 382
condicion = False
print(
    """
    +=========================================+
    |  ¡Bienvenido a mi juego, Ser no magico! |
    |       Introduce un numero entero        |
    |        y adivina que numero he          |
    |           elegido para ti.              |
    |   Entonces,¿Cuál es el numero secreto?  |
    +=========================================+
    """)
while(condicion == False):
    eleccion = int(input("Ingresa el numero: "))
    if eleccion == numerito:
        condicion = True
    else: 
        print("¡Ja, ja, ja! ¡Estas atrapado en mi bucle infinito!")
print("¡Bien hecho, Ser no magico! Eres libre por ahora.")