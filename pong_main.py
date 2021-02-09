"""
import turtle

#"""Make a Chiaki picture the backround"""

screen = turtle.Screen()
screen.title = "Chiaki Pong Showdown"
screen.bgcolor = "pink"
screen.setup(width = 1000, height=600)

#Left and right paddle features
rp = turtle.Turtle()
rp.speed(0)
rp.shape("square")
rp.color("purple")
rp.shapesize(stretch_wid=6, stretch_len=2)
rp.penup()
rp.goto(400, 0)

lp = turtle.Turtle()
lp.speed(0)
lp.shape("square")
lp.color("purple")
lp.shapesize(stretch_wid=6, stretch_len=2)
lp.penup()
lp.goto(-400, 0)

#Ping pong ball features
ping_pong = turtle.Turtle()
ping_pong.speed(30)
ping_pong.shape("circle")
ping_pong.color("grey")
ping_pong.penup()
ping_pong.goto(0,0)
ping_pong.dx = 5
ping_pong.dy = -5

lp = 0
rp = 0

# Score
score = turtle.Turtle()
score.speed(0)
score.color("purple")
score.penup()
score.hideturtle
score.goto(0,260)
score.write("Player One: 0    Player Two: 0",
            align="center", font=("Orbitron", 30, "bold"))

#Moves the paddles vertically
def paddle_up():
    y = lp.ycor()
    y += 20
    lp.sety(y)

def paddle_down():
    y = lp.ycor()
    y -= 20
    lp.sety(y)

def paddle_ups():
    y = rp.ycor()
    y += 20
    rp.sety(y)

def paddle_downs():
    y = rp.ycor()
    y -= 20
    rp.sety(y)


#paddle controls
screen.listen()
screen.onkeypress(paddle_up, "e")
screen.onkeypress(paddle_down, "x")
screen.onkeypress(paddle_ups, "Up")
screen.onkeypress(paddle_downs, "Down")


while True:
    screen.update()

    ping_pong.setx(ping_pong.xcor()+ping_pong.dx)
    ping_pong.sety(ping_pong.ycor()+ping_pong.dy)


    if ping_pong.ycor() > -280:
        ping_pong.sety(280)
        ping_pong.dy *= -1

    if ping_pong.ycor() < -280:
        ping_pong.sety(-280)
        ping_pong.dy *= -1

    if ping_pong.xcor() > 500:
        ping_pong.goto(0,0)
        ping_pong.dy *= -1
        lp += 1
        score.clear()
        score.write("Left Player: {}     Right Player:  {}". format
                    (lp, rp), align="center",
                    font =("Orbitron", 30, "bold"))

            
if (ping_pong.xcor() > 360 and ping_pong.xcor() < 370) and (ping_pong.ycor() < rp.ycor()+40 and ping_pong.ycor() > rp.ycor()-40):
    ping_pong.setx(360)
    ping_pong.dx*=-1


if (ping_pong.xcor() < -360 and ping_pong.xcor() > -370) and (ping_pong.ycor() < lp.ycor()+40 and ping_pong.ycor() > lp.ycor()-40):
    ping_pong.setx(-360)
    ping_pong.dx*=-1
"""
# Import required libraray 
import turtle 


# Create screen 
sc = turtle.Screen() 
sc.title("Pong game") 
sc.bgcolor("white") 
sc.setup(width=1000, height=600) 


# Left paddle 
left_pad = turtle.Turtle() 
left_pad.speed(0) 
left_pad.shape("square") 
left_pad.color("black") 
left_pad.shapesize(stretch_wid=6, stretch_len=2) 
left_pad.penup() 
left_pad.goto(-400, 0) 


# Right paddle 
right_pad = turtle.Turtle() 
right_pad.speed(0) 
right_pad.shape("square") 
right_pad.color("black") 
right_pad.shapesize(stretch_wid=6, stretch_len=2) 
right_pad.penup() 
right_pad.goto(400, 0) 


# Ball of circle shape 
hit_ball = turtle.Turtle() 
hit_ball.speed(40) 
hit_ball.shape("circle") 
hit_ball.color("blue") 
hit_ball.penup() 
hit_ball.goto(0, 0) 
hit_ball.dx = 5
hit_ball.dy = -5


# Initialize the score 
left_player = 0
right_player = 0


# Displays the score 
sketch = turtle.Turtle() 
sketch.speed(0) 
sketch.color("blue") 
sketch.penup() 
sketch.hideturtle() 
sketch.goto(0, 260) 
sketch.write("Left_player : 0 Right_player: 0", 
			align="center", font=("Courier", 24, "normal")) 


# Functions to move paddle vertically 
def paddleaup(): 
	y = left_pad.ycor() 
	y += 20
	left_pad.sety(y) 


def paddleadown(): 
	y = left_pad.ycor() 
	y -= 20
	left_pad.sety(y) 


def paddlebup(): 
	y = right_pad.ycor() 
	y += 20
	right_pad.sety(y) 


def paddlebdown(): 
	y = right_pad.ycor() 
	y -= 20
	right_pad.sety(y) 


# Keyboard bindings 
sc.listen() 
sc.onkeypress(paddleaup, "e") 
sc.onkeypress(paddleadown, "x") 
sc.onkeypress(paddlebup, "Up") 
sc.onkeypress(paddlebdown, "Down") 


while True: 
	sc.update() 

	hit_ball.setx(hit_ball.xcor()+hit_ball.dx) 
	hit_ball.sety(hit_ball.ycor()+hit_ball.dy) 

	# Checking borders 
	if hit_ball.ycor() > 280: 
		hit_ball.sety(280) 
		hit_ball.dy *= -1

	if hit_ball.ycor() < -280: 
		hit_ball.sety(-280) 
		hit_ball.dy *= -1

	if hit_ball.xcor() > 500: 
		hit_ball.goto(0, 0) 
		hit_ball.dy *= -1
		left_player += 1
		sketch.clear() 
		sketch.write("Left_player : {} Right_player: {}".format( 
					left_player, right_player), align="center", 
					font=("Courier", 24, "normal")) 

	if hit_ball.xcor() < -500: 
		hit_ball.goto(0, 0) 
		hit_ball.dy *= -1
		right_player += 1
		sketch.clear() 
		sketch.write("Left_player : {} Right_player: {}".format( 
								left_player, right_player), align="center", 
								font=("Courier", 24, "normal")) 

	# Paddle ball collision 
	if (hit_ball.xcor() > 360 and
						hit_ball.xcor() < 370) and
						(hit_ball.ycor() < right_pad.ycor()+40 and
						hit_ball.ycor() > right_pad.ycor()-40): 
		hit_ball.setx(360) 
		hit_ball.dx*=-1
		
	if (hit_ball.xcor()<-360 and
					hit_ball.xcor()>-370) and
					(hit_ball.ycor()<left_pad.ycor()+40 and
						hit_ball.ycor()>left_pad.ycor()-40): 
		hit_ball.setx(-360) 
		hit_ball.dx*=-1














