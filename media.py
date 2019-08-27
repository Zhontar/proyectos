
#Crea un programa que calcule la media de los elementos de la lista de números introducida por el usuario.

numero_usuario = (input("Introduzca un número: (Escriba 'media' para finalizar) "))
serie = []

while numero_usuario != "media":
    if numero_usuario.isnumeric():
        serie.append(int(numero_usuario))
        numero_usuario = (input("Introduzca un número: (Escriba 'media' para finalizar) "))
    else:
        numero_usuario = (input("Introduzca un número: (Escriba 'media' para finalizar) "))

largo_lista = 0

for pos in serie:
    largo_lista += 1

suma = sum(serie)

media = suma / largo_lista

print(f"La media de los números introducidos es: {media}")




