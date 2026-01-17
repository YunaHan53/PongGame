from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

# Screen Setup
screen = Screen()
screen.setup(width=1200, height=700)
screen.bgcolor("black")
screen.title("The Pong Arcade Game")
screen.tracer(0)

# Create 2 paddles, 1 ball and scoreboard objects
r_paddle = Paddle((550, 0))
l_paddle = Paddle((-550, 0))
ball = Ball()
scoreboard = Scoreboard()

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
    time.sleep(ball.move_speed)
    ball.move()

    # Detects balls collision with the top and bottom wall
    if ball.ycor() > 330 or ball.ycor() < -330:
        ball.bounce_y()
    # Detects collision with the paddles
    if ball.distance(r_paddle) < 50 and ball.xcor() > 520 or ball.distance(l_paddle) < 50 and ball.xcor() < -520:
        ball.bounce_x()
    # Detects when the paddle misses the ball
    if ball.xcor() > 600 or ball.xcor() < -600:
        scoreboard.end_round(ball.pos())
        scoreboard.count_rounds()
        ball.reset_ball()
        ball.increase_speed()

screen.exitonclick()