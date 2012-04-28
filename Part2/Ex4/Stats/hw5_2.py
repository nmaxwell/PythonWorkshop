from preliminaries import *
import random, scipy.special, scipy.interpolate, math, numpy
import itertools as itt
from sys import stdout
norm = numpy.linalg.norm
dot = numpy.dot
array = numpy.array
import pickle
ln2 = numpy.log(2.0)


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

def xsample(N, mean, sig):
    xsamps = numpy.zeros((N, len(mean)) )
    for j in range(len(mean)):
        xsamps[:,j] = numpy.random.normal(mean[j], sig[j], N)
    return xsamps

class save_class:
    pass

save = pickle.load(open("/home/nmaxwell/save.pickle", 'r'))


def fit(n_samples=100, sig=1.0, lam=1.0):
    n = save.n
    
    xsamples = save.xsamples[0:n_samples]
    
    #d = mean(( norm(x-xsamples[0]) for x in random.sample(xsamples, 100) ))
    #print "d=", d
    #sig *= d
     
    X_poly = save.X_poly[0:n_samples, :]
    
    coefficients = save.coefficients
    Y = numpy.dot(X_poly, coefficients)
    
    M = numpy.exp(-( save.distancesq_matrix[0:n_samples, 0:n_samples] )/(2*sig**2))
    
    Mt = M.transpose()
    Gamma = lam*numpy.eye(n_samples)
    A = dot(Mt,M) + dot(Gamma.transpose(), Gamma)
    est_data = dot(numpy.linalg.inv(A), dot(Mt, Y))
    
    est_Y = dot(M, est_data)
    
    return norm(Y-est_Y)/norm(Y)



def test(n_samples, sig, lam):
    n = save.n
    p_degree = save.p_degree
    #print "drawing x samples:",
    xsamples = xsample(n_samples, save.means, save.sigs)

    #print "building poly matrix..."
    X_poly = numpy.array( [[mi_pow(x, i) for x in xsamples ] for i in mi_itt(n, p_degree)] ).transpose()
    #print "shape of X_poly:", numpy.shape(save.X_poly)
    
    coefficients = save.coefficients
    Y = numpy.dot(X_poly, coefficients)
    
    #print "building  distance squared matrix... "
    
    MM = dot(xsamples, xsamples.transpose())
    distancesq_matrix = numpy.zeros((n_samples, n_samples), dtype=numpy.float64)
    for i,j in itt.product(range(n_samples), range(n_samples)):
        distancesq_matrix[i,j] = MM[i,i] + MM[j,j] - 2*MM[i,j]
    
    M = numpy.exp(-( distancesq_matrix[0:n_samples, 0:n_samples] )/(2*sig**2))
    Mt = M.transpose()
    Gamma = lam*numpy.eye(n_samples)
    A = dot(Mt,M) + dot(Gamma.transpose(), Gamma)
    est_data = dot(numpy.linalg.inv(A), dot(Mt, Y))
    
    est_Y = dot(M, est_data)
    
    return norm(Y-est_Y)/norm(Y)


def train(n_samples):
    
    n_trials = 10
    k = 1.0
    median = 1.0
    sigs = numpy.random.weibull(k, n_trials)*(median/(ln2**(1.0/k)))
    lams = numpy.random.weibull(k, n_trials)*(median/(ln2**(1.0/k)))
    
    samps = []
    for sig in sigs:
        for lam in lams:
            samps.append((sig, lam, fit(n_samples, sig, lam)))
            #print samps[-1]
    
    mn = min(samps, key=lambda x:x[2])
    return mn



def script(n_samples):
    print n_samples

    print "\n*** New Session ***\n"
    print "n_samples: ", n_samples
    print "training..."
    (sig, lam, train_err) = train(n_samples)
    print "randomized training (sig,lam): ", sig, lam
    print "testing..."
    print "traning error: ", train_err, "\n"
    for j in range(5):
        test_err = test(n_samples, sig, lam)
        print "testing error: ", test_err
        
    print "\noptimizing...\n"
    (sig_opt, lam_opt) = scipy.optimize.fmin(lambda x: fit(n_samples, x[0], x[1]), (sig, lam), maxfun=200, maxiter=200)
    print "\noptimized training (sig,lam): ", sig_opt, lam_opt, "\n"
    
    for j in range(5):
        test_err = test(n_samples, sig_opt, lam_opt)
        print "optimized testing error: ", test_err
    print "\n*** End Session ***\n"

if __name__ == "__main__":
    
    import sys
    args = sys.argv[1:]
    if len(args)>0:
        n_samples = int(args[0])
        script(n_samples)
    

"""
import os

for n in [10, 20, 50, 100, 200, 500, 1000, 2000, 5000, 10000]:
    os.system("high-priority python hw5_2.py " + str(n) + " | tee -a output ")
"""



