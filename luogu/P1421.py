# P1421 小玉买文具
from math import floor

PEN_PRICE = 10 + 9          # single price of pen in jiao

a, b = map(int, input().strip().split())

total_money = 10 * a + b
total_pen = floor(total_money / PEN_PRICE)

print(total_pen)