import os
menu = "1. Registrar Ciudad\n2. Registrar Sismo\n3. Buscar Sismo por ciudad\n4. Reporte\n5.Salir\n"
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