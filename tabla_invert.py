

numero_usuario = int(input("Introduzca el numero: "))

for multiplo in reversed(range(1, 11)):
   print(f"{numero_usuario} x {multiplo} = {multiplo * numero_usuario}")
