#include<iostream>
#include<vector>
#include"gtest/gtest.h"

int linearSearch(std::vector<int>&data,int value);
int binarySearch(std::vector<int>&data,int value);

TEST(LinearSearchTest,BasicTest){
    std::vector<int> data = {1,2,3,4,5};
    EXPECT_EQ(linearSearch(data,2),1);
    EXPECT_EQ(linearSearch(data,4),3);
    EXPECT_EQ(linearSearch(data,10),-1);
}

TEST(BinarySearchTest,BasicTest){
    std::vector<int> data = {1,2,3,4,5};
    EXPECT_EQ(binarySearch(data,2),1);
    EXPECT_EQ(binarySearch(data,4),3);
    EXPECT_EQ(binarySearch(data,10),-1);
}
int main(int argc, char **argv) {
  ::testing::InitGoogleTest(&argc, argv);
  return RUN_ALL_TESTS();
}