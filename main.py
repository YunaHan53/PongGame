from turtle import Screen
from paddle import Paddle
from ball import Ball
import time

# Screen Setup
screen = Screen()
screen.setup(width=1200, height=700)
screen.bgcolor("black")
screen.title("The Pong Arcade Game")
screen.tracer(0)

# Create 2 paddles and ball
r_paddle = Paddle((550, 0))
l_paddle = Paddle((-550, 0))
ball = Ball()

screen.listen()
# Right paddle movement
screen.onkey(r_paddle.up, "Up")
screen.onkey(r_paddle.down, "Down")

# Left paddle movement
screen.onkey(l_paddle.up, "w")
screen.onkey(l_paddle.down, "s")


game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    ball.move()

    # Detects balls collision with the top and bottom wall
    if ball.ycor() > 330 or ball.ycor() < -330:
        ball.bounce()


screen.exitonclick()