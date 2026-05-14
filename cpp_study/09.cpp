#include <iostream>
#include <vector>
#include <string>

int main() {
    // create and initialize
    std::vector<int> scores;                        // empty std::vector
    std::vector<int> nums{3, 1, 4, 1, 5, 9};        // list initialization of std::vector
    std::vector<std::string> names(5, "Undefined"); // 5 elements, all of them are "Undefined"

    // append elements
    scores.push_back(90);
    scores.push_back(85);
    scores.push_back(92);

    // access elements
    std::cout << "First one: " << scores[0] << std::endl;       // access by index, no boundary check
    std::cout << "Second one: " << scores.at(1) << std::endl;   // access by at(), boundary check

    // commonly used elements
    std::cout << "Size: " << scores.size() << std::endl;
    std::cout << "Empty: " << scores.empty() << std::endl;

    // remove elements
    scores.pop_back();
    scores.erase(scores.begin());

    // traverse by index
    for (int i = 0; i < static_cast<int>(nums.size()); ++i) {
        std::cout << nums[i] << " ";
    }
    std::cout << std::endl;

    // traverse by for-each loop
    for (int n : nums) {
        std::cout << n << " ";
    }
    std::cout << std::endl;

    // traverse by iterator
    for (auto it = nums.begin(); it != nums.end(); ++it) {
        std::cout << *it << " ";
    }
    std::cout << std::endl;

    // clear all
    nums.clear();
    std::cout << "Size after clear: " << nums.size() << std::endl;
}