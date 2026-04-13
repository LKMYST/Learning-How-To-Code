# P2433 小学数学N合一
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
    print(f"{drink_per_person:.6f}")
elif question_number == 5:
    time = (260 + 220) // (12 + 20)
    print(time)
elif question_number == 6:
    print(sqrt(6 ** 2 + 9 ** 2))
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
    print(2 * PI * r)
    print(PI * (r ** 2))
    print(3 * PI * (r ** 3) / 4)
elif question_number == 9:
    total_peach = (((((1 + 1) * 2) + 1) * 2) + 1) * 2
    print(total_peach) 
elif question_number == 10:
    
# elif question_number == 11:

# elif question_number == 12:

# elif question_number == 13:

# elif question_number == 14:
