

player1_num = int(input("Elige numero, y que no lo veo tu amigo: "))
player2_num = int(input("Adivina el numero: "))

while player2_num != player1_num:
    print("No es ese numero, intentalo otra vez: ")
    player2_num = int(input("Adivina el numero: "))

print("¡Acertaste! El numero elegido era el {}".format(player1_num))