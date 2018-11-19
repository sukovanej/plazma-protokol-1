from math import sqrt

from scipy import integrate as itg
import numpy as np
import matplotlib.pyplot as plt

y_init = 1
B_0 = 1.0e13

def derivs(y, t, E, B, q, m):
    d = np.zeros(np.shape(y))
    v = y[3:6]
    d[0:3] = v

    B[2] = B_0 * y[1] * y[1] / (y_init * y_init) # B_z = y * y / (y_0 * y_0)

    d[3:6] = q / m * (E + np.cross(v, B))
    return d

E = np.array([0.0, 0.0, 0.0])
B = np.array([0.0, 0.0, 1.0e-20])

q_e, m_e = -1.602e-19, 9.1e-31
q_p, m_p = 1.602e-19, 1.7e-27

q, m = q_e, m_e
y_0 = 0

ti = 0.0
tf = 38e9
num_points = 1000
t = np.linspace(ti, tf, num_points)

v_0 = 1e4

y0 = np.array([0.0, 0.0, 0.0, v_0 * sqrt(2), v_0 * sqrt(2), 0.0])
res = itg.odeint(derivs, y0, t, args=(E, B, q, m))

x = [i[0] for i in res]
y = [i[1] for i in res]
z = [i[2] for i in res]

plt.plot(y, x)
plt.show(block=True)
