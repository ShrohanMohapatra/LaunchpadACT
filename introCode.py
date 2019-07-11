from unittest import TestCase,main
from random import randint
def schoolBook(A,B):
    n = len(A)
    C = [[0 for j in range(n)] for i in range(n)]
    for i in range(n):
        for j in range(n):
            for k in range(n):
                C[i][j] = C[i][j] + A[i][k] * B[k][j]
    return C
def add(A,B):
    n = len(A)
    return [[A[i][j]+B[i][j] for j in range(n)] for i in range(n)]
def sub(A,B):
    n = len(A)
    return [[A[i][j]-B[i][j] for j in range(n)] for i in range(n)]
def strassenAlgo(C,A,B):
    n = len(A)
    if n == 1:
        C[0][0] = A[0][0]*B[0][0]
        return
    k = 1
    while not(k>=n): k = k * 2
    A1 = [
        [A[i][j] if j<n and i<n else 0 for j in range(k)]
        for i in range(k)
        ]
    B1 = [
        [B[i][j] if j<n and i<n else 0 for j in range(k)]
        for i in range(k)
        ]
    x11 = [[A1[i][j] for j in range(int(k/2))] for i in range(int(k/2))]
    x12 = [[A1[i][j] for j in range(int(k/2),k)] for i in range(int(k/2))]
    x21 = [[A1[i][j] for j in range(int(k/2))] for i in range(int(k/2),k)]
    x22 = [[A1[i][j] for j in range(int(k/2),k)] for i in range(int(k/2),k)]
    y11 = [[B1[i][j] for j in range(int(k/2))] for i in range(int(k/2))]
    y12 = [[B1[i][j] for j in range(int(k/2),k)] for i in range(int(k/2))]
    y21 = [[B1[i][j] for j in range(int(k/2))] for i in range(int(k/2),k)]
    y22 = [[B1[i][j] for j in range(int(k/2),k)] for i in range(int(k/2),k)]
    p01 = [[0 for j in range(int(k/2))] for i in range(int(k/2))]
    p02 = [[0 for j in range(int(k/2))] for i in range(int(k/2))]
    p03 = [[0 for j in range(int(k/2))] for i in range(int(k/2))]
    p04 = [[0 for j in range(int(k/2))] for i in range(int(k/2))]
    p05 = [[0 for j in range(int(k/2))] for i in range(int(k/2))]
    p06 = [[0 for j in range(int(k/2))] for i in range(int(k/2))]
    p07 = [[0 for j in range(int(k/2))] for i in range(int(k/2))]
    strassenAlgo(p01,add(x11,x22),add(y11,y22))
    strassenAlgo(p02,add(x21,x22),y11)
    strassenAlgo(p03,x11,sub(y12,y22))
    strassenAlgo(p04,x22,sub(y21,y11))
    strassenAlgo(p05,add(x11,x22),y22)
    strassenAlgo(p06,sub(x21,x11),add(y11,y12))
    strassenAlgo(p07,sub(x12,x22),add(y21,y22))
    c11 = sub(add(add(p01,p04),p07),p05)
    c12 = add(p03,p05)
    c21 = add(p02,p04)
    c22 = sub(add(add(p01,p03),p06),p02)
    C1 = [[0 for j in range(k)] for i in range(k)]
    for i in range(k):
        for j in range(k):
            if i < int(k/2) and j < int(k/2): C1[i][j] = c11[i][j]
            elif i < int(k/2) and j>=int(k/2): C1[i][j] = c12[i][j-int(k/2)]
            elif i >= int(k/2) and j<int(k/2): C1[i][j] = c21[i-int(k/2)][j]
            else: C1[i][j] = c22[i-int(k/2)][j-int(k/2)]
    for i in range(n):
        for j in range(n): C[i][j] = C1[i][j]
    return
class testFrameWork(TestCase):
    def test1(self):
        trueSigW = True
        for k in range(25):
            n = randint(3,5)
            A = [[1 for j in range(n)] for j in range(n)]
            B = [[1 for j in range(n)] for j in range(n)]
            C = schoolBook(A,B)
            trueSig = True
            for i in range(n):
                for j in range(n):
                    trueSig = trueSig and C[i][j] == n
            trueSigW = trueSigW and trueSig
        self.assertTrue(trueSigW)
    def test2(self):
        n = randint(2,10)
        A = [[1 for j in range(n)] for i in range(n)]
        B = [[2 for j in range(n)] for i in range(n)]
        C = add(A,B)
        trueSig = True
        for i in range(n):
            for j in range(n): trueSig = trueSig and C[i][j] == 3
        self.assertTrue(trueSig)
        C = sub(A,B)
        trueSig = True
        for i in range(n):
            for j in range(n): trueSig = trueSig and C[i][j] == -1
        self.assertTrue(trueSig)
    def test3(self):
        trueSigW = True
        for k in range(25):
            n = randint(3,15)
            A = [[1 for j in range(n)] for j in range(n)]
            B = [[1 for j in range(n)] for j in range(n)]
            C1 = [[0 for j in range(n)] for j in range(n)]
            strassenAlgo(C1,A,B)
            trueSig = True
            for i in range(n):
                for j in range(n):
                    trueSig = trueSig and C1[i][j] == n
            trueSigW = trueSigW and trueSig
        self.assertTrue(trueSigW)
if __name__ == '__main__':
    main()