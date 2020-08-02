def linear_search(data, value):
    for i in range(len(data)):
        if(data[i] == value):
            return i
    return -1


def binary_search(data, value):
    l, r = 0, len(data)-1

    while(l <= r):
        mid = (l+r)//2
        if(data[mid] == value):
            return mid
        elif value > data[mid]:
            l = mid+1
        elif value < data[mid]:
            r = mid-1
    return -1
