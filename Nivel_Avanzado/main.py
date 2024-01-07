import os
import jugadores as jugador
import torneo

categorias = ["Novato", "Intermedio", "Avanzado"]
jugadores_torneo = {}

for categoria in categorias:
    print(f"Inscribiendo jugadores en la categoría {categoria}:")
    jugadores_torneo.update(torneo.iniciarCategoria(categoria))

while True:
    os.system("cls")
    print("1. Registrar Partido\n2. Obtener Ganador por Categoría\n3. Salir")
    try:
        opcion = int(input(":)"))
    except ValueError:
        print("Opción inválida. Ingrese un número.")
        os.system("pause")
        continue

    if opcion == 1:
        print("Jugadores inscritos:")
        for jugador_id, jugador_info in jugadores_torneo.items():
            print(f"{jugador_id}: {jugador_info['nombre']}")

        jugador_id = input("Ingrese el ID del jugador que participará en el partido: ")
        jugador_seleccionado = jugadores_torneo.get(jugador_id)
        if jugador_seleccionado:
            torneo.registrarPartido(jugador_seleccionado, jugador_seleccionado["categoria"])
        else:
            print("Jugador no encontrado.")
            os.system("pause")

    elif opcion == 2:
        print("Categorías disponibles:")
        for categoria in categorias:
            print(f"{categoria}")

        categoria_seleccionada = input("Ingrese la categoría para obtener al ganador: ")
        ganador = torneo.obtenerGanador(categoria_seleccionada, jugadores_torneo)
        if ganador:
            print("Ganador:")
            jugador.mostrarJugador(ganador)
        os.system("pause")

    elif opcion == 3:
        break
