#include<vector>

int linearSearch(std::vector<int> &data, int value){
    for(int i=0;i<data.size(); i++){
        if(data[i] == value) return i;
    }
    return -1;
}

int binarySearch(std::vector<int> &data, int value){
    int low = 0, high = data.size()-1;
    int mid;
    while(low<=high){
        mid =(high+low)/2;
        if(data[mid] == value) return mid;
        else if(data[mid]<value) low = mid+1;
        else high=mid-1;
    }
    return -1;
}