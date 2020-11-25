
from itertools import permutations 
from collections import Counter

def greedy(w,p,max):
    assert len(p) == len(w), "W and p not equal length"

    pw = [(i,p[i]/w[i]) for i in range(len(w))]
    pw.sort(key=lambda x: x[1],reverse=True)
    
   
    curr_w = 0
 
    profit = 0
    selected = ['0' for i in range(len(p))]
    for i,ratio in pw:
        

        if(curr_w+w[i] <= max):
            curr_w += w[i] 
            selected[i] = '1'
            profit += p[i]


        else:

            rem = max - curr_w

            profit += (ratio*rem)
        
            selected[i] = str(round(rem/w[i],2))
    



    return (''.join(selected),profit)

def bruteforce(w,p,max):
    # For all weights, calculate the profit
    assert len(p) == len(w), "W and p not equal length"
    maxProfit = 0
    n = len(w)
    maxSeletion = ['0'] *n 

    solutions = [list(bin(x)[2:].rjust(n,'0')) for x in range(2**n)]
    for s in solutions:

        profit = sum(int(s[i])*p[i] for i in range(n))
        weight = sum(int(s[i])*w[i] for i in range(n))

        if weight <= max and profit > maxProfit:
            maxProfit = profit
            maxSeletion = s


    return (''.join(maxSeletion),maxProfit)

def bruteforce_fractional(w,p,C):
    # For all weights, calculate the profit
    assert len(p) == len(w), "W and p not equal length"
    maxProfit = 0
    n = len(w)
    maxSeletion = ['0'] *n 

    solutions = [list(bin(x)[2:].rjust(n,'0')) for x in range(2**n)]
    for s in solutions:
        
        indices_1 = [i for i, x in enumerate(s) if x == '1']
        indices_0 = [i for i, x in enumerate(s) if x == '0']
        non_frac_profit = 0
        weight = 0
        for i in indices_1:
            non_frac_profit += p[i]
            weight += w[i]

        fracProfit = 0
        newS = s

        if weight<C:
            maxIndex = 0
            for i in indices_0:
                rem = C-weight if(C-weight < w[i]) else w[i]
                frac = (p[i]/w[i])*(rem)
                if frac > fracProfit:
                    fracProfit = frac
                    maxIndex = i
            newS[maxIndex] = str(round(fracProfit/p[i],2))
                

        totalProfit = fracProfit + non_frac_profit

        if weight<= C and totalProfit >= maxProfit:
            maxProfit = totalProfit
            maxSeletion = newS


    return (''.join(maxSeletion),maxProfit)


def bruteforce_fractionalV2(w,p,m):

    maxProfit = 0
    n = len(w)
    maxSelection = '0' *n 

    solutions = [bin(x)[2:].rjust(n,'0') for x in range(2**n)]
    for s in solutions:
        
        i_0 = []
        i_1 = []
        
        for i,x in enumerate(s):
            if x=='0':
                i_0.append(i)
            else:
                i_1.append(i)
        
        
       
        profit = sum(int(s[i])*p[i] for i in range(n))
        weight = sum(int(s[i])*w[i] for i in range(n))

        fraction = 0
     

        if weight<m:
      
            for i in i_0:
                if(m-weight < w[i]):
                    remainder = m-weight
                    
                else: remainder = w[i]
                 
                frac = (p[i]/w[i])*(remainder)
                if frac > fraction:
                    fraction = frac
         
                

        profit  += fraction

        if weight<= m and profit >= maxProfit:
            maxProfit = profit
            maxSelection = s


    return (maxSelection,maxProfit)


def dp(w,p,m):
    assert len(w) == len(p), "W and P not equal length"
    n = len(w)
    v = [[0 for i in range(m+1)] for j in range(n+1)] 
 
    w = [0]+w
    p = [0] + p
    for i in range(1,n+1):
        for j in range(1,m+1):
            if(j-w[i]<0):
                continue
            
            v[i][j] = max(v[i-1][j],
                    v[i-1][j-w[i]]+p[i])


                    
    selection = ['0']*n
    
    #Show Table
    # for i in range(n+1):
    #     for j in range(m+1):
    #         print(v[i][j],end=" ")
    #     print()

    i=n
    j=m
    while i != 0:
  
        if v[i][j] > v[i-1][j]:
            selection[i-1] = '1'
            j = j - w[i]
            if (j<=0): break
        i-=1
        

    return (''.join(selection),v[n][m])
    



















