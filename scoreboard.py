from turtle import Turtle
ALIGN = "center"
FONT = ("Courier", 70, "bold")
SCORE_POSITIONS = {
    "right": (100, 250),
    "left": (-100, 250)}

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color('white')
        self.l_score = 0
        self.r_score = 0
        self.number_of_rounds = 0
        self.update_scoreboard()
        self.count_rounds()

    def update_scoreboard(self):
        self.clear()
        for position in SCORE_POSITIONS.values():
            if position == SCORE_POSITIONS["right"]:
                self.goto(position)
                self.write(self.r_score, align=ALIGN, font=FONT)
            elif position == SCORE_POSITIONS["left"]:
                self.goto(position)
                self.write(self.l_score, align=ALIGN, font=FONT)

    def end_round(self, position):
        if position[0] > 600:
            self.l_score += 1
        elif position[0] < -600:
            self.r_score += 1
        self.update_scoreboard()

    def count_rounds(self):
        self.number_of_rounds += 1
        self.goto(0, 0)
        self.write(f"Round {self.number_of_rounds}", align=ALIGN, font=FONT)