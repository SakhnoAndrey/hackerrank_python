import calendar
from datetime import datetime


def calendar_module():
    m, d, y = map(int, input().strip().split())
    day_num = calendar.weekday(y, m, d)
    print(calendar.day_name[day_num].upper())


def time_delta():
    # Input
    t1, t2 = input(), input()
    # Function
    t1_datetime_obj = datetime.strptime(t1, "%a %d %b %Y %H:%M:%S %z")
    t2_datetime_obj = datetime.strptime(t2, "%a %d %b %Y %H:%M:%S %z")
    return str(int(abs(t1_datetime_obj - t2_datetime_obj).total_seconds()))


delta = time_delta()
print(delta)
