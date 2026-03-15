# Abraham M.R. 23310382

anio = int(input("Introduce un año: "))
if anio < 1582:
	print("No esta dentro del periodo del calendario Gregoriano")
else:
	if anio % 4 != 0:
		print("Año Comun")
	elif anio % 100 != 0:
		print("Año Bisiesto")
	elif anio % 400 != 0:
		print("Año Comun")
	else:
		print("Año Bisiesto")