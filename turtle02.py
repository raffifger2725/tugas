import turtle
turtle.shape("turtle")
for i in range (1):    
    for j in range(0,2):
        turtle.back(100)
        turtle.left(90)
    for j in range (0,4):
        turtle.left(90)
        turtle.forward(90)
turtle.exitonclick()