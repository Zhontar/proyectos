#Crea un programa que sea capaz de guardar los nombres de tus amigos y sus años de nacimiento.

salida = False
agenda = dict()

while not salida:
    accion = input("Qué deseas hacer: [Añadir nombre[A] / Consultar fecha[C] / Salir[S]: ]")

    if accion == "A":
        print("Vamos a añadir un nombre: ")
        print("----------------------------")
        nombre = input("Dime el nombre: ")
        fecha = input("Fecha de nacimiento: ")
        agenda[nombre] = fecha

    elif accion == "C":
        print("Vamos a consultar una fecha: ")
        print("-----------------------------")
        nombre = input("Dime el nombre: ")
        print(agenda[nombre])

    elif accion == "S":
        salida = True



