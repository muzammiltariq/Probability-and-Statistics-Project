import turtle
import random 
prob = [0.5, 0.5,0]  # Change this to change the probability
wn = turtle.Screen()
wn.bgcolor("light blue")
wn.title("Task 1 Simulation")
numbers = []
for i in range(50):
    numbers.append(random.random())
print(numbers)
bob= turtle.Turtle()
start = 40   # Change start position
bob.penup()
bob.goto(start,0)
bob.pendown()
bob.speed(1)
bob.color("green")
bob.shape("circle")
dist = 0
for rand in numbers:
    if rand == prob[2]:
        continue
    elif rand > prob[0]:
        print("forward")
        dist = dist + 1
        bob.forward(50)
    elif rand < prob[1]:
        print("backward")
        dist = dist - 1
        bob.backward(50)
print("Total distance from starting position is: " + str(dist))
turtle.mainloop()