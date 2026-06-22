import random

piedra = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

papel = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

tijera = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

imagenes = [piedra, papel, tijera]

def jugar():
    sigue_jugando = True
    while sigue_jugando:
        eleccion_del_usuario = int(input("¿Qué eliges? Escribe 0 para Piedra, 1 para Papel o 2 para Tijeras.\n"))

        if eleccion_del_usuario >= 0 and eleccion_del_usuario <= 2:
            print(imagenes[eleccion_del_usuario])

        eleccion_de_la_computadora = random.randint(0, 2)
        print("La computadora eligió:")
        print(imagenes[eleccion_de_la_computadora])

        if eleccion_del_usuario >= 3 or eleccion_del_usuario < 0:
            print("Has introducido un número inválido. Perdiste!\n")
        elif eleccion_del_usuario == 0 and eleccion_de_la_computadora == 2:
            print("Ganaste!\n")
        elif eleccion_de_la_computadora == 0 and eleccion_del_usuario == 2:
            print("Perdiste!\n")
        elif eleccion_de_la_computadora > eleccion_del_usuario:
            print("Perdiste!\n")
        elif eleccion_del_usuario > eleccion_de_la_computadora:
            print("Ganaste!\n")
        elif eleccion_de_la_computadora == eleccion_del_usuario:
            print("Empate!\n")

        sigue_jugando = input("¿Querés seguir jugando? Escribí 'si' o 'no'\n").lower() == "si"

jugar()
