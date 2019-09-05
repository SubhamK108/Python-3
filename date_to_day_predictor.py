od_day = {
    '0' : 'Sunday',
    '1' : 'Monday',
    '2' : 'Tuesday',
    '3' : 'Wednesday',
    '4' : 'Thursday',
    '5' : 'Friday',
    '6' : 'Saturday'
}

month_od_day = {
    1 : 3,
    2 : 0,
    3 : 3,
    4 : 2,
    5 : 3,
    6 : 2,
    7 : 3,
    8 : 3,
    9 : 2,
    10 : 3,
    11 : 2,
    12 : 3
}

century_od_day = {
    100 : 5,
    200 : 3,
    300 : 1,
    400 : 0
}

def no_leap_year_getter(n):
    return (n // 4)

def no_od_day_getter(n):
    return (n % 7)

def closest_century(n):
    c = 400
    while (c < n):
        c += 400
    c -= 400
    return c

def is_leap_year(y):
    if y % 100 != 0 and y % 4 == 0:
        return True
    elif y % 100 == 0 and y % 400 == 0:
        return True
    else:
        return False

d, m, y = map(int, input('Enter Date (DD.MM.YYYY): ').split('.'))
y2 = y - 1
cy = closest_century(y)
a = y2 - cy
if a < 100:
    b = a
    a = 0
else:
    b = a % 100
    a -= b
    a = century_od_day.get(a)
b2 = no_leap_year_getter(b)
b -= b2
b2 *= 2
sum = a + b + b2
for i in range(1, m):
    sum += month_od_day.get(i)
sum += no_od_day_getter(d)
if m > 2 and is_leap_year(y):
    sum += 1
sum = no_od_day_getter(sum)

day = od_day.get(str(sum))
print(f"It's a {day}.")