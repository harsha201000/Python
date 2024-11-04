import numpy as np
import matplotlib
import matplotlib.pyplot as plt 
from matplotlib.animation import PillowWriter

fig = plt.figure()
l, = plt.plot([], [], 'k-')

plt.xlim(-5, 5)
plt.ylim(-5, 5)

def func(x):
    return np.sin(x)*3

xlist = np.linspace(-5,5,100)
ylist = func(xlist)

l.set_data(xlist,ylist)
plt.show()