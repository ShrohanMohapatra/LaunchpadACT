from matplotlib import pyplot as plt
from time import time
from unittest import TestCase
def fact(n):
    if n == 0: return 1
    else: return n*fact(n-1)
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
class testFrameWork(TestCase):
    def test1(self):
        A = {}
        for k in range(998):
            if k == 0: A[k] = 0
            else:
                A[k] = A[k-1]*k
        flag = True
        for k in range(998): flag = flag and fact(k) == A[k]
        self.assertTrue(flag)
A = [0 for i in range(998)]
for k in range(len(A)):
    start = time()
    fact(k)
    end = time()
    A[k] = end-start
A = movingaverage(A,60)
plt.plot(A)
plt.show()