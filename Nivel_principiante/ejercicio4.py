import os
cont = 0
contp = 0
conti = 0
contm = 0
contc = 0
contv = 0
conta = 0
suma_par = 0
suma_impar = 0
isActive = True
while (isActive):
    os.system("cls")
    try:
        num = int(input("Ingrese numero entero positivo: "))
        while (num >= 0):
            cont += 1
            if (num % 2 == 0):
                contp += 1
                suma_par += num
            else: 
                conti += 1
                suma_impar += num
            if (num > 100):
                contc += 1
            elif (num >= 20 and num <= 50):
                contv += 1 
            else:
                conta += 1 
            num = int(input("Ingrese numero entero positivo: "))

        if (contp > 0):
            prom_par = round(suma_par / contp,1)
        else:
            prom_par = 0
        if (contp > 0):
            prom_impar = round(suma_impar / conti,1)
        else:
            prom_impar = 0
        print("")
        print("Total de números ingresados: ",cont)
        print("Total de números pares ingresados: ", contp)
        print("Promedio de los números pares: ",prom_par )
        print("Promedio de los números impares: ",prom_impar)
        print("Cuantos números son menores que 10: ",conta)
        print("Cuantos números están entre 20 y 50: ",contv)
        print("Cuantos números son mayores que 100: ",contc)
    except ValueError:
        print("")
        print("Error en el dato ingresado...")
        print("")
        os.system("Pause")
    else:
        isActive = False