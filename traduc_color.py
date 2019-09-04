#Crea un programa que al decirle el nombre de un color nos devuelva su traducción en inglés

salida = False
traducciones = {"Blanco": "White", "Negro": "Black", "Gris": "Grey", "Rojo": "Red", "Azul": "Blue", "Amarillo": "Yellow",
"Verde": "Green", "Naranja": "Orange", "Marron": "Brown", "Rosa": "Pink", "Violeta": "Violet", "Morado": "Purple", "Dorado": "Golden",
"Plata": "Silver"}

while not salida:
    accion = input("¿Que deseas hacer? : [Traducir color [T] / Salir[S] ]")

    if accion == "T":
        nombre = input("Introduce el nombre en español: ")
        print(traducciones[nombre])

    else:
        salida = True

        