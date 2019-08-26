

input_usuario = input("Introduce una frase: ")

n_mayus = 0
for letra in input_usuario:
    if letra.isupper():
        n_mayus += 1

print("El numero de mayusculas en esa frase es {}".format(n_mayus))

