
#include "LinAlg.h"




void mat_mult1(int N1, int N2, int N3, double *A, double *B, double *AB) {
  
  for (int i=0; i<N1; i++)
    for (int j=0; j<N3; j++) {
      double sum = 0.0;
      for (int k=0; k<N2; k++)
	sum += A[i*N2+k]*B[k*N3+j];
      AB[i*N3+j] = sum;
    }
  
}

void mat_mult2(ArrayStruct2d<double> *A, ArrayStruct2d<double> *B, ArrayStruct2d<double> *AB) {
  
  for (int i=0; i<A->size1; i++)
    for (int j=0; j<B->size2; j++) {
      double sum = 0.0;
      for (int k=0; k<A->size2; k++)
	sum += (*A)(i,k)*(*B)(k,j);
      (*AB)(i,j) = sum;
    }
  
}


