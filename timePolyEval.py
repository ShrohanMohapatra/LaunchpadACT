from time import time
from random import randint
from polyEval import polyEval1, polyEval2
print('--------------------------------------------------')
print('Welcome to the polynomial evaluation simulation!')
print('Here we will compare the time complexities of')
print('Horner\'s scheme and normal polynomial evaluation.')
print('--------------------------------------------------')
print('Size     Normal eval. time       Horner\'s eval. time')
k = 1
while k<=30:
    A = [randint(0,5) for j in range(k)]
    x = randint(0,10)
    start1 = time()
    polyEval1(A,x)
    end1 = time()
    start2 = time()
    polyEval2(A,x)
    end2 = time()
    print(k if k>9 else '0'+str(k),'       ',
    round((end1-start1)*10**6),'usec','               ',
    round((end2-start2)*10**6),'usec'
    )
    k = k + 1