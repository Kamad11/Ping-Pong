import turtle
import winsound


wn = turtle.Screen()
wn.title("Pong Game")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)

#score
score_a = 0
score_b = 0

#Paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("yellow")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350, 0)

#Paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("red")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup()
paddle_b.goto(350, 0)

#Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("blue")
ball.penup()
ball.goto(0, 0)
ball.dx = 0.17
ball.dy = 0.17

#pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.up()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player A: 0 || Player B: 0", align="center", font=("Courier", 24, "normal"))


#Function
def paddle_a_up():
    y = paddle_a.ycor()
    y += 20
    paddle_a.sety(y)

def paddle_b_up():
    y = paddle_b.ycor()
    y += 20
    paddle_b.sety(y)

def paddle_a_down():
    y = paddle_a.ycor()
    y -= 20
    paddle_a.sety(y)

def paddle_b_down():
    y = paddle_b.ycor()
    y -= 20
    paddle_b.sety(y)

#keyboard binding
wn.listen()
wn.onkeypress(paddle_a_up, "a")
wn.onkeypress(paddle_a_down, "d")
wn.onkeypress(paddle_b_up, "j")
wn.onkeypress(paddle_b_down, "l")


#Main game loop

while True:
    wn.update()

    #move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    #border check
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1
        winsound.PlaySound("jump.wav", winsound.SND_ASYNC)

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1
        winsound.PlaySound("jump.wav", winsound.SND_ASYNC)

    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_a += 1
        pen.clear()
        pen.write(f"Player A: {score_a} || Player B: {score_b}", align="center", font=("Courier", 24, "normal"))

    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_b += 1
        pen.clear()
        pen.write(f"Player A: {score_a} || Player B: {score_b}", align="center", font=("Courier", 24, "normal"))

    #ball collision
    if (340 < ball.xcor() < 350) and (paddle_b.ycor() - 45 < ball.ycor() < paddle_b.ycor() + 45):
        ball.setx(340)
        ball.dx *= -1
        winsound.PlaySound("jump.wav", winsound.SND_ASYNC)

    if (-350 < ball.xcor() < -340) and (paddle_a.ycor() - 45 < ball.ycor() < paddle_a.ycor() + 45):
        ball.setx(-340)
        ball.dx *= -1
        winsound.PlaySound("jump.wav", winsound.SND_ASYNC)

    #AI Player
    if paddle_b.ycor() < ball.ycor() and abs(paddle_b.ycor() - ball.ycor()) > 10:
        paddle_b_up()
    elif paddle_b.ycor() > ball.ycor() and abs(paddle_b.ycor() - ball.ycor()) > 10:
        paddle_b_down()