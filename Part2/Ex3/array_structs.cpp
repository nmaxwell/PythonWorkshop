#ifndef ARRAY_STRUCTS_CPP
#define ARRAY_STRUCTS_CPP

//#define __SAFE__

template<class T >
class ArrayStruct
{
public:
  int size;
  int stride;
  void *data;
  
  ArrayStruct(T *data, int stride, int size)
    :data(data), stride(stride), size(size) {}
  
  inline T& operator()(const int &index) {
#ifdef __SAFE__
    assert(data != NULL);
    assert(0 <= index);
    assert(index < size);
#endif
    return *(T *)((char *)data + stride*index);
  }
};

template<class T >
class ArrayStruct2d
{
public:
  int size1, size2;
  int stride1, stride2;
  void *data;
  
  ArrayStruct2d(T *data, int stride1, int stride2, int size1, int size2)
    :data(data), stride1(stride1), stride2(stride2), size1(size1), size2(size2) {}
  
  inline T& operator()(const int index1, const int index2) {
#ifdef __SAFE__
    assert(data != NULL);
    assert(0 <= index1);
    assert(index1 < size1);
    assert(0 <= index2);
    assert(index2 < size2);
#endif
    return *(T *)((char *)data + stride1*index1 + stride2*index2);
  }
  
};

template<class T >
class ArrayStruct3d
{
public:
  int size1, size2, size3;
  int stride1, stride2, stride3;
  void *data;
  
  ArrayStruct3d(T *data, int stride1, int stride2, int stride3, int size1, int size2, int size3)
    :data(data), stride1(stride1), stride2(stride2), stride3(stride3), size1(size1), size2(size2), size3(size3) {}
  
  inline T& operator()(const int &index1, const int &index2, const int &index3) {
#ifdef __SAFE__
    assert(data != NULL);
    assert(0 <= index1);
    assert(index1 < size1);
    assert(0 <= index2);
    assert(index2 < size2);
    assert(0 <= index3);
    assert(index3 < size3);
#endif
    return *(T *)((char *)data + stride1*index1 + stride2*index2 + stride3*index3);
  }
  
};




#endif



