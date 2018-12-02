import numpy as np
import matplotlib.pyplot as plt

c = ['r', 'g', 'b', 'm', 'k', 'y', 'c']
eVk = 11604.519

for i in range(0, 3):
    filename = 'adv_csk' + str(i + 1) + '.dat'
    f = open(filename)
    d = f.read()
    f.close()

    data = d.replace('\t','\n').split('\n')[:-1:]

    # The logic is really dumb here. I'm checking the approx. number of digits (by log10) and
    # if this number is big enough I assume its in Kelvin and the factor is set to `eKv`
    # otherwise 1 is used the value remains the same. Disadvantages are that I need to know the 
    # whole array at this point thus the processing cant be lazy and it will fail when the values are
    # smaller but still in Kelvins.

    factor = eVk if np.log10(float(data[-2])) > 7 else 1

    x = np.array([float(j) / factor for j in data[0::2]])
    y = np.array([np.log(float(j) / (1.602 * 10**-19)) for j in data[1::2]])

    plt.plot(x, y, c[i], label=filename)
    plt.xlim(0, 1e6 / eVk)

plt.legend()
plt.show(block=True)
