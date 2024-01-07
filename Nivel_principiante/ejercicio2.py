import os

isActive = True

while (isActive):
    os.system("cls")
    try:
        print("BIENVENIDO AL INDICE DE MASA CORPORAL")
        print("---------------------------------------")
        print("")
        nombre = input("Nombre del estudiante: ")
        edad = int(input("Edad del estudiante: "))
        peso = float(input("Peso (kg) del estudiante: "))
        altura = float(input("Altura (m) del estudiante: "))

        imc = round(peso / (altura * altura),2)
        print("")
        print("---------------------------------------")
        print("nombre:", nombre)
        print("edad: ",edad)
        print("IMC: ",imc)
        print("")
        print("RESULTADO")
        if ( imc > 40 ):
            print("OBESIDAD III")
        elif ( imc > 35):
            print("OBESIDAD II")
        elif ( imc > 30 ):
            print("OBESIDAD I")
        elif ( imc > 25 ):
            print("SOBREPESO")
        elif ( imc > 18.5 ):
            print("NORMAL")
        else:
            print("BAJO DE PESO")
    except ValueError:
        print("")
        print("Error en el dato ingresado")
        os.system("pause")
    else:
        isActive = False



