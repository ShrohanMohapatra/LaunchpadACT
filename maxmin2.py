from random import randint
from unittest import TestCase, main
def maxmin(A,n):
    min1, max1 = A[0],A[0]
    for i in range(1,n):
        if min1>A[i]: min1 = A[i]
        if max1<A[i]: max1 = A[i]
    return [min1,max1]
class SortTest(TestCase):
    def test_Max(self):
        numberOfTests = randint(20,100)
        flag1, flag2 = True, True
        for k in range(numberOfTests):
            N = randint(50,100)
            A = [randint(1,100) for i in range(N)]
            [min3,max3] = maxmin(A,N)
            for i in range(N):
                flag1 = flag1 and A[i]>=min3
                flag2 = flag2 and A[i]<=max3
        print('Number of cases',numberOfTests)
        self.assertTrue(flag1 and flag2)
if __name__ == '__main__':
    main()