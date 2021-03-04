from sympy import *
y = Function('y')
n = symbols('n',integer=True)
c, d= symbols('c d')
f = y(n)-3*y(n-1)-c*2**n-d
print(simplify(rsolve(f,y(n),{y(0):0})))