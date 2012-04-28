import finance
from fit import *
from datetime import datetime as datetime
import pickle

START_DATE, END_DATE = "01/01/2000", "05/01/2011"
tickers = ["NASDAQ:INTC", "NYSE:IBM", "NASDAQ:MSFT", "NYSE:HPQ", "NYSE:F", "NYSE:XOM", "NASDAQ:ORCL",  "NYSE:PG", "NYSE:JNJ", "NYSE:SNY", "NYSE:HMC", "NYSE:FDX", "NYSE:UPS", "NYSE:KFT", "NASDAQ:COKE", "NYSE:PEP"  ]

load_data = False
save_data = not load_data

def get_finance_data(ticker, start_date, end_date):
    csv = finance.get_google_csv(ticker, start_date, end_date)
    data = finance.parse_csv(csv)
    return data

def fetch_data():
    start_date = datetime.strptime(START_DATE, "%m/%d/%Y")
    end_date = datetime.strptime(END_DATE, "%m/%d/%Y")
    
    length = 1000000
    raw_data = [[] for xt in tickers]
    for k,xt in enumerate(tickers):
        times, raw_data[k] = zip(*get_finance_data(xt, start_date, end_date))
        length = min(length, len(raw_data[k]))
        
    times = numpy.array(times[0:length])
    data = numpy.zeros((length, len(raw_data)), dtype=float)
    for k,xt in enumerate(tickers):
        data[:,k] = raw_data[k][0:length]
    
    return times, data



def Part1():
    if load_data is True:
        data = pickle.load(open("data.pickle", 'r'))
    else:
        data = fetch_data()
        if save_data is True:
            pickle.dump(data, open("data.pickle", 'w'),  pickle.HIGHEST_PROTOCOL)
    
    times, data = data
    N,K = numpy.shape(data)
    print "data size: ", N, K
    #N = 1000
    times = times[0:N]
    Y_data = data[0:N,0]
    X_data = data[0:N,1:]
    
    print "linear regression:"
    coefficients = fit_linear(X_data, Y_data)
    Y_fit = numpy.dot(X_data, coefficients)
    print "\tVar(Y-\hatY), E(Y-\hatY), l2 rel error (%):"
    print '\t%06.2e\t%06.2e\t%04.2f\n'%(var(Y_fit - Y_data), mean(Y_fit-Y_data), 100*norm(Y_fit-Y_data)/norm(Y_data))
    if True:
        plt.clf()
        fig = plt.figure()
        ax = plt.gca()
        plt.plot(times, Y_data, color='0.7', lw=2)
        plt.plot(times, Y_fit,  color='0.0', lw=1)
        plt.title("Stock price: " + tickers[0] +" (light) and linear fit (dark).")
        plt.xlabel("Time")
        plt.ylabel("Stock price($)")
        from matplotlib.ticker import LinearLocator
        from matplotlib.dates import  DateFormatter
        ax.xaxis.set_major_locator(LinearLocator(20))
        ax.xaxis.set_major_formatter(DateFormatter('%b %y'))
        plt.setp( plt.gca().get_xticklabels(), rotation=45, horizontalalignment='right')
        plt.savefig("out/linear_fit.png")
    
    print "non-linear regression:"
    print "training..."
    N = len(Y_data)
    rand_indices = range(N)
    random.shuffle(rand_indices)
    rand_indices_train = rand_indices[0:N/2]
    rand_indices_test = rand_indices[N/2:]
    X_train = X_data[rand_indices_train]
    Y_train = Y_data[rand_indices_train]
    X_test = X_data[rand_indices_test]
    Y_test = Y_data[rand_indices_test]
    sig, lam, alpha, err_train, err_test = train(X_train, Y_train, X_test, Y_test)
    kernel = exp_kernel(sig)
    ker_mat = kernel(dist_sq(X_data, X_train))
    Y_fit = numpy.dot(ker_mat, alpha)
    
    print "\nresults:\n\t(sig,lam): ", sig, lam
    print "\ttain error, test error: "
    print "\t%06.2e\t%06.2e\n"%(err_train, err_test)
    print "\tVar(Y-\hatY), E(Y-\hatY), l2 rel error (%):"
    print '\t%06.2e\t%06.2e\t%04.2f\n'%(var(Y_fit - Y_data), mean(Y_fit-Y_data), 100*norm(Y_fit-Y_data)/norm(Y_data))
    if True:
        plt.clf()
        fig = plt.figure()
        ax = plt.gca()
        plt.plot(times, Y_data, color='0.7', lw=2)
        plt.plot(times, Y_fit,  color='0.0', lw=1)
        plt.title("Stock price: " + tickers[0] +" (light) and non-linear fit (dark).")
        plt.xlabel("Time")
        plt.ylabel("Stock price($)")
        from matplotlib.ticker import LinearLocator
        from matplotlib.dates import  DateFormatter
        ax.xaxis.set_major_locator(LinearLocator(20))
        ax.xaxis.set_major_formatter(DateFormatter('%b %y'))
        plt.setp( plt.gca().get_xticklabels(), rotation=45, horizontalalignment='right')
        plt.savefig("out/non-linear_fit.png")

        


def Part2():
    if load_data is True:
        data = pickle.load(open("data.pickle", 'r'))
    else:
        data = fetch_data()
        if save_data is True:
            pickle.dump(data, open("data.pickle", 'w'),  pickle.HIGHEST_PROTOCOL)
    
    times, data = data
    data = data[1:]-data[0:-1]
    
    mean = [numpy.mean(data[:,k]) for k in range(len(tickers))]
    std = [numpy.std(data[:,k]) for k in range(len(tickers))]
    
    import scipy.stats
    kstest = scipy.stats.kstest
    titles = []
    
    def fit(data, distribution, title=''):
        fname = title
        params = distribution.fit(data)
        D,p_value = kstest(data, cdf=distribution.cdf, args=params)
        title += ", p-value: %05.4f"%p_value
        if p_value > 0.05:
            title += ", Pass"
        else:
            title += ", Fail"
        
        titles.append(title)
        plt.clf()
        sample_range = numpy.linspace(min(data), max(data), 1000)
        plt.hist(data, bins=100, normed=True, color='0.75')
        plt.plot(sample_range, [distribution.pdf(x, *params) for x in sample_range], color='0.0', lw=3)
        plt.title(title)
        plt.ylabel("Probability density")
        plt.xlabel("Daily change in stock price")
        plt.savefig("out/" + fname + ".png")
    
    print "Fitting distribution:"
    for j in range(len(tickers)):
        fit(data[:,j], scipy.stats.laplace, tickers[j]+ ", Laplace distribution")
    
    for j in range(len(tickers)):
        fit(data[:,j], scipy.stats.cauchy, tickers[j]+ ", Cauchy distribution")
        
    for j in range(len(tickers)):
        fit(data[:,j], scipy.stats.hypsecant, tickers[j]+ ", Hyperbolic sec distribution")
    
    for j in range(len(tickers)):
        fit(data[:,j], scipy.stats.norm, tickers[j]+ ", Normal distribution")

    for title in titles:
        print title
    
Part1()
#Part2()



