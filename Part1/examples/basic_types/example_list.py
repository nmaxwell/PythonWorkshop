#Lists

#characteristics of a list
t = [] #empty list, is falsy
print len(t) #should equal zero
print not t
print t

#as a vector
t.append(1) #append at the end
t.append(2)
t.append(3)
print t

#as a stack
print t.pop(), t #3 [1,2]
print t.pop(), t #2 [1]
print t.pop(), t #1 []

#as queue
t = [1,2,3] #literal syntax
print t
print t.pop(0), t #1 [2,3]
print t.pop(0), t #2 [3]
print t.pop(0), t #3 []


t = [1,2,3]
t += [4,5,6] #append another list
print t

#some nice operations
t.reverse()
print t

t.sort()
print t

#heterogenous list
xs = [1,2,'3',4,5,6,'moose', ['nested', 'list'], 55]
print xs

#slices
print xs[-1] #last
print xs[0] #first
print xs[:3] #first three
print xs[3:] #everything except the first three
print xs[::-1] #reversed
print xs[::2] #every other

print [xs[0],xs[-1]] #first and last
