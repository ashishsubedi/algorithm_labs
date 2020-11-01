from algorithm import mergesort,insertionSort
import matplotlib.pyplot as plt
import numpy as np
import random
import time

class SortAnalysis:
    def __init__(self):
        self.plotData = {
                    'i':[],
                    'm':[]
                } 
    
    def analyzeInsertionSort(self,low=10,high=1000,step=10):
        print("Started analysis for insertion sort")
        for i in range(low,high,step):
            data = random.sample(range(0,100000),i)
            start = time.time()
            insertionSort(data)
            end = time.time()
            taken = end-start 
            self.plotData['i'].append((i,taken))
#            print(f"Time for {i} numbers : {taken}") 



      


    def analyzeMergeSort(self,low=10,high=1000,step=10):

        print("Started analysis for merge sort")
        for i in range(low,high,step):
            data = random.sample(range(0,100000),i)
            l = len(data)
            start = time.time()
            mergesort(data,0,l)
            end = time.time()
            taken = end-start 
            self.plotData['m'].append((i,taken))
#            print(f"Time for {i} numbers : {taken}") 


    def showPlot(self):
        plt.xlabel("Total No of elements ")
        plt.ylabel("Total time taken (in ms)")
        for key in self.plotData:
            plt.plot(*zip(*self.plotData[key]),label=key)

        plt.legend()
        plt.show()
if __name__=='__main__':
    analyzer = SortAnalysis()
    analyzer.analyzeInsertionSort(high=50000,step=10000)
    analyzer.analyzeMergeSort(high=100000,step=10000)

    analyzer.showPlot()
