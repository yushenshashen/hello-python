# date: 2018-12-9
# author: zp
# goal: finish the koch snowflower

import time
import turtle


def koch(size, n):
    if n == 0:
        turtle.fd(size)
    else:        
        koch( size/3, n-1 )
        turtle.left(60) 
        koch( size/3, n-1 )
        turtle.right(120)        
        koch( size/3,n-1 )
        turtle.left(60)
        koch( size/3, n-1 )

def main()
    level = 3
    turtle.setup(1000,1000,200,200)
    turtle.penup()
    turtle.pensize(3)
    turtle.goto(-200,100)
    turtle.pendown()
    koch(400,level)
    turtle.right(120)
    koch(400,level)
    turtle.right(120)
    koch(400,level)
    turtle.hideturtle()
    turtle.done()
main()
