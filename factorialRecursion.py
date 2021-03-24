# In this program that uses sympy, I am computing the recurrence relation
# for the factorial programs with and without Karatsuba algorithm ....

from sympy import *

# A short example ....

print('Some initial example y(n)-y(n-1)+(n-2) = 0 ')

y = Function('y')
n = var('n',integer=True)
f = y(n)-y(n-1)+(n-2)
print(rsolve(f,y(n)))

# Number of digits in n! for large n, Log(n!) ~ n Log(n)
# Proof below ....

print(
    "limit(log(gamma(n+1))/(n*log(n)),n,oo,"'+'")",
    limit(log(gamma(n+1))/(n*log(n)),n,oo,"+")
    )

# Karatsuba algorithm ...

print('Karatsuba algorithm f(n) - 3*f(n-1) - k * 2**n - m == 0 ')

f = Function('f')
k, m = symbols('k m')
cr = rsolve(f(n) - 3*f(n-1) - k * 2**n - m,f(n))
print(
    simplify(
    simplify(cr.subs(n,log(n))).subs(n,n*log(n))
    ))

# Some manual solving gives Tfact(n) = O( (n log n)**1.58 )

# School book algorithm algorithm ...

print('School book algorithm f(n) - 4*f(n-1) - k * 2**n - m == 0 ')

f = Function('f')
k, m = symbols('k m')
cr = rsolve(f(n) - 4*f(n-1) - k * 2**n - m,f(n))
print(
    simplify(
    simplify(cr.subs(n,log(n))).subs(n,n*log(n))
    ))

# Some manual solving gives Tfact(n) = O( (n log n)**2 )