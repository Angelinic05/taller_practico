import os
def registrar_dependencia(dep, nombre):
    dep.append({"nombre": nombre, "consumo": 0, "dispositivos": []})
    print(f"Dependencia '{nombre}' registrada con éxito.")

def registrar_consumo(dep,nombre,consumo):
    for dependencia in dep:
        if dependencia["nombre"] == nombre:
            dependencia["consumo"] += consumo
            print(f"Consumo registrado con éxito para la dependencia '{nombre}'.")
            break
    else:
        print(f"No se encontró la dependencia '{nombre}'.")
    dispositivos = int(input("Ingrese el número de dispositivos a registrar: "))
    for _ in range(dispositivos):
        isActive = True
        while(isActive):
            os.system("cls")
            try:
                dispositivo_nombre = input("Ingrese el nombre del dispositivo: ")
                dispositivo_potencia = float(input("Ingrese la potencia del dispositivo en watts: "))
                tiempo_uso = float(input("Ingrese el tiempo de uso del dispositivo en horas: "))
                consumo_dispositivo = (dispositivo_potencia * tiempo_uso) / 1000  # Convertir a kWh
                dependencia["dispositivos"].append({"nombre": dispositivo_nombre, "consumo": consumo_dispositivo})
                print(f"Dispositivo '{dispositivo_nombre}' registrado con éxito.")
            except ValueError:
                print("")
                print("Error en el dato ingresado...")
                print("")
            else:
                isActive = False
            

