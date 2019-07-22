from pprint import pprint

trueCheck = 0 # A counter used for generating new variables
def newPoly(var,num_coeffs): # tested
    dictPoly = {
        'var': var,
        'poly': [[num_coeffs[i],[]] for i in range(len(num_coeffs))]
    }
    return dictPoly

def addCoeffPoly(a,var,n,c): # tested
    num_coeffs = [0,0,0,0]
    num_coeffs[0] = 1
    num_coeffs[n] = 1
    ret = newPoly(var,num_coeffs)
    ret['poly'][0][1].append(a)
    ret['poly'][n][1].append(c)
    return ret

def addPoly(a,b): # to be checked
    num_coeffs = [0,0,0,0]
    c = newPoly(a['var'],num_coeffs)
    for i in range(4):
        c['poly'][i][0] = a['poly'][i][0] + b['poly'][i][0]
        minimum = len(a['poly'][i][1]) if len(a['poly'][i][1]) < len(b['poly'][i][1]) else len(b['poly'][i][1])
        maximum = len(a['poly'][i][1]) if len(a['poly'][i][1]) > len(b['poly'][i][1]) else len(b['poly'][i][1])
        for j in range(minimum):
            c['poly'][i][1][j] = addPoly(a['poly'][i][1][j],b['poly'][i][1][j])
        if maximum == len(a['poly'][i][1]):
            for j in range(minimum,maximum):
                c['poly'][i][1][j] = a['poly'][i][1][j]
        else:
            for j in range(minimum,maximum):
                c['poly'][i][1][j] = b['poly'][i][1][j]
    return c

def multiplyPoly(a,b): # tested
    c = newPoly(a['var'],[0 for i in range(len(a['poly']))])
    c['poly'][0][0] = a['poly'][0][0] * b['poly'][0][0]
    c['poly'][1][0] = a['poly'][1][0] * b['poly'][0][0]
    c['poly'][2][0] = a['poly'][0][0] * b['poly'][2][0]
    c['poly'][3][0] = a['poly'][1][0] * b['poly'][2][0]
    for i in range(len(a['poly'][0][1])): c['poly'][0][1].append(a['poly'][0][1][i])
    for i in range(len(b['poly'][0][1])): c['poly'][0][1].append(b['poly'][0][1][i])
    for i in range(len(a['poly'][1][1])): c['poly'][1][1].append(a['poly'][1][1][i])
    for i in range(len(b['poly'][0][1])): c['poly'][1][1].append(b['poly'][0][1][i])
    for i in range(len(a['poly'][0][1])): c['poly'][2][1].append(a['poly'][0][1][i])
    for i in range(len(b['poly'][2][1])): c['poly'][2][1].append(b['poly'][2][1][i])
    for i in range(len(a['poly'][1][1])): c['poly'][3][1].append(a['poly'][1][1][i])
    for i in range(len(b['poly'][2][1])): c['poly'][3][1].append(b['poly'][2][1][i])
    return c

def convConstToPoly(A,var): # tested
    return [
        [newPoly(var,[A[i][j],0,0,0]) for j in range(len(A[i]))]
        for i in range(len(A))
    ]

def coeff(exp,poly): # tested
    try:
        num_coeff = poly['poly'][exp][0]
        term_coeff = poly['poly'][exp][1][0]
        for i in range(len(term_coeff['poly'])):
            term_coeff['poly'][i][0] = term_coeff['poly'][i][0] * num_coeff
        return term_coeff
    except:
        term_coeff = convConstToPoly([[0]],poly['var'])
        return term_coeff[0][0]

