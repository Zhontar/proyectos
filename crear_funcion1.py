#Escribe una función que encuentre el numero más grande entre 3 numeros

def mas_grande(uno, dos, tres):
    maximo = 0

    for num in (uno, dos, tres):
        if num > maximo:
            maximo = num
    return maximo

print(mas_grande(15, 28, 68))




