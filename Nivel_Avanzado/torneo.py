import jugadores 
def iniciarCategoria(categoria: str) -> dict:
    jugadores_categoria = {}
    inscritos_minimos = 5
    while len(jugadores_categoria) < inscritos_minimos:
        jugadores_categoria.update(jugadores.regJugador(categoria))

    return jugadores_categoria

def calcularPuntosAFavor(partido: dict) -> int:
    return abs(partido["puntos_realizados"] - partido["puntos_recibidos"])

def registrarPartido(jugador: dict, categoria: str) -> None:
    puntos_realizados = int(input(f"Ingrese los puntos realizados por {jugador['nombre']}: "))
    puntos_recibidos = int(input(f"Ingrese los puntos recibidos por {jugador['nombre']}: "))
    jugador["partidos_jugados"] += 1

    if puntos_realizados > puntos_recibidos:
        jugador["partidos_ganados"] += 1

    jugador["puntos_a_favor"] += calcularPuntosAFavor({"puntos_realizados": puntos_realizados, "puntos_recibidos": puntos_recibidos})
    print("Partido registrado exitosamente!")

def obtenerGanador(categoria: str, jugadores: dict) -> dict:
    if len(jugadores) < 2:
        print(f"No hay suficientes jugadores en la categoría {categoria} para determinar un ganador.")
        return {}

    ganador = max(jugadores.values(), key=lambda x: (x["partidos_ganados"] * 2 + x["puntos_a_favor"]))
    return ganador
