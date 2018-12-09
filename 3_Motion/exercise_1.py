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

# I configured the E and B so the final Lorentz force remains similar to the case of 
# q = 1 and m = 1

q = 1.602e-19
m = 9.109e-31

# the direction of the drift is given by E x B
# >>> np.cross([1, 0, 0], [0, 0, 1])
# array([ 0, -1,  0])

# the drift doesn't depend on the charge sign nor the mass
# so both electron and positron drift "to the left" in the graph (because of the negative
# sign of the vector product)

ti = 0.0
tf = 10.0
num_points = 1000
t = np.linspace(ti,tf,num_points)

y0 = np.array([0.0, 0.0, 0.0, 2.0, 0.0, 0.0])
res = itg.odeint(derivs,y0,t,args=(E,B,q,m))

x = [ i[0] for i in res ]
y = [ i[1] for i in res ]
z = [ i[2] for i in res ]

plt.plot(y,x)
plt.show(block=True)
