import unittest
import knapsack

class KnapsackTest(unittest.TestCase):
    def setUp(self):
        self.p = [5,6,7,2]
        self.w = [4,2,3,1]
        self.max = 8

        self.w1 = [1,2,3]
        self.p1 = [10,15,40]
        self.max1 = 6

    def testGreedy(self):
        output = ('0.5111',17.5)
        result = knapsack.greedy(self.w,self.p,self.max)
        self.assertTupleEqual(result,output)

        output = ('111',65)
        result = knapsack.greedy(self.w1,self.p1,self.max1)
        self.assertTupleEqual(result,output)

    def testBruteforceFrac(self):
        output = ('0.5111',17.5)
        result = knapsack.bruteforce_fractional(self.w,self.p,self.max)
        self.assertTupleEqual(result,output)

        output = ('111',65)
        result = knapsack.bruteforce_fractional(self.w1,self.p1,self.max1)
        self.assertTupleEqual(result,output)

    def testBruteforce(self):
        output = ('0111',15)
        result = knapsack.bruteforce(self.w,self.p,self.max)
        self.assertTupleEqual(result,output)

        output = ('111',65)
        result = knapsack.bruteforce(self.w1,self.p1,self.max1)
        self.assertTupleEqual(result,output)
        
    def testDP(self):
        output = ('0111',15)

        result = knapsack.dp(self.w,self.p,self.max)

        self.assertTupleEqual(result,output)

        output = ('111',65)
        result = knapsack.dp(self.w1,self.p1,self.max1)
        self.assertTupleEqual(result,output)


if __name__ == "__main__":
    unittest.main()