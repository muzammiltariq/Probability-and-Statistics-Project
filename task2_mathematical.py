import random 
import matplotlib.pyplot as plt 

prob1 = [0.5, 0.5, 0]
prob2 = [0.5, 0.5, 0]

start = 0   # Change this to change starting position 
  
numbers = []
for i in range(10):
    numbers.append(random.randint(0,1000)/1000.0)
apart = 200
pos1 = (apart//2)/100
pos2 = (-apart//2)/100
positions1 = [(apart//2)/100]
positions2 = [(-apart//2)/100]
time = 0    #Assumption that this is in seconds
while True:
    #print(positions1[-1],positions2[-1])
    if positions1[-1] == positions2[-1]:
        break
    time = time + 1
    rand1 = random.randint(0,1000)/1000.0
    rand2 = random.randint(0,1000)/1000.0
    if rand1 == prob1[2]:
        positions1.append(positions1[-1])
    elif rand1 > prob1[0]:
        pos1 = pos1 + 1
        positions1.append(positions1[-1]-1)
    elif rand1 < prob1[1]:
        pos1 = pos1 - 1
        positions1.append(positions1[-1]+1)
    if rand2 == prob2[2]:
        positions2.append(positions2[-1])
    elif rand2 > prob2[0]:
        pos2 = pos2 + 1
        positions2.append(positions2[-1]-1)
    elif rand2 < prob2[1]:
        pos2 = pos2 - 1
        positions2.append(positions2[-1]+1)
  
# plotting down the graph of the random walk in 1D 
figure,plots = plt.subplots(2)
plots[0].plot(positions1)
plt.xlabel("time(S)")
plots[1].plot(positions2) 
plt.show() 