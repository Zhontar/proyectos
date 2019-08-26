
input_usuario = input("Introduce una frase: ")

puntos = ["."]
comas = [","]
espacios = [" "]

n_puntos = 0
n_comas = 0
n_espacios = 0

for punt in input_usuario:
    if punt in puntos:
        n_puntos += 1
    elif punt in comas:
        n_comas += 1
    elif punt in espacios:
        n_espacios += 1

print("Hay {} punto/s en la frase".format(n_puntos))
print("Hay {} coma/s en la frase".format(n_comas))
print("Hay {} espacio/s en la frase".format(n_espacios))
