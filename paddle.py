from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.penup()
        self.color("white")
        self.shapesize(stretch_wid=1, stretch_len=8)
        self.goto(position)

    def move_right(self):
        if self.xcor() < 300:
            self.goto(self.xcor() + 40, self.ycor())

    def move_left(self):
        if self.xcor() > -300:
            self.goto(self.xcor() - 40, self.ycor())
