
#Integer
print 1 + 2 # addition
print 1 - 2 # subtraction
print 1 * 2 # multiplication
print 1 / 2 # integer division
print 2 ** 3

#Float
print 1.5 + 2.5 # addition
print 1 - 2.5   # subtraction
print 10 * .5   # multiplication, (automagic upgrade)
print 1 / 2.0   # division (automagic upgrade)
print 2 ** 3.5

#Decimal
from decimal import *

getcontext().prec = 100

print Decimal(1.1) + Decimal(2.2) # addition
print Decimal(1.1) - Decimal(2.2) # subtraction
print Decimal(1.1) * Decimal(1.1) # multiplication
print Decimal(1.1) / Decimal(2.2) # division
print Decimal(2) ** Decimal(3)

#Fractions
from fractions import *

print Fraction(1,3) #should be exactly 1
print (1.0 / 3.0)

#Complex
print complex(2,3) + complex(1,1)
print complex(4,5) - complex(6,7)
print complex(10,11) * complex(12,13)
print complex(712,23) / complex(1000,88)
print complex(1,1) ** 2
