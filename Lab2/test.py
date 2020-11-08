import unittest
import algorithm

class MergeSortTest(unittest.TestCase):
    def testInt(self):
        data = [9,8,5,1,3]
        output = [1,3,5,8,9]
        algorithm.mergesort(data,0,len(data))
        self.assertEqual(data,output)
        
    def testInt2(self): 
        data = [1,  8, 10, 19, 26, 11,3, 5, 18,  29]
        output = [1, 3, 5, 8, 10, 11, 18, 19, 26, 29]

        algorithm.mergesort(data,0,len(data))
        self.assertEqual(data,output)

class InsertionSortTest(unittest.TestCase):
    def testInt(self):

        
        data = [9,8,5,1,3]

        output = [1,3,5,8,9]
        algorithm.insertionSort(data)
        self.assertEqual(data,output)

    def testInt2(self): 
        data = [1,  8, 10, 19, 26, 11,3, 5, 18,  29]
        output = [1, 3, 5, 8, 10, 11, 18, 19, 26, 29]

        algorithm.insertionSort(data)
        self.assertEqual(data,output)

    def testChar(self):
        data = ['a','z','b','h','c']
        output = ['a','b','c','h','z']

        algorithm.insertionSort(data)
        self.assertEqual(data,output)

if __name__ == "__main__":
    unittest.main()
