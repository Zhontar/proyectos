#Dada una lista de strings, devolver una lista con el largo de cada string

strings = input("introduce una string: (Escribe 'charcount' para contar los caracteres de cada string) ")
lista_strings = []
largo_str = []

while strings != "charcount":
    lista_strings.append(strings)
    strings = input("introduce una string: (Escribe 'charcount' para contar los caracteres de cada string) ")


for str in lista_strings:
    len(str)
    largo_str.append(len(str))

print(largo_str)