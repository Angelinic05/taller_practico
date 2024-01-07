import os

def regJugador(categoria: str) -> dict:
    id_jugador = input("Ingrese el ID del jugador: ")
    nombre = input("Ingrese el nombre del jugador: ")
    edad = int(input("Ingrese la edad del jugador: "))
    jugador = {
        "id": id_jugador,
        "nombre": nombre,
        "edad": edad,
        "partidos_jugados": 0,
        "partidos_ganados": 0,
        "partidos_perdidos": 0,
        "puntos_a_favor": 0,
        "categoria": categoria
    }
    return {id_jugador: jugador}

def mostrarJugador(jugador: dict):
    for llave, valor in jugador.items():
        print(f"{llave}: {valor}")
    os.system("pause")
