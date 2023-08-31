porcentaje_producto1 = float(input("Ingrese el porcentaje de aceptación del producto 1: "))
porcentaje_producto2 = float(input("Ingrese el porcentaje de aceptación del producto 2: "))
porcentaje_producto3 = float(input("Ingrese el porcentaje de aceptación del producto 3: "))

producto_mas_aceptado = None
producto_menos_aceptado = None

if porcentaje_producto1 > porcentaje_producto2 and porcentaje_producto1 > porcentaje_producto3:
    producto_mas_aceptado = "Producto 1"
elif porcentaje_producto2 > porcentaje_producto1 and porcentaje_producto2 > porcentaje_producto3:
    producto_mas_aceptado = "Producto 2"
else:
    producto_mas_aceptado = "Producto 3"

if porcentaje_producto1 < porcentaje_producto2 and porcentaje_producto1 < porcentaje_producto3:
    producto_menos_aceptado = "Producto 1"
elif porcentaje_producto2 < porcentaje_producto1 and porcentaje_producto2 < porcentaje_producto3:
    producto_menos_aceptado = "Producto 2"
else:
    producto_menos_aceptado = "Producto 3"

print("Producto más aceptado:", producto_mas_aceptado, "- Porcentaje:", porcentaje_producto1 if producto_mas_aceptado == "Producto 1" else porcentaje_producto2 if producto_mas_aceptado == "Producto 2" else porcentaje_producto3)
print("Producto menos aceptado:", producto_menos_aceptado, "- Porcentaje:", porcentaje_producto1 if producto_menos_aceptado == "Producto 1" else porcentaje_producto2 if producto_menos_aceptado == "Producto 2" else porcentaje_producto3)
