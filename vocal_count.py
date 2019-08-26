

user_input = input("Introduzca una frase: ")

vocal = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
lista = []

for pos in user_input:
    if pos in vocal:
        lista.append(pos)

print("Las vocales de esa frase son {}".format(lista))

