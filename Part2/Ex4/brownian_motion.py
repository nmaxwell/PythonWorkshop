import numpy
import numpy as np

l2norm = numpy.linalg.norm
#normalvariate = random.normalvariate

def hitting_position( x=(0.,0.), dt=0.1, drift=lambda t:0.0, region=lambda x: l2norm(x)<=1.0 ):
    
    dimension = len(x)
    sqrt_dt = np.sqrt(dt)
    dW = lambda : sqrt_dt*numpy.random.normal(0.,1., dimension)
    drift_function = drift
    
    t = 0.0
    X = np.array(x)
    logM = 0.0
    
    while region(X):
        
        dW_ = dW()
        drift_ = drift(t)
        
        dX = dW_ + drift_*dt
        logM += -np.dot(drift_,dW_) -.5*dt*np.dot(drift_,drift_)
        
        X += dX
        t += dt
    
    M = np.exp(logM)
    
    return X, M

def hitting_value_distribuion( n_samples=100, measure_sets=[[]], x=(0.,0.), f=lambda x:l2norm(x), dt=0.1, drift=lambda t:0.0, region=lambda x: l2norm(x)<=1.0 ):
    
    distribution = [0. for s in measure_sets ]
    distribution_nocom = [0. for s in measure_sets ]
    
    for k in range(n_samples):
        X, M = hitting_position(x, dt, drift, region)
        fX = f(X)
        
        for k,E in enumerate(measure_sets):
            if fX in E:
                distribution[k] += M/n_samples
                distribution_nocom[k] += 1.0/n_samples
    
    return distribution, distribution_nocom

def sig_m(X):
    xm = mean(X)
    return sqrt(sum([ (xi - xm)**2 for xi in X ])/(len(X)*(len(X)-1)))

def solution( x=(0.,0.) , f=lambda x:l2norm(x), n_samples = 100, dt=0.1, drift=lambda t:0.0, region=lambda x: l2norm(x)<=1.0 ):
    
    results = []
    for k in range(n_samples):
        
        (X, M) = hitting_position(x, dt, drift, region)
        fX = f(X)
        print X, M, fX
        results.append(fX*M)
    
    return mean(results), sig_m(results)















