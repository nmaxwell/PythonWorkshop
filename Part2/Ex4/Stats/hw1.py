from preliminaries import *
import random, scipy.special, math


def Weibull(theta=1.0, k=1):
    return lambda: random.weibullvariate(theta, k)

def Weibull_dist(theta=1.0, k=1):
    return lambda x: ((x**(k-1))*k/(theta**k))*math.exp(-(x/theta)**k)*(x > 0.01 )

def Weibull_cdf(theta=1.0, k=1):
    return lambda x: 1.0 - math.exp(-(x/theta)**k)

def gamma_dist(K, th):
    return lambda x: x**(K-1)*math.exp(-x/th)/(th**K* scipy.special.gamma(K))

def MLE_Weibull_theta(k=1.0):
    return lambda samples : mean((X**k for X in samples))**(1.0/k)

def Question3(theta, k, n_samples, file_name):
    
    X = Weibull(theta, k)
    f = Weibull_dist(theta, k)
    cdf = Weibull_cdf(theta, k)
    
    threshold = 0.01
    cutoff = find_end(lambda x: 1.0-cdf(x)-threshold , 0.01)
    
    n_bins = 70
    samples = [X() for u in range(n_samples)]
    sample_range = numpy.linspace(0.0, cutoff, num=1000)
    plt.clf()
    plt.axis([0.05, cutoff, 0.0, 1.0])
    plt.hist(samples, bins=numpy.linspace(0.0,cutoff, num=n_bins), normed=True, color='grey')
    plt.plot(sample_range, [f(x) for x in sample_range], color='black')
    plt.title('Histogram of ' + str(n_samples) + ' samples of Weibull distribution, with pdf. \n' \
        + 'with k = ' + str(k) + ', theta = ' + str(theta))
    plt.xlabel("range of random variable, with tail cutoff")
    plt.ylabel("probability density")
    plt.savefig(file_name)

def Question7(theta, k, file_name):
    
    MLE = MLE_Weibull_theta(k=k)
    X = Weibull(theta=theta, k=k)
    
    theta_hat = lambda N: MLE((X() for j in range(N)))
    
    start = 100
    end = 100000
    steps = 1000
    rate = (float(end)/start)**(1.0/steps)
    n_samples = [ int(start*rate**j) for j in range(0,steps+1)]
    
    plt.clf()
    plt.plot([math.log(n, 10) for n in n_samples], [theta_hat(N) for N in n_samples], color="black")
    plt.title("ML estimator of theta for Weibull \n distribution v.s. number of samples, k=" + str(k))
    plt.xlabel("base-10 logarithm of number of samples")
    plt.ylabel("ML estimator output")
    plt.savefig(file_name)

def MLE_Expectation(N, k, theta, n_samples):
    MLE = MLE_Weibull_theta(k=k)
    X = Weibull(theta=theta, k=k)
    theta_hat = lambda N: MLE((X() for j in range(N)))
    
    E = theta*scipy.special.gamma(N+1.0/k)/(scipy.special.gamma(N)*N**(1.0/k))
    return E, mean((theta_hat(N) for i in range(n_samples)))

print MLE_Expectation(N=10,k=0.5, theta=1.0, n_samples=10000)
print MLE_Expectation(N=10,k=1.0, theta=1.0, n_samples=10000)
print MLE_Expectation(N=10,k=1.5, theta=1.0, n_samples=10000)
print MLE_Expectation(N=100,k=0.5, theta=1.0, n_samples=10000)
print MLE_Expectation(N=100,k=1.0, theta=1.0, n_samples=10000)
print MLE_Expectation(N=100,k=1.5, theta=1.0, n_samples=10000)

k_list = [0.5, 1.5]
n_samples_list = [500, 1000, 2000, 5000, 10000]
file_number = 0
for k in k_list:
    for n_samples in n_samples_list:
        Question3(theta=1.0, k=k, n_samples=n_samples, file_name=str(file_number)+".png")
        file_number += 1

k_list = [0.5, 1.0, 1.5]
for k in k_list:    
    Question7(theta = 1.0, k=k, file_name=str(file_number)+".png")
    file_number+=1
