def matrixProd(A,B):
    global trueCheck
    n = len(A)
    if n == 1: return [[multiplyPoly(A[0][0],B[0][0])]]
    else:
        a = [[A[i][j] for j in range(int(n/2))] for i in range(int(n/2))]
        b = [[A[i][j] for j in range(int(n/2),n)] for i in range(int(n/2))]
        c = [[A[i][j] for j in range(int(n/2))] for i in range(int(n/2),n)]
        d = [[A[i][j] for j in range(int(n/2),n)] for i in range(int(n/2),n)]
        e = [[B[i][j] for j in range(int(n/2))] for i in range(int(n/2))]
        f = [[B[i][j] for j in range(int(n/2),n)] for i in range(int(n/2))]
        g = [[B[i][j] for j in range(int(n/2))] for i in range(int(n/2),n)]
        h = [[B[i][j] for j in range(int(n/2),n)] for i in range(int(n/2),n)]
        trueCheck = trueCheck + 1
        l = 'x'+str(trueCheck)
        k1 = [
            [ addCoeffPoly(a[i][j],l,2,c[i][j]) for j in range(int(n/2)) ]
            for i in range(int(n/2)) ]
        k2 = [
            [ addCoeffPoly(e[i][j],l,1,f[i][j]) for j in range(int(n/2)) ] 
            for i in range(int(n/2)) ]
        k3 = [
            [ addCoeffPoly(b[i][j],l,2,d[i][j]) for j in range(int(n/2)) ]
            for i in range(int(n/2)) ]
        k4 = [
            [ addCoeffPoly(g[i][j],l,1,h[i][j]) for j in range(int(n/2)) ] 
            for i in range(int(n/2)) ]
        print('k1')
        pprint(k1)
        print('k2')
        pprint(k2)
        print('k3')
        pprint(k3)
        print('k4')
        pprint(k4)
        ap = matrixProd(k1,k2)
        bp = matrixProd(k3,k4)
        a1 = [[0 for i in range(int(n/2))] for j in range(int(n/2))]
        a2 = [[0 for i in range(int(n/2))] for j in range(int(n/2))]
        a3 = [[0 for i in range(int(n/2))] for j in range(int(n/2))]
        a4 = [[0 for i in range(int(n/2))] for j in range(int(n/2))]
        print('A\'')
        pprint(ap)
        print('B\'')
        pprint(bp)
        for i in range(int(n/2)): # how to add the subsequent coefficients
            for j in range(int(n/2)):
                a1[i][j] = addPoly(coeff(0,ap[i][j]),coeff(0,bp[i][j]))
                a2[i][j] = addPoly(coeff(1,ap[i][j]),coeff(1,bp[i][j]))
                a3[i][j] = addPoly(coeff(2,ap[i][j]),coeff(2,bp[i][j]))
                a4[i][j] = addPoly(coeff(3,ap[i][j]),coeff(3,bp[i][j]))
        C = [[0 for i in range(n)] for j in range(n)]
        for i in range(n):
            for j in range(n):
                if i<int(n/2) and j<int(n/2): C[i][j] = a1[i][j]
                if i>=int(n/2) and j<int(n/2): C[i][j] = a2[i-int(n/2)][j]
                if i<int(n/2) and j>=int(n/2): C[i][j] = a3[i][j-int(n/2)]
                if i>=int(n/2) and j>=int(n/2): C[i][j] = a4[i-int(n/2)][j-int(n/2)]
        return C

def actualMatrixProduct(A,B):
    global trueCheck
    trueCheck = 0
    Ap = convConstToPoly(A,'x'+str(trueCheck))
    Bp = convConstToPoly(B,'x'+str(trueCheck))
    Cp = matrixProd(Ap,Bp)
    C = [[ Cp[i][j]['poly'][0][0] for j in range(len(A))] for i in range(len(A))]
    print('C')
    return C

def stubTest():
    pprint(newPoly('x',[9,90,10,3,4]))
    a = newPoly('x',[1,0,1,0])
    c = newPoly('x',[1,1,0,0])
    d = addCoeffPoly(a,'y',2,c)
    pprint(d)
    a1 = newPoly('x',[11,0,11,0])
    c1 = newPoly('x',[12,12,0,0])
    d1 = addCoeffPoly(a1,'y',1,c1)
    pprint(d1)
    pprint(multiplyPoly(d1,d))
    a = [[1,1],[1,1]]
    pprint(convConstToPoly(a,'x0'))
    print(coeff(1,d1))
    print(coeff(3,d1))
    e1 = {'var':'x','poly':[[12,[]],[12,[]],[0,[]],[0,[]]]}
    e2 = {'var':'x','poly':[[12,[]],[1,[]],[10,[]],[11,[]]]}
    print(addPoly(e1,e2))

def mainDriveTest():
    A = [
        [1,0],
        [0,1]
        ]
    B = [
        [1,0],
        [0,1]
        ]
    d = actualMatrixProduct(A,B)
    for i in range(len(d)):
        for j in range(len(d)):
            print(d[i][j], end = " ")
        print('')

stubTest()
#mainDriveTest()