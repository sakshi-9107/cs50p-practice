import colorsys
import turtle
screen = turtle.Screen()
screen.bgcolor("black")
t = turtle.Turtle()
t.speed(-50)
t.width(1)
n , h = 50 , 0
for i in range(500):
    c = colorsys.hsv_to_rgb(h,1,1)
    t.color("red")
    h += 1/n
    t.forward(i)
    t.left(100)
    t.forward(1)
    t.left(8)
    t.circle(i, 3)
turtle.done()