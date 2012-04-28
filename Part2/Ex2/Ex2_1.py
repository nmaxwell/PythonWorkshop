

import numpy as np

import matplotlib
matplotlib.use("MacOSX")
import matplotlib.pyplot as plt


fname = "data/9.pha"
with open(fname, 'r') as f:
    lines = f.readlines()

lines = [l.strip() for l in lines]
lines = [l.split() for l in lines]
lines = [map(float, l) for l in lines]
data = np.array(lines)
print data.shape

fname = "data/9.pha"
with open(fname, 'r') as f:
    lines = f.readlines()

lines = [map(float, l.strip().split()) for l in lines]
data = np.array(lines)
print data.shape


for k in range(4):
    plt.subplot(4,1,k+1)
    plt.plot(data[:,k], 'b')
plt.show()




