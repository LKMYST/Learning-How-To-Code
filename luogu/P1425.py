# P1425 小鱼的游泳时间
a, b, c, d = list(map(int, input().strip().split()))

passed_hours = c - a
passed_minutes = d - b

if passed_minutes < 0:
    passed_hours -= 1
    passed_minutes += 60
    
print(f"{passed_hours} {passed_minutes}")