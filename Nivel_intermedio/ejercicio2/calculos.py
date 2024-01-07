import os
def mostrar_co2_producido(dependencias):
    for dependencia in dependencias:
        co2_producido = dependencia["consumo"] * 0.3  # Factor de emisión para energía térmica
        print(f"CO2 producido en '{dependencia['nombre']}': {co2_producido} tCO2eq")
        os.system("Pause")


def dependencia_mayor_co2(dependencias):
    if not dependencias:
        print("No hay dependencias registradas.")
        return

    dependencia_mayor = max(dependencias, key=lambda x: x["consumo"])
    print(f"La dependencia que produce mayor CO2 es '{dependencia_mayor['nombre']}' con un consumo de {dependencia_mayor['consumo']} kWh.")
    os.system("Pause")
