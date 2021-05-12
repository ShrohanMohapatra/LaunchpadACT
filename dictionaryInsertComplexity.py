from random import randint
from time import time
from matplotlib import pyplot
dictA = {
    'a':'apple',
    'b':'ball',
    'c':'canonical',
    'd':'dynamic',
    'e':'ergodicity',
    'f':'fanaticism'
}
numberOfTrials = 10**4
numberOfLetters = 6
listOfTimes = [0 for k in range(numberOfTrials)]
for k in range(numberOfTrials):
    s = ''
    for k1 in range(numberOfLetters):
        s = s + str(chr(randint(65,90)))
    start = time()
    dictA[chr(randint(65,90))] = s
    end = time()
    listOfTimes[k] = end-start
pyplot.plot(listOfTimes)
pyplot.show()