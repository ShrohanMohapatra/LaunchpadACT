from time import time
from matplotlib import pyplot as plt
# Sieve of Eratosthenes using Fermat primality test
def exponent(a,x,n):
    # x is an integer ...
    k = 1
    r = a%n
    while k<x:
        r = (a*r)%n
        k = k + 1
    return r
def primality(p): return exponent(2,p-1,p)==1
def sieveOfEratosthenes(maxNum):
    # because the Fermat's little theorem fails for p = 2 ....
    prime = [2]
    compo = [2*k for k in range(2,int(maxNum/2))]
    for k in range(2,maxNum+1):
        if k in compo: pass
        else:
            if primality(k):
                prime.append(k)
                for m in range(2*k,maxNum+1,k):
                    if m not in compo: compo.append(m)
    return [prime, compo]
print(exponent(2,4,5))
print(exponent(2,1,2))
print(primality(2))
print(sieveOfEratosthenes(100))
totalNum = 120
X = [5*k for k in range(2,totalNum)]
Y = [0 for k in range(2,totalNum)]
for h in X:
    start = time()
    sieveOfEratosthenes(h)
    end = time()
    Y[int(h/5)-2] = end-start
plt.plot(X,Y)
plt.show()