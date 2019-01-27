import numpy as np
from scipy.interpolate import interp1d

f = open("sigmaion.dat")
d = f.read()
f.close()
data = d.replace('\n',',').split(',')[:-1:]
x = np.array([float(i) for i in data[0::2]])
y = np.array([float(i) for i in data[1::2]])

v = np.linspace(0.0,1e7,1e6)
sigma = interp1d(x,y,kind='cubic',bounds_error=False,fill_value=0.0)

def Fv(v, T):
    m = 9.109e-31
    kB = 1.3806485e-23
    # T = 11604.0*15.0
    a = m/kB/T
    return np.sqrt(2.0/np.pi)*v**2*a**(3.0/2.0)*np.exp(-a/2*v**2)

def gaussian(x,x0,sigma):
    return np.exp(-(x-x0)**2/(2*sigma**2))/np.sqrt(2*np.pi)/sigma

kr_MB = lambda T: np.trapz(v * Fv(v, T) * sigma(v), x=v)

def kr_beam(T):
    vmean = np.trapz(Fv(v, T) * v, x=v)
    return np.trapz(v * gaussian(v, vmean, vmean / 100) * sigma(v), x=v)

import matplotlib.pyplot as plt

temperatures = np.linspace(1e3, 5e6, 100)

print("calculating...")

kr_beam_data = [kr_beam(t) for t in temperatures]
kr_MB_data = [kr_MB(t) for t in temperatures]
vmeans = [np.trapz(Fv(v, t) * v, x=v) / 1e20 for t in temperatures]

print("plotting...")

plt.plot(temperatures, kr_beam_data, label='gaussian')
plt.plot(temperatures, kr_MB_data, label='MB')
plt.plot(temperatures, vmeans, label='mean velocity')
plt.legend(loc='upper right')
plt.show()


"""
The mono-energetic beam exceeds the MB coefficient for T ~ <3e5, 2e6>.

I also added the mean velocity in respect to T to the graph - from this plot I can
see that the rate coefficient is highest when the mean velocity is similar to velocities
for which the cross section values are highest.

Thus it makes sence that the gaussian distribution is giving higher rate coefficient
because the integral will have peak if the x0 value is near the sigma extremum. Also
for these heigher temperatures MB distribution is having non-zero values for more
velocities but must have lower extremum (so the total probability is 1).
"""
