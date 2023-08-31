primer_carta = input("Ingrese la primera carta (palo y número): ")
mazo = set()

contador = 1

while True:
    carta = input(f"Ingrese la carta {contador + 1} (palo y número): ")
    if carta[0] == primer_carta[0] and carta[1:] > primer_carta[1:]:
        break
    mazo.add(carta)
    contador += 1

print(f"Se necesitaron {contador} cartas para encontrar una del mismo palo y mayor número.")
