from turtle import Turtle,Screen
import time
from snake import Snake
from food import Food
from score import ScoreCard
screen=Screen()
screen.setup(width=700,height=700)
screen.bgcolor("black")
screen.title("Snake Game")
snake=Snake()
food=Food()
score=ScoreCard()
race_on = True
screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")
# screen.onkey(snake,"Enter")

while race_on:
    screen.update()

    # for j in range(3):
    #     snakelis[j].forward(10)
    snake.move()
    if snake.head.distance(food)<10:
        food.refresh()
        score.increase()
        screen.update()
        snake.add()
    if snake.head.xcor()==350 or snake.head.xcor()==-350 or snake.head.ycor()==350 or snake.head.ycor()==-350:
        print('hitted')
        score.refresh()
        race_on=False
    for i in snake.snakelis[1:]:
        if snake.head.distance(i)<3:
            score.refresh()
            race_on=False




    # snake[0].forward(10)
    # snake[0].left(90)





screen.exitonclick()
