import os
def regCiudad(ciudades) -> list:
    codigo = input("Ingrese el codigo de la ciudad : ")
    nombre = input("Ingrese el nombre de la ciudad : ")
    ciudad = [codigo, nombre, []]
    ciudades.append(ciudad)
    for item in ciudades:
        print(item)
    return ciudad

def buscarCiudad(codCiudad, ciudades):
    print("Buscando ciudad con código:", codCiudad) 
    for item in ciudades:
        if codCiudad == item[0]:
            print("Información de la ciudad:")
            print(item)
    os.system("pause")