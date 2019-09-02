#Crear un programa que le repita al usuario lo que dice pero con todas las vocales cambiadas por i.

frase_user = input("Introduzca una frase: ")
frase_modificada = []
vocales = ["a", "A", "e", "E", "o", "O", "u", "U"]

for car in frase_user:
    if car in vocales:
        frase_user = frase_user.replace(car, "i")

print(frase_user)