import unittest

from search import linear_search, binary_search


class TestLinearSearchMethods(unittest.TestCase):
    def testLinear(self):
        data = [1, 2, 3, 4, 5]
        self.assertEqual(linear_search(data, 2), 1)
        self.assertEqual(linear_search(data, 10), -1)
    def testChar(self):
        data = ['a','e','i','o','u']
        self.assertEqual(linear_search(data, 'a'), 0)
        self.assertEqual(linear_search(data, 'z'), -1)
        self.assertEqual(linear_search(data, 'u'), 4)
  


class TestBinarySearch(unittest.TestCase):
    def testBinary(self):
        data = [1, 2, 3, 4, 5]
        self.assertEqual(binary_search(data, 2), 1)
        self.assertEqual(binary_search(data, 10), -1)

    def testChar(self):
        data = ['a','e','i','o','u']
        self.assertEqual(binary_search(data, 'a'), 0)
        self.assertEqual(binary_search(data, 'z'), -1)
        self.assertEqual(binary_search(data, 'u'), 4)

if __name__ == "__main__":
    unittest.main()
