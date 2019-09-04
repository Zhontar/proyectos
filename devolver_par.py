#Escribe una función que reciba una lista de números y devuelva otra pero conteniendo solo los números pares.

def devolver_par(lista):

    lista_par = []

    for num in lista:
        if num % 2 == 0:
            lista_par.append(num)
    return lista_par

print(devolver_par([51, 287, 846, 258, 241]))