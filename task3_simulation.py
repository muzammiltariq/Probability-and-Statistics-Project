import turtle
import random
import math
bob = turtle.Turtle()
bob.hideturtle()
node = turtle.Turtle()
node.hideturtle()
moves = [0,0.5,1]
angles = [0,90,180,270,360]
wn = turtle.Screen()
wn.bgcolor("light blue")
wn.title("Task 3 Simulation")
bob.circle(100)
node.penup()
node.goto(0,100)
node.pendown()
node.showturtle()
node.color("green")
while True:
    move = random.choice(moves)*10
    deg = random.choice(angles)
    current = ((node.pos()[0]-0)**2) + ((node.pos()[1]-100)**2)
    x,y = node.pos()
    node.penup()
    print(current)
    node.right(deg)
    node.forward(move)
    if math.sqrt(current) >= 100:
        node.goto(x,y) # Takes the node back to the centre of the circle 
    else:
        node.backward(move)
        node.pendown()
        node.forward(move)
        node.right(deg)

# from turtle import *
# import random
# import math



# # Task-03
# def Task_03():
    


    
#     T1 = Turtle()
    
#     T1.penup()
#     T1.setpos(0,-100)
#     T1.pendown()
    
#     T1.begin_fill()
#     T1.color("Black")
#     T1.circle(100)
    
    
#     T1.penup()
    
#     T2 = Turtle()
    
#     T2.penup()
    
#     while True:

#       T2.pendown()
      
      
#       x,y = T2.position() # xcor, ycor
#       old_x , old_y = x, y 
#       discrete_steps = [0, 0.5, 1]
#       discrete_angle = 90 * (random.randint(1, 5) - 1)
      
#       # new coordinates 
#       new_x , new_y = x+(random.choice(discrete_steps)* math.cos(discrete_angle)), y+ (random.choice(discrete_steps)* math.sin(discrete_angle))
      
#       # if with in the boundary -> move in any direction
#       if math.sqrt((new_x)*2 + (new_y)*2) < 100:
#           T2.setheading(discrete_angle)
#           #T2.goto(new_x, new_y)
#           x,y = new_x, new_y
#           T2.goto(x,y)
          

#       else:
#           # bounce back / reverse and move negative in direction
#           #T2.setheading(discrete_angle)
#           T2.hideturtle()
#           T2.penup()
#           # reversing the coordinates
#           x,y = -old_x, -old_y
#           T2.goto(x,y)
#           T2.pendown()


          
# Task_03()