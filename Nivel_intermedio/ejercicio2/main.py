import dependencias as depe
import calculos as cal
import menu 
import os

dep = []
isActive = True
opcion = 0

while(isActive):
    os.system("cls")
    try:
        opcion = menu.menuPrincipal()        
    except ValueError:
        print("")
        print("Error en el dato ingresado...")
        print("")
        os.system("pause")
    else:
        if opcion == 1:
            nombre = input("Ingrese el nombre de la dependencia: ")
            depe.registrar_dependencia(dep,nombre)
        elif opcion == 2:
            nombre = input("Ingrese el nombre de la dependencia: ")
            consumo = float(input("Ingrese el consumo en kilovatios-hora (kWh): "))
            depe.registrar_consumo(dep,nombre,consumo)
        elif opcion == 3:
            cal.mostrar_co2_producido(dep)
        elif opcion == 4:
            cal.dependencia_mayor_co2(dep)
        elif opcion == 5:
            isActive = False
        else:
            print("Opción no válida. Intente nuevamente.")
            os.system("pause")
        

