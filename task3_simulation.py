import turtle
import random
bob = turtle.Turtle()
node = turtle.Turtle()
moves = [0,0.5,1]
bob.circle(100)
node.penup()
node.goto(0,100)
node.pendown()
node.color("green")
while True:
    move = random.choice(moves)*10
    deg = random.randint(0,360)
    current = ((node.pos()[0]-0)**2) + ((node.pos()[1]-100)**2)
    print(current)
    if current >= (100**2):
        node.goto(0,100) # Takes the node back to the centre of the circle
    #if (node.pos()[0] >= 100 or node.pos()[0] <= -100) or (node.pos()[1] >= 100 or node.pos()[1] <= -100):
    #    node.goto(0,100)
    node.forward(move)
    node.right(deg)