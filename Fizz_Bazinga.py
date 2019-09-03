#Realizar FizzBuzz con las mismas reglas pero en el caso que el numero sea divisible entre 3 y 5, cambiar el texto por “Bazinga”.

lista_user = (input("Introduce un numero: (Escribr 'go' para inciar) "))
lista_numeros = []
lista_final = []

while lista_user != 'go':
    if lista_user.isdigit():
        lista_numeros.append(int(lista_user))
        lista_user = (input("Introduce un numero: (Escribr 'go' para inciar) "))

print(lista_numeros)

for car in range(len(lista_numeros)):
    numero = lista_numeros[car]

    if numero % 3 == 0 and numero % 5 != 0:
        lista_numeros[car] = ""
        lista_numeros[car] += "fizz"

    elif numero % 5 == 0 and numero % 3 != 0:
        lista_numeros[car] = ""
        lista_numeros[car] += "buzz"

    elif numero % 5 == 0 and numero % 3 == 0:
        lista_numeros[car] = ""
        lista_numeros[car] += "Bazinga"



print(lista_numeros)
