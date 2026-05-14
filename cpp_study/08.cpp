#include <iostream>
#include <array>

int main() {
    /**
     * C-style array: 
     * - fixed size during compile time
     * - cannot resize dynamically
     * - no boundary check (can lead to undefined behavior)
     */
    
    int scores[5]{90, 85, 92, 78, 95};
    int n = sizeof(scores) / sizeof(scores[0]);   // calculate array size

    for (int i = 0; i < n; ++i) {
        std::cout << scores[i] << " ";
    }
    std::cout << std::endl;

    /**
     * std::array: 
     * - fixed size during compile time
     * - .at() have boundary check
     * - .at() can throw exceptions
     */
    std::array<float, 3> position{1.0f, 2.0f, 3.0f};

    std::cout << "x=" << position[0] 
              << " y=" << position[1] 
              << " z=" << position[2] << std::endl;
    std::cout << "size: " << position.size() << std::endl;
}