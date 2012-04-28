from preliminaries import *
import random, scipy.special, scipy.interpolate, math

from math import *


def invert_data(y, sample_points, samples, eps=0.01, interp_kind="linear"):
    sign = samples[-1] - samples[0]
    if sign >= 0:
        if y < samples[0]:
            return sample_points[0]
    else:
        if y > samples[0]:
            return sample_points[0]
    interp = scipy.interpolate.interp1d(sample_points, samples, kind=interp_kind)
    return find_zero( lambda x: interp(x)-y, eps,  sample_points[0],  sample_points[-1])




a,b = 0, 1.8
N = 20
X = sorted([random.uniform(a,b) for k in range(N)])
Y = [ sin(x) for x in X]
plt.plot(X, Y)
plt.show()


samples = numpy.linspace(min(Y), max(Y), 500)

g = scipy.interpolate.interp1d(Y, X, "linear")
plt.clf()
plt.plot(Y, X, 'bo')
plt.show()
plt.plot(Y, X, 'bo')
plt.plot(samples, [g(s) for s in samples])
plt.show()

































