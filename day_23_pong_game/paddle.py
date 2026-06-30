from turtle import Turtle

class Paddle(Turtle):

    def __init__(self, posicion):
        super().__init__()
        self.crear_paddle(posicion)

    def crear_paddle(self, posicion):
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(*posicion)

    def mover_arriba(self):
        if self.ycor() < 250:
            self.sety(self.ycor() + 20)

    def mover_abajo(self):
        if self.ycor() > -230:
            self.sety(self.ycor() - 20)
