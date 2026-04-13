# P5708 三角形面积
from math import sqrt

a, b, c = list(map(float, input().strip().split()))
p = (a + b + c) / 2
area = sqrt(p * (p - a) * (p - b) * (p - c))

print(f"{area:.1f}")