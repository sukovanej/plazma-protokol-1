from scipy import integrate as itg
import numpy as np
import matplotlib.pyplot as plt

def derivs(y,t,E,B,q,m):
    d = np.zeros(np.shape(y))
    d[0:3] = y[3:6]
    d[3:6] = q/m*(E + np.cross(y[3:6],B))
    return d

E = np.array([1e-11, 0.0, 0.0])
B = np.array([0.0, 0.0, 1e-11])

q = 1.602e-19
m = 1.672e-27

ti = 0.0
tf = 20000.0

# for the proton value of q / m is ~1000times lower thus the tf
# must be scaled ~1000times so I can observe similar motion like in the case of proton/positron
# also the magnitude of the oscillation are about 3 orders higher

num_points = 1000
t = np.linspace(ti,tf,num_points)

y0 = np.array([0.0, 0.0, 0.0, 2.0, 0.0, 0.0])
res = itg.odeint(derivs,y0,t,args=(E,B,q,m))

x = [ i[0] for i in res ]
y = [ i[1] for i in res ]
z = [ i[2] for i in res ]

plt.plot(y,x)
plt.show(block=True)
