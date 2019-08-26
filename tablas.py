
numero_tabla = int(input("¿De que numero deseas botener su tabla?: "))

for multiplo in range(1, 11):
    if multiplo % 2 == 0:
        print(f"{numero_tabla} x {multiplo} = {numero_tabla * multiplo}")