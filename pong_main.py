import turtle

"""Make a Chiaki picture the backround"""

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
score.wirte("Player_One: 0    Player_Two: 0",
            align="center", font=("Orbitron", 30, "bold"))

#Moves the paddles vertically
def paddle_up():
    




def paddle_down():





def paddle_ups():





def paddle_downs():










