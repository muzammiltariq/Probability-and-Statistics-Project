import turtle
import random
wn = turtle.Screen()
wn.bgcolor("light blue")
wn.title("Task 1 Simulation")
numbers = []
for i in range(10):
    numbers.append(random.random())
print(numbers)
bob= turtle.Turtle()
bob.speed(1)
for rand in numbers:
    if rand > 0.5:
        bob.forward(50)
    if rand < 0.5:
        bob.backward(50)
turtle.mainloop()