import turtle

turtle.pensize(4)
turtle.speed(6)
# roof:
turtle.goto(200,200)
turtle.goto(400,0)
turtle.left(180)
turtle.forward(400)

# walls:
turtle.left(90)
turtle.forward(200)
turtle.left(90)
turtle.forward(400)
turtle.left(90)
turtle.forward(200)
turtle.goto(400,-200)
turtle.left(90)

# garden: 
turtle.forward(800)
turtle.right(180)
turtle.forward(1000)

# tree:
turtle.goto(-200,-200)
turtle.right(270)
turtle.forward(200)
turtle.goto(-200,-200)
turtle.goto(-250,-200)
turtle.forward(200)

# test 1:
duck = turtle.Pen()
duck.pensize(4)
duck.speed(10)
duck.penup()
duck.goto(-250,0)
duck.pendown()
duck.speed(1000)
duck.left(230)
for x in range(150):
    duck.forward(1)
    duck.right(1)
print(duck.pos())

# tree part 1:
duck.penup()
duck.goto(-350.72,45.90)
duck.pendown()
duck.speed(1000)
duck.left(90)
for x in range(150):
    duck.forward(1)
    duck.right(1)
print(duck.pos())

# tree part 2:
duck.penup()
duck.goto(-361.33,156.08)
duck.pendown()
duck.speed(1000)
duck.left(90)
for x in range(150):
    duck.forward(1)
    duck.right(1)
print(duck.pos())

# tree part 3:
duck.penup()
duck.goto(-271.22,220.36)
duck.pendown()
duck.speed(1000)
duck.left(90)
for x in range(150):
    duck.forward(1)
    duck.right(1)
print(duck.pos())

# tree part 4:
duck.penup()
duck.goto(-170.50,174.46)
duck.pendown()
duck.speed(1000)
duck.left(120)
for x in range(150):
    duck.forward(1)
    duck.right(1)
print(duck.pos())

# tree part 5:
duck.penup()
duck.goto(-106.22,84.35)
duck.pendown()
duck.speed(1000)
duck.left(70)
for x in range(150):
    duck.forward(1)
    duck.right(1)
print(duck.pos())



