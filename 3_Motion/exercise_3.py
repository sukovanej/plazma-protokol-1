from math import sqrt

from scipy import integrate as itg
import numpy as np
import matplotlib.pyplot as plt


def derivs(y, t, E, B, q, m):
    B_0 = 1e-8 # for this magnitude B_O field I can observe a drift in the x-direction
    y_0 = 1e1

    d = np.zeros(np.shape(y))
    B[2] = B_0 * y[1] * y[1] / (y_0 * y_0) # B_z = y * y / (y_0 * y_0)

    d[0:3] = y[3:6]
    d[3:6] = q / m * (E + np.cross(y[3:6], B))
    return d

E = np.array([0.0, 0.0, 0.0])
B = np.array([0.0, 0.0, 0.0])

q = 1.602e-19
m = 9.109e-31

y_0 = 0

ti = 0.0
tf = 10.0
num_points = 1000
t = np.linspace(ti, tf, num_points)

v_0 = 1.0

y0 = np.array([0.0, 0.01, 0.0, v_0 * sqrt(2), v_0 * sqrt(2), 0.0])
res = itg.odeint(derivs, y0, t, args=(E, B, q, m))

x = [i[0] for i in res]
y = [i[1] for i in res]
z = [i[2] for i in res]

plt.plot(y, x)
plt.show(block=True)
