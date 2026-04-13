# P3954 成绩
a, b, c = list(map(int, input().strip().split()))
total_marks = a * 0.2 + b * 0.3 + c * 0.5
print(int(total_marks))