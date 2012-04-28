from preliminaries import *
import random, scipy.special, math



def Poisson(Lambda=1.0):
    return lambda : numpy.random.poisson(lam=Lambda)

def MLE_Poisson():
    return lambda samples : mean((X for X in samples))



def Question2():

    Lambda = 3.7
    lamhat = MLE_Poisson()
    X = Poisson(Lambda)
    
    N = 20
    n_samples = 1000
    lower, upper = 0.05, 0.95
    samples = [lamhat(X() for x in range(N)) for _ in range(n_samples)]
    samples.sort()
    Q_minus = samples[int(lower*n_samples)]
    Q_plus = samples[int(upper*n_samples)]
    
    print Q_minus, Q_plus

lam = 1.0
N = 10
X = Poisson(lam)
Y = lambda : float(sum(X() for _ in range(N)))
Y = Poisson(lam*N)

plt.hist([Y() for k in range(10000)], bins=100, )
plt.show()




























