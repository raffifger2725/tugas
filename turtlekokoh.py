import turtle
turtle.shape("turtle")
for i in range(1):
	for j in range(0,2):
		turtle.forward(200)
		turtle.right(90)
	for j in range(0,1):
		turtle.left(90)
		turtle.forward(200)
	for j in range(0,3):
		turtle.right(90)
		turtle.forward(200)
	for j in range(0,2):
		turtle.back(200)
		turtle.right(90)
turtle.penup()
for i in range(1):
	for j in range(0,3):
		turtle.forward(20)
turtle.pendown()
for i in range(1):
	for j in range(0,1):
		turtle.left(90)
		turtle.forward(400)
turtle.penup()
for i in range(1):
	for j in range(0,1):
		turtle.right(90)
		turtle.forward(50)
turtle.pendown()
for i in range(1):
	for j in range(0,1):
		turtle.right(90)
		turtle.forward(400)
turtle.exitonclick()