suma = 0
producto = 1

for num in range(20, 501):
    if num % 2 == 0:
        suma += num
        producto *= num

print("Suma de números pares:", suma)
print("Producto de números pares:", producto)
