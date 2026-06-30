from turtle import Screen
from paddle import Paddle
from pelota import Pelota
from scoreboard import Scoreboard
from controles import Controles
import time

PADDLE_DERECHO_POSICION_INICIAL = (370, 0)
PADDLE_IZQUIERDO_POSICION_INICIAL = (-380, 0)

screen = Screen()

screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong Game (by Santiago Lloveras)")
screen.tracer(0)

paddle_derecho = Paddle(PADDLE_DERECHO_POSICION_INICIAL)
paddle_izquierdo = Paddle(PADDLE_IZQUIERDO_POSICION_INICIAL)
pelota = Pelota()
scoreboard = Scoreboard()
controles = Controles()

screen.listen()
screen.onkeypress(lambda: controles.presionar_tecla("Up"), "Up")
screen.onkeyrelease(lambda: controles.liberar_tecla("Up"), "Up")

screen.onkeypress(lambda: controles.presionar_tecla("Down"), "Down")
screen.onkeyrelease(lambda: controles.liberar_tecla("Down"), "Down")

screen.onkeypress(lambda: controles.presionar_tecla("w"), "w")
screen.onkeyrelease(lambda: controles.liberar_tecla("w"), "w")

screen.onkeypress(lambda: controles.presionar_tecla("s"), "s")
screen.onkeyrelease(lambda: controles.liberar_tecla("s"), "s")

game_over = False
while not game_over:
    time.sleep(pelota.velocidad_movimiento)
    screen.update()

    if controles.teclas_presionadas["Up"]:
        paddle_derecho.mover_arriba()
    if controles.teclas_presionadas["Down"]:
        paddle_derecho.mover_abajo()
    if controles.teclas_presionadas["w"]:
        paddle_izquierdo.mover_arriba()
    if controles.teclas_presionadas["s"]:
        paddle_izquierdo.mover_abajo()

    pelota.mover()
    if pelota.ycor() > 275 or pelota.ycor() < -275:
        pelota.rebotar_y()

    if (pelota.distance(paddle_derecho) < 45 and pelota.xcor() > 320
            or pelota.distance(paddle_izquierdo) < 45 and pelota.xcor() < -320):
        pelota.rebotar_x()

    if pelota.xcor() > 410:
        scoreboard.punto_izquierda()
        pelota.resetear_posicion()
    elif pelota.xcor() < -410:
        scoreboard.punto_derecha()
        pelota.resetear_posicion()

screen.exitonclick()
