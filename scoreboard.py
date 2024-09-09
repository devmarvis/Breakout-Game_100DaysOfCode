from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.color("white")
        self.goto(300, 240)
        self.score = 0
        self.hideturtle()

    def point(self):
        self.clear()
        self.score += 1
        self.write(self.score, font=("Arial", 32, "bold"), align="center")