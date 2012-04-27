for x in [1,2,3,4]:
    if x == 1:
        print x
    elif x == 2:
        continue
    elif x == 3:
        break

fun = lambda x: x + 1

print fun(1)
print fun(2)

print filter(lambda x: x > 2,[1,2,3])
print map(lambda x: x * x, [1,2,3])
print [x * x for x in [1,2,3]]

if 1 > 2:
    print "nope"
elif 2 > 3: 
    print "nope again"
else:
    print "Yay"

try:
    print "starting divide"
    1 / 0
    print "i accomplished the impossible"
except:
    print "oops"

with open('afile','w'):
    print "i automatically open and close things"


def infinite_fib():
    a = b = 1
    while True:
        yield a
        a,b = b,a+b

xs = infinite_fib()
for x in xs:
    if x > 100:
        break
    print x




