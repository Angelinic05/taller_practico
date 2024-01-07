import os
import menu as menu
import ciudades as st
import sismos as sis
ciudades =[]
isActive = True
opMenu=0

while (isActive) :
    os.system("cls")
    try:
        opMenu = menu.menuPrincipal()
    except ValueError:
        print("Error en el dato de de ingreso")
        os.system("pause")
    else:
        if(opMenu == 1):
            rta = "S"
            while (rta in ["S","s"]):
                os.system("cls")
                st.regCiudad(ciudades)
                rta = input("Desea registrar otra Ciudad S(si) o N(No)").upper()
        elif (opMenu == 2):
            rta = "S"
            while (rta in ["S","s"]):
                os.system("cls")
                sis.regSismo(ciudades)
                rta = input("Desea registrar otro Sismo S(si) o N(No)").upper()
        elif (opMenu == 3):
            codCiudad = input("Ingrese el codigo a buscar : ")
            st.buscarCiudad(codCiudad,ciudades)
        elif (opMenu == 4):
            os.system("cls")
            sis.reporte(ciudades)
        elif (opMenu == 5):
            print("Nos vemos pronto...")
            isActive = False