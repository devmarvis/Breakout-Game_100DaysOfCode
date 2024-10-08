import time
from turtle import Screen
from paddle import Paddle
from ball import Ball
from bricks import Brick, BrickDrawer
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Breakout Game")
screen.tracer(0)


pad = Paddle((0, -270))
ball = Ball()
brick_drawer = BrickDrawer(5, 13, -365, 220, 20, 50)
scoreboard = Scoreboard()

screen.listen()

# move pad to right
screen.onkey(fun=pad.move_right, key="Right")
# move pad to left
screen.onkey(fun=pad.move_left, key="Left")

while True:
    time.sleep(ball.move_speed)
    screen.update()

    ball.move()

    # Detect ball collision with wall
    if ball.xcor() > 380 or ball.xcor() < -380:
        ball.bounce_x()

    # Detect collision with Pad
    if pad.xcor() - 50 < ball.xcor() < pad.xcor() + 50 and ball.ycor() < -220:
        ball.bounce_y()
    # if ball.distance(pad) < 50 and ball.ycor() < -220:
    #     ball.bounce_y()

    # Detect if pad misses ball
    if ball.ycor() < -280:
        ball.goto(0, 0)
        pad.goto(0, -270)
        ball.bounce_y()
        ball.move_speed = 0.06

    if ball.ycor() >= 220 and ball.y_move > 0:
        ball.bounce_y()

    if brick_drawer.check_collision(ball):
        scoreboard.point()

    # Detect collision with brick

screen.exitonclick()
