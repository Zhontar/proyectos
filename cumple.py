#Crea un programa que te diga cuando falta para tu cumpleaños y que día de la semana será.

import datetime

dia = int(input("Dime el dia: "))
mes = int(input("Dime el mes: "))
año = int(input("Dime el año: "))

fecha = datetime.datetime(año, mes, dia)
saber = fecha - datetime.datetime.now()
dia_semana = fecha.weekday()
dia_nombre = ""

if dia_semana == 0:
    dia_nombre = "Lunes"
if dia_semana == 1:
    dia_nombre = "Martes"
if dia_semana == 2:
    dia_nombre = "Miercoles"
if dia_semana == 3:
    dia_nombre = "Jueves"
if dia_semana == 4:
    dia_nombre = "Viernes"
if dia_semana == 5:
    dia_nombre = "Sábado"
if dia_semana == 6:
    dia_nombre = "Domingo"

print("Faltan para tu cumpleaños: {} y cae en {}".format(saber, dia_nombre))
