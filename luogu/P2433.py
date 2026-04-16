# P2433 小学数学N合一
# TODO: WA: 8, 11, 13, 14, cnm精度还得套
from math import sqrt

question_number = int(input())

if question_number == 1:
    print("I love Luogu!")
elif question_number == 2:
    a = 2
    uim = 4
    b = 10 - a - uim
    print(a + uim, b)
elif question_number == 3:
    apple_per_person = 14 // 4
    apple_distributed = apple_per_person * 4
    apple_remain = 14 % 4
    print(f"{apple_per_person}\n{apple_distributed}\n{apple_remain}")
elif question_number == 4:
    drink_per_person = 500 / 3
    print(f"{drink_per_person:.6g}")
elif question_number == 5:
    time = (260 + 220) // (12 + 20)
    print(time)
elif question_number == 6:
    result = sqrt(6 ** 2 + 9 ** 2)
    print(f"{result:.6g}")
elif question_number == 7:
    balance = 100
    balance += 10
    print(balance)
    balance -= 20
    print(balance)
    balance -= balance
    print(balance)
elif question_number == 8:
    PI = 3.141593
    r = 5
    perimeter = 2 * PI * r
    area = PI * (r ** 2)
    sphere_volume = 3 * PI * (r ** 3) / 4
    print(f"{perimeter:.6g}")
    print(f"{area:.6g}")
    print(f"{sphere_volume:.6g}")
elif question_number == 9:
    total_peach = (((((1 + 1) * 2) + 1) * 2) + 1) * 2
    print(total_peach) 
elif question_number == 10:
    print(int((15 + 7.5 * 10) / 10))
elif question_number == 11:
    print(100 / (8 - 5))
elif question_number == 12:
    number = ord('M') - ord('A') + 1
    character = chr(ord('A') + 18 - 1)
    print(f"{number}\n{character}")
elif question_number == 13:
    NEW_PI = 3.141593
    item_1 = NEW_PI * 4 ** 2
    item_2 = NEW_PI * 10 ** 2
    side = (item_1 + item_2) ** (1 / 3)
    if side.is_integer():
        print(int(side))
    else:
        print(side)
elif question_number == 14:
    people = (100 - sqrt((-100) ** 2 - 4 * 2400)) / 2
    if people.is_integer():
        print(int(people))
    else:
        print(round(people))