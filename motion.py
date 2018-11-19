from scipy import integrate as itg
import numpy as np
import matplotlib.pyplot as plt

def derivs(y, t, E, B, q, m):
    d = np.zeros(np.shape(y))
    v = y[3:6]
    d[0:3] = v
    d[3:6] = q / m * (E + np.cross(v, B))
    return d

E = np.array([1.0, 0.0, 0.0])
B = np.array([0.0, 0.0, 1.0e-20])

q_e, m_e = -1.602e-19, 9.1e-31
q_p, m_p = 1.602e-19, 1.7e-27

q, m = q_p, m_p

ti = 0.0
tf = 80e12
num_points = 1000
t = np.linspace(ti, tf, num_points)

y0 = np.array([0.0, 0.0, 0.0, 0.0, 0.0, 0.0])
res = itg.odeint(derivs, y0, t, args=(E, B, q, m))

x = [i[0] for i in res]
y = [i[1] for i in res]
z = [i[2] for i in res]

plt.plot(y, x)
plt.show(block=True)
