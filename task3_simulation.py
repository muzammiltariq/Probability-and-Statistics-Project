import turtle
import random
bob = turtle.Turtle()
node = turtle.Turtle()
moves = [0,0.5,1]
bob.circle(100)
node.penup()
node.goto(0,100)
node.pendown()
while True:
    current = ((node.pos()[0]-0)**2) + ((node.pos()[1]-100)**2)
    print(current,100**2)
    if current < (100**2):
        node.right(180)
    node.forward(random.choice(moves)*100)
    node.right(random.randint(0,360))