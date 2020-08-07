from search import linear_search, binary_search
from time import time, time_ns
import matplotlib.pyplot as plt
import math

import random
import numpy as np


class LinearSearch:
    def __init__(self):
        self.plottingDatas = []
        self.MAX = 300000
        self.MIN = 10000
        self.STEP = 5000
        

    def clearData(self):
        self.plottingDatas = []

    def plotData(self, title,color):
        if(len(self.plottingDatas) <= 0):
            raise Exception("No data found")
        plt.plot(*zip(*self.plottingDatas),c=color)
        plt.title(title)
        plt.show()

    def testBestCase(self):
        print("Best Case")
        self.clearData()
        for length in range(self.MIN, self.MAX, self.STEP):
            data = random.sample(range(self.MAX), length)
            start = time()
            linear_search(data, data[0])
            end = time()
            elapsed = end-start
            print(f"Elapsed Time for {length} datas: {round(elapsed,6)}")
            self.plottingDatas.append((length, round(elapsed,6)))
        # print("Average Best Case: ",np.mean( list(zip(*self.plottingDatas))[1]))
        self.plotData("Linear Search- Best Case",'green')

    def testWorstCase(self):
        print("Worst Case")
        self.clearData()
        for length in range(self.MIN, self.MAX, self.STEP):
            data = random.sample(range(self.MAX), length)
            start = time()
            linear_search(data, data[-1])
            end = time()
            elapsed = end-start
            print(f"Elapsed Time for {length} datas: {round(elapsed,6)}")
            self.plottingDatas.append((length, round(elapsed,6)))
       
        # print("Average Worst Case: ",np.mean( list(zip(*self.plottingDatas))[1]))
      
        self.plotData("Linear Search- Worst Case",'blue')

    def testAverageCase(self):
        print("Average Case")
        self.clearData()
        for length in range(self.MIN, self.MAX, self.STEP):
            data = random.sample(range(self.MAX), length)
            r = random.randint(0, length)
            start = time()
            linear_search(data, data[r])
            end = time()
            elapsed = end-start
            print(f"Elapsed Time for {length} datas: {round(elapsed,6)}")
            self.plottingDatas.append((length, round(elapsed,6)))

        # print("Average Average Case: ",np.mean( list(zip(*self.plottingDatas))[1]))

        self.plotData("Linear Search- Average Case",'red')


class BinarySearch:
    def __init__(self):
        self.plottingDatas = []
        self.MAX = 10000000
        self.MIN = 10000
        self.STEP = 10000

    def clearData(self):
        self.plottingDatas = []

    def plotData(self, title):
        if(len(self.plottingDatas) <= 0):
            raise Exception("No data found")
        plt.plot(*zip(*self.plottingDatas))
        plt.title(title)
        plt.show()

    def testBestCase(self):
        print("Best Case")
        self.clearData()
        for length in range(self.MIN, self.MAX, self.STEP):
            data = range(length)
            start = time_ns()
            binary_search(data, data[length//2-1])
            end = time_ns()
            elapsed = end-start
            print(f"Elapsed Time for {length} datas: {round(elapsed,6)}")
            self.plottingDatas.append((length, round(elapsed,6)))

        # print("Average Best Case: ",np.mean( list(zip(*self.plottingDatas))[1]))

        self.plotData("Binary Search- Best Case")

    def testWorstCase(self):
        print("Worst Case")
        self.clearData()
        k = int(math.log2(self.MIN))+1
        n = 2 ** k - 1

        while(n <= self.MAX):
            data = range(n)
            start = time_ns()
            binary_search(data, data[-1])
            end = time_ns()
            elapsed = end-start
            print(f"Elapsed Time for {n} datas: {round(elapsed,6)}")
            self.plottingDatas.append((n, round(elapsed,6)))

            k += 1
            n = 2 ** k - 1

        # print("Average Worst Case: ",np.mean( list(zip(*self.plottingDatas))[1]))
        self.plotData("Binary Search- Worst Case")

    def testAverageCase(self):
        print("Average Case")
        self.clearData()
        for length in range(self.MIN, self.MAX, self.STEP):
            data = range(length)
            r = random.randint(0, length)
            start = time_ns()
            rand = data[r]
            # binary_search(data, data[r])
            binary_search(data, rand)
            end = time_ns()
            elapsed = end-start
            print(f"Elapsed Time for {length} datas: {round(elapsed,6)}")
            self.plottingDatas.append((length, round(elapsed,6)))

        # print("Average Average Case: ",np.mean( list(zip(*self.plottingDatas))[1]))
        self.plotData("Binary Search- aAverage Case")


if __name__ == "__main__":
    # LinearSearch().testAverageCase()
    # LinearSearch().testBestCase()
    LinearSearch().testWorstCase()
    # BinarySearch().testWorstCase()
    # BinarySearch().testBestCase()
    # BinarySearch().testAverageCase()
    # BinarySearch().testWorstCase()
