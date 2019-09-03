#Crear un programa que encuentre el numero más grande de una lista (sin usar la función max)

lista_user = input("Introduce un numero: (Escribe 'go' para iniciar) ")
lista_numeros = []

while lista_user != 'go':
    if lista_user.isdigit():
        lista_numeros.append(int(lista_user))
        lista_user = (input("Introduce un numero: (Escribr 'go' para inciar) "))

print(lista_numeros)

mayor = 0

for car in lista_numeros:
    if car > mayor:
        mayor = car

print(f"El número mayor de tu lista es: {mayor}")