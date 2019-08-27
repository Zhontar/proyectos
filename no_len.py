
# Programa que cuente los elementos de la lista de números introducida por el usuario.
# Está prohibido utilizar la función len() para resolver el problema.

numero_usuario = (input("Introduzca un número: (Escriba 'contar' para finalizar) "))
serie = []

while numero_usuario != "contar":
    if numero_usuario.isnumeric():
        serie.append(int(numero_usuario))
        numero_usuario = (input("Introduzca un número: (Escriba 'contar' para finalizar) "))
    else:
        numero_usuario = (input("Introduzca un número: (Escriba 'contar' para finalizar) "))

largo_lista = 0

for pos in serie:
    largo_lista += 1

print(f"La lista contiene {largo_lista} números.")
print(serie)