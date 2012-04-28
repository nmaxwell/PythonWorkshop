#for loops

for x in [1,2,3]:
    print x

for c in "foobar":
    print c


for x in range(0,100):
    print x,
    if x % 3 == 0 and x % 5 == 0:
        print "baz"
    elif x % 3 == 0:
        print "foo"
    elif x % 5 == 0:
        print "bar"
    else:
        print 



#list comprehensions

xs = [x for x in [1,2,3]] #[1,2,3]
print xs

xs = [x * 2 for x in [1,2,3]] #[2,4,6]
print xs

xs = [x for x in [1,2,3] if x == 3] # [3]
print xs

xs = [[x,y] for x in [1,2,3] for y in ['1','2','3']] #powerset of x,y
print xs


#sets

xs = set([1,1,1,2,3]) #set([1,2,3])
print xs 
