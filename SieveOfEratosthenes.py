from time import time
from matplotlib import pyplot as plt
from unittest import TestCase, main
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
# Visual testing .....
print(exponent(2,4,5))
print(primality(7))
print(sieveOfEratosthenes(25))
# Time evaluation .....
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
# Some test cases .....
class ListOfTestCases(TestCase):
    def test1(self):
        p, c = sieveOfEratosthenes(10)
        p1 = [2,3,5,7]
        c1 = [4,6,8,9,10]
        flag = True
        for k in range(len(p)): flag = flag and p[k] in p1
        for k in range(len(c)): flag = flag and c[k] in c1
        self.assertTrue(flag)
    def test2(self):
        p, c = sieveOfEratosthenes(20)
        p1 = [2,3,5,7,11,13,17,19]
        c1 = [4,6,8,9,10,12,14,15,16,18,20]
        flag = True
        for k in range(len(p)): flag = flag and p[k] in p1
        for k in range(len(c)): flag = flag and c[k] in c1
        self.assertTrue(flag)
    def test3(self):
        p, c = sieveOfEratosthenes(50)
        p1 = [2,3,5,7,11,13,17,19,23,29,31,37,41,43,47]
        c1 = [
            4,6,8,9,10,12,14,15,16,18,20,21,22,24,25,26,27,28,
            30,32,33,34,35,36,38,39,40,42,44,45,46,48,49,50
        ]
        flag = True
        for k in range(len(p)): flag = flag and p[k] in p1
        for k in range(len(c)): flag = flag and c[k] in c1
        self.assertTrue(flag)
if __name__ == '__main__': main()