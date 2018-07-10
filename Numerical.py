from __future__ import division
import numpy
import matplotlib.pyplot as pyplot

def f(x):
    ''' This function operates the following mathematical function'''
    return numpy.cos(x)*(x**2)

def compute_numeric_integral(x0, x1, n_panels):
    ''' This function calculates the definite integral of f(x) from x0 to x1
        using the Simpson's rule and N panels'''
    panel_width = (x1-x0)/ n_panels # to calculate panel width
    func_sum = 0        # sum simpsons approx of panels

    for ix in range(n_panels):
        a = x0 + (ix * panel_width) # a - left (x-axis) of panel
        b = a + panel_width         # b - right (x-axis) of panel
        m = (a+b)/2                 # m - middle (x-axis) of panel
        # Simpsons approximation formulae
        func_sum += ((b-a)/6) * (f(a) + (4*f(m)) + f(b))
    
    return func_sum

def compute_analytic_integral(x0,x1):
    '''This function is an analytical formula to integrate function
    over the same interval'''
    y0 = ((x0**2 - 2) * numpy.sin(x0)) + (2 *(x0) * numpy.cos(x0))
    y1 = ((x1**2 - 2) * numpy.sin(x1)) + (2*(x1) * numpy.cos(x1))
    return y1 - y0
    
# This is a range of panel sizes to be evaluated
PANEL_COUNTS = [4, 8, 16, 32, 64, 128, 256, 512, 1024]
# Bounds to integrate
x0, x1 = 0, 2

# Evaluate error for various panel counts
y_data = []
ref = compute_analytic_integral(x0,x1)

for n in PANEL_COUNTS:
    # for loop to compute numeric integral at different n panels
    s = compute_numeric_integral(0, 2, n)
    # percentage error - abs uses absolute magnitude
    p_error = abs((s-ref)/ref)*100
    # append(p_error) adds values to empty list y_data
    y_data.append(p_error)

pyplot.figure(figsize=(6,6))
pyplot.loglog()
pyplot.scatter(PANEL_COUNTS, y_data)
pyplot.title('''Percentage error in numerical method for f'(x)''')
pyplot.xlabel('Number of Panels')
pyplot.ylabel('Percentage error in numerical method')             
pyplot.tight_layout()
 
pyplot.show()    
