

pokemon_elegido = input("¿Contra que pokemon quieres luchar? (Squirtle / Charmander / Bulbasaur):").upper()
vida_enemigo = 0
ataque_enemigo = 0
vida_picachu = 100

if pokemon_elegido == "SQUIRTLE":
    vida_enemigo = 90
    ataque_enemigo = 8
    nombre_pokemon = "SQUIRTLE"

elif pokemon_elegido == "CHARMANDER":
    vida_enemigo = 80
    ataque_enemigo = 7
    nombre_pokemon = "CHARMANDER"

elif pokemon_elegido == "BULBASAUR":
    vida_enemigo = 100
    ataque_enemigo = 9
    nombre_pokemon = "BULBASAUR"

while vida_picachu >0 and vida_enemigo >0:
    ataque_elegido = input("¿Que ataque quieres hacer? ( Chispazo / Bola voltio)").upper ()
    if ataque_elegido == "CHISPAZO":
        vida_enemigo -= 20
    elif ataque_elegido == "BOLA VOLTIO":
        vida_enemigo -= 32

    print("La vida de {} es ahora de {}".format(nombre_pokemon, vida_enemigo))

    vida_picachu -= ataque_enemigo
    print("{} te hace {} de daño".format(nombre_pokemon, ataque_enemigo))
    print("La vida de Picachu es de {}".format(vida_picachu))

print("El combate ha terminado")

if vida_picachu > 0:
    print("Has ganado")
else:
    print("Has perdido")