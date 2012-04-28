
import numpy

from Ex1_2 import random_walk

if __name__ == "__main__":
    
    import matplotlib
    matplotlib.use("MacOSX")
    import matplotlib.pyplot as plt
    
    n_steps = 30000
    n_samples = 1000
    
    sample = lambda : random_walk(n_steps)[-1]/n_steps**.5
    samples = [sample() for _ in range(n_samples)]
    
    from scipy.stats import norm, kstest
    params = norm.fit(samples)
    print params
    D, p_value = kstest(samples, cdf=norm.cdf, args=params)
    print p_value
    print "p-value: %05.4f"%p_value
    if p_value > 0.05:
        print "PASS"
    else:
        print "FAIL"
    
    plt.hist(samples, bins=30)
    plt.show()
