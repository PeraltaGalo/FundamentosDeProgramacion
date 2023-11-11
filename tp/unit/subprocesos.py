def Ingresar_Pedidos():
    cliente=input("Ingrese el cliente: ").upper()
    direccion=input("Ingrese la direccion: ").upper()
    importe=float(input("Ingrese el importe: "))
    hora=int(input("Ingrese el tiempo estimado: "))
    
    pedido={
        'cliente':cliente,
        'direccion':direccion,
        'importe':importe,
        'hora':hora
    }
    return pedido

def Cargar_Pedidos(Pedidos, lim):
    opcion=input("Ingrese s para cargar un pedido: ").lower()
    while (opcion=='s' and lim<(len(Pedidos))):
        nuevo_pedido=Ingresar_Pedidos()
        Pedidos[lim]=nuevo_pedido
        lim+=1
        print()
        if lim<(len(Pedidos)):
            opcion=input("Ingrese s para cargar un pedido: ").lower()
    return lim

def burbuja(Pedidos, limite,campo):
    for i in range(limite - 1):
        for j in range(limite - 1 - i):
            orden_actual = Pedidos[j][campo]
            orden_siguiente = Pedidos[j+1][campo]
            if orden_actual > orden_siguiente:
                aux = Pedidos[j]
                Pedidos[j] = Pedidos[j + 1]
                Pedidos[j + 1] = aux

def busqueda_binaria(Pedidos,limite, buscado):
    pri = 0
    ult = limite-1
    pos = -1
    while (pos == -1) and (pri <= ult):
        med = (pri + ult) // 2
        if (Pedidos[med]['cliente'])== buscado:
            pos = med
        elif (Pedidos[med]['cliente']) >= buscado:
            ult = med - 1
        else:
            pri = med + 1
    return pos

def total_pedidos(Pedidos,limite):
    imp_total=0
    for i in range (limite):
        imp_total+=Pedidos[i]['importe']
    return imp_total

def total_cliente(Pedidos,limite,buscado):
    total_vip=0
    for i in range (limite):
        if Pedidos[i]['cliente']==buscado:
            total_vip+=Pedidos[i]['importe']
    return total_vip

def total_direccion(Pedidos,limite,buscado):
    total_dir=0
    for i in range (limite):
        if Pedidos[i]['direccion']==buscado:
            total_dir+=1
    return total_dir

def total_horas(Pedidos,limite):
    total_hora=0
    for i in range (limite):
        total_hora+=Pedidos[i]['hora']
    return total_hora/limite