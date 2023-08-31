x_mayor_y = 0
y_mayor_x = 0

for _ in range(50):
    x = float(input("Ingrese el valor de x: "))
    y = float(input("Ingrese el valor de y: "))
    
    if x > y:
        x_mayor_y += 1
    elif y > x:
        y_mayor_x += 1

print("Pares con x > y:", x_mayor_y)
print("Pares con y > x:", y_mayor_x)
