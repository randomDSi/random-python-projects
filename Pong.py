
import turtle as t
import os

# Score varibales

player_a_score = 0
player_b_score = 0

win = t.Screen()    # creating a window
win.title("Pong") # Giving name to the game.
win.bgcolor('black')    # providing color to the HomeScreen
win.setup(width=800,height=600) # Size of the game panel 
win.tracer(0)   # which speed up's the game.

# Creating left paddle for the game

paddle_left = t.Turtle()
paddle_left.speed(0)
paddle_left.shape('square')
paddle_left.color('beige')
paddle_left.shapesize(stretch_wid=5,stretch_len=1)
paddle_left.penup()
paddle_left.goto(-350,0)

# Creating a right paddle for the game

paddle_right = t.Turtle()
paddle_right.speed(0)
paddle_right.shape('square')
paddle_right.shapesize(stretch_wid=5,stretch_len=1)
paddle_right.color('green')
paddle_right.penup()
paddle_right.goto(350,0)

# Creating a pong ball for the game

ball = t.Turtle()
ball.speed(0)
ball.shape('circle')
ball.color('red')
ball.penup()
ball.goto(0,0)
ball_dx = 1.5   # Setting up the pixels for the ball movement.
ball_dy = 1.5

# Creating a pen for updating the Score

pen = t.Turtle()
pen.speed(0)
pen.color('teal')
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write("Humans: 0                    Zombies: 0 ",align="center",font=('Monaco',24,"normal"))


# Moving the left Paddle using the keyboard

def paddle_left_up():
    y = paddle_left.ycor()
    y = y + 15
    paddle_left.sety(y)

# Moving the left paddle down

def paddle_left_down():
    y = paddle_left.ycor()
    y = y - 15
    paddle_left.sety(y)

# Moving the right paddle up

def paddle_right_up():
    y = paddle_right.ycor()
    y = y + 15
    paddle_right.sety(y)

# Moving right paddle down

def paddle_right_down():
    y = paddle_right.ycor()
    y = y - 15
    paddle_right.sety(y)

# Keyboard binding

win.listen()
win.onkeypress(paddle_left_up,"w")
win.onkeypress(paddle_left_down,"s")
win.onkeypress(paddle_right_up,"Up")
win.onkeypress(paddle_right_down,"Down")




# Main Game Loop

while (player_a_score<10 and player_b_score<10):
    win.update() # This methods is mandatory to run any game

    # Moving the ball
    ball.setx(ball.xcor() + ball_dx)
    ball.sety(ball.ycor() + ball_dy)

    # setting up the border

    if ball.ycor() > 290:   # Right top paddle Border
        ball.sety(290)
        ball_dy = ball_dy * -1
        
    
    if ball.ycor() < -290:  # Left top paddle Border
        ball.sety(-290)
        ball_dy = ball_dy * -1
        

    if ball.xcor() > 390:   # right width paddle Border
        ball.goto(0,0)
        ball_dx = ball_dx * -1
        player_a_score = player_a_score + 1
        pen.clear()
        pen.write("Humans: {}                    Zombies: {} ".format(player_a_score,player_b_score),align="center",font=('Monaco',24,"normal"))
        os.system("afplay wallhit.wav&")



    if(ball.xcor()) < -390: # Left width paddle Border
        ball.goto(0,0)
        ball_dx = ball_dx * -1
        player_b_score = player_b_score + 1
        pen.clear()
        pen.write("Humans: {}                    Zombies: {} ".format(player_a_score,player_b_score),align="center",font=('Monaco',24,"normal"))
        os.system("afplay wallhit.wav&")


    # Handling the collisions with paddles.

    if(ball.xcor() > 340) and (ball.xcor() < 350) and (ball.ycor() < paddle_right.ycor() + 40 and ball.ycor() > paddle_right.ycor() - 40):
        ball.setx(340)
        ball_dx = ball_dx * -1
        os.system("afplay paddle.wav&")

    if(ball.xcor() < -340) and (ball.xcor() > -350) and (ball.ycor() < paddle_left.ycor() + 40 and ball.ycor() > paddle_left.ycor() - 40):
        ball.setx(-340)
        ball_dx = ball_dx * -1
        os.system("afplay paddle.wav&")

# Winning the game
if(player_a_score==10):
    pen.goto(0,0)
    pen.write('Humans Win!',align=("center"),font=('Monaco',110,"normal"))
if(player_b_score==10):
    pen.goto(0,0)
    pen.write("Zombies Win!",align=("center"),font=('Monaco',110,"normal"))

            
