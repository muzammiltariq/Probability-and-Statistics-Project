import turtle
import random
wn = turtle.Screen()
wn.bgcolor("light blue")
wn.title("Task 4 Simulation")
numbers = []
for i in range(10):
    numbers.append(random.random())
print(numbers)
bob = turtle.Turtle()
bob.speed(1)
pos1 = bob.pos()
for i in range(100):  # this range could be change to observe more number of trials, e.g. for i in range(1000)
    choose = random.choice(numbers)
    if (choose > 0.5):
        bob.color("red")
        bob.forward(random.uniform(0, 1))
    if (choose < 0.5):
        bob.color("green")
        bob.backward(random.uniform(0, 1))
pos2 = bob.pos()
print(pos2)
distance = pos1[0]-pos2[0]
print("Distance from start position is:", round(abs(distance), 3))
turtle.mainloop()
