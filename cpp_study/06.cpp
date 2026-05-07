/* 06 - function declaration and function definition */
#include <iostream>
#include <string>

// function declaration
int add(int a, int b);  // pass by value
void greet(const std::string& name);    // pass by const reference (to avoid copying)
bool isEven(int n);     // pass by value

int main() {
    std::cout << "3 + 4 = "  << add(3, 4) << std::endl;
    greet("Jin Zicheng");
    std::cout << "7 is even: " << (isEven(7) ? "true" : "false") << std::endl;
}

// function definition
int add(int a, int b) {
    return a + b;
}

void greet(const std::string& name) {
    std::cout << "Hello, " << name << "! " << std::endl;
}

bool isEven(int n) {
    return n % 2 == 0;
}
