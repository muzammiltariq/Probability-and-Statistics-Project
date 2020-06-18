import turtle
import random
bob = turtle.Turtle()
node = turtle.Turtle()
node1 = turtle.Turtle()

moves = [0,1]
angles = [0,360]
steps = 0

for i in range(5):

    bob.speed(10)
    bob.circle(100)

    node.speed(10)
    node1.speed(10)

    node.penup()
    node.goto(random.uniform(moves[0],moves[1])*100,random.uniform(moves[0],moves[1])*100)
    node.pendown()
    node.color("blue")

    node1.penup()
    node1.goto(random.uniform(moves[0],moves[1])*100,random.uniform(moves[0],moves[1])*100)
    node1.pendown()
    node1.color("green")

    while True:
        if (abs((abs(node1.pos()[1]) - abs(node.pos()[1]))) < 10) or (abs((abs(node1.pos()[0]) - abs(node.pos()[0]))) < 10):
            break
        move = random.uniform(moves[0],moves[1])*10
        deg = random.uniform(angles[0],angles[1])
        current = ((node.pos()[0]-0)**2) + ((node.pos()[1]-100)**2)

        move1 = random.uniform(moves[0],moves[1])*10
        deg1 = random.uniform(angles[0],angles[1])
        current1 = ((node1.pos()[0]-0)**2) + ((node1.pos()[1]-100)**2)    

        if current >= (100**2) :
            node.penup()
            node.goto(random.uniform(moves[0],moves[1])*100,random.uniform(moves[0],moves[1])*100) # Takes the node a random position within the circle 
            node.pendown()
            steps = steps + 1
        if current1>= (100**2):
            node1.penup()
            node1.goto(random.uniform(moves[0],moves[1])*100,random.uniform(moves[0],moves[1])*100)
            node1.pendown()
            steps = steps + 1

        node.forward(move)
        node.right(deg)

        node1.forward(move1)
        node1.right(deg1)

        steps = steps + 1
        
    node.clear()
    node1.clear()


print("Average Steps = ", steps//5)
