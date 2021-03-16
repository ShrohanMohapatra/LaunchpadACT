from random import randint
from math import log10
from unittest import TestCase, main
# module to test radix sort on random sizes of arrays ....
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
class testSuite(TestCase):
    k1 = 6
    def test1(self):
        n = randint(1,50)
        arr = [randint(1,10**self.k1) for k in range(n)]
        arr = RadixSort(arr)
        flag = True
        for k in range(1,n): flag = flag and arr[k-1]<=arr[k]
        self.assertTrue(flag)
    def test2(self):
        n = randint(1,50)
        arr = [randint(1,10**self.k1) for k in range(n)]
        arr = RadixSort(arr)
        flag = True
        for k in range(1,n): flag = flag and arr[k-1]<=arr[k]
        self.assertTrue(flag)
    def test3(self):
        n = randint(1,50)
        arr = [randint(1,10**self.k1) for k in range(n)]
        arr = RadixSort(arr)
        flag = True
        for k in range(1,n): flag = flag and arr[k-1]<=arr[k]
        self.assertTrue(flag)
    def test4(self):
        n = randint(1,50)
        arr = [randint(1,10**self.k1) for k in range(n)]
        arr = RadixSort(arr)
        flag = True
        for k in range(1,n): flag = flag and arr[k-1]<=arr[k]
        self.assertTrue(flag)
    def test5(self):
        n = randint(1,50)
        arr = [randint(1,10**self.k1) for k in range(n)]
        arr = RadixSort(arr)
        flag = True
        for k in range(1,n): flag = flag and arr[k-1]<=arr[k]
        self.assertTrue(flag)
if __name__ == '__main__': main()