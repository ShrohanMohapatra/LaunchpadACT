from random import choice
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
listOfChoices = ['a','b','c','d','e','f']
numberOfTrials = 10**4
listOfTimes = [0 for k in range(numberOfTrials)]
for k in range(numberOfTrials):
    start = time()
    record = dictA[choice(listOfChoices)]
    end = time()
    listOfTimes[k] = end-start
pyplot.plot(listOfTimes)
pyplot.show()