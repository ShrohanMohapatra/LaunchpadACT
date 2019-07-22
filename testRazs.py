from matrixMultiplyRazs import matrixMultiplyRaz, sumLog
from unittest import TestCase, main
from random import randint
class testProduct(TestCase):
    def testSumLog(self):
        k = 1
        trueSig = True
        while k <= 30:
            A = [randint(0,100) for j in range(k)]
            B = [randint(0,100) for j in range(k)]
            C = [A[j]*B[j] for j in range(k)]
            C1 = sumLog(A,B)
            C2 = sum(C)
            trueSig = trueSig and (C1==C2)
            k = k + 1
        self.assertTrue(trueSig)
    def testProduct(self):
        k = 1
        trueSig = True
        while k <= 30:
            A = [[randint(0,100) for j in range(k)] for i in range(k)]
            B = [[randint(0,100) for j in range(k)] for i in range(k)]
            C1 = [[0 for j in range(k)] for i in range(k)]
            for m in range(k):
                for n in range(k):
                    for p in range(k):
                        C1[m][n] = C1[m][n] + A[m][p] * B[p][n]
            C2 = matrixMultiplyRaz(A,B)
            trueSig = trueSig and (C1==C2)
            k = k + 1
        self.assertTrue(trueSig)
if __name__ == '__main__':
    main()