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
    x = np.array([float(j) / eVk for j in data[0::2]])
    y = np.array([np.log10(float(j)) for j in data[1::2]])

    plt.plot(x, y, c[i], label=filename)
    plt.xlim(0, 5e6 / eVk)

plt.legend()
plt.show(block=True)

# What is on the x-axis, what o y-axis. Can the threshold be -2eV? Can the
# temperature be negative? Threshold is always the value of the independent
# variable (temperature).
# -------------------------------------------------------------------------
# On the x-axis are temperatures of electrons (in eV), y-axis contains effective 
# cross-section magnitudes [m^2]. I understand now, firstly I looked up for a wrong
# axis and I forgot it is actually log-scaled.

# ionatization threshold ~ 70 eV
# excitation threshold ~ 30 eV

