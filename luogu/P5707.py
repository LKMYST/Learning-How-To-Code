# P5707 上学迟到
from math import ceil

s, v = map(int, input().strip().split())
needed_time = ceil(s / v) + 10                  # time in minutes

if needed_time > 24 * 60:
    print("08:00")
else:
    needed_time_hours = int(needed_time / 60)   # hours
    needed_time_minutes = needed_time % 60      # minutes
    if needed_time_minutes == 0:
        if needed_time_hours > 8:
            result_time_hours = 8 + 24 - needed_time_hours
        else:
            result_time_hours = 8 - needed_time_hours
        print(f"{result_time_hours:0>2}:00")
    else:
        result_time_minutes = 0 + 60 - needed_time_minutes
        if needed_time_hours > 8 - 1:
            result_time_hours = 8 - 1 + 24 - needed_time_hours
        else:
            result_time_hours = 8 - 1 - needed_time_hours
        print(f"{result_time_hours:0>2}:{result_time_minutes:0>2}")