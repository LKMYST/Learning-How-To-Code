# P5706 再分肥宅水
t, n = input().strip().split()
mililiter_per_person = float(t) / int (n)
total_cup = 2 * int(n)
print(f"{mililiter_per_person:.3f}\n{total_cup}")