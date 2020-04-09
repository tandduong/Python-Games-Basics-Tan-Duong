# For the windows
import turtle

#tandduong
#The basic Ping-Pong game build by Python 3


# windows screenplay
windows = turtle.Screen();
windows.title("Ping Pong Built by tandduong")
windows.bgcolor("blue")
windows.setup(width=800, height=600)  # Top is 300px, bottom is -300px, left is -400 and right is 400
windows.tracer(0)  # Stop the window from updating

# Name of players display:
name = turtle.Turtle()
name.speed(0)
name.color("white")
name.penup()  # No drawing footprint when the object move
name.hideturtle()
name.goto(0, 270)  # Set the position
name_a = input("Enter your name: ")
name_b = input("Enter your name: ")
name.write(f"{name_a}  vs  {name_b}", align="center", font=("Courier", 24, "normal"))

# Score
score_a = 0
score_b = 0


# Player A
player_a = turtle.Turtle()
player_a.speed(0)
player_a.shape("square")
player_a.color("yellow")
player_a.shapesize(stretch_wid=5, stretch_len=1)
player_a.penup()
player_a.goto(-350, 0)

# Player B
player_b = turtle.Turtle()
player_b.speed(0)
player_b.shape("square")
player_b.color("light green")
player_b.shapesize(stretch_wid=5, stretch_len=1)
player_b.penup()
player_b.goto(350, 0)

# Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0, 0)  # middle of the screen

# Ball Move

# if x degree is >0, move right to 2px each time
ball.dx = 2
# if y degree is >0, move down to 2px each time
ball.dy = -2

# Result
result = turtle.Turtle()
result.speed(0)
result.color("white")
result.penup()
result.hideturtle()  # Hide the turtle symbol on the screen
result.goto(0, 240)
result.write(f"0       0", align="center", font=("Courier", 24, "normal"))


# Game Function - make it move up and down
def player_a_move_up():
    y = player_a.ycor()
    y += 20  # Move up 20px each time
    player_a.sety(y)


def player_a_move_down():
    y = player_a.ycor()
    y -= 20  # Move down 20px each time
    player_a.sety(y)


def player_b_move_up():
    y = player_b.ycor()
    y += 20  # Move up 20px each time
    player_b.sety(y)


def player_b_move_down():
    y = player_b.ycor()
    y -= 20  # Move down 20px each time
    player_b.sety(y)


# Keyboard Binding
windows.listen()
windows.onkeypress(player_a_move_up, "w")  # When user press 'w', call the function player_a_moveUp()
windows.onkeypress(player_a_move_down, "s")  # When user press 's', call the function player_a_movedown()
windows.onkeypress(player_b_move_up, "Up")  # When user press 'up arrow key', call the function player_b_moveUp()
windows.onkeypress(player_b_move_down, "Down")  # When user press 'down arrow key', call the function player_b_movedown()
# Main game

while True:
    windows.update() # Every time the loop run, the screen updated

    # Ball Move
    ball.setx(ball.xcor() + ball.dx)  # each time for the loop, the ball move 2px
    ball.sety(ball.ycor() + ball.dy)  # each time for the loop, the ball move 2px

    # Ball Bouncing (Screen border)

    # Check if the ball hit the border
    if ball.ycor() > 290:
        ball.sety(290)  # if ball at the ycor > 290px, set it to exactly 290px
        ball.dy *= -1  # reverse the ball direction

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1

    if ball.xcor() > 390:
        ball.goto(0, 0)  # If go off the screen to the right, turn back to the middle of the screen
        ball.dx *= -1
        score_a += 1
        result.clear()  # clear the text
        result.write("{}       {}".format(score_a, score_b), align="center",
                     font=("Courier", 24, "normal"))

    if ball.xcor() < -390:
        ball.goto(0, 0)  # If go off the screen to the left, turn back to the middle of the screen
        ball.dx *= -1
        score_b += 1
        result.clear()  # clear the text
        result.write("{}       {}".format(score_a, score_b), align="center",
                     font=("Courier", 24, "normal"))
    # Ball Bouncing (Player)
    if (340 < ball.xcor() < 350) and (player_b.ycor() + 50 > ball.ycor() > player_b.ycor() - 50):
        ball.setx(340)
        ball.dx *= -1

    if (-350 < ball.xcor() < -340) and (player_a.ycor() + 50 > ball.ycor() > player_a.ycor() - 50):
        ball.setx(-340)
        ball.dx *= -1


