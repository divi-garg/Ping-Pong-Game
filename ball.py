from turtle import Turtle
class Ball(Turtle):
    def __init__(self):
        super().__init__()
        ball = Turtle()
        ball.color("white")
        ball.shape("circle")
        ball.penup()

    def movi(self):
        new_x = self.xcor()+10
        new_y = self.ycor()+10
        self.goto(new_x, new_y)