from matplotlib import pyplot
factorial1 = [0 for k in range(1000)]
def factorial(n): # I am using dynamic programming here ....
    if n == 0:
        factorial1[0] = 1
        return 1
    elif factorial1[n] == 0:
        p = n*factorial(n-1)
        factorial1[n] = p
        return p
    else: return factorial1[n]
def FindUpperLimit(n):
    u = n
    q = u**u
    while True:
        p = factorial(u)
        p = p/factorial(n)
        p = p/factorial(u-n)
        if p>=q: break
        else: u = u + 1
    return u
a = [n for n in range(5)]
b = [FindUpperLimit(n) for n in range(5)]
pyplot.plot(a)
pyplot.plot(b)
pyplot.show()
