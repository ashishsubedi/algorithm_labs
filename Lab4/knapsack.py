
def greedy(w,p,max):
    assert len(p) == len(w), "W and p not equal length"

    pw = [(i,p[i]/w[i]) for i in range(len(w))]
    pw.sort(reverse=True)
    
   
    curr_w = 0
    i = pw[0][0]
    index = 0
    profit = 0
    selected = ['0' for i in range(len(p))]
    while True:
        if(curr_w+w[i] <= max):
            curr_w += w[i] 
            selected[i] = '1'
            profit += p[i]
            index += 1
            i = pw[index][0]
            if (index == len(p)): break

        else:
            rem = max - curr_w
            profit += (pw[index][1]*rem)
            break
    return (''.join(selected),profit)


if __name__=="__main__":
    p = [5,6,7,2]

    w = [4,2,3,1]
    max = 8

    sel,profit =  greedy(w,p,max)
    print(sel,profit)
