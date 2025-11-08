#polygon
import turtle

pen = turtle.Turtle()

number_of_sides = 6
side_length = 80

for i in range(number_of_sides):
    pen.forward(side_length)
    pen.right(360 / number_of_sides)


turtle.done()