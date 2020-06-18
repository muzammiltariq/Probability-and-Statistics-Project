import turtle
import random
bob = turtle.Turtle()
node = turtle.Turtle()
moves = [0,1]
angles = [0,360]
bob.circle(100)
node.penup()
node.goto(0,100)
node.pendown()
node.color("blue")

while True:
    move = random.uniform(moves[0],moves[1])*10
    deg = random.uniform(angles[0],angles[1])
    current = ((node.pos()[0]-0)**2) + ((node.pos()[1]-100)**2)
    print(current)
    if current >= (100**2):
        node.penup()
        node.goto(0,100) # Takes the node back to the centre of the circle 
        node.pendown()
    node.forward(move)
    node.right(deg)
move = random.uniform(moves[0],moves[1])
print (move)
