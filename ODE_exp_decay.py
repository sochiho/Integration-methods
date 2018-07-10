from __future__ import division
import numpy
import matplotlib.pyplot as pyplot

'''Decay curve for Iodine-133 analytically and numerically
Comparison of Euler and Heuns method for integrating simple ODE for radiactive decay'''

T_HALF = 20.8 #Hrs
TAU = T_HALF/ numpy.log(2)


def f(n):
    '''Implements the differential for radioactive decay of 'n' nuclei'''
    return -n/ TAU
    # dn/dt = -n/ TAU

def analytic(N0, timebase):
    '''This function calculates the analytical number of atoms at the chosen times'''
    n_analytic = N0 * numpy.exp(-timebase / TAU)

    return n_analytic

def solve_euler(n0, t1, n_panels):
    ''' This function uses Euler's method to integrate DEQ'''
    dt = t1/ n_panels #width of panel
    # Initialise simulation parameters
    n, t = n0, 0
    # Make array
    n_history = numpy.zeros((n_panels,))
    # Integrate each panel
    for i in range(n_panels):
        n_history[i] = n # Record current values
        n = n + f(n)*dt

    return n_history

def solve_heun(N0, t1, n_panels):
    ''' This function uses Heun's method to integrate DEQ'''
    dt = t1/ n_panels
    n, t = N0, 0
    n_history = numpy.zeros((n_panels,))
    for i in range(n_panels):
        n_history[i] = n
        k0 = f(n)
        k1 = f(n + k0 * dt)
        n = n + dt/2 * (k0 + k1)

    return n_history

N0 = 1500
t1 = 60
N_PANELS = 15

timebase = numpy.arange(0, t1, t1/N_PANELS)

n_analytic = analytic(N0, timebase)
n_euler = solve_euler(N0, t1, N_PANELS)
n_heun = solve_heun(N0, t1, N_PANELS)

pyplot.figure()
pyplot.subplot(211)
pyplot.plot(timebase, n_analytic, label = 'analytic', color = 'grey')
pyplot.plot(timebase, n_euler, label = 'euler dt = 4.0 hrs', color = 'red')
pyplot.plot(timebase, n_heun, label = 'heun dt = 4.0 hrs', color = 'blue', linestyle='--')
pyplot.title('Decay curve for Iodine-133')
pyplot.xlabel('Time /hrs')
pyplot.ylabel('Number of atoms')
pyplot.legend(loc= 'upper right')
pyplot.tight_layout()

pyplot.subplot(212)
pyplot.semilogy()
error_euler = abs(n_euler - n_analytic)/n_analytic
error_heun = abs(n_heun - n_analytic)/n_analytic
pyplot.plot(timebase, error_euler, label = 'Euler', color = 'red')
pyplot.plot(timebase, error_heun, label = 'heun', color = 'blue')
pyplot.xlabel('Time /hrs')
pyplot.ylabel('Error in decay curve')
pyplot.legend(loc= 'lower right')
pyplot.tight_layout()

pyplot.show()

'''Heun's method is more accurate than Euler's as it uses trapeziums instead of
rectangles which more accurately represent the curve of the function. Also with Heun's method,
the function is tangent is evaluated at both ends of the interval for a more accurate prediction.'''
    
    

    


