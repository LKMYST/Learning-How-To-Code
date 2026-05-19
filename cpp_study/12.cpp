#include <iostream>
#include <string>
#include <vector>

struct Student {
    std::string name;
    int score;
};

void add_student(std::vector<Student>& students);
void print_list(const std::vector<Student>& students);

int main() {
    std::vector<Student> students;

    while (true) {
        std::cout << "1.add 2.list 0.exit" << std::endl;
        std::cout << "Please enter: ";
        
        int command;
        std::cin >> command;

        if (command == 1) {
            add_student(students);
        } else if (command == 2) {
            print_list(students);
        } else if (command == 0) {
            break; 
        } else {
            continue;
        }
    }
}

void add_student(std::vector<Student>& students) {
    Student new_student;

    std::cout << "Please enter student name: ";
    std::cin >> new_student.name;

    std::cout << "Please enter student score: ";
    std::cin >> new_student.score;

    students.push_back(new_student);
}

void print_list(const std::vector<Student>& students) {
    std::cout << "--- Student List ---" << std::endl;

    for (const auto& s : students) {
        std::cout << s.name << "\t" << s.score << std::endl;
    }
}

