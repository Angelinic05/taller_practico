menu = "1. Registrar Dependencia\n2. Registrar consumo por dependencia\n3. Ver CO2 producido\n4. Dependencia que produce mayor CO2\n5. Salir\n"
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