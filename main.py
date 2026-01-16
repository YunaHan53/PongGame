from turtle import Screen
from paddle import Paddle
import time

# Screen Setup
screen = Screen()
screen.setup(width=1200, height=700)
screen.bgcolor("black")
screen.title("The Pong Arcade Game")
screen.tracer(0)

paddle = Paddle()

screen.listen()
# Right paddle movement
screen.onkey(paddle.r_up, "Up")
screen.onkey(paddle.r_down, "Down")

# Left paddle movement
screen.onkey(paddle.l_up, "w")
screen.onkey(paddle.l_down, "s")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)



screen.exitonclick()