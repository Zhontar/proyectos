#Crear un programa que cambia las vocales por su numero de aparición

frase_user = input("Introduce una frase: ")
frase_sus = ""
vocales = ["a", "A", "e", "E", "o", "O", "u", "U"]
valor = 1

for car in frase_user:
    if car in vocales:
        frase_user = frase_user.replace(car, str(valor), 1)
        valor += 1

print(frase_user)