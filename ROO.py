import turtle
import time

# Screen setup
screen = turtle.Screen()
screen.bgcolor("black")
screen.title("Simple Shooting Fire Animation")
screen.tracer(0)

# Create a fire projectile turtle
fire = turtle.Turtle()
fire.shape("circle")
fire.color("orange")
fire.penup()
fire.speed(0)
fire.goto(0, -200)
fire.dy = 15  # vertical speed

def shoot_fire():
    y = fire.ycor()
    y += fire.dy
    fire.sety(y)

    if y > 200:
        fire.hideturtle()
        fire.goto(0, -200)
        fire.showturtle()

# Animation loop
while True:
    shoot_fire()
    screen.update()
    time.sleep(0.03)
