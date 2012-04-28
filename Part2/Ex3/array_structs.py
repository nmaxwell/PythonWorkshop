import numpy
import ctypes
from ctypes import c_int, c_double, c_void_p

class ArrayStruct(ctypes.Structure):            
    _fields_ = [ ("size", ctypes.c_int),
                 ("stride", ctypes.c_int),
                 ("data", ctypes.c_void_p) ]

    def __init__(self, var=None):
        if var is not None:
            #if type(var) != numpy.ndarray:
            #    self.array = numpy.array(var)
            #    var = self.array
            
            self.size = len(var)
            self.stride = var.strides[0]
            self.data = var.ctypes.data_as(ctypes.c_void_p)
    
    def pointer(self,):
        return ctypes.byref(self)

class ArrayStruct2d(ctypes.Structure):
    #{int size; int stride; T *data}
    _fields_ = [ ("size1", ctypes.c_int),
                 ("size2", ctypes.c_int),
                 ("stride1", ctypes.c_int),
                 ("stride2", ctypes.c_int),
                 ("data", ctypes.c_void_p) ]
    
    def __init__(self, var=None):
        if var is not None:
            self.size1, self.size2 = var.shape
            self.stride1, self.stride2 = var.strides
            self.data = var.ctypes.data_as(ctypes.c_void_p)

    def pointer(self,):
        return ctypes.byref(self)

class ArrayStruct3d(ctypes.Structure):
    #{int size; int stride; T *data}
    _fields_ = [ ("size1", ctypes.c_int),
                 ("size2", ctypes.c_int),
                 ("size3", ctypes.c_int),
                 ("stride1", ctypes.c_int),
                 ("stride2", ctypes.c_int),
                 ("stride3", ctypes.c_int),
                 ("data", ctypes.c_void_p) ]
    
    def __init__(self, var=None):
        if var is not None:
            self.size1, self.size2, self.size3 = var.shape
            self.stride1, self.stride2, self.stride3 = var.strides
            self.data = var.ctypes.data_as(ctypes.c_void_p)
    
    def pointer(self,):
        return ctypes.byref(self)


class array_struct:
    def __init__(self, array):
        if array is None:
            self.obj = None
            self.pointer = ctypes.c_void_p(0)
        else:
            
            if type(array) == numpy.ndarray:
                #assert(array.dtype == numpy.float64)
                self.array = array
            elif hasattr(array, "__len__"):
                self.array = numpy.array(array, dtype=numpy.float64)
            else:
                raise TypeError
            
            dims = len(numpy.shape(self.array))
            
            types = [ArrayStruct, ArrayStruct2d, ArrayStruct3d, ArrayStruct4d]
            self.obj = types[dims-1](self.array)
            self.pointer = self.obj.pointer()








