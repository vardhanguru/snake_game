from turtle import Turtle
MOVE_DISTANCE=10
LIS = [0, -10, -20]
class Snake:
    def __init__(self):
        self.snakelis=[]
        Snake.snakeObj(self)

        self.head=self.snakelis[0]

    def snakeObj(self):
        for i in range(3):
            s = Turtle()
            s.penup()
            s.speed(0)
            s.shape("square")
            s.shapesize(0.5, 0.5, 1)
            s.color("white")
            s.goto(x=LIS[i], y=0)
            self.snakelis.append(s)
    def move(self):
        for j in range(len(self.snakelis) - 1, 0, -1):
            self.snakelis[j].speed("fastest")
            new_x = self.snakelis[j - 1].xcor()
            new_y = self.snakelis[j - 1].ycor()
            self.snakelis[j].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def add_segment(self,position):
        new_seg=Turtle("square")
        new_seg.penup()
        new_seg.speed(0)
        new_seg.shape("square")
        new_seg.shapesize(0.5, 0.5, 1)
        new_seg.goto(position)
        new_seg.color("white")
        self.snakelis.append(new_seg)


    def up(self):
        if self.head.heading()!=270:
            self.head.seth(90)
    def down(self):
        if self.head.heading()!=90:
            self.head.seth(270)
    def left(self):
        if self.head.heading()!=0:
            self.head.seth(180)
    def right(self):
        if self.head.heading()!=180:
            self.head.seth(0)
    def add(self):
        self.add_segment(self.snakelis[-1].position())
