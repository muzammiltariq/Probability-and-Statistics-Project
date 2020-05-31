import random 
import matplotlib.pyplot as plt 

prob = [0.5, 0.5]   

start = 0   # Change this to change starting position
positions = [start] 
  
numbers = []
for i in range(10):
    numbers.append(random.random()) 
downp=[]
upp=[]
for i in numbers:
    if i < prob[0]:
        positions.append(positions[-1]-1)
    elif i > prob[1]:
        positions.append(positions[-1]+1)
  
# plotting down the graph of the random walk in 1D 
plt.plot(positions) 
plt.show() 