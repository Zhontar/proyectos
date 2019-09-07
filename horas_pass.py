#Crea un programa que te diga, introduciendo cualquier fecha, cuantas horas han pasado desde ese momento.

import datetime

dia = int(input("Dime el dia: "))
mes = int(input("Dime el mes: "))
año = int(input("Dime el año: "))

fecha = datetime.datetime(año, mes, dia)

dias_pasados = datetime.datetime.now() - fecha

horas = dias_pasados.total_seconds() / 3600

print("Han pasado {} horas desde {}".format(horas, fecha))