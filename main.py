from turtle import Turtle, Screen
from paddlestructure import Paddle
from ballcreation import Ball
import time
from scoreboard import Score

screen= Screen()
screen.screensize(600,600)
screen.bgcolor("black")
screen.title("PONG")
screen.tracer(0)
l_paddle= Paddle(-280,0)
r_paddle= Paddle(280,0)
ball= Ball()
score=Score()

screen.listen()
screen.onkey(l_paddle.going_up, "Up")
screen.onkey(l_paddle.going_down, "Down")
screen.onkey(r_paddle.going_up, "Right")
screen.onkey(r_paddle.going_down, "Left")

game_is_on=True

while game_is_on:
    time.sleep(0.1)
    screen.update()
    ball.move()
    if ball.ycor() > 290 or ball.ycor() > -290:
        ball.bounce_y()

    if ball.distance(r_paddle) < 20 and ball.xcor()>280 or ball.distance(l_paddle) < 20 and ball.xcor()<-280:
        ball.bounce_x()

    if ball.xcor() > 290 or ball.xcor() > -290:
        game_is_on=False





screen.exitonclick()
