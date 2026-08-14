import turtle

pen = turtle.Turtle()
pen.speed(0)  # Makes it draw instantly

# A sequence that adds 5 to the line length every single step
length = 5

for i in range(60):
    pen.forward(length)
    pen.right(91)  # A slight tilt makes a cool spiral pattern
    length = length + 5  # <--- Our math sequence rule

turtle.done()
