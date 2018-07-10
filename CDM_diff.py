from __future__ import division
import numpy
import matplotlib.pyplot as pyplot

def f(x):
    '''Function operates the mathematical function f(x)=sin(x)'''
    return numpy.sin(x)

def f_prime_numeric(x, dx):
    '''This function uses the central difference method
        to estimate the derivatve of f(x) w.r.t x'''
    return (f(x + (dx/2)) - f(x - (dx/2)))/dx

xs = numpy.linspace(-numpy.pi, numpy.pi, 100)
# Returns a sample of 100 evenly spaced numbers from -pi to pi 

# Evaluate derivatives for three values of dx
df_dx_small = f_prime_numeric(xs, dx =10e-16)
df_dx_medium = f_prime_numeric(xs, dx =10e-3)
df_dx_large = f_prime_numeric(xs, dx =10)

pyplot.figure(figsize=(8,4))
pyplot.plot(xs, df_dx_small - numpy.cos(xs), label='small dx 10$^{-16}$', color='blue')
pyplot.plot(xs, df_dx_medium - numpy.cos(xs), label='medium dx 10$^{-3}$', color='green')
pyplot.plot(xs, df_dx_large - numpy.cos(xs), label='large dx 10', color='red')
pyplot.title('A graph of Error in derivative f(x)')
pyplot.xlabel('radians')
pyplot.ylabel('Error in df')
pyplot.legend(loc= 'lower right')
pyplot.tight_layout()
pyplot.show()

'''From the equation for central difference method, as dx tends to zero,
the value approximated for the gradient becomes closer to the true value of f'(x)
hence at large values of dx, the gradient error is big.However the calculations are performed
only to a finite precision so when dx is too small a large rounding error manifests which
explains the fluctuations in the error for small dx.'''
    
