#include <iostream>
#include <string>

int main() {
    // create and initialize
    std::string s1 = "Hello";
    std::string s2("world");
    std::string s3(5, '*');     // "*****"

    // append
    std::string greeting = s1 + ", " + s2 + "!";
    std::cout << greeting << std::endl;

    s1.append(" C++");
    std::cout << s1 << std::endl;

    // length
    std::cout << "length: " << greeting.size() << std::endl;

    // access by index
    std::cout << "first char: " << greeting[0] << std::endl;
    std::cout << "last char: " << greeting[greeting.size() - 1] << std::endl;

    // substring
    std::string sub = greeting.substr(0, 5);    // start from index 0, include 5 chars
    std::cout << "substring: " << sub << std::endl;

    // find
    int pos = greeting.find("world");
    if (pos != std::string::npos) {
        std::cout << "world at: " << pos << std::endl;
    } else {
        std::cout << "target not found" << std::endl;
    }

    // compare
    std::cout << "equals: " << (s1 == s2) << std::endl; // == compares the value of std::string

    // std::string cast to numerical type
    int num = 42;
    std::string num_str = std::to_string(num);  // int -> std::string
    int parsed = std::stoi("123");              // std::string -> int
    double parsed2 = std::stod("3.14");         // std::string -> double
    std::cout << "convert: " << num_str << ", "
              << "parsed: " << parsed << ", "
              << "parsed2: " << parsed2 << std::endl;

    // traverse each char
    for (char c : greeting) {
        std::cout << c << " ";
    }
    std::cout << std::endl;
}
