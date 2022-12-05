from turtle import Turtle
class ScoreCard(Turtle):
    def __init__(self):
        super().__init__()
        self.score=0
        self.penup()
        self.goto(0, 310)
        self.speed("fastest")
        self.hideturtle()
        self.color("white")
        self.write(f"score: {self.score}", align="center",font=("calibri",27,"normal"))

    def updated_score(self):
        self.write(f"score: {self.score}", align="center", font=("calibri", 27, "normal"))
    def increase(self):
        self.score+=1
        self.clear()
        self.speed("fastest")
        self.updated_score()

    def refresh(self):
        self.score=0
        self.goto(0,0)
        self.write(f"GAME OVER", align="center", font=("calibri", 27, "normal"))
