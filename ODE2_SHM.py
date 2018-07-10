from __future__ import division


import numpy
import matplotlib.pyplot as pyplot
import scipy.integrate

# Constants
g = 9.81 # m/s^2

# Pendulum Parameters
LENGTH = 1.50 # length, m
MASS = 0.50   # mass, kg

def f(X, t):
    '''DEG for the simple pendulum'''
    theta, omega = X # unpack state into variables

    dTheta = omega
    dOmega = -(g/ LENGTH) * theta
    
    return numpy.array((dTheta, dOmega))

# Initial conditions
THETA0 = 0.2
OMEGA0 = 0.0
X0 = numpy.array((THETA0, OMEGA0))

def solve_euler(X0, t1, n_panels):
    ''' This function uses the Euler method to solve DEQ'''
    
    dt = t1 /n_panels
    X0 = numpy.array((THETA0, OMEGA0))

    res_euler = numpy.zeros((n_panels, 2))
    
    x = X0
    for i in range(n_panels):
        res_euler[i] = x
        x = x + f(x,t1) * dt

    return res_euler

# Scipy solver
n_panels, t1 = 2500, 30
timebase = numpy.arange(0, t1, t1/n_panels)
res_scipy = scipy.integrate.odeint(f, X0, timebase)

def energy(res):

    theta = res[:,0]
    omega = res[:,1]
    energy = MASS * g * LENGTH * (1 - numpy.cos(theta)) + 0.5 * MASS * (LENGTH**2) * (omega **2)

    return energy

res_euler1 = solve_euler(X0, t1, n_panels)

energy_euler = energy(res_euler1)
energy_scipy = energy(res_scipy)

pyplot.figure()
pyplot.subplot(211)
pyplot.plot(timebase, res_scipy[:,0], label = 'scipy', color = 'red')
pyplot.plot(timebase, res_euler1[:,0], label = 'Euler', color = 'blue')
pyplot.title('Value of theta vs. Time')
pyplot.xlabel('Time /s')
pyplot.ylabel('theta /degrees')
pyplot.legend(loc = "lower right")

pyplot.subplot(212)
pyplot.plot(timebase, energy_scipy, label = 'Scipy', color = 'red')
pyplot.plot(timebase, energy_euler, label = 'Euler', color = 'blue')
pyplot.title('Total Energy vs. Time')
pyplot.xlabel('Time /s')
pyplot.ylabel('Energy / J')
pyplot.legend(loc = "lower right")

pyplot.tight_layout()
pyplot.show()

''' There is an error in the Euler method which is present in each
timestep, causing the total energy in the pendlum to exponentially increase'''

''' The error in odeint appears to fluctuate between being a positive
or negative error. Therefore after multiple periods of the pendulum, the errors
cancel each other so it appears that total energy is conserved and remains constant'''
