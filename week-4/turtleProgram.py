import turtle
wn = turtle.Screen()

amy = turtle.Turtle()
amy.pencolor("Pink")
amy.forward(50)
if amy.pencolor() == "Pink":
    amy.right(60)
    amy.forward(100)
else:
    amy.left(60)
    amy.forward(100)

kenji = turtle.Turtle()
kenji.forward(60)
if kenji.pencolor() == "Pink":
    kenji.right(60)
    kenji.forward(100)
else:
    kenji.left(60)
    kenji.forward(100)

yoda = turtle.Turtle()
yoda.pencolor("Green")
yoda.backward(50)
if yoda.pencolor() == "Green":
    yoda.left(120)
    yoda.forward(100)
else:
    yoda.left(60)
    yoda.backward(60)
    
franklin = turtle.Turtle()
franklin.backward(60)
if franklin.pencolor() == "Yellow":
    franklin.right(60)
    franklin.forward(100)
else:
    franklin.right(120)
    franklin.forward(100)