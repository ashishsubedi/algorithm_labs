import knapsack


if __name__=="__main__":
    # p = [5,6,7,8]

    # w = [2,4,5,1]
    # max = 8
    p = [5,6,7,2]

    w = [4,2,3,1]
    max = 10
    # p = [60,100,120]
    # w = [10,20,30]
    # max = 50
   
    #0-1
    sel,profit =  knapsack.dp(w,p,max)
    print(sel,profit)
  
    sel,profit =  knapsack.bruteforce(w,p,max)
    print(sel,profit)
    
    #Frac
    sel,profit =  knapsack.bruteforce_fractionalV2(w,p,max)
    print(sel,profit)

    sel,profit =  knapsack.greedy(w,p,max)
    print(sel,profit)
 


