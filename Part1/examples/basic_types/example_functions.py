def add(x,y):
    return x + y

def add_varargs(*args):
    return sum(args)

def add_kwargs(**kwargs):
    for key,value in kwargs.items():
        print "adding",key,value
    return sum(kwargs.values())


add_1(1,2)

add_varargs(1,2,3,4,5)

add_varargs(*range(100))

add_kwargs(x=1,y=2,z=3)


def square_and_cube(x):
    return (x * x, x * x * x)

square,cube = square_and_cube(3)
