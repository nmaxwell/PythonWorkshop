
import numpy

b = [1.,2,3,4]
A = numpy.array([[1.,0,4,1],
                 [6,9,numpy.pi, numpy.e],
                 [0,0,0,1],
                 [1,2,3,4]])

print "*"*70
print A
A[2,3] = 21.
print A

x = numpy.linalg.solve(A, b)

norm = numpy.linalg.norm
print "*"*70
print norm(numpy.dot(A, x) - b)


import numpy as np
Ainv = np.linalg.inv(A)
print "*"*70
print abs(np.round(np.dot(A, Ainv), 2))


print "*"*70
print A
A[1:3, 2:] = numpy.random.normal(1.3, 0.3, (2, 2))
print A

import scipy as sp
from scipy.stats import bernoulli

B = bernoulli.rvs(0.3, size=(4,4))

print "*"*70
print B
print A*B
print np.dot(A, B)

[a0,a1,a2,a3] = A
print "*"*70
print A
print a2

