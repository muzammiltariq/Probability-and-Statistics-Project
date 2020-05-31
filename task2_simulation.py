import turtle
import random
prob1 = [0.5, 0.5, 0]
prob2 = [0.5, 0.5, 0]
wn = turtle.Screen()
wn.bgcolor("light blue")
wn.title("Task 2 Simulation")

bob1 = turtle.Turtle()
bob2 = turtle.Turtle()
apart = 200
bob1.penup()
bob1.goto(apart/2,0)
bob1.pendown()
bob2.penup()
bob2.goto(-apart/2,0)
bob2.pendown()
bob1.speed(1)
bob2.speed(1)
bob2.color("red")
bob1.color("green")
bob1.shape("circle")
bob2.shape("circle")
time = 0    #Assumption that this is in seconds and each step takes 1 second
while True:
    if bob1.pos()[0] == bob2.pos()[0]:
        break
    time = time + 1
    rand1 = random.randint(0,1000)/1000.0
    rand2 = random.randint(0,1000)/1000.0
    if rand1 == prob1[2]:
        bob1.forward(0)
    elif rand1 > prob1[0]:
        bob1.forward(50)
    elif rand1 < prob1[1]:
        bob1.backward(50)
    if rand2 == prob2[2]:
        bob2.forward(0)
    elif rand2 > prob2[0]:
        bob2.forward(50)
    elif rand2 < prob2[1]:
        bob2.backward(50)
print("It took " + str(time) + " seconds")
turtle.mainloop()