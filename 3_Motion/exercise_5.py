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
tf = 1.0
num_points = 10000
t = np.linspace(ti,tf,num_points)

print("solving")
res = itg.odeint(derivs,y0,t,args=(E,q,m,magM))
print("done")

x = [ i[0]/re for i in res ]
y = [ i[1]/re for i in res ]
z = [ i[2]/re for i in res ]

r = []
phi = []
theta = []

def to_spherical(x, y, z):
    r = np.sqrt(x * x + y * y + z * z)
    theta = np.arccos(z / r) * 180 / np.pi
    phi = np.arctan2(y, x) * 180 / np.pi
    return r, theta, phi

for i, _ in enumerate(x):
    polar = to_spherical(x[i], y[i], z[i])
    r.append(polar[0])
    phi.append(polar[1])
    theta.append(polar[2] / np.pi * 180)

plt.plot(t, r, c="b")
plt.plot(t, phi, c="r")
plt.plot(t, theta, c="g")

plt.legend([
    'r-axis of the motion',
    'phi-axis of the motion [rads]',
    'theta-axis of the motion [degrees]',
])

# From the graph analysis
# - the distance from the earth is remaining almost the same during the motion
# - the particle is drifting alogn the magnetic field lines, near the equator the gyration
#   is not as conspicuous as near the pole because in the equator the B field is parallel
#   with the particle velocity
# - due to the mirror effect for theta = n * pi the particle change the direction (the phi-axis
#   is a harmonic function) because near the poles the magnetic field lines are more 
#   concentrated, also one can observe that the theta-axis curve changes quicker near 
#   pi, 2pi, 3pi, etc...

plt.show()
