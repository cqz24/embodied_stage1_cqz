#include <iostream>
#include <vector>
#include <sstream>
#include <string>
#include <numeric>
#include <algorithm>

int main() {
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
        return 0;
    }

    int max_val = *std::max_element(nums.begin(),nums.end());
    int min_val = *std::min_element(nums.begin(),nums.end());
    double sum = std::accumulate(nums.begin(),nums.end(),0.0);
    double avg = sum / nums.size();

    std::cout << "最大值：" << max_val << std::endl;
    std::cout << "最小值：" << min_val << std::endl;
    std::cout << "平均值：" << avg << std::endl;
    
    return 0;
}