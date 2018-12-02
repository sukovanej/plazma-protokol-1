import numpy as np
import matplotlib.pyplot as plt

colors = ['r', 'g', 'b', 'm', 'k', 'y', 'c']

x = np.linspace(0, np.pi * 2, 1000)
for i in range(1, 5):
    plt.plot(x, np.sin(i * x) / x, colors[i], label="sin(" + str(i) + "x)/x")

plt.legend()
plt.show(block=True)
