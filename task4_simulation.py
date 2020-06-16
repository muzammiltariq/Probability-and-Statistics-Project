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
bob.speed(3)

while True:
    choose = random.choice(numbers)
    if (choose > 0.5):
        bob.forward(random.uniform(0, 1))
    elif (choose < 0.5):
        bob.backward(random.uniform(0, 1))
turtle.mainloop()
