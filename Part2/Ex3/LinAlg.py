import numpy
import array_structs


def py_mat_mult(A, B):
    A = numpy.array(A)
    B = numpy.array(B)
    N1, N2 = A.shape
    N2, N3 = B.shape
    C = numpy.zeros((N1, N3), dtype=float)
    for i in range(N1):
        for j in range(N3):
            S = 0.0
            for k in range(N2):
                S += A[i,k]*B[k,j]
            C[i,j] = S
    return C

import ctypes

linalg_dll = "liblinalg.dynlib"
c_linalg = ctypes.cdll.LoadLibrary(linalg_dll)
#print dir(c_linalg)
c_linalg.mat_mult1.argtypes=[ctypes.c_int, ctypes.c_int, ctypes.c_int, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p ]
c_linalg.mat_mult2.argtypes=[ ctypes.c_void_p ]*3

def c_mat_mult1(A, B):
    N1, N2 = numpy.shape(A)
    N2, N3 = numpy.shape(B)
    A_flat = numpy.array(numpy.array(A, dtype=numpy.float64, order='C').flat)
    B_flat = numpy.array(numpy.array(B, dtype=numpy.float64, order='C').flat)
    AB_flat = numpy.zeros(N1*N3, dtype=numpy.float64, order='C')
    assert(AB_flat.strides == (8,))
    assert(A_flat.strides == (8,))
    assert(B_flat.strides == (8,))
    c_linalg.mat_mult1(N1, N2, N3, A_flat.ctypes.data_as(ctypes.c_void_p), 
                       B_flat.ctypes.data_as(ctypes.c_void_p), 
                       AB_flat.ctypes.data_as(ctypes.c_void_p) )
    AB = AB_flat.reshape(N1, N3)
    return AB

def c_mat_mult2(A, B):
    N1, N2 = numpy.shape(A)
    N2, N3 = numpy.shape(B)
    
    A = numpy.array(A, dtype=numpy.float64)
    B = numpy.array(B, dtype=numpy.float64)
    AB = numpy.zeros((N1, N3), dtype=numpy.float64)
    
    A_ = array_structs.ArrayStruct2d(A)
    B_ = array_structs.ArrayStruct2d(B)
    AB_ = array_structs.ArrayStruct2d(AB)
    
    c_linalg.mat_mult2(A_.pointer(), B_.pointer(), AB_.pointer())
    
    return AB






if __name__ == "__main__":
    
    from time import time
    
    N1,N2,N3 = numpy.random.randint(1, 10, 3)
    A = numpy.random.normal(0,1, (N1,N2))
    B = numpy.random.normal(0,1, (N2,N3))
    
    AB1 = numpy.dot(A, B)
    AB2 = py_mat_mult(A, B)
    
    norm = numpy.linalg.norm
    
    if norm(AB1-AB2)/norm(AB1) < 1E-10:
        print "1\tPASS"
    else:
        print "1\tFAIL"
    
    AB3 = c_mat_mult1(A, B)
    
    if norm(AB1-AB3)/norm(AB1) < 1E-10:
        print "2\tPASS"
    else:
        print "2\tFAIL"
    
    AB4 = c_mat_mult2(A, B)
    
    if norm(AB1-AB4)/norm(AB1) < 1E-10:
        print "3\tPASS"
    else:
        print "3\tFAIL"
    
    N = 100
    A = numpy.zeros((N,N))
    B = numpy.zeros((N,N))
    
    if 1:
        time1 = time()
        AB2 = py_mat_mult(A, B)
        time2 = time()
        print "python time: \t", time2-time1
    
    time1 = time()
    AB2 = numpy.dot(A, B)
    time2 = time()
    print "numpy time: \t", time2-time1
    
    time1 = time()
    AB2 = c_mat_mult1(A, B)
    time2 = time()
    print "C (1) time: \t", time2-time1
    
    time1 = time()
    AB2 = c_mat_mult2(A, B)
    time2 = time()
    print "C (2) time: \t", time2-time1
