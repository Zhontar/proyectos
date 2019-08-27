
numero_usuario = (input("Introduzca un numero: (Escriba 'buscar' para finalizar) "))
serie = []

while numero_usuario != "buscar":
    if numero_usuario.isnumeric():
        serie.append(int(numero_usuario))
        numero_usuario = (input("Introduzca un numero: (Escriba 'buscar' para finalizar) "))
    else:
        numero_usuario = (input("Introduzca un numero: (Escriba 'buscar' para finalizar) "))

print(f"esta es tu lista de números:{serie}")

min = serie[0]

for pos in serie:
    if pos < min:
        min = pos

print(f"El numero mas bajo de esa serie es {min}")

