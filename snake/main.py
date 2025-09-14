from turtle import Turtle,Screen
from snake import Snake
import time
from food import Food
from scoreboard import Score

screen = Screen()
screen.setup(width=600,height=600)
screen.bgcolor('black')
screen.title("My Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
score = Score()


score.update_score()

screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.left,"Left")
screen.onkey(snake.down,"Down")
screen.onkey(snake.right,"Right")


game_on = True
while game_on:
    screen.update()
    time.sleep(0.1)

    snake.move()

#     DETECT COLLISION WITH FOOD

    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        score.increase_score()

#     DETECT COLLISION WITH WALL
    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
        score.reset()
        snake.reset()

#     DETECT COLLISION WITH THE TAIL
#     if the head collides with any segments in the tail
#     TRIGGER GAME OVER
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            score.reset()
            snake.reset()













screen.exitonclick()