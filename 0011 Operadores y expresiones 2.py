# Abraham M.R. 23310382

print("Por favor ingrese los datos en formato de 24 horas")
horas = int(input("Hora de inicio (horas): "))
minutos = int(input("Minuto de inicio (minutos): "))
evento = int(input("Duración del evento (minutos): "))
minutos = minutos + evento 
horas = horas + minutos // 60 
minutos = minutos % 60 
horas = horas % 24 
print(horas, ":", minutos, sep='')