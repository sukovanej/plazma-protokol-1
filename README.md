# My solution

## Exercise 1

I configured the magnetic field to be of magnitude ![eq1](https://latex.codecogs.com/gif.latex?10%5E%7B-20%7D). I also
set the charge and weight `q_e` and `m_e` for the electron and `q_p` and `m_p` for the proton so I can easily change
then on demand.

```python
E = np.array([1.0, 0.0, 0.0])
B = np.array([0.0, 0.0, 1.0e-20])

q_e, m_e = 1.602e-19, 9.1e-31
q_p, m_p = 1.602e-19, 1.7e-27

q, m = q_p, m_p
```

I used time scale:

```python
tf = 38e9
```

The result for each particle (electron, positron) is:

![proton](https://raw.githubusercontent.com/sukovanej/plazma-protokol-1/master/electron.png)
![proton](https://raw.githubusercontent.com/sukovanej/plazma-protokol-1/master/positron.png)

 - *What kind of drift do you observe?*
    - Its ![eq2](https://latex.codecogs.com/gif.latex?E%20%5Ctimes%20B) drift
 - *What is the direction of the drift for an electron a what for a positron?*
    - Positron should have the drift velocity in a direction of ![eq2](https://latex.codecogs.com/gif.latex?E%20%5Ctimes%20B), thus in the direction of y axis. Electron have the same magnitude of velocity but in an opposite direction.

## Exercise 2

For proton I setup the time scale to

```python
tf = 80e12
```

![proton](https://raw.githubusercontent.com/sukovanej/plazma-protokol-1/master/proton.png)

Amplitudes of the oscillation for proton are about 2000times bigger then for the electron/positron. Drift velocities
should be the same - the time scale I used for proton is ~2000 times bigger and the x-axis scale in the
graph is also about 2000times bigger - so it probably works.

# Exercises

**Exercise 1**
* Run the [script](https://github.com/tungli/F5170-python/blob/master/3_Motion/motion.py).  
* Configure the velocity, position and fields as you want.  
* Configure the mass and charge to that of an electron.  
* What kind of drift do you observe?  
* What is the direction of the drift for an electron a what for a positron?  

**Exercise 2**
* Now configure the parameters for a proton
* How many times do you have to increase/decrease the time scale for the plot of the trajectory to be comparable to that of an electron
* Compare the amplitudes of the oscillation and the magnitudes of the drift velocities for proton and electron

**Exercise 3**
* Study a charged particle in the following field and with the following velocity:

[prob3](https://camo.githubusercontent.com/84882879c5267533ff99ac912d8b84e11c750fa3/687474703a2f2f6d61746875726c2e636f6d2f796370346135776a2e706e67)

* Do you observe any drift? If yes, for what parameters did you use? What is the direction of the drift velocity for an electron and a positron?
* Try to match your observations with theoretical predictions.

**Advanced exercise**
* Study both an electron and a proton in an electric field which varies harmonically with time and in uniform magnetic field. Try different frequencies.
* How do they react to the field?
* Compare the effect for various frequencies 
