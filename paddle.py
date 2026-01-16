from turtle import Turtle
POSITION = {(-550, 0), (550, 0)}

class Paddle(Turtle):
    def __init__(self):
        super().__init__()
        self.paddles = []
        self.create_paddle()
        self.l_paddle = self.paddles[0]
        self.r_paddle = self.paddles[1]


    def create_paddle(self):
        for pos in POSITION:
            new_paddle = Turtle("square")
            new_paddle.color("white")
            new_paddle.shapesize(stretch_wid=5, stretch_len=1)
            new_paddle.penup()
            new_paddle.goto(pos)
            self.paddles.append(new_paddle)

    def r_up(self):
        new_y = self.r_paddle.ycor() + 20
        self.r_paddle.goto(self.r_paddle.xcor(), new_y)

    def r_down(self):
        new_y = self.r_paddle.ycor() - 20
        self.r_paddle.goto(self.r_paddle.xcor(), new_y)

    def l_up(self):
        new_y = self.l_paddle.ycor() + 20
        self.l_paddle.goto(self.l_paddle.xcor(), new_y)

    def l_down(self):
        new_y = self.l_paddle.ycor() - 20
        self.l_paddle.goto(self.l_paddle.xcor(), new_y)