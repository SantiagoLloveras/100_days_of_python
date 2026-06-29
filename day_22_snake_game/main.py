from turtle import Screen
from scoreboard import Scoreboard
from snake import Snake
from comida import Comida
import time

TIEMPO_REFRESCO = 0.075

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game (by Santiago Lloveras)")
screen.tracer(0)

snake = Snake()
comida = Comida()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(key="Up",  fun=snake.up)
screen.onkey(key="Down", fun=snake.down)
screen.onkey(key="Left", fun=snake.left)
screen.onkey(key="Right", fun=snake.right)

game_over = False
while not game_over:
    screen.update()
    time.sleep(TIEMPO_REFRESCO)
    snake.mover()

    # Detectar colisiones con la comida
    if snake.cabeza.distance(comida) < 20:
        comida.refrescar()
        snake.crecer()
        scoreboard.incrementar_score()

    # Detectar colisiones con el muro
    if snake.cabeza.xcor() > 299 or snake.cabeza.xcor() < -290 or snake.cabeza.ycor() > 299 or snake.cabeza.ycor() < -299:
        game_over = True
        scoreboard.game_over()

    # Detectar colisiones con la cola
    for segmento in snake.segmentos[1:]:
        if snake.cabeza.distance(segmento) < 10:
            game_over = True
            scoreboard.game_over()

screen.exitonclick()
