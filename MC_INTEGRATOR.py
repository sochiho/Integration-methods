'''An Adaptive Monte Carlo Integrator'''

#!//////////////////////////////////////////////////////////#
#!//Chiho So
#!//July 2018
#!//////////////////////////////////////////////////////////#
#! /usr/bin/env python

#include "Python.h"
from __future__ import with_statement
from __future__ import division
import vegas
import math, cmath, string, fileinput, pprint
import  os
import sys
from optparse import OptionParser
import random
import cython

#comment out the following if not using matplotlib and numpy
import matplotlib
import mpmath as mp
import numpy as np
import pylab as pl
import scipy
from scipy import interpolate, signal
import matplotlib.font_manager as fm
from matplotlib.ticker import MultipleLocator, FormatStrFormatter
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import matplotlib.path as path
import sys
from scipy.special import spence as Li
import time
import errno
import cPickle as pickle
import shutil
import resource
import gc

date = time.strftime("%m-%d-%H:%M")
cwd = os.getcwd()
base = os.path.splitext(os.path.basename(__file__))[0]

print '\n'
print '----====================================================----'
print 'Adaptive Monte Carlo Integrator'
print '----====================================================----'
print '\n'

def test(x):
    '''test function to integrate'''

    return 1/(math.sqrt(2*math.pi)) * np.exp(-x**2/2)

def integrator(x1, x2, func, Neval):
    '''This function evaluates the integral of f(x) using the MC method of uniform sampling'''
    if isinstance(x1, list):
        ranlist = [y - x for x,y in zip(x1, x2)]
    else:
        ranlist = x2 - x1 #range of integration limits
    #print ranlist

    sum_w = 0
    sum_w_sq = 0
    w_max = 0

    w_ii_array = []
    X_ii_array = []
    
    for ii in range(Neval):

        sys.stdout.write("progress: %d%%   \r" % (float(ii)*100./(Neval)) )
        sys.stdout.flush()
        
        #generate random number
        X_ii = x1 + random.random() * ranlist
        X_ii_array.append(X_ii)

        #calculate weight and append to list
        w_ii = func(X_ii) * ranlist
        w_ii_array.append(w_ii)

        #sum weights, average approximates the integrand
        sum_w += w_ii
        sum_w_sq += w_ii**2

        if w_ii > w_max:
            w_max = w_ii
            X_max = X_ii

    INT = sum_w / Neval
    
    plt.figure
##    plt.scatter(X_ii_array, w_ii_array, color='red', linewidth=1.)
##    plt.xlabel('X_ii')
##    plt.ylabel('w_ii')
##
##    plt.show()
        
    # and its error through the variance
    variance = sum_w_sq/Neval - (sum_w/Neval)**2
    error = math.sqrt(variance/Neval)

    print '----=============================================----'
    print (' Integral: %s \n Variance: %s \n Error: %s \n' % (INT, variance, error))
    print '----=============================================----'
    return 


##integrator([3, 5], [40, 13], test, 100)
for i in range(1):    
    integrator(-2, 2, test, 1000)
        
          
        
    
