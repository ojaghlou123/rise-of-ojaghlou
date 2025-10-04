import turtle
import time
import random

# Setup screen
screen = turtle.Screen()
screen.bgcolor("black")
screen.title("Shooting Fire with Explosion")
screen.tracer(0)

# Fire projectile
fire = turtle.Turtle()
fire.shape("circle")
fire.color("orange")
fire.penup()
fire.speed(0)
fire.goto(0, -200)
fire.dy = 15

# Explosion turtle
explosion = turtle.Turtle()
explosion.hideturtle()
explosion.penup()
explosion.speed(0)

def show_explosion(x, y):
    colors = ["yellow", "orange", "red", "white"]
    explosion.goto(x, y)
    for size in range(10, 60, 10):
        explosion.color(random.choice(colors))
        explosion.goto(x, y - size // 2)
        explosion.pendown()
        explosion.begin_fill()
        explosion.circle(size)
        explosion.end_fill()
        explosion.penup()
        screen.update()
        time.sleep(0.05)
        explosion.clear()

def shoot_fire():
    y = fire.ycor()
    y += fire.dy
    fire.sety(y)
    if y > 200:
        fire.hideturtle()
        show_explosion(fire.xcor(), fire.ycor())
        fire.goto(0, -200)
        fire.showturtle()

while True:
    shoot_fire()
    screen.update()
    time.sleep(0.03)
