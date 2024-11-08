from turtle import Turtle
class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.L_score = 0
        self.R_score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(-100,200)
        self.write(self.L_score, align="center", font=("Arial", 50, "normal"))
        self.goto(100,200)
        self.write(self.R_score, align="center", font=("Arial", 50, "normal"))

    def l_point(self):
        self.L_score += 1
        self.update_scoreboard()

    def r_point(self):
        self.R_score += 1
        self.update_scoreboard()