# let make make a ping pong game

import turtle

gm = turtle.Screen()
gm.title("ping_pong by @gautam saha")
gm.bgcolor("black")
gm.setup(width=800, height=600)
gm.tracer

#SOCER
score_a = 0
score_b = 0
#side A
side_a= turtle.Turtle()
side_a.speed(0)
side_a.shape("square")
side_a.color("red")
side_a.shapesize(stretch_wid=5, stretch_len=1)
side_a.penup()
side_a.goto(-390,0)

#sideB
side_b= turtle.Turtle()
side_b.speed(0)
side_b.shape("square")
side_b.color("blue")
side_b.shapesize(stretch_wid=5, stretch_len=1)
side_b.penup()
side_b.goto(390,0)


# Ball


ball= turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0,0)
ball.dx = 3
ball.dy = 3

# contol funtion
def side_a_up():
    Y = side_a.ycor()
    Y += 20
    side_a.sety(Y)
    
def side_a_down():
    Y = side_a.ycor()
    Y -= 20
    side_a.sety(Y)
    
def side_b_up():
    Y = side_b.ycor()
    Y += 20
    side_b.sety(Y)
    
def side_b_down():
    Y = side_b.ycor()
    Y -= 20
    side_b.sety(Y)
    
#keyborad contol
gm.listen()
gm.onkeypress(side_a_up,"w")
gm.onkeypress(side_a_down,"s")
gm.onkeypress(side_b_up, "Up")
gm.onkeypress(side_b_down,"Down")
 # pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen. hideturtle()
pen.goto(0,260)
pen.write("Player A:0 Player B:0" ,align="center", font=("courier",24,"bold") )
 

#main loop
while True:
    gm.update()
    
    # ball movement
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)
    # boder upper and lower
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1
        
    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1
        
    if ball.xcor() >390:
        ball.goto(0,0)
        ball.dx *= -1
        score_a += 1
        pen.clear()
        pen.write("Player A:{} Player B:{}".format(score_a ,score_b) ,align="center", font=("courier",24,"bold") )
 
        
    if ball.xcor() <-390:
        ball.goto(0,0)
        ball.dx *= -1
        score_b += 1
        pen.clear()
        pen.write("Player A:{} Player B:{}".format(score_a,score_b) ,align="center", font=("courier",24,"bold") )
        
    if (ball.xcor()> 340 and ball.xcor()<350) and (ball.ycor( )< side_b.ycor() + 50 and ball.ycor () > side_b.ycor() -50):
        ball.setx(340)
        ball.dx *= -1
        
    if (ball.xcor()<  -340 and ball.xcor()>-350) and (ball.ycor( )< side_a.ycor() + 50 and ball.ycor () > side_a.ycor() -50):
        ball.setx(-340)
        ball.dx *= -1
    
        