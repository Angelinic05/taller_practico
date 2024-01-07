import os
def regSismo(ciudades):
    rta ="S"
    while rta in ["S", "s"]:
        codigo = input("Código de la ciudad: ")
        for item in ciudades:
            if codigo in item:
                sismo = float(input("Sismo: "))
                item[2].append(sismo)
        rta = input("Desea registrar otro Sismo S(si) o N(no): ").upper()

def reporte(ciudades):
    print("REPORTE DE SISMOS POR CIUDAD")
    print("")
    cantidades_sismos = [len(ciudad[2]) for ciudad in ciudades]
    if len(set(cantidades_sismos)) != 1:
        print("LAS CIUDADES NO TIENEN LA MISMA CANTIDAD DE SISMOS REGISTRADOS")
        print("")
        print("---------------------------------------------------------------")
        for item in ciudades:
            print(item[1], ": ",len(item[2]))
        os.system("pause")
        return
    for item in ciudades:
        print("Ciudad:", item[1])
        if len(item[2]) > 0:
            promedio = sum(item[2]) / len(item[2])
            print("Promedio de sismos:", promedio)
            if promedio < 2.5:
                print("AMARILLO (Sin riesgo)")
            elif promedio >= 2.5 and promedio < 4.5:
                print("NARANJA (Riesgo medio)")
            else:
                print("ROJO (Riesgo alto)")
            print("")
        else:
            print("No se han registrado sismos para esta ciudad")
    os.system("pause")