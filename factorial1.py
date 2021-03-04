from matplotlib import pyplot as plt
from time import time
from unittest import TestCase
from random import randint

def movingaverage(arr,win):
    b = []
    for k in range(int(win/2)): b.append(arr[k])
    for k in range(int(win/2),len(arr)-int(win/2)):
        s = 0
        for l in range(k-int(win/2),k+int(win/2)): s = s + arr[l]
        b.append(s/win)
    for k in range(len(arr)-int(win/2),len(arr)): b.append(arr[k])
    return b

def decToBinary(num):
    s,A = num,[]
    while s>0:
        A.append(s%2)
        s = int(s/2)
    n = len(A)
    for k in range(int(n/2)):
        A[k] = A[k] + A[n-1-k]
        A[n-1-k] = A[k] - A[n-1-k]
        A[k] = A[k] - A[n-1-k]
    return A

# print(decToBinary(15))
# print(decToBinary(11))
# print(decToBinary(22))
# print(decToBinary(45))

def binaryToDec(arr):
    s,n = 0,len(arr)
    for k in range(n): s = 2*s + arr[k]
    return s

a = randint(0,2**20-1)
start = time()
assert binaryToDec(decToBinary(a)) == a
end = time()
print(round((end-start)*10**6,3),"usec")

def FullBinaryAdd(arrA,arrB,n):
    xor = lambda a,b: int((not(a) and b) or (not(b) and a))
    carry = lambda a,b,c: int((a and b) or (b and c) or (c and a))
    c = 0
    S = [0 for k in range(n)]
    for k in range(n-1,-1,-1):
        S[k] = xor(xor(arrA[k],arrB[k]),c)
        c = carry(arrA[k],arrB[k],c)
    S.insert(0,c)
    return S

def binaryAdd(a,b):
    A = decToBinary(a)
    B = decToBinary(b)
    if len(A)>len(B):
        while len(A)!=len(B): B.insert(0,0)
    elif len(B)>len(A):
        while len(A)!=len(B): A.insert(0,0)
    return binaryToDec(FullBinaryAdd(A,B,len(A)))

a = randint(0,2**20-1)
b = randint(0,2**20-1)
start = time()
assert binaryAdd(a,b) == a + b
end = time()
print(round((end-start)*10**6,3),"usec")

# A = [0 for i in range(998)]
# for k in range(len(A)):
#     start = time()
#     fact(k)
#     end = time()
#     A[k] = end-start
# A = movingaverage(A,60)
# plt.plot(A)
# plt.show()