from math import log2
from sys import setrecursionlimit
from time import time
from matplotlib import pyplot as plt

def movingaverage(arr,win):
    b = []
    for k in range(int(win/2)): b.append(arr[k])
    for k in range(int(win/2),len(arr)-int(win/2)):
        s = 0
        for l in range(k-int(win/2),k+int(win/2)):
            s = s + arr[l]
        b.append(s/win)
    for k in range(len(arr)-int(win/2),len(arr)): b.append(arr[k])
    return b

def karatsuba_Algo(a,b):
    n1 = int(log2(a)+1) if a!=0 else 1
    n2 = int(log2(b)+1) if b!=0 else 1
    n = n1 if n1>n2 else n2
    if n == 1: return a*b
    m = int(n/2)
    x0, x1 = int(a/(2**m)), a%(2**m)
    y0, y1 = int(b/(2**m)), b%(2**m)
    z0 = karatsuba_Algo(x0,y0)
    z1temp = karatsuba_Algo(x0+x1,y0+y1)
    z2 = karatsuba_Algo(x1,y1)
    z1 = z1temp - z0 - z2
    return z0*(2**(2*m))+z1*(2**m)+z2

def fact(n):
    if n == 0: return 1
    else: return n*fact(n-1)

def modifiedFactorial(n):
    if n == 0: return 1
    else: return karatsuba_Algo(n,modifiedFactorial(n-1))

#setrecursionlimit(998)
N = 60
A = [0 for i in range(60)]
B = [0 for i in range(60)]
for k in range(len(A)):
    start = time()
    fact(k)
    end = time()
    A[k] = end-start
    print("Number",k,"actual fact done")
    start = time()
    modifiedFactorial(k)
    end = time()
    B[k] = end-start
    print("Number",k,"modified fact done")
A = movingaverage(A,int(N/3))
B = movingaverage(B,int(N/3))
plt.plot(A,'b')
plt.plot(B,'r')
plt.show()