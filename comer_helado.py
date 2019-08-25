
apetece_helado_input = input("¿Te apetece un helado? (Si/No)").upper()

if apetece_helado_input == "SI":
    apetece_helado = True
elif apetece_helado_input == "NO":
    apetece_helado = False
else:
    print("O si o no, pero no me aburras, cuento como que no..")


tiene_dinero_input = input("¿Tienes dinero para comprarlo? (Si/No)").upper()

if tiene_dinero_input == "SI":
    tiene_dinero = True
elif tiene_dinero_input == "NO":
     tiene_dinero= False
else:
    print("O si o no, pero no me aburras, cuento como que no..")

esta_senor_helados_input = input("¿Esta el señor de los helados? (Si/No)").upper()

if esta_senor_helados_input == "SI":
    esta_senor_helados = True
elif esta_senor_helados_input == "NO":
    esta_senor_helados = False
else:
    print("O si o no, pero no me aburras, cuento como que no..")


esta_tia_input = input("¿Estas con tu tia? (Si/No)").upper()

if apetece_helado_input == "SI":
    apetece_helado = True
elif apetece_helado_input == "NO":
    apetece_helado = False
else:
    print("O si o no, pero no me aburras, cuento como que no..")


apetece_helado = apetece_helado_input == "SI"
puede_permitirselo = tiene_dinero_input == "SI" or esta_tia_input == "SI"
esta_senor_helados = esta_senor_helados_input == "SI"


if apetece_helado and puede_permitirselo and esta_senor_helados:
    print("Pues comete un helado")
else:
    print("Pues nada")
