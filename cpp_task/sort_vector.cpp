#include <iostream>
#include <vector>
#include <algorithm>
#include <sstream>
#include<string>

int main(){
    std::cout << "请输入若干整数，用空格分隔：";
    std::string line;
    std::getline(std::cin,line);

    std::vector<int> nums;
    std::stringstream ss(line);
    int num;
    while (ss >> num) {
        nums.push_back(num);
    }
    if (nums.empty()) {
        std::cout << "没有输入任何数字！" << std::endl;
        return  0;
    }
    std::sort(nums.begin(), nums.end());
    std::cout << "排序后的数字：";
    for(int x : nums) {
        std::cout << x << " ";
    }
    std::cout << std::endl;
    return 0;
}