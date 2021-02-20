from random import randint
from unittest import TestCase, main
def maxmin(A,n):
    if n==1: return [A[0],A[0]]
    elif n==2:
        if A[0]>=A[1]: max1,min1 = A[0],A[1]
        else: max1,min1 = A[1],A[0]
        return [min1,max1]
    else:
        B = [A[i] for i in range(int(n/2),n)]
        C = [A[i] for i in range(int(n/2))]
        [min1,max1] = maxmin(C,len(C))
        [min2,max2] = maxmin(B,len(B))
        return [min1 if min1<=min2 else min2, max1 if max1>=max2 else max2]
class SortTest(TestCase):
    def test_Max(self):
        numberOfTests = randint(20,100)
        flag1, flag2 = True, True
        for k in range(numberOfTests):
            N = randint(5,10)
            A = [randint(1,100) for i in range(N)]
            [min3,max3] = maxmin(A,N)
            for i in range(N):
                flag1 = flag1 and A[i]>=min3
                flag2 = flag2 and A[i]<=max3
        print('Number of cases',numberOfTests)
        self.assertTrue(flag1 and flag2)
if __name__ == '__main__':
    main()