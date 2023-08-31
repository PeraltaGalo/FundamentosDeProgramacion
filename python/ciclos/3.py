max_valor = float(input("Ingrese un valor: "))
max_orden = 1

for i in range(2, 476):
    valor = float(input("Ingrese un valor: "))
    
    if valor > max_valor:
        max_valor = valor
        max_orden = i

print("Valor máximo:", max_valor)
print("Orden de lectura:", max_orden)
