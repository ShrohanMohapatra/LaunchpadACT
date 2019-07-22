def sumLog(A,B):
    p = len(A)
    q = len(B)
    if p < q:
        while len(A)!=len(B): A.append(0)
    else:
        while len(A)!=len(B): B.append(0)
    if len(A) == 1 and len(B) == 1:
        return A[0]*B[0]
    else:
        n = len(A)
        C0 = [A[i] for i in range(int(n/2))]
        C1 = [A[i] for i in range(int(n/2),n)]
        D0 = [B[i] for i in range(int(n/2))]
        D1 = [B[i] for i in range(int(n/2),n)]
        return sumLog(C0,D0)+sumLog(C1,D1)
def matrixMultiplyRaz(A,B):
    n = len(A)
    C = [[0 for j in range(n)] for i in range(n)]
    D = [[B[j][i] for j in range(n)] for i in range(n)]
    for i in range(n):
        for j in range(n):
            C[i][j] = sumLog(A[i],D[j])
    return C