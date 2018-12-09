# date: 2018-12-9
# author: zp
# goal: finish the clock 7段管

import time
import turtle

print(time.gmtime())
print(time.ctime())

# def drawGap()

def drawLine( draw ):
    if draw:
        turtle.pendown()
    else:
        turtle.penup()
    turtle.fd(40)
    
def drawDigit( digit ):
    #first line
    if digit in [2,3,4,5,6,8,9]:
        drawLine(True)
    else:
        drawLine(False)
    
    #drawLine(True) if digit in [2,3,4,5,6,8,9] else drawLine(False)
    turtle.right(90)
    #second line
    drawLine(True) if digit in [0,1,3,4,5,6,7,8,9] else drawLine(False)
    turtle.right(90)
    drawLine(True) if digit in [0,2,3,5,6,8] else drawLine(False)
    turtle.right(90)
    drawLine(True) if digit in [0,2,6,8] else drawLine(False)
#     turtle.right(90)
    drawLine(True) if digit in [0,4,5,6,8,9] else drawLine(False)
    turtle.right(90)
    drawLine(True) if digit in [0,2,3,5,7,8,9] else drawLine(False)
    turtle.right(90) 
    drawLine(True) if digit in [0,1,2,3,4,7,8,9] else drawLine(False)
#     turtle.left(90)
#     turtlr.fd(50)

def drawDate( date ):
    turtle.pencolor('red')
    for i in date:
        if i == '-':
            turtle.write('年', font=('Arial', 18,'normal'))
            turtle.pencolor('green')
            turtle.fd(40)
        elif i == '=':
            turtle.write('月',font=('Arial',18,'normal'))
            turtle.pencolor('blue')
            turtle.fd(40)
        elif i == '+':
            turtle.write('日',font=('Arial',18,'normal'))
            turtle.pencolor('purple')
        else:
            drawDigit(int(i))
            turtle.left(90)
            turtle.penup()
            turtle.fd(40)
            
def main():
    turtle.setup(1000,350,200,200)
    turtle.penup()
    turtle.fd(-400)
    turtle.pensize(5)


    print(time.strftime('%Y-%m=%d+'))
    drawDate( time.strftime('%Y-%m=%d+') )    
    turtle.done()

main()
