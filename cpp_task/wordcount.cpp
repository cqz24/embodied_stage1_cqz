#include <iostream>
#include <fstream>
#include <string>
int main() {
    std::string filename;
    std::cout << "请输入要统计的文件名：";
    std::cin >> filename;
    std::ifstream file(filename);
    if (!file.is_open()) {
        std::cerr << "无法打开文件" << filename << std::endl;
        return 1;
    }
    int word_count = 0;
    std::string word;
    while (file >> word) {
        word_count++;
    }
    std::cout << "文件" << filename << "中的单词数：" << word_count << std::endl;
    file.close();
    return 0;
}