import os
import menu as menu
import productos as st
# import sismos as sis
productos =[]
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
                st.regProducto(productos)
                rta = input("Desea registrar otro producto S(si) o N(No)").upper()
        elif (opMenu == 2):
            st.visualizarProductos(productos)
        elif (opMenu == 3):
            codProducto = input("Ingrese el codigo a buscar : ")
            st.actualizarStock(codProducto,productos)
        elif (opMenu == 4):
            st.informeProductos(productos)
        elif (opMenu == 5):
            st.GananciaPotencial(productos)
        elif (opMenu == 6):
            print("Nos vemos pronto...")
            isActive = False