import turtle
import random
prob = [0.5, 0.5,0] 
wn = turtle.Screen()
wn.bgcolor("light blue")
wn.title("Task 4 Simulation")
bob= turtle.Turtle()
start = 40   # Change start position
bob.penup()
bob.goto(start,0)
bob.pendown()
bob.speed(1)
dist = 0
for i in range(10):
    rand = random.randint(0,10)/10
    print(rand)
    if rand == prob[2]:
        continue
    elif rand > prob[0]:
        dist = dist + 1
        bob.forward((random.randint(0,1000)/1000.0)*100)
    elif rand < prob[1]:
        dist = dist - 1
        bob.backward((random.randint(0,1000)/1000.0)*100)
turtle.mainloop()