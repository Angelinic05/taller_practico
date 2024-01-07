import os

cont1 = 0
cont2 = 0
cont3 = 0
conts = 0
contn = 0
contb = 0

isActive = True

for i in range(1,21,1):
    print("BIENVENIDO AL INDICE DE MASA CORPORAL")
    print("---------------------------------------")
    print(f"Estudiante {i}:")
    print("")
    peso = float(input("Peso (kg) del estudiante: "))
    altura = float(input("Altura (m) del estudiante: "))

    imc = round(peso / (altura * altura),2)
    print("IMC: ",imc)

    if ( imc > 40 ):
        print("OBESIDAD III")
        cont3 = cont3 + 1
    elif ( imc > 35):
        print("OBESIDAD II")
        cont2 = cont2 + 1
    elif ( imc > 30 ):
        print("OBESIDAD I")
        cont1 = cont1 + 1
    elif ( imc > 25 ):
        print("SOBREPESO")
        conts = conts + 1
    elif ( imc > 18.5 ):
        print("NORMAL")
        contn = contn + 1
    else:
        print("BAJO DE PESO")
        contb = contb + 1
    os.system("Pause")
    os.system("cls")

print("INDICE DE MASA CORPORAL")
print("---------------------------------------")
print("")
print("Cantidad de estudiantes en peso ideal: ", contn)
print("Cantidad de estudiantes en obesidad grado I: ", cont1)
print("Cantidad de estudiantes en obesidad grado II: ",cont2)
print("Cantidad de estudiantes en obesidad grado III: ",cont3)
print("Cantidad de estudiantes en Sobrepeso: ",conts)
print("Cantidad de estudiantes en Bajo de peso: ",contb)

