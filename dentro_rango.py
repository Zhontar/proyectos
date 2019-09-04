#Escribe una funcion que dado un numero y un rango (otros dos numeros), compruebe que ese numero está dentro del rango

def en_rango(num, min, max):
    if num >= min and num <=max:
        return True
    else:
        return False

print(en_rango(51, 28, 50))