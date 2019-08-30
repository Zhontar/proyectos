
#Dada una lista mixta de enteros y strings, devolver dos listas, una con todos los enteros y otra con todas las strings

lista_user = input("Introduce un dato: (Escribe 'salir' para terminar el proceso) ")
lista_usuario = []
list_str = []
list_int = []

while lista_user != "salir":
    lista_usuario.append(lista_user)
    lista_user = input("Introduce un dato: (Escribe 'salir' para terminar el proceso) ")


print(f"Esta es tu lista: {lista_usuario}")

for elemento in lista_usuario:
    if elemento.isdigit():
        list_int.append(int(elemento))
    else:
        list_str.append((elemento))

print(f"Esta es la lista de strings: {list_str}")
print(f"Esta es la lista de números: {list_int}")