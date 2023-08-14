import turtle
turtle.pensize(5)

print("r=red, g=green, B=black, b=blue, P=purple, p=pink, o=orange, y=yellow, w=white, arrows=move")

def drawUp():
    turtle.seth(90)
    turtle.fd(20)
    
def drawDown():
    turtle.seth(270)
    turtle.fd(20)

def drawLeft():
    turtle.seth(180)
    turtle.fd(20)
    
def drawRight():
    turtle.seth(360)
    turtle.fd(20)

def setRed():
    turtle.color('Red')

def setGreen():
    turtle.color('Green')

def setBlack():
    turtle.color('Black')

def setBlue():
    turtle.color('Blue')

def setPurple():
    turtle.color('Purple')

def setPink():
    turtle.color('Pink')

def setOrange():
    turtle.color('Orange')

def setYellow():
    turtle.color('Yellow')

def setWhite():
    turtle.color('White')

turtle.onkey(drawUp,'Up')
turtle.onkey(drawDown,'Down')
turtle.onkey(drawLeft,'Left')
turtle.onkey(drawRight,'Right')

turtle.onkey(setRed,'r')
turtle.onkey(setGreen,'g')
turtle.onkey(setBlack,'B')
turtle.onkey(setBlue,'b')
turtle.onkey(setPurple,'P')
turtle.onkey(setPink,'p')
turtle.onkey(setOrange,'o')
turtle.onkey(setYellow,'y')
turtle.onkey(setWhite,'w')

turtle.listen()
