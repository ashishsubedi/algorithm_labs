import math
def mergesort(data:list,p:int,r:int):
    if(p<r):
        
        q = (p+r)//2

        mergesort(data,p,q)
        mergesort(data,q+1,r)
        merge(data,p,q,r)
     


def merge(data:list,p:int,q:int,r:int):
    L = data.copy()[p:q+1]
    R = data.copy()[q+1:r+1]
    L.append(math.inf)
    R.append(math.inf)


    i,j=0,0

    for k in range(p,r+1):
        
        if(L[i]<R[j]):
            if(k<len(data)):
                data[k] = L[i]
                i+=1
        else:
            if(k<len(data)):
     
                data[k] = R[j]
                
                j+=1
   
def insertionSort(data:list):
    for j in range(1,len(data)):
        key = data[j]
        i = j-1
        while i>=0 and data[i]>key:
            data[i+1] = data[i]
            i-=1
        data[i+1] = key
