from random import randint
from math import log10
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
length = 10
arr = [randint(1,10000) for k in range(length)]
print(arr)
arr = RadixSort(arr)
print(arr)