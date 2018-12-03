from scipy import integrate as itg
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm

def derivs(y,t,E,q,m,magM):
    d = np.zeros(np.shape(y))
    d[0:3] = y[3:6]
    d[3:6] = q/m*(E + np.cross(y[3:6],bfield(y[0:3],magM)))
    return d

def bfield(radius, M):
    r = np.sqrt(radius[0] * radius[0] + radius[1] * radius[1] + radius[2] * radius[2])
    mu_0 = 4 * np.pi * 10**-7

    return mu_0 / (4 * np.pi) * (3 * radius * np.dot(M, radius) / (r**5) - M / r**3)


E = np.array([0.0,0.0,0.0])
magM = np.array([0.0,0.0,8.10e22])
q = 1.60217662e-19
m = 1.6726219e-27
c = 3e8
re = 6.38e6
Ek_ev = 5e7

#Velocity
vr = c/np.sqrt(1.0+m*c**2/Ek_ev/np.abs(q))
vp = 0.0
vt = np.pi/4
v = np.array([vr*np.sin(vt)*np.cos(vp),vr*np.sin(vt)*np.sin(vp),vr*np.cos(vt)])
#Position
rr = 2.5*re
rp = 0.0
rt = np.pi/2
r = np.array([rr*np.sin(rt)*np.cos(rp),rr*np.sin(rt)*np.sin(rp),rr*np.cos(rt)])
#State vector
y0 = np.array([r[0],r[1],r[2],v[0],v[1],v[2]])

ti = 0.0
tf = 25.0
num_points = 10000
t = np.linspace(ti,tf,num_points)

print("solving")
res = itg.odeint(derivs,y0,t,args=(E,q,m,magM))
print("done")

x = [ i[0]/re for i in res ]
y = [ i[1]/re for i in res ]
z = [ i[2]/re for i in res ]

u, v = np.mgrid[0:2*np.pi:20j, 0:np.pi:10j]
xs = np.cos(u)*np.sin(v)
ys = np.sin(u)*np.sin(v)
zs = np.cos(v)

plt.plot(t, x, c="b")
plt.plot(t, y, c="r")
plt.plot(t, z, c="g")

plt.legend([
    'x-axis of the motion',
    'y-axis of the motion',
    'z-axis of the motion',
])

plt.show()
