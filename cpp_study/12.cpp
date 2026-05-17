#include <iostream>
#include <string>
#include <vector>

struct Student {
    std::string name;
    int score;
};

void append_student(std::vector<Student>& list);
void remove_student(std::vector<Student>& list);
void print_list(const auto& list);

int main() {
    std::vector<Student> student_list;
    
    while (true) {
        std::cout << "1.append 2.remove 3.print list 0.exit" << std::endl;
        std::cout << "Please enter: ";
        
        int command;
        std::cin >> command;
        
        switch (command)
        {
        case 1: 
            append_student(student_list);
            break;
        case 2:
            remove_student(student_list);
            break;
        case 3:
            print_list(student_list);
            break;
        case 0:
            return 0;
        default:
            break;
        }
    }

    return 0;
}

void append_student(auto& list) {
    
}