from turtle import Turtle
import random


colors = ['red', 'blue', 'green', 'purple']


class Brick(Turtle):
    def __init__(self, x, y, width, height):
        super().__init__()
        self.shape('square')
        self.color(random.choice(colors))
        self.shapesize(stretch_wid=width / 20, stretch_len=height / 20)
        self.penup()
        self.goto(x, y)
        self.width = width
        self.height = height
        self.visible = True

    def hide(self):
        self.hideturtle()
        self.visible = False

    def is_collide(self, ball):

        if not self.visible:
            return False
        brick_left = self.xcor() - self.width / 2
        brick_right = self.xcor() + self.width / 2
        brick_top = self.ycor() + self.height / 2
        brick_bottom = self.ycor() - self.height / 2

        ball_x = ball.xcor()
        ball_y = ball.ycor()

        # Check if ball's position overlaps with brick's boundaries
        if (brick_left <= ball_x <= brick_right) and (brick_bottom <= ball_y <= brick_top):
            return True
        return False


class BrickDrawer:
    def __init__(self, rows, columns, start_x, start_y, brick_width, brick_height, padding=10):
        self.rows = rows
        self.columns = columns
        self.brick_width = brick_width
        self.brick_height = brick_height
        self.padding = padding
        self.bricks = []
        self.create_bricks(start_x, start_y)

    def create_bricks(self, start_x, start_y):
        for row in range(self.rows):
            for column in range(self.columns):
                x = start_x + column * (self.brick_height + self.padding)
                y = start_y - row * (self.brick_width + self.padding)
                brick = Brick(x, y, self.brick_width, self.brick_height)
                self.bricks.append(brick)

    def check_collision(self, ball):
        # Check if the ball collides with any visible brick
        for brick in self.bricks:
            if brick.is_collide(ball):
                brick.hide()
                # Reflect ball direction
                ball.y_move *= -1
                return True  # Only handle one collision at a time


