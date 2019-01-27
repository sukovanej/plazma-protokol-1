import numpy as np
import matplotlib.pyplot as plt

v = np.linspace(0, 4000, 5000)
amu = 1.66053904e-27
m = 40.0 * amu
kB = 1.3806485e-23
T = 1000.0
a = m / kB / T

def Fv(v):
    return np.sqrt(2 / np.pi) * v ** 2 * a ** (3.0 / 2.0) * np.exp(-a / 2 * v ** 2)


v_mean = np.trapz(v * Fv(v), x=v)
v_sq_mean = np.sqrt(np.trapz(v ** 2 * Fv(v), x=v))

v_mp = max([(x, Fv(x)) for x in v], key=lambda x: x[1])[0]
mp = Fv(v_mp)

v_mean_an = 727.54
v_sq_mean_an = np.sqrt(623584)
v_mp_an = np.sqrt(2 / a)


print(v_mean, v_sq_mean, v_mp)
print(v_mean_an, v_sq_mean_an, v_mp_an)
print(v_mean - v_mean_an, v_sq_mean - v_sq_mean_an, v_mp - v_mp_an)

plt.plot(v, Fv(v))
plt.plot(v_mean, Fv(v_mean), 'o')
plt.plot(v_sq_mean, Fv(v_sq_mean), 'o')
plt.plot(v_mp, Fv(v_mp), 'o')
plt.show(block=True)

"""
 - Differences between analytical and numerical values are really small, the difference is
   probably caused by finite domain of the integral instead of set <0, +inf> used in the
   analytical approach.
 - Calculated values are in order v_mp > v_mean > v_sq_mean and their order doesnt change
   with temperature.
 - The lower the number of points of integration is, the difference between numerical and
   analytical is higher -> so to have better result of the integral we have to make sure
   the density of the domaing set is high enough.
"""
