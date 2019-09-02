
#Crear un programa que cambie todas las ‘A’ o ‘a’ por la string ‘VACA’ de una string introducida por el usuario.

frase_user = input("introduce una frase: ").upper()
frase_alterada = []

for car in frase_user:
        frase_alterada = frase_user.replace("A", "VACA")

print(f"Esta es tu frase alterada: {frase_alterada.lower()}")