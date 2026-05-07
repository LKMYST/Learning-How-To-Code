/* function overload and default argument */
#include <iostream>
#include <string>

int max_value(int a, int b);
double max_value(double a, double b);
int max_value(int a, int b, int c);
void attack(const std::string& target,
    int damage = 10,
    const std::string& element = "physical");

int main() {
    std::cout << max_value(3, 7) << std::endl;  // call int version
    std::cout << max_value(3.14, 2.17) << std::endl;    // call double version
    std::cout << max_value(1, 5, 3) << std::endl;   // call three parameters version

    attack("slime");
    attack("goblin", 25);
    attack("dragon", 100, "fire");
}

int max_value(int a, int b) {
    return (a > b) ? a : b;
}

double max_value(double a, double b) {
    return (a > b) ? a : b;
}

int max_value(int a, int b, int c) {
    return max_value(max_value(a, b), c);
}

void attack(
    const std::string& target,
    int damage,
    const std::string& element) {
    std::cout << "Deal " << damage 
              << " points of " << element 
              << " damage to " << target << ".\n";
}
