import turtle
t = turtle.Pen()
colors = ["red", "yellow", "blue", "green"]
t.speed(1)
for x in range(2000):
    t.pencolor( colors[ x % 4])
    t.forward(x)
    t.left(91)