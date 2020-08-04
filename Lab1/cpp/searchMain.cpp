#include<iostream>
#include<stdlib.h>
#include<vector>
#include<map>
#include<cmath>
#include<ctime>
// #include<string>
#include "search.cpp"

class LinearSearch{
public:
    std::map<int,std::clock_t> plottingDatas;
    int MAX,MIN,STEP;
    LinearSearch(){
        MAX = 200000;
        MIN = 10000;
        STEP = 5000;
        std::srand(time(NULL));
    }
    void clearData(){
        plottingDatas.clear();
    }
    void saveData(char* filename){
        FILE* f;
        f = fopen(filename,"w");
        fprintf(f,"# Number of Datas \t Time Interval (ms)\n");
        
        for(std::map<int,std::clock_t>::iterator it=plottingDatas.begin(); it!=plottingDatas.end();++it){
            fprintf(f,"%d\t%lf\n",it->first,(double)it->second);
            // std::cout<<"\t"<<it->first<<"\t"<<it->second<<std::endl;

        }
        std::cout<<"Data saved "<<filename<<std::endl;
        fclose(f);
    }
    void testBestCase(){
        std::vector<int> data;
        clearData();
        int index = 0;
        for(int i=MIN;i<MAX;i+=STEP){
            for(int j=0;j<i;j++){
                data.push_back(std::rand()%i);
            }
            std::clock_t start = std::clock();
            linearSearch(data,data[0]);
            std::clock_t end = std::clock();
            std::clock_t elapsed =(end-start);
            plottingDatas.insert({i,elapsed});
        }
        saveData("ls_best.dat");
    }
    void testAverageCase(){
        std::vector<int> data;
        clearData();

        int index = 0;
        for(int i=MIN;i<MAX;i+=STEP){
            for(int j=0;j<i;j++){
                data.push_back(std::rand()%i);
            }
            int r = data[rand()%i];
            std::clock_t start = std::clock();
            linearSearch(data,r);
            std::clock_t end = std::clock();
            std::clock_t elapsed = (end-start);
            // std::cout<<r<<" "<<elapsed<<std::endl;
            plottingDatas.insert({i,elapsed});
        }
        saveData("ls_avg.dat");
    }
    void testWorstCase(){
        std::vector<int> data;
        clearData();

        int index = 0;
        for(int i=MIN;i<MAX;i+=STEP){
            for(int j=0;j<i;j++){
                data.push_back(std::rand()%i);
            }
            int r = data[i-1];
            std::clock_t start = std::clock();
            linearSearch(data,r);
            std::clock_t end = std::clock();
            std::clock_t elapsed = (end-start);
            plottingDatas.insert({i,elapsed});
        }
        saveData("ls_worst.dat");
    }
    void plotData(){
        
        system("gnuplot ../plot.gp");
        std::cout<<"Data plotted, check your build file"<<std::endl;
    }
};


int main(){
    LinearSearch ls = LinearSearch();
    ls.testBestCase();
    ls.testAverageCase();
    ls.testWorstCase();
    ls.plotData();
    
    return 0;
}