import os
def regProducto(productos) -> list:
    codigo = input("Ingrese el codigo del producto : ")
    nombre = input("Ingrese el nombre del producto : ")
    valor_compra = int(input("Ingrese el valor total de la comrpra: "))
    valor_venta = int(input("Ingrese el valor total de la venta: "))
    stock_min = int(input("Ingrese el stock minimo: "))
    stock_max = int(input("Ingrese el stock maximo: "))
    proveedor = input("Nombre del proveedor: ")
    producto = [codigo, nombre, valor_compra, valor_venta, stock_min, stock_max, proveedor]
    productos.append(producto)
    for item in productos:
        print(item)
    return producto

def visualizarProductos(productos):
    print ("CODIGO          NOMBRE           VALOR COMPRA      VALOR DE VENTA           STOCK MINIMO            STOCK MAXIMO          PROVEEDOR  ")
    for item in productos:
        print(item[0], "           ",item[1], "           ",item[2], "               ",item[3], "             ",item[4], "                   ",item[5], "              ",item[6])
    os.system("pause")

def actualizarStock(codProducto, productos):
    for item in productos:
        if codProducto == item[0]:
            ar = int(input("¿Desea (1. agregar) o (2. restar) al stock?"))
            if (ar == 1):
                cant = int(input("Cantidad a agregar?: "))
                res = cant + item[4]
                print(res)
                item[4] = res
            else:
                cant = int(input("Cantidad a restar?: "))
                res = cant - item[5]
                item[5] = res
    os.system("pause")

def informeProductos(productos):
    print("Productos con stock por debajo del límite mínimo:")
    for item in productos:
        print ("CODIGO          NOMBRE           STOCK MINIMO            STOCK ACTUAL")
        if item[4] > item[5]:
            print(item[0], "           ", item[1], "           ", item[4], "                   ", item[5])
    os.system("pause")

def GananciaPotencial(productos):
    ganancia_total = 0
    for item in productos:
        ganancia_total += (item[3] - item[2]) * item[5]
    print("La ganancia potencial total es:", ganancia_total)
    os.system("pause")
    