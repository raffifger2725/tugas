import turtle
turtle.shape("hyena")
for i in range(1):
    turtle.left(90)
    turtle.forward(185)
turtle.penup()
for i in range(1):
    for j in range(0,1):
        turtle.right(90)
        turtle.forward(90)
turtle.pendown()
for i in range(1):
    for j in range(0,2):
        turtle.forward(90)
        turtle.right(90)
    for j in range(0,3):
        turtle.forward(90)
        turtle.left(90)
turtle.penup()
for i in range(1):
    for j in range(0,1):
        turtle.right(90)
        turtle.forward(90)
turtle.pendown()
for i in range(1):
    for j in range(0,4):
        turtle.forward(90)
        turtle.left(90)
    for j in range(0,1):
        turtle.forward(90)
        turtle.left(90)
    for j in range(0,2):
        turtle.forward(90)
    for j in range(0,2):
        turtle.left(90)
        turtle.forward(90)
turtle.exitonclick()