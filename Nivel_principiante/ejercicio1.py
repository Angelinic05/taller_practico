import os
isActive = True
while(isActive):
    os.system("cls")
    try:
        n1 = int(input("INGRESE NUMERO ENTERO 1: "))
        n2 = int(input("INGRESE NUMERO ENTERO 2: "))
        n3 = int(input("INGRESE NUMERO ENTERO 3: "))
        suma = n1 + n2 + n3
        if (n1 >= 0 and n2 >= 0 and n3 >= 0):
            print("SUMA DE LOS 3 NUMEROS: ",suma)
        else:
            print("Error, ingrese numeros positivos")
    except ValueError:
        print("Error en el dato ingresado")
        os.system("pause")
    else:
        isActive = False