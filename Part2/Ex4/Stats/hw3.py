from preliminaries import *
import random, scipy.special, scipy.interpolate, math


def X(theta=1.0):
    u = random.random()
    return (1.0-(1-u)**(2.0/3.0)-u)/(theta*(u-1))

def f(x, theta=1.0):
    return (3.0*theta)/(1 + theta*x)**4

def theta_hat(N, theta):
    return 1.0/(2.0*mean( (X(theta) for j in range(N)) ))

def T_hat(N, theta):
    that = theta_hat(N, theta)
    if that <= 1:
        return 1.0
    if that < 2:
        return that
    return 2.0

def data_inverse(sample_points, samples):
    interp = scipy.interpolate.interp1d(samples, sample_points, kind="linear", bounds_error = False, fill_value=0.0)
    sign = samples[-1] - samples[0]
    def ret(x):
        if sign >= 0:
            if x < samples[0]:
                return sample_points[0]
            if x > samples[-1]:
                return sample_points[-1]
        else:
            if x > samples[0]:
                return sample_points[0]
            if x < samples[-1]:
                return sample_points[-1]
        return interp(x)
    return ret


def confidence_interval(thetas, Q_plus, Q_minus):
    A = data_inverse(thetas, Q_plus)
    B = data_inverse(thetas, Q_minus)
    return lambda t_hat: (A(t_hat), B(t_hat))


def question4():
    n = 500
    samples = [T_hat(n, 1.5) for j in range(500)]
    plt.clf()
    plt.hist(samples, bins=40, normed=True)
    plt.title("HIST($\\theta$), $\\theta=1.5$")
    plt.xlabel("Range of $\\hat T$")
    plt.ylabel("Probability density")
    plt.savefig("out/Q4.png")
    print "mean of estimator samples:", "%5.2f"%mean(samples)
    print "mean equadratic error in samples:", "%5.2f"%mean(((s-1.5)**2 for s in samples))

def question56789():
    
    n = 500
    N = 1000
    thetas = [1.0, 1.1, 1.2, 1.3, 1.4, 1.5, 1.6, 1.7, 1.8, 1.9]
    Q_minus, Q_plus = [], []
    
    for theta in thetas:
        samples = sorted([T_hat(n, theta) for j in range(N)])
        Q_minus.append(samples[int(0.05*N)])
        Q_plus.append(samples[int(0.95*N)])
        print "theta:", theta, "Q_minus, Q_plus:", Q_minus[-1], Q_plus[-1]
        print "mean of estimator samples:", "%5.2f"%mean(samples)
        print "mean equadratic error in samples:", "%5.2e"%mean(((s-theta)**2 for s in samples)), "\n"
        if True:
            plt.clf()
            plt.hist(samples, bins=40, normed=True)
            plt.title("HIST($\\theta$), $\\theta=" + "%4.1f"%theta + "$" )
            plt.xlabel("Range of $\\hat T$")
            plt.ylabel("Probability density")
            plt.savefig("out/Q5, theta=" + "%4.1f"%theta +".png")
    
    if True:
        plt.clf()
        plt.plot(thetas, Q_minus, 'ro')
        plt.plot(thetas, Q_plus, 'bo')
        plt.title("$\\theta \\mapsto Q^-$(red), $\\theta \\mapsto Q^+$(blue)")
        plt.xlabel("$\\theta$")
        plt.savefig("out/Quartiles.png")
    
    A = data_inverse(thetas, Q_plus)
    B = data_inverse(thetas, Q_minus)
    
    if True:
        M = 100
        points = numpy.linspace(1.0, 2.0, 100)
        plt.clf()
        plt.plot(Q_minus, thetas, 'ro')
        plt.plot(Q_plus, thetas, 'bo')
        plt.plot( points, [A(x) for x in points], 'k.')
        plt.plot( points, [B(x) for x in points], 'k.')
        plt.title("$z \\mapsto A(z), z \mapsto B(z)$")
        plt.xlabel("$z$")
        plt.axis((1.0, 2.0, 0.9, 2.0))
        plt.savefig("out/Condfidence Intervals.png")
    
    CI = confidence_interval(thetas, Q_plus, Q_minus)
    length = lambda (a,b): b-a
    print "Average CI length:", "%6.3f"%mean(( length(CI(T_hat(n, 1.5))) for j in range(N) ))
    
question4()
question56789()






























