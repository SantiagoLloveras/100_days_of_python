from turtle import Turtle

X_MOVIMIENTO = 10
Y_MOVIMIENTO = 10
VELOCIDAD_MOVIMIENTO_INICIAL = 0.075

class Pelota(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.x_movimiento = X_MOVIMIENTO
        self.y_movimiento = Y_MOVIMIENTO
        self.velocidad_movimiento = 0.075

    def mover(self):
        nueva_x = self.xcor() + self.x_movimiento
        nueva_y = self.ycor() + self.y_movimiento
        self.goto(nueva_x, nueva_y)

    def rebotar_y(self):
        self.y_movimiento *= -1

    def rebotar_x(self):
        self.x_movimiento *= -1
        self.velocidad_movimiento *= 0.9
        self.goto(self.xcor() + self.x_movimiento, self.ycor()) # La mando fuera del rango del paddle para que no rebote varias veces

    def resetear_posicion(self):
        self.home()
        self.velocidad_movimiento = VELOCIDAD_MOVIMIENTO_INICIAL
        self.rebotar_x()
