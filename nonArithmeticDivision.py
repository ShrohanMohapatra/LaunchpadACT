# Problem statement: You are not allowed to use division operator (/) or the
# remainder operator (%), but you have to print the decimal representation 
# of x/7 upto n places of decimal, x and n being the user input. 
# Find the complexity growth of the algorithm without growing x and n.

from matplotlib import pyplot as plt
import numpy as np
from time import time
from random import randint

def DivisionBy7(x,n):
    # Division by 7 from the user inputs x and n ....
    # Perform long division to find the quotient s=int(x/7) and r=x%7 ....
    x = int(x)
    n = int(n)
    s,r = 0,x
    while r>=7:
        r = x - 7
        s = s + 1
        x = r
    # Now I am storing the repetitive digits in the array
    # ListOfRemainders for decimal representation of x/7
    # where 0<=x<=6 ....
    ListOfRemainders = [
        [0,0,0,0,0,0],
        [1,4,2,8,5,7],
        [2,8,5,7,1,4],
        [4,2,8,5,7,1],
        [5,7,1,4,2,8],
        [7,1,4,2,8,5],
        [8,5,7,1,4,2]
    ]
    # Now I am simply going to import the ListOfRemainders from here ....
    decimalPoints = []
    for k in range(n): decimalPoints.append(ListOfRemainders[x][k%6])
    return s,decimalPoints

# Some instantaneous test cases ....

assert DivisionBy7(200,4) == (28,[5,7,1,4])
assert DivisionBy7(50,9) == (7,[1,4,2,8,5,7,1,4,2])

# Complexity plotting ....

def timeComplexity(x,n):
    start = time()
    DivisionBy7(x,n)
    end = time()
    return end-start

fig = plt.figure()
M = 500
x = np.linspace(1,M,M)
n = np.linspace(1,M,M)
T = [[0 for i in range(len(n))] for j in range(len(x))]
for i in range(len(x)):
    for j in range(len(n)):
        start = time()
        timeComplexity(x[i],n[j])
        end = time()
        T[i][j] = end-start
plt.plot(n,T[randint(0,len(x)-1)])
plt.show()
plt.plot(x,[T[i][randint(0,len(n)-1)] for i in range(len(x))])
plt.show()