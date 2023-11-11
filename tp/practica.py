#Supongamos que tienes una lista de pedidos de entrega de alimentos a domicilio. De cada pedido, se tienen los siguientes datos:
#Nombre del cliente.
#Dirección de entrega.
#Total del pedido en pesos.
#Hora de entrega estimada.
#NOTA: Deben utilizar funciones o procedimientos, su correspondiente invocación, como asi también ordenamiento burbuja y Búsqueda Binaria.
#Se pide:
#Cargar las estructura que corresponda, hasta que el usuario desee.
#Listado ordenado por el total del pedido.
#Determinar si el cliente con nombre "ClienteVIP" ha realizado algún pedido. 
#Mostrar el Total de pedidos.
#Mostrar el porcentaje que representa el total del pedido del cliente "ClienteVIP" sobre el total de todas las ventas.
#Cantidad de pedidos con dirección de entrega en una zona específica (por ejemplo, "Centro de la ciudad").
#Hora 
from io import open 
from unit.subprocesos import Cargar_Pedidos, burbuja, busqueda_binaria, total_pedidos, total_cliente, total_direccion, total_horas
Pedidos = [0, 0, 0, 0, 0, 0]
lim = 0
archivo = "archivo.txt"

with open(archivo, "w") as archivo_actual:
    limite = Cargar_Pedidos(Pedidos, lim)
    archivo_actual.write(f"El límite es de: {limite}\n")

    campo = 'importe'
    archivo_actual.write(f"Campo: {campo}\n")
    burbuja(Pedidos, limite, campo)
    archivo_actual.write(f"Pedidos ordenados: {', '.join(map(str, Pedidos))}\n")

    buscado = input('Ingrese el cliente: ')
    archivo_actual.write(f"Cliente ingresado: {buscado}\n")

    campo = 'cliente'
    archivo_actual.write(f"Campo por ordenar: {campo}\n")
    burbuja(Pedidos, limite, campo)
    archivo_actual.write(f"Pedidos ordenados por cliente: {', '.join(map(str, Pedidos))}\n")

    x = busqueda_binaria(Pedidos, limite, buscado)
    if x != -1:
        archivo_actual.write('El cliente realizó un pedido\n')
    else:
        archivo_actual.write('No es cliente\n')

    total_ventas = total_pedidos(Pedidos, limite)
    archivo_actual.write(f"El importe total es: {total_ventas}\n")

    Tot_vip = total_cliente(Pedidos, limite, buscado)
    porce_vip = Tot_vip * 100 / total_ventas
    archivo_actual.write(f"El porcentaje de compras del cliente es: {porce_vip}\n")

    zona = input('Ingrese zona a buscar: ')
    archivo_actual.write(f"Zona a buscar: {zona}\n")
    cantidad = total_direccion(Pedidos, limite, zona)
    archivo_actual.write(f"Cantidad de direcciones {zona}: {cantidad}\n")

    archivo_actual.write(f"El promedio de entrega es: {total_horas(Pedidos, limite)}\n")
