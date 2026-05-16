#include <iostream>
#include <string>

struct Player {
    std::string name;;
    int hp;
    int attack;
    bool is_alive;
};

void print_player(const Player& p) {
    std::cout << "name = " << p.name
              << " hp = " << p.hp
              << " attack = " << p.attack
              << " is_alive = " << p.is_alive << std::endl;
}

int main() {
    // create and initialize
    Player p1{"Warrior", 200, 30, true};
    Player p2{"Wizard", 100, 50, true};

    // access and modify
    p1.hp -= 50;
    p1.attack += 10;

    print_player(p1);
    print_player(p2);
}