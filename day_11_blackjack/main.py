import random
from art import logo


def repartir_carta():
    """Retorna una carta al azar del mazo."""
    mazo = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    carta = random.choice(mazo)
    return carta


def calcular_puntaje(cartas):
    """Toma una lista de cartas y retorna el puntaje correspondiente."""
    if sum(cartas) == 21 and len(cartas) == 2:
        return 0

    if 11 in cartas and sum(cartas) > 21:
        cartas.remove(11)
        cartas.append(1)

    return sum(cartas)


def comparar(u_puntaje, c_puntaje):
    """Compara el puntaje del usuario (u_score) con el puntaje de la computadora (c_score)."""
    if u_puntaje == c_puntaje:
        return "Empate 🙃"
    elif c_puntaje == 0:
        return "Perdiste, tu oponente tiene Blackjack 😱"
    elif u_puntaje == 0:
        return "Ganaste con Blackjack!!! 😎"
    elif u_puntaje > 21:
        return "Te pasaste. Perdiste 😭"
    elif c_puntaje > 21:
        return "Tu oponente se pasó. Ganaste! 😁"
    elif u_puntaje > c_puntaje:
        return "Ganaste! 😃"
    else:
        return "Perdiste 😤"


def jugar():
    print(logo)
    cartas_del_usuario = []
    cartas_de_la_computadora = []
    puntaje_computadora = -1
    puntaje_usuario = -1
    es_game_over = False

    for _ in range(2):
        cartas_del_usuario.append(repartir_carta())
        cartas_de_la_computadora.append(repartir_carta())

    while not es_game_over:
        puntaje_usuario = calcular_puntaje(cartas_del_usuario)
        puntaje_computadora = calcular_puntaje(cartas_de_la_computadora)
        print(f"Tus cartas: {cartas_del_usuario}, puntaje actual: {puntaje_usuario}")
        print(f"Primer carta de la computadora: {cartas_de_la_computadora[0]}")

        if puntaje_usuario == 0 or puntaje_computadora == 0 or puntaje_usuario > 21:
            es_game_over = True
        else:
            quiere_otra_carta = input("Escribí 's' para sacar otra carta, escribí 'n' para pasar: ")
            print()
            if quiere_otra_carta == "s":
                cartas_del_usuario.append(repartir_carta())
            else:
                es_game_over = True

    while puntaje_computadora != 0 and puntaje_computadora < 17:
        cartas_de_la_computadora.append(repartir_carta())
        puntaje_computadora = calcular_puntaje(cartas_de_la_computadora)

    print()
    print(f"Tu mano final: {cartas_del_usuario}, puntaje final: {puntaje_usuario}")
    print(f"Mano final de la computadora: {cartas_de_la_computadora}, puntaje final: {puntaje_computadora}")
    print(comparar(puntaje_usuario, puntaje_computadora))


while input("\n¿Querés jugar una partida de Blackjack? Escribí 's' or 'n': ") == "s":
    print("\n" * 20)
    jugar()
