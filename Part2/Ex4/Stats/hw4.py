from preliminaries import *
import random, scipy.special, scipy.interpolate, math
import itertools as itt
from sys import stdout
norm = numpy.linalg.norm
array = numpy.array

n = 10
p_degree = 3
fit_degree = 4
n_samples = 5000

def mi_itt(length, degree):
    prod = itt.product(range(degree+1), repeat=length)
    return ( i for i in prod if sum(i) <= degree )

def mi_pow(x, i):
    y = 1.0
    for j in range(len(x)):
        y *= x[j]**i[j]
    return y

def mpoly_eval(coeff, x, degree):
    return sum( coeff[j]*mi_pow(x, i) for j,i in enumerate(mi_itt(len(x), degree)) )

def X(mean, sig):
    return array([random.normalvariate(mean[k], sig[k]) for k in range(len(means))])

def xsample(N, mean, sig, p):
    xsamps = numpy.zeros((N, len(mean)) )
    for j in range(len(mean)):
        xsamps[:,j] = numpy.random.normal(mean[j], sig[j], N)
    return xsamps



print "\n\n**** New session ****\n"

print "params:"
print "n = ", n
print "p_degree = ", p_degree
print "fit_degree = ", fit_degree
print "n_samples = ", n_samples


print "drawing coefficients..."
coefficients = numpy.array( \
    [random.normalvariate(0,1) for j in mi_itt(n, p_degree)] )

p = lambda x: mpoly_eval(coefficients, x, p_degree)

means = array([random.normalvariate(0,1) for j in range(n) ])
sigs = 0.5*abs(means)

print "drawing x samples:", n_samples
xsamples = xsample(n_samples, means, sigs, p)

print "building poly matrix..."
X_poly = numpy.array( [[mi_pow(x, i) for x in xsamples ] for i in mi_itt(n, p_degree)] ).transpose()

print numpy.shape(X_poly)

print "building fit matrix..."
if fit_degree != p_degree:
    X_fit = numpy.array([[mi_pow(x, i) for x in xsamples ] for i in mi_itt(n, fit_degree)]).transpose()
else:
    X_fit = X_poly.copy()

print "computing samples..."
Y = numpy.dot(X_poly, coefficients)

print "computing LSQ..."
X2 = numpy.dot(X_fit.T, X_fit)
X2inv = numpy.linalg.inv(X2)
X3 = numpy.dot(X2inv, X_fit.T)
est_coeff = numpy.dot(X3, Y)

est_Y = numpy.dot(X_fit, est_coeff)

if False:
    for i in range(len(Y)):
        print "%08.3e\t%08.3e"%(Y[i], est_Y[i])

print "error:", norm(Y-est_Y)/norm(Y)
print "det:", numpy.linalg.det(X2)
print "cond:", numpy.linalg.cond(X2)


print "\n**** Finished ****\n"





