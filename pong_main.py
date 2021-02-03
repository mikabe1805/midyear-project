import turtle

"""Make a Chiaki picture the backround"""

screen = turtle.Screen
screen.title = "Chiaki Pong Showdown"
screen.bgcolor = "pink"
screen.setup(width = 2000, height = 800)

#Paddles
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