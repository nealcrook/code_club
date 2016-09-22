from turtle import *
from random import *

side=10
while side < 400:
    a1 = randint(87,93)
    a2 = randint(87,93)
    a3 = randint(87,93)
    a4 = randint(87,93)

    forward(side)
    left(a1)
    side = side+10

    forward(side)
    left(a4)
    side = side+10

    forward(side)
    left(a3)
    side = side+10

    forward(side)
    left(a2)
    side = side+10    
