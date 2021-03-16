from random import randint
from math import log10
from time import time
from matplotlib import pyplot as plt
def bubbleSort(arr):
    n = len(arr)
    if n<=1: return
    for i in range(n-1):
        min1 = arr[i]
        pos = i
        for j in range(i+1,n):
            if min1>arr[j]:
                min1 = arr[j]
                pos = j
        if pos!=i:
            arr[i] = arr[i] + arr[pos]
            arr[pos] = arr[i] - arr[pos]
            arr[i] = arr[i] - arr[pos]
def mergeSort(arr):
    n = len(arr)
    if n == 1: return
    elif n == 2:
        if arr[0]>arr[1]:
            arr[0] = arr[0] + arr[1]
            arr[1] = arr[0] - arr[1]
            arr[0] = arr[0] - arr[1]
    else:
        n2 = int(n/2)
        firstHalf = [arr[k] for k in range(n2)]
        secondHalf = [arr[k] for k in range(n2,n)]
        mergeSort(firstHalf)
        mergeSort(secondHalf)
        i,j,k = 0,n2,0
        while i<n2 and j<n:
            if firstHalf[i] < secondHalf[j-n2]:
                arr[k] = firstHalf[i]
                k = k + 1
                i = i + 1
            else:
                arr[k] = secondHalf[j-n2]
                k = k + 1
                j = j + 1
        while i<n2:
            arr[k] = firstHalf[i]
            k = k + 1
            i = i + 1
        while j<n:
            arr[k] = secondHalf[j-n2]
            k = k + 1
            j = j + 1
def RadixSort(arr):
    # Array of positive numbers ....
    n = len(arr)
    if n == 0: return arr
    else:
        min1, max1 = arr[0], arr[0]
        for k in range(1,n):
            if min1 > arr[k]: min1 = arr[k]
            if max1 < arr[k]: max1 = arr[k]
        k1 = int(log10(max1))
        buckets = {}
        for k in range(10): buckets[k] = [0 for k in range(10**k1)]
        for k in range(n):
            y = arr[k]
            x = buckets[int(y/10**(k1))][y%10**(k1)]
            x = x + 1
            buckets[int(y/10**(k1))][y%10**(k1)] = x
        newArr = []
        for i in range(10):
            for j in range(10**k1):
                while buckets[i][j]>0:
                    newArr.append((10**k1)*i+j)
                    x = buckets[i][j]
                    x = x - 1
                    buckets[i][j] = x
        return newArr
num = 1500
X = [k for k in range(1,num)]
Y1 = [0 for k in range(1,num)]
Y2 = [0 for k in range(1,num)]
Y3 = [0 for k in range(1,num)]
for k in range(1,num):
    print('Array of length ',k,' being processed')
    A1 = [randint(1,99) for i in range(k)]
    A2 = [A1[i] for i in range(k)]
    A3 = [A1[i] for i in range(k)]
    start = time()
    bubbleSort(A1)
    end = time()
    Y1[k-1] = end-start
    start = time()
    mergeSort(A2)
    end = time()
    Y2[k-1] = end-start
    start = time()
    RadixSort(A3)
    end = time()
    Y3[k-1] = end-start
plt.plot(X,Y1)
plt.plot(X,Y2)
plt.plot(X,Y3)
plt.legend(["Bubble Sort","Merge Sort","Radix Sort"])
plt.show()
