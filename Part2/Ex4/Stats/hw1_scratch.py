from preliminaries import *
import random, scipy.special, math

def Weibull(theta=1.0, k=1):
    return lambda: random.weibullvariate(theta, k)
















Lambda = 1.3
N = 10

X = lambda : random.expovariate(Lambda)
Z = lambda : sum([X() for j in range(N)])
G = lambda : random.gammavariate(N, 1.0/Lambda)
def gamma_dist(k, theta):
    return lambda x: x**(k-1)*math.exp(-x/theta)/(theta**k* scipy.special.gamma(k))
g = gamma_dist(N, 1.0/Lambda)


n_samples = 100000
samples = [Z() for u in range(n_samples)] 
sample_range = numpy.linspace(min(samples), max(samples), num=500)
plt.hist(samples, bins=100, normed=True)
plt.plot(sample_range, [g(x) for x in sample_range])
plt.show()



























