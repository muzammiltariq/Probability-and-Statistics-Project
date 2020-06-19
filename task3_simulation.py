import turtle
import random
bob = turtle.Turtle()
node = turtle.Turtle()
moves = [0,0.5,1]
angles = [0,90,180,270,360]
wn = turtle.Screen()
wn.bgcolor("light blue")
wn.title("Task 3 Simulation")
bob.circle(100)
node.penup()
node.goto(0,100)
node.pendown()
node.color("green")
while True:
    move = random.choice(moves)*100
    deg = random.choice(angles)
    current = ((node.pos()[0]-0)**2) + ((node.pos()[1]-100)**2)
    node.penup()
    print(current)
    node.right(deg)
    node.forward(move)
    if current >= (100**2):
        #node.penup()
        node.goto(0,100) # Takes the node back to the centre of the circle 
        #node.pendown()
    else:
        node.backward(move)
        node.pendown()
        node.forward(move)
        node.right(deg)