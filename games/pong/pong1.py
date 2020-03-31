import turtle
import time
import keyboard
import os
# import tkinter as TK

wn = turtle.Screen()
# wn.bgcolor('blue')
# wn.bgpic("./gitty.jpg")
# window
wn.title("Pong")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)

# Paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350, 0)
scoreA = 0

# Paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup()
paddle_b.goto(350, 0)
scoreB = 0


# Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = .03
ball.dy = .03


# function
def paddle_a_up():
    y = paddle_a.ycor()
    y += 20
    paddle_a.sety(y)


def paddle_a_down():
    y = paddle_a.ycor()
    y -= 20
    paddle_a.sety(y)


def paddle_b_up():
    y = paddle_b.ycor()
    y += 20
    paddle_b.sety(y)


def paddle_b_down():
    y = paddle_b.ycor()
    y -= 20
    paddle_b.sety(y)


def pause():
    while keyboard.wait('p'):
        time.sleep(.1)


def doney():
    wn.done()


# score board
lilly = turtle.Turtle()
lilly.sety(-150)
lilly.speed(0)
lilly.color('deep pink')
style = ("Arial", 15)
lilly.write("{}".format(scoreA), font=style, align='left')
lilly.write("{}:".format(scoreB), font=style, align='right')
lilly.hideturtle()


# keyboard binding
wn.listen()
wn.onkeypress(paddle_a_up, "w")
wn.onkeypress(paddle_a_down, "s")
wn.onkeypress(paddle_b_up, "Up")
wn.onkeypress(paddle_b_down, "Down")
wn.onkeypress(pause, "p")
wn.onkeypress(doney, "d")


# main game loop
automode = True

while True:
    wn.update()

    # if automode:
    #     paddle_a.sety(ball.ycor())
    #    paddle_b.sety(ball.ycor())

    # move ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Boarder Checking
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1

    if ball.xcor() > 430:
        ball.goto(0, 0)
        ball.dx *= -1
        scoreA += 1
        lilly.clear()
        lilly.write("{}".format(scoreA), font=style, align='left')
        lilly.write("{}:".format(scoreB), font=style, align='right')

    if ball.xcor() < -430:
        ball.goto(0, 0)
        ball.dx *= -1
        scoreB += 1
        lilly.clear()
        lilly.write("{}".format(scoreA), font=style, align='left')
        lilly.write("{}:".format(scoreB), font=style, align='right')

    # set variables
    BallDx = ball.xcor()
    BallDy = ball.ycor()
    aDx = paddle_a.xcor()
    aDy = paddle_a.ycor()
    bDx = paddle_b.xcor()
    bDy = paddle_b.ycor()

    # calulations check
    def calcwrite():
        bill = turtle.Turtle()
        bill.sety(-150)
        bill.speed(0)
        bill.color('deep pink')
        style = ("Arial", 15)
        bill.write("xcor for ball:{:.3f}\
            \nycor for ball:{:.3f}\
            \n\nxcor pad A:{:.3f}\
            \nycor pad A:{:.3f}\
            \n\nxcor pad B:{:.3f}\
            \nycor pad B:{:.3f}\
            \n\nCOLLISION MATH:\
            \n\npadatopy:{}\
            \npadabottomy:{}\
            \npadafrontx:{}\
            \npaddle size:{}".format(
                BallDx,
                BallDy,
                aDx,
                aDy,
                bDx,
                bDy,
                aDy + 10,
                aDy - 20,
                aDx + 1,
                paddle_a.shapesize()), font=style, align='left')
        bill.hideturtle()
        bill.clear()

    # calcwrite()
    if aDx - 2 <= BallDx <= aDx + 2 and aDy - 50 <= BallDy <= aDy + 50:
        ball.dx *= -1
        os.system("aplay ./roblox.wav&")
    if bDx - 2 <= BallDx <= bDx + 2 and bDy - 50 <= BallDy <= bDy + 50:
        ball.dx *= -1
