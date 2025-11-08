import turtle

pen = turtle.Turtle()
pen.speed(1)
pen.color("black")
pen.fillcolor("red")

pen.begin_fill()

for i in range(4):
    pen.forward(100)
    pen.left(70)

pen.end_fill()

turtle.done()