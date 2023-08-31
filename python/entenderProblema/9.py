#Factura de Producto
monto = float(input("Ingrese el monto del producto: "))
subtotal = monto
iva = subtotal * 0.21
total = subtotal + iva

print(f"Subtotal: {subtotal}")
print(f"IVA: {iva}")
print(f"Total a pagar: {total}")
