T0 = 0.22
a = 0.2
w1 = 8.0
p = 0.2
y0 = 0.5

T(x) = T0 *exp(-a*x)*cos(w1*x+p) + y0

fit T(x) filename using 1:2 via T0,a,w1,p,y0

plot filename using 1:2, T(x)