import matplotlib.pyplot as plt
import random

heads_tails = [0, 0]

for x in range(100000):
    if x % 50 == 0:
        heads_tails[random.randint(0, 1)] += 1
        plt.bar([0,1], heads_tails, color=("blue", "red"))
        plt.pause(0.001)

plt.show()