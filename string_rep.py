#Crea un programa que cuente el número de veces que aparece una palabra en una string

frase_user = input("Introduce una frase: ")
base_palabras = dict()
frase_lista = frase_user.split()

for palabra in frase_lista:
    if palabra in base_palabras :
        base_palabras[palabra] += 1
    else:
        base_palabras[palabra] = 1

print(base_palabras)