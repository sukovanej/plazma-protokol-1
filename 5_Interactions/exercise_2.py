import numpy as np
import matplotlib.pyplot as plt
import scipy.integrate as integrate

v = np.linspace(0, 10000, 5000)


def Fv(v):
    amu = 1.66053904e-27
    m = 28.0 * amu
    kB = 1.3806485e-23
    T = 293.15 # room temperature
    a = m / kB / T
    return np.sqrt(2 / np.pi) * v ** 2 * a ** (3.0 / 2.0) * np.exp(-a / 2 * v ** 2)


n = 1.7e25


for i in [50, 500, 1000, 2500, 5000, 10000]:
    p = integrate.quad(Fv, i, 10000)[0]
    print(str(p * n) + " particles / m^3 are moving fater than " + str(i) + " m / s.")

"""
Result:
1.69781832444e+25 particles / m^3 are moving fater than 50 m / s.
7.00051758969e+24 particles / m^3 are moving fater than 500 m / s.
1.5913347934e+23 particles / m^3 are moving fater than 1000 m / s.
29893323351.1 particles / m^3 are moving fater than 2500 m / s.
9.99666425874e-37 particles / m^3 are moving fater than 5000 m / s.
0.0 particles / m^3 are moving fater than 10000 m / s.
"""
