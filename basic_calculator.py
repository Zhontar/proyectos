

print("Bienvenido a la calculadora básica")

operacion = input("¿Que operación quieres realizar? (sumar / restar / multiplicar / dividir)").upper()
primer_numero = float(input("primer numero: "))
segundo_numero = float(input("segundo numero: "))
resultado = 0

if operacion == "SUMAR":
    resultado = primer_numero + segundo_numero

elif operacion == "RESTAR":
    resultado = primer_numero - segundo_numero

elif operacion == "MULTIPLICAR":
    resultado = primer_numero * segundo_numero

elif operacion == "DIVIDIR":
    resultado = primer_numero / segundo_numero

print("Resultado es: {}".format(resultado))



