from turtle import *

t=[Turtle(), Turtle(), Turtle(), Turtle()]


# get all turtles to starting point
def thome():
    t[0].penup()
    t[1].penup()
    t[2].penup()
    t[3].penup()
    t[0].goto(250,250)  # top right
    t[1].goto(250,-250) # bottom right
    t[2].goto(-250,250) # top left
    t[3].goto(-250,-250)
    t[2].seth(180)
    t[3].seth(180)
    t[0].pendown()
    t[1].pendown()
    t[2].pendown()
    t[3].pendown()

def tforward(dis):
    t[0].forward(dis)
    t[1].forward(dis)
    t[2].forward(dis)
    t[3].forward(dis)

def tleft(angle):
    t[0].left(angle)
    t[1].right(angle)
    t[2].right(angle)
    t[3].left(angle)
    





thome()
t[0].speed(0)
t[1].speed(0)
t[2].speed(0)
t[3].speed(0)
side=10
while side < 200:
    tforward(side)
    tleft(90)
    side = side+10
    


#tforward(100)
#tleft(90)
#tforward(100)
#tleft(90)
#tforward(100)
#tleft(90)
#tforward(100)
#tleft(90)

    
    
