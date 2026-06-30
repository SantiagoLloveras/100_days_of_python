from turtle import Turtle

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.score_izquierdo = 0
        self.score_derecho = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(-100, 200)
        self.write(self.score_izquierdo, align="center", font=("Courier", 70, "bold"))
        self.goto(100, 200)
        self.write(self.score_derecho, align="center", font=("Courier", 70, "bold"))

    def punto_izquierda(self):
        self.score_izquierdo += 1
        self.update_scoreboard()

    def punto_derecha(self):
        self.score_derecho += 1
        self.update_scoreboard()