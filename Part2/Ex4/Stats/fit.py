from preliminaries import *
import itertools as itt

def tikhonov_reg(A, lam):
    A = numpy.matrix(A)
    n,p = numpy.shape(A)
    Id = numpy.eye(p)
    return numpy.array( (A.T*A + Id*(lam**2)).I*A.T )

def fit_linear(X, Y):
    fit_mat = tikhonov_reg(X, 0.0)
    return numpy.dot(fit_mat, Y)

def dist_sq_slow(x, y):
    n,m = len(x), len(y)
    D = numpy.zeros((n,m), dtype=float)
    for i,j in itt.product(range(n), range(m)):
        D[i,j] = norm(x[i] - y[j])**2
    return D

def dist_sq(x, y):
    if numpy.rank(x) == 1:
        x = numpy.matrix(x).T
        y = numpy.matrix(y).T
        x2 = numpy.multiply(x,x)
        y2 = numpy.multiply(y,y)
        nx, ny = len(x), len(y)
    else:
        x = numpy.matrix(x)
        y = numpy.matrix(y)
        nx,p = numpy.shape(x)
        ny,p = numpy.shape(y)
        ones  = numpy.matrix(numpy.ones(p)).T
        x2 = numpy.multiply(x,x)*ones
        y2 = numpy.multiply(y,y)*ones
    
    ones  = numpy.matrix(numpy.ones(ny))
    x2 = numpy.array(x2*ones)
    ones  = numpy.matrix(numpy.ones(nx))
    y2 = numpy.array(y2*ones).T
    return numpy.array(x2 + y2 - 2* x*y.T)


def exp_kernel(sig):
    return lambda x2: numpy.exp(-x2/(2.0*sig*sig))

def fit_nonlin(X, Y, sig, lam):
    kernel = exp_kernel(sig)
    ker_mat = kernel(dist_sq(X))
    fit_mat = tikhonov_reg(ker_mat, lam)
    coefficients = numpy.dot(fit_mat, Y)
    return numpy.dot(ker_mat, coefficients)


def train(X_train, Y_train, X_test, Y_test):
    dist2_train = dist_sq(X_train, X_train)
    dist2_test = dist_sq(X_test, X_train)
    
    n_trials=5
    k = 1.0
    median = 1.0
    ln2 = numpy.log(2.0)
    sigs = numpy.random.weibull(k, n_trials)*(median/(ln2**(1.0/k)))
    lams = numpy.random.weibull(k, n_trials)*(median/(ln2**(1.0/k)))
    
    def fit(sig, lam):
        kernel = exp_kernel(sig)
        ker_mat_train = kernel(dist2_train)
        fit_mat_train = tikhonov_reg(ker_mat_train, lam)
        alpha = numpy.dot(fit_mat_train, Y_train)
        ker_mat_test = kernel(dist2_test)
            
        res_train = Y_train - numpy.dot(ker_mat_train, alpha)
        res_test = Y_test - numpy.dot(ker_mat_test, alpha)
        
        err_train =  norm(res_train)/norm(Y_train)
        err_test =  norm(res_test)/norm(Y_test)
        return err_train, err_test, alpha
    
    results = []
    for sig in sigs:
        for lam in lams:
            err_train, err_test, alpha = fit(sig, lam)
            results.append((sig, lam, alpha, err_train, err_test))
            #print results[-1]
    
    mn = min(results, key=lambda x: x[3]+x[4] )    
    sig, lam, alpha, err_train, err_test = mn
    def opt_func(x):
        err_train, err_test, alpha = fit(x[0], x[1])
        return err_train + err_test
    sig_opt, lam_opt = scipy.optimize.fmin(lambda x: opt_func(x), (sig, lam), maxfun=200, maxiter=200)
    err_train, err_test, alpha = fit(sig_opt, lam_opt)
    return sig_opt, lam_opt, alpha, err_train, err_test

    





