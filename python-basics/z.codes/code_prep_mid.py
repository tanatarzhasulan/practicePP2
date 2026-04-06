# import math
# x = 90
# (math.tan(x*math.pi/180))

''' import datetime

today = datetime.date.today()
yesterday = today.replace(day=today.day-1)
print(today)
print(yesterday)

delta = today - yesterday
print(delta)
'''

''' from datetime import datetime, timedelta
start = datetime(2026, 2, 1)
end = datetime(2026, 2, 15)

diff = end - start
print(diff)
print(diff.days)

print()

d = datetime(2026, 2, 1)
new_date = d + timedelta(days=10)
print(new_date)
'''


from datetime import datetime, timedelta

''' a = input()
b = input()

start = datetime.strptime(a, "%Y-%m-%d")
end = datetime.strptime(b, "%Y-%m-%d")
print(start)
print(end)
diff = end - start
print(diff.days)
print(diff)


print()
'''
''' date = input()
d = int(input())

date_form = datetime.strptime(date, "%Y-%m-%d")
new_date = date_form + timedelta(days=d)
print(new_date.strftime("%Y-%m-%d"))
'''


d = input()
n = int(input())
d2 = input()
d3 = input()
d4 = input()

date = datetime.strptime(d, "%Y-%m-%d")
date2 = datetime.strptime(d2, "%Y-%m-%d")
date3 = datetime.s