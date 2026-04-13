# B2029 大象喝水
from math import ceil
PI = 3.14

h, r = map(int, input().strip().split())    # centimeter
volume = PI * (r ** 2) * h / 1000           # liter
bucket_number = ceil(20.0 / volume)

print(bucket_number)