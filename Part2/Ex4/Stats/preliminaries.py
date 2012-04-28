
# includes:
import numpy
import scipy
import random
import matplotlib
#matplotlib.use('Cairo')
matplotlib.use('MacOSX')
import matplotlib.pyplot as plt
import math
import scipy.optimize
Infinity = float("inf")
norm = numpy.linalg.norm
var = numpy.var
std = numpy.std
pi = numpy.pi

"""
outp = ""
        stdout.write("\b"*len(outp))
        outp = "%d/%d"%(i, N)
        stdout.write(outp)
        stdout.flush()
"""

# helper functions:

def mean(values):
    try:
        return numpy.mean(values)
    except:
        n = 0
        Sum = 0.0
        for x in values:
            n += 1
            Sum += x
        return (1.0/n)*Sum

def find_zero(function, eps = 0.01, start=0.0, x_max=Infinity, scale=1.0):
    """
    Tries to find first point x \in [start, \infinity)
    at which function(x)=0, to within eps.
    
    If function has multiple zeros, may not return the first zero.
    """
    
    sign = function(start)
    if abs(sign) <= 1E-20:
        return start
    
    def binary_search(a,b):
        if ( b-a < eps*2):
            return (a+b)*0.5
        
        if sign*function(0.5*(a+b)) > 0:
            # in right half
            return binary_search(0.5*(a+b), b)
        else:
            # in left half
            return binary_search(a, 0.5*(a+b))
    
    if start+1.0 >= x_max:
        return binary_search(start, x_max)
    
    x = scale
    while sign*function(start+x) > 0:
        x *= 2.0
        if start+x >= x_max:
            if sign*function(start+x) <= 0:
                return binary_search(start+0.5*x, x_max)
            else:
                return None
    
    if x>1.5*scale:
        x1 = 0.5*x
        x2 = x
    else:
        x1 = 0.0
        x2 = scale
    
    return binary_search(start+x1, start+x2)


class DiscretePDF:
    def __init__(self, mode='unenumerated'):
        if mode == 'unenumerated':
            self.reset = self.reset_unenumerated
            self.add_sample = self.add_sample_unenumerated
            self.PDF = self.PDF_unenumerated
        else:
            self.reset = self.reset_enumerated
            self.add_sample = self.add_sample_enumerated
            self.PDF = self.PDF_enumerated
        self.reset()
    
    def size_range(self, ):
        return len(self._count)
    
    def reset_enumerated(self, ):
        self._count = []
        self.n_samples = 0
    
    def add_sample_enumerated(self, sample):
        while sample >= len(self._count):
            self._count.append(0)
         
        self._count[sample] += 1
        self.n_samples += 1
    
    def PDF_enumerated(self ):
        return [ float(self._count[k])/self.n_samples for k in range(len(self._count)) ]
    
    def reset_unenumerated(self, ):
        self._range = []
        self._count = []
        self.n_samples = 0
    
    def add_sample_unenumerated(self, sample):
        if sample not in self._range:
            self._range.append(sample)
            self._count.append(0)
        
        index = self._range.index(sample)
        self._count[index] += 1
        self.n_samples += 1
    
    def PDF_unenumerated(self ):
        return [(self._range[k], float(self._count[k])/self.n_samples) for k in range(len(self._count)) ]

def least_squares( sample_points, data, function, initial_parameters ):
    
    def fit_func(params ):
        return [ data[k] - function(x, params) \
            for k,x in enumerate(sample_points) ]
    
    returned = \
        scipy.optimize.minpack.leastsq( \
        fit_func, initial_parameters )
    fitted_params = returned[0]
    
    l2_dist = sqrt(sum([y**2 for y in fit_func(fitted_params)])) \
        / sqrt(sum([y**2 for y in data]))
    
    return fitted_params, l2_dist



# classes:

class PoissonProcess:
    
    def __init__(self, Lambda):
        self.Lambda = Lambda
        self.reset()
    
    def time(self):
        return random.expovariate(self.Lambda)
    
    def reset(self):
        self.cumulative_times = [0.0, self.time() ]
    
    def sample_path(self, t):
                
        while t >= self.cumulative_times[-1]:
            self.cumulative_times.append(self.time() + self.cumulative_times[-1])
        
        k = len(self.cumulative_times)-1
        while t < self.cumulative_times[k]:
            k -= 1
        return k
    
    def fixed_time_sample(self, t):
        k=0
        s = self.time()
        if t < s:
            return 0
        while s <= t:
            s += self.time()
            k += 1
        return k
