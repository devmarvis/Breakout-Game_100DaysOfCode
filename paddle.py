from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.penup()
        self.color("white")
        self.shapesize(stretch_wid=1, stretch_len=5)
        self.goto(position)

    def move_right(self):
        if self.xcor() < 350:
            self.goto(self.xcor() + 20, self.ycor())

    def move_left(self):
        if self.xcor() > -350:
            self.goto(self.xcor() - 20, self.ycor())
