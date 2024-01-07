import os
menu = "1. Registrar Producto\n2. Visualizacion de productos\n3. Actualizacion de Stock\n4. Informe de productos criticos\n5. Calculo de Ganancia Potencial\n6. Salir\n"
hasError = True
def menuPrincipal() -> int:
    global hasError
    hasError = True
    print(menu)
    while (hasError == True):
        try:
            return int(input())
        except ValueError:
            hasError = True