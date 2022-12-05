from turtle import Turtle
import random
class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.shape("circle")
        self.penup()
        self.speed("fastest")
        self.color("red")
        self.shapesize(0.5)
        self.hideturtle()
        self.refresh()

    def refresh(self):
        new_x=random.randint(-330,330)
        new_y=random.randint(-330,330)
        self.goto(new_x,new_y)
        self.showturtle()

