import unittest
import algorithm

class MergeSortTest(unittest.TestCase):
    def testInt(self):
        data = [9,8,5,1,3]
        output = [1,3,5,8,9]
        algorithm.mergesort(data,0,len(data))
        self.assertEqual(data,output)
   
class InstertionSortTest(unittest.TestCase):
    def testInt(self):

        
        data = [9,8,5,1,3]

        output = [1,3,5,8,9]
        algorithm.insertionSort(data)
        self.assertEqual(data,output)
if __name__ == "__main__":
    unittest.main()
