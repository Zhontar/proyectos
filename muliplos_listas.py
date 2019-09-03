#Crear un programa que guarde e imprima varias listas y sean múltiplos de 2, de 3, de 5 y de 7.

lista_user = input("Introduce un numero: (Escribe 'go' para iniciar) ")
lista_numeros = []

while lista_user != 'go':
    if lista_user.isdigit():
        lista_numeros.append(int(lista_user))
        lista_user = (input("Introduce un numero: (Escribr 'go' para inciar) "))

print(lista_numeros)

multiplos_dos = []
multiplos_tres = []
multiplos_cinco = []
multiplos_siete = []

for car in lista_numeros:
    if car % 2 == 0:
        multiplos_dos.append(car)
    if car % 3 == 0:
        multiplos_tres.append(car)
    if car % 5 == 0:
        multiplos_cinco.append(car)
    if car % 7 == 0:
        multiplos_siete.append(car)

print(f"multiplos de dos: {multiplos_dos}")
print(f"multiplos de tres: {multiplos_tres}")
print(f"multiplos de cinco: {multiplos_cinco}")
print(f"multiplos de siete: {multiplos_siete}")
