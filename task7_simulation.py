import turtle
import random
bob = turtle.Turtle()
node = turtle.Turtle()
moves = [0, 0.5, 1]
# angles = [0, 90, 180, 270, 360]
bob.circle(100)
node.penup()
node.goto(0, 100)
node.pendown()
node.color("green")
while True:
    # move = random.choice(moves)
    # deg = random.choice(angles)
    current = ((node.pos()[0]-0)**2) + ((node.pos()[1]-100)**2)
    print(current)
    if current >= (100**2):
        node.penup()
        node.goto(0, 100)  # Takes the node back to the centre of the circle
        node.pendown()
    # if (node.pos()[0] >= 100 or node.pos()[0] <= -100) or (node.pos()[1] >= 100 or node.pos()[1] <= -100):
    #    node.goto(0,100)

    # randomly generates a number between 0 and 1
    node.forward(random.choice(moves))
    # randomly generates a number between 0 and 360
    node.right(random.uniform(0, 360))
