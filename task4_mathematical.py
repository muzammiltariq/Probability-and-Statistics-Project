import matplotlib.pyplot as plt
import math
from scipy.stats import uniform

n = 1000
start = 0
width = 1

data_uniform = uniform.rvs(size=n, loc=start, scale=width)
plt.plot(data_uniform)
plt.show()
