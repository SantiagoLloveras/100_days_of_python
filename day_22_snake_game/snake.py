from turtle import Turtle

POSICION_INICIAL = [(0, 0), (-20, 0), (-40, 0)]
TAMANO_SNAKE = (1, 1, 2)
DISTANCIA_MOVIMIENTO = 20
SNAKE_COLOR = "green"
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:

    def __init__(self):
        self.segmentos = []
        self.crear_snake()
        self.cabeza = self.segmentos[0]

    def crear_snake(self):
        for posicion in POSICION_INICIAL:
            self.agregar_segmento(posicion)

    def agregar_segmento(self, posicion):
        nuevo_segmento = Turtle(shape="square")
        nuevo_segmento.color(SNAKE_COLOR)
        nuevo_segmento.shapesize(*TAMANO_SNAKE)
        nuevo_segmento.penup()
        nuevo_segmento.goto(posicion)
        self.segmentos.append(nuevo_segmento)

    def crecer(self):
        self.agregar_segmento(self.segmentos[-1].position())

    def mover(self):
            for seg_num in range(len(self.segmentos) - 1, 0, -1):
                nueva_x = self.segmentos[seg_num - 1].xcor()
                nueva_y = self.segmentos[seg_num - 1].ycor()
                self.segmentos[seg_num].goto(nueva_x, nueva_y)
            self.segmentos[0].forward(DISTANCIA_MOVIMIENTO)

    def up(self):
        if self.cabeza.heading() != DOWN:
            self.cabeza.setheading(UP)

    def down(self):
        if self.cabeza.heading() != UP:
            self.cabeza.setheading(DOWN)

    def left(self):
        if self.cabeza.heading() != RIGHT:
            self.cabeza.setheading(LEFT)

    def right(self):
        if self.cabeza.heading() != LEFT:
            self.cabeza.setheading(RIGHT)
