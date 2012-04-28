
import numpy

def random_walk(n_steps=10):
    pos = [0,]
    for k in range(n_steps):
        r = numpy.random.randint(0,2)
        if r == 0:
            pos.append(pos[-1] + 1)
        else:
            pos.append(pos[-1] - 1)
    return pos

def random_walk(n_steps=10):
    r = numpy.random.randint(0,2, n_steps)
    r[0] = 0
    r = r*2 - 1
    r = numpy.cumsum(r)
    return r

if __name__ == "__main__":
    
    import matplotlib
    matplotlib.use("MacOSX")
    import matplotlib.pyplot as plt
    
    rw = random_walk(1000)
    plt.plot(rw, )
    plt.show()


