sist1 = 0
sist2 = 0
sist3 = 0

for _ in range(1200):
    respuesta = int(input("Ingrese respuesta (1, 2 o 3): "))
    
    if respuesta == 1:
        sist1 += 1
    elif respuesta == 2:
        sist2 += 1
    elif respuesta == 3:
        sist3 += 1

if sist1 > sist2 and sist1 > sist3:
    preferido = 1
elif sist2 > sist1 and sist2 > sist3:
    preferido = 2
else:
    preferido = 3

print("Sistema operativo preferido:", preferido)
