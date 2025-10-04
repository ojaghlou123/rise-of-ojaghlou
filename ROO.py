import turtle
import time

# Setup screen
screen = turtle.Screen()
screen.bgcolor("black")
screen.title("Simple Shooting Fire Animation")

# Create turtle for shooting fire
fire = turtle.Turtle()
fire.shape("circle")
fire.color("orange")
fire.penup()
fire.speed(0)
fire.goto(0, -200)
fire.dy = 15  # speed of the fire moving upward

def shoot_fire():
    y = fire.ycor()
    y += fire.dy
    fire.sety(y)

    # When fire reaches top of screen, reset to start position
    if y > 200:
        fire.hideturtle()
        fire.goto(0, -200)
        fire.showturtle()

# Animation loop
while True:
    shoot_fire()
    screen.update()
    time.sleep(0.03)  # control the speed

screen.mainloop()
