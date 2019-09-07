#Crea un programa que te diga la fecha de hace 5 días respecto a hoy, y el día de la semana.
import datetime

fecha_menos = (datetime.datetime.now() - datetime.timedelta(days= 5))
fecha_pedida = fecha_menos.weekday()
dia_semana = ""

if fecha_pedida == 0:
    dia_semana = "Lunes"
if fecha_pedida == 1:
    dia_semana = "Martes"
if fecha_pedida == 2:
    dia_semana = "Miercoles"
if fecha_pedida == 3:
    dia_semana = "Jueves"
if fecha_pedida == 4:
    dia_semana = "Viernes"
if fecha_pedida == 5:
    dia_semana = "Sábado"
if fecha_pedida == 6:
    dia_semana = "Domingo"

print("Hace cinco dias fue: {} y fué {}".format(fecha_menos.strftime("%d del %m de %Y"), dia_semana))
