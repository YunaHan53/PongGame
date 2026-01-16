from turtle import Screen
from paddle import Paddle
import time

# Screen Setup
screen = Screen()
screen.setup(width=1200, height=700)
screen.bgcolor("black")
screen.title("The Pong Arcade Game")
screen.tracer(0)

# Create 2 paddles
r_paddle = Paddle((550, 0))
l_paddle = Paddle((-550, 0))

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



screen.exitonclick()