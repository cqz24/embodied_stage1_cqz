#include <iostream>
#include <cmath>
bool isPrime(int n) {
    if (n <= 1) return false;
    if (n == 2) return true;
    if (n % 2 == 0) return false;
    int limit = static_cast<int>(std::sqrt(n)) + 1;
    for (int i =3; i <= limit; i +=2){
        if (n % i == 0) return false;
    }
    return true;
}
int main() {
    int n;
    std::cout << "请输入一个整数：";
    std::cin >> n;
    if (isPrime(n)) {
        std::cout << n << "是素数" << std::endl; 
    }else{
        std::cout << n << "不是素数" << std::endl;
    }
    return 0;
}