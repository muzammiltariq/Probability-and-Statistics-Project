import random 
import matplotlib.pyplot as plt 
import math
random.seed()
prob = [0.5, 0.5, 0] # Change this to change the probability
start = 0   # Change this to change starting position
positions = [start] 
  
numbers = []
for i in range(50):
    numbers.append(random.randint(0,1000)/1000.0)
for i in numbers:
    if i == prob[2]:
        positions.append(positions[-1])
    elif i < prob[0]:
        positions.append(positions[-1]-1)
    elif i > prob[1]:
        positions.append(positions[-1]+1)

plt.plot(positions) 
plt.show() 