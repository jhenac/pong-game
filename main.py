from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
from line import Line
import time

screen = Screen()
screen.setup(height=600, width=800)
screen.bgcolor("black")
screen.title("My Pong Game")
screen.tracer(0)

right_paddle = Paddle((370,0))
left_paddle = Paddle((-370,0))
ball = Ball()
score = Scoreboard()
dotted_line = Line()

screen.listen()
screen.onkeypress(right_paddle.go_up, "Up")
screen.onkeypress(right_paddle.go_down, "Down")
screen.onkeypress(left_paddle.go_up, "w")
screen.onkeypress(left_paddle.go_down, "s")


game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # Detect collision with wall.
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # Detect collision with right_paddle.
    if ball.distance(right_paddle) < 50 and ball.xcor() > 340 or ball.distance(left_paddle) < 50 and ball.xcor() < -340:
        ball.bounce_x()

    # Right paddle misses.
    if ball.xcor() > 380:
        ball.reset_position()
        score.update_scoreboard()
        score.increase_right_score()

    # Left paddle misses.
    if ball.xcor() < -380:
        ball.reset_position()
        score.update_scoreboard()
        score.increase_left_score()

screen.exitonclick()