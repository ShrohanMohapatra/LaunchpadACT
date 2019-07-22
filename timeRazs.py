from matrixMultiplyRazs import matrixMultiplyRaz, sumLog
from time import time
from random import randint
print('Time complexity tests for logarithmic sum calculations')
k = 1
while k <= 30:
    A = [randint(0,10) for i in range(k)]
    B = [randint(0,10) for i in range(k)]
    start = time()
    sumLog(A,B)
    end = time()
    print('Size',k,'Time',round((end-start)*10**6),'usec')
    k = k + 1
print('Time complexity tests for n^2 log n matrix multiplication')
k = 1
while k <= 30:
    A = [[randint(0,10) for j in range(k)] for i in range(k)]
    B = [[randint(0,10) for i in range(k)] for i in range(k)]
    start = time()
    matrixMultiplyRaz(A,B)
    end = time()
    print('Size',k,'Time',round((end-start)*10**6),'usec')
    k = k + 1