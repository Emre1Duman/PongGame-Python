from turtle import Screen
from paddle import Paddle

#Screen controls
screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong!")
screen.tracer(0)

#paddles
r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))



screen.listen()
screen.onkey(fun=r_paddle.up, key="Up")
screen.onkey(fun=r_paddle.down, key="Down")

screen.onkey(fun=l_paddle.up, key="w")
screen.onkey(fun=l_paddle.down, key="s")

game_is_on = True
while game_is_on:
    screen.update()





screen.exitonclick()