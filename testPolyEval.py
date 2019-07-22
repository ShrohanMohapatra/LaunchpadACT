from unittest import TestCase,main
from polyEval import polyEval1, polyEval2
from random import randint
class testPoly(TestCase):
    def testGen1(self):
        k, trueSig = 1, True
        while k <= 10:
            A = [1 for i in range(k)]
            x = randint(2,10)
            c = polyEval1(A,x)
            trueSig = trueSig and (c == int((x**k-1)/(x-1)))
            k = k + 1
        self.assertTrue(trueSig)
    def testSpecific1(self):
        A = [1,-2,1]
        x = 1
        self.assertEqual(polyEval1(A,x),0)
    def testSpecific2(self):
        A = [1,-2,1]
        x = (-1)
        self.assertEqual(polyEval1(A,x),4)
    def testSpecific3(self):
        A = [1,-6,9]
        x = 3
        self.assertEqual(polyEval1(A,x),0)
    def testSpecific4(self):
        A = [1,-6,9]
        x = 15
        self.assertEqual(polyEval1(A,x),144)
    def testGen2(self):
        k, trueSig = 1, True
        while k <= 10:
            A = [1 for i in range(k)]
            x = randint(2,10)
            c = polyEval2(A,x)
            trueSig = trueSig and (c == int((x**k-1)/(x-1)))
            k = k + 1
        self.assertTrue(trueSig)
    def testSpecific5(self):
        A = [1,-2,1]
        x = 1
        self.assertEqual(polyEval2(A,x),0)
    def testSpecific6(self):
        A = [1,-2,1]
        x = (-1)
        self.assertEqual(polyEval2(A,x),4)
    def testSpecific7(self):
        A = [1,-6,9]
        x = 3
        self.assertEqual(polyEval2(A,x),0)
    def testSpecific8(self):
        A = [1,-6,9]
        x = 15
        self.assertEqual(polyEval2(A,x),144)
if __name__ == '__main__':
    main()
