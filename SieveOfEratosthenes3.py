from time import time
from matplotlib import pyplot as plt
from SieveOfEratosthenes import sieveOfEratosthenes
from SieveOfEratosthenes2 import sieveOfEratosthenes2
totalNum = 120
X = [5*k for k in range(2,totalNum)]
Y1 = [0 for k in range(2,totalNum)]
Y2 = [0 for k in range(2,totalNum)]
for h in X:
    start = time()
    sieveOfEratosthenes(h)
    end = time()
    Y1[int(h/5)-2] = end-start
    start = time()
    sieveOfEratosthenes2(h)
    end = time()
    Y2[int(h/5)-2] = end-start
fig = plt.figure()
line1 = plt.plot(X,Y1,'r')
line2 = plt.plot(X,Y2,'g')
plt.legend((line1,line2),('FermatTest','SqrtPrimality'))
plt.show()