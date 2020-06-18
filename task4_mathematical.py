# import matplotlib.pyplot as plt
# import math
# from scipy.stats import uniform

# n = 1000
# start = 0
# width = 1

# data_uniform = uniform.rvs(size=n, loc=start, scale=width)
# plt.plot(data_uniform)
# plt.show()

import random
import matplotlib.pyplot as plt
import math
random.seed()
prob = [0.5, 0.5, 0]  # Change this to change the probability

start = 0   # Change this to change starting position
positions = [start]

numbers = []
for i in range(50):
    numbers.append(random.randint(0, 1000)/1000.0)
for i in numbers:
    if i == prob[2]:
        positions.append(random.uniform(0, 1))
    elif i < prob[0]:
        positions.append(random.uniform(0, 1))
    elif i > prob[1]:
        positions.append(random.uniform(0, 1))
plt.title("task 4")
plt.plot(positions)
plt.show()
print(math.inf)
