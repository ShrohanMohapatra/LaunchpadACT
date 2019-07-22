def polyEval1(A,x): # Horner's scheme
    if len(A) == 1: return A[0]
    else:
        n = A[len(A)-1]
        del A[-1]
        return polyEval1(A,x)*x+n
def polyEval2(A,x): # Normal iterative calculation
    p,s = 1,0
    for i in range(len(A)-1,-1,-1):
        s = s + p * A[i]
        p = p * x
    return s