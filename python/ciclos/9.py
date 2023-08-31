mayores_15 = 0
mayores_50 = 0
entre_25_45 = 0

for _ in range(100):
    numero = int(input("Ingrese un número: "))
    
    if numero > 15:
        mayores_15 += 1
    if numero > 50:
        mayores_50 += 1
    if 25 <= numero <= 45:
        entre_25_45 += 1

print("Números mayores que 15:", mayores_15)
print("Números mayores que 50:", mayores_50)
print("Números entre 25 y 45:", entre_25_45)
