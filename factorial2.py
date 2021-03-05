# Debugged using factorial1.py
from random import randint
from time import time
from sys import setrecursionlimit
def digits(num):
    s,d = num,[]
    while s>0:
        d.append(s%10)
        s = int(s/10)
    d.reverse()
    return d

def numberFromDigits(arr):
    s = 0
    for k in range(len(arr)): s = 10*s + arr[k]
    return s

def FullCarryAdd(arrA,arrB):
    if len(arrA)>=len(arrB):
        while len(arrA)!=len(arrB): arrB.insert(0,0)
    else:
        while len(arrA)!=len(arrB): arrA.insert(0,0)
    c,n = 0,len(arrA)
    S = [0 for k in range(n)]
    for k in range(n-1,-1,-1):
        S[k] = (arrA[k]+arrB[k]+c)%10
        c = int((arrA[k]+arrB[k]+c)/10)
    S.insert(0,c)
    return S

def FullCarrySub(arrA,arrB):
    if len(arrA)>=len(arrB):
        while len(arrA)!=len(arrB): arrB.insert(0,0)
    else:
        while len(arrA)!=len(arrB): arrA.insert(0,0)
    n = len(arrA)
    S = [0 for k in range(n)]
    for k in range(n-1,-1,-1):
        if arrA[k]>=arrB[k]: S[k] = (arrA[k]-arrB[k])
        else:
            S[k] = (10+arrA[k]-arrB[k])
            arrA[k-1] = arrA[k-1]-1
    return S

def karatsuba_algorithm(arrA,arrB):
    div = lambda n,m: int(n/m)
    if len(arrA)>=len(arrB):
        while len(arrA)!=len(arrB): arrB.insert(0,0)
    else:
        while len(arrA)!=len(arrB): arrA.insert(0,0)
    N = len(arrA)
    if N == 1:
        print(arrA[0],"*",arrB[0],'=',arrA[0]*arrB[0])
        return [arrA[0]*arrB[0]]
    else:
        print("arrA = ",arrA,"arrB = ",arrB)
        flagA,flagB = True,True
        for k in range(N):
            flagA = flagA and arrA[k] == 0
            flagB = flagB and arrB[k] == 0
        if flagA or flagB: return [0 for i in range(N)]
        X0 = [arrA[k] for k in range(div(N,2))]
        X1 = [arrA[k] for k in range(div(N,2),N)]
        Y0 = [arrB[k] for k in range(div(N,2))]
        Y1 = [arrB[k] for k in range(div(N,2),N)]
        print("X0 = ",X0,"X1 = ",X1,"Y0 = ",Y0,"Y1 = ",Y1)
        print("X0 + Y0 = ",FullCarryAdd(X0,Y0),"X1 + Y1 = ",FullCarryAdd(X1,Y1))
        Z0 = karatsuba_algorithm(X0,Y0)
        Z1 = karatsuba_algorithm(X1,Y1)
        Z2 = karatsuba_algorithm(FullCarryAdd(X0,Y0),FullCarryAdd(X1,Y1))
        Z2 = FullCarrySub(Z2,Z0)
        Z2 = FullCarrySub(Z2,Z1)
        Z = []
        print("Z0 = ",Z0,numberFromDigits(Z0))
        print("Z2 = ",Z2,numberFromDigits(Z2))
        print("Z1 = ",Z1,numberFromDigits(Z1))
        for k in range(div(N,2)): Z.append(Z0[k])
        for k in range(div(N,2)): Z.append(Z2[k])
        for k in range(div(N,2)): Z.append(Z1[k])
        print("Z = ",numberFromDigits(Z))
        return Z

setrecursionlimit(10)

#assert numberFromDigits(karatsuba_algorithm(digits(4),digits(5))) == 20

print( numberFromDigits(karatsuba_algorithm(digits(11),digits(5))) )

# a = randint(5,100)
# b = randint(5,100)
# start = time()
# assert numberFromDigits(karatsuba_algorithm(digits(a),digits(b))) == a*b
# end = time()
# print("a = ",a,"b = ",b,"Time taken ",round((end-start)*10**6,3),"usec")