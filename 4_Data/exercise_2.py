import numpy as np
import matplotlib.pyplot as plt

c = ['r', 'g', 'b', 'm', 'k', 'y', 'c']
eVk = 11604.519

for i in range(0, 3):
    filename = 'csk' + str(i + 1) + '.dat'
    f = open(filename)
    d = f.read()
    f.close()

    data = d.replace('\t', '\n').split('\n')[:-1:]
    x = np.array([float(j) / eVk  for j in data[0::2]])
    y = np.array([np.log(float(j) / (1.602 * 10**-19)) for j in data[1::2]])

    # excitation threshold ~ -3eV
    # ionatization threshold ~ -2eV

    plt.plot(x, y, c[i], label=filename)
    plt.xlim(0, 1e6 / eVk)

plt.legend()
plt.show(block=True)
